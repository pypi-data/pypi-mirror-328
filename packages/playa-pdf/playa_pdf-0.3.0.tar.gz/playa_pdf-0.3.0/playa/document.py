"""
Basic classes for PDF document parsing.
"""

import io
import itertools
import logging
import mmap
import re
import struct
import warnings
from concurrent.futures import Executor
from hashlib import md5, sha256, sha384, sha512
from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    NamedTuple,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    Union,
    overload,
)

try:
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
except ImportError:
    default_backend = None  # type: ignore

from playa.arcfour import Arcfour
from playa.data_structures import NameTree, NumberTree
from playa.exceptions import (
    PDFEncryptionError,
    PDFPasswordIncorrect,
    PDFSyntaxError,
)
from playa.font import CIDFont, Font, TrueTypeFont, Type1Font, Type3Font
from playa.page import (
    Page,
    DeviceSpace,
)
from playa.parser import (
    KEYWORD_TRAILER,
    KEYWORD_XREF,
    KEYWORD_OBJ,
    LIT,
    IndirectObject,
    IndirectObjectParser,
    Lexer,
    ObjectParser,
    ObjectStreamParser,
    PDFObject,
    PSLiteral,
    Token,
    literal_name,
    reverse_iter_lines,
)
from playa.pdftypes import (
    ContentStream,
    DecipherCallable,
    ObjRef,
    decipher_all,
    dict_value,
    int_value,
    list_value,
    resolve1,
    str_value,
    stream_value,
    uint_value,
)
from playa.utils import (
    choplist,
    decode_text,
    format_int_alpha,
    format_int_roman,
    nunpack,
)
from playa.structtree import StructTree
from playa.structure import Tree
from playa.outline import Outline, Destination
from playa.worker import (
    _set_document,
    _ref_document,
    _deref_document,
    _deref_page,
    in_worker,
    PageRef,
)

log = logging.getLogger(__name__)


# Some predefined literals and keywords (these can be defined wherever
# they are used as they are interned to the same objects)
LITERAL_PDF = LIT("PDF")
LITERAL_TEXT = LIT("Text")
LITERAL_FONT = LIT("Font")
LITERAL_OBJSTM = LIT("ObjStm")
LITERAL_XREF = LIT("XRef")
LITERAL_CATALOG = LIT("Catalog")
LITERAL_PAGE = LIT("Page")
LITERAL_PAGES = LIT("Pages")
INHERITABLE_PAGE_ATTRS = {"Resources", "MediaBox", "CropBox", "Rotate"}


class XRefPos(NamedTuple):
    streamid: Optional[int]
    pos: int
    genno: int


class XRef(Protocol):
    """
    Duck-typing for XRef table implementations, which are expected to be read-only.
    """

    @property
    def trailer(self) -> Dict[str, Any]: ...
    @property
    def objids(self) -> Iterable[int]: ...
    def get_pos(self, objid: int) -> XRefPos: ...


class XRefTable:
    """Simplest (PDF 1.0) implementation of cross-reference table, in
    plain text at the end of the file.
    """

    def __init__(self, parser: ObjectParser, offset: int = 0) -> None:
        self.offsets: Dict[int, XRefPos] = {}
        self.trailer: Dict[str, Any] = {}
        self._load(parser, offset)

    def _load(self, parser: ObjectParser, offset: int) -> None:
        while True:
            pos, line = parser.nextline()
            if line == b"":
                break
            line = line.strip()
            if not line:
                continue
            if line.startswith(b"trailer"):
                parser.seek(pos)
                break
            f = line.split(b" ")
            if len(f) != 2:
                error_msg = f"Trailer not found: {parser!r}: line={line!r}"
                raise IndexError(error_msg)
            try:
                (start, nobjs) = map(int, f)
            except ValueError:
                error_msg = f"Invalid line: {parser!r}: line={line!r}"
                raise ValueError(error_msg)
            for objid in range(start, start + nobjs):
                _, line = parser.nextline()
                if line == b"":
                    break
                line = line.strip()
                f = line.split(b" ")
                if len(f) != 3:
                    error_msg = f"Invalid XRef format: {parser!r}, line={line!r}"
                    raise ValueError(error_msg)
                (pos_b, genno_b, use_b) = f
                if use_b != b"n":
                    continue
                self.offsets[objid] = XRefPos(None, int(pos_b) + offset, int(genno_b))
        self._load_trailer(parser)

    def _load_trailer(self, parser: ObjectParser) -> None:
        (_, kwd) = next(parser)
        if kwd is not KEYWORD_TRAILER:
            raise PDFSyntaxError(
                "Expected %r, got %r"
                % (
                    KEYWORD_TRAILER,
                    kwd,
                )
            )
        (_, dic) = next(parser)
        self.trailer.update(dict_value(dic))

    def __repr__(self) -> str:
        return "<XRefTable: offsets=%r>" % (self.offsets.keys())

    @property
    def objids(self) -> Iterable[int]:
        return self.offsets.keys()

    def get_pos(self, objid: int) -> XRefPos:
        return self.offsets[objid]


PDFOBJ_CUE = re.compile(rb"^(\d+)\s+(\d+)\s+obj\b")


class XRefFallback:
    """In the case where a file is non-conforming and has no
    `startxref` marker at its end, we will reconstruct a
    cross-reference table by simply scanning the entire file to find
    all indirect objects."""

    def __init__(self, parser: IndirectObjectParser) -> None:
        self.offsets: Dict[int, XRefPos] = {}
        self.trailer: Dict[str, Any] = {}
        self._load(parser)

    def __repr__(self) -> str:
        return "<XRefFallback: offsets=%r>" % (self.offsets.keys())

    def _load(self, parser: IndirectObjectParser) -> None:
        parser.seek(0)
        parser.reset()
        doc = parser.doc
        assert doc is not None
        # Get all the objects
        for pos, obj in parser:
            self.offsets[obj.objid] = XRefPos(None, pos, obj.genno)
            # Expand any object streams right away
            if (
                isinstance(obj.obj, ContentStream)
                and obj.obj.get("Type") is LITERAL_OBJSTM
            ):
                stream = stream_value(obj.obj)
                try:
                    n = stream["N"]
                except KeyError:
                    log.warning("N is not defined in object stream: %r", stream)
                    n = 0
                parser1 = ObjectParser(stream.buffer, doc)
                objs: List = [obj for _, obj in parser1]
                # FIXME: This is choplist
                n = min(n, len(objs) // 2)
                for index in range(n):
                    objid1 = objs[index * 2]
                    self.offsets[objid1] = XRefPos(obj.objid, index, 0)
        # Now get the trailer
        itor = iter(parser.trailer)
        s1 = next(itor)
        for s2 in itor:
            _, token = s1
            if token is KEYWORD_TRAILER:
                _, dic = s2
                self.trailer.update(dict_value(dic))
                return
            s1 = s2
        # If not, then try harder
        for pos, line in reverse_iter_lines(parser.buffer):
            line = line.strip()
            if line == b"trailer":
                _, trailer = next(
                    ObjectParser(parser.buffer, doc, pos + len(b"trailer"))
                )
                if not isinstance(trailer, dict):
                    break
                self.trailer.update(trailer)
                return
        log.warning("b'trailer' not found in document or invalid")

    @property
    def objids(self) -> Iterable[int]:
        return self.offsets.keys()

    def get_pos(self, objid: int) -> XRefPos:
        return self.offsets[objid]


class XRefStream:
    """Cross-reference stream (as of PDF 1.5)"""

    def __init__(self, parser: IndirectObjectParser, offset: int = 0) -> None:
        self.offset = offset
        self.data: Optional[bytes] = None
        self.entlen: Optional[int] = None
        self.fl1: Optional[int] = None
        self.fl2: Optional[int] = None
        self.fl3: Optional[int] = None
        self.ranges: List[Tuple[int, int]] = []
        self._load(parser)

    def __repr__(self) -> str:
        return "<XRefStream: ranges=%r>" % (self.ranges)

    def _load(self, parser: IndirectObjectParser) -> None:
        (_, obj) = next(parser)
        stream = obj.obj
        if (
            not isinstance(stream, ContentStream)
            or stream.get("Type") is not LITERAL_XREF
        ):
            raise ValueError(f"Invalid PDF stream spec {stream!r}")
        size = stream["Size"]
        index_array = stream.get("Index", (0, size))
        if len(index_array) % 2 != 0:
            raise PDFSyntaxError("Invalid index number")
        for start, end in choplist(2, index_array):
            self.ranges.append((int_value(start), int_value(end)))
        (self.fl1, self.fl2, self.fl3) = stream["W"]
        assert self.fl1 is not None and self.fl2 is not None and self.fl3 is not None
        self.data = stream.buffer
        self.entlen = self.fl1 + self.fl2 + self.fl3
        self.trailer = stream.attrs

    @property
    def objids(self) -> Iterator[int]:
        for start, nobjs in self.ranges:
            for i in range(nobjs):
                assert self.entlen is not None
                assert self.data is not None
                offset = self.entlen * i
                ent = self.data[offset : offset + self.entlen]
                f1 = nunpack(ent[: self.fl1], 1)
                if f1 == 1 or f1 == 2:
                    yield start + i

    def get_pos(self, objid: int) -> XRefPos:
        index = 0
        for start, nobjs in self.ranges:
            if start <= objid and objid < start + nobjs:
                index += objid - start
                break
            else:
                index += nobjs
        else:
            raise KeyError(objid)
        assert self.entlen is not None
        assert self.data is not None
        assert self.fl1 is not None and self.fl2 is not None and self.fl3 is not None
        offset = self.entlen * index
        ent = self.data[offset : offset + self.entlen]
        f1 = nunpack(ent[: self.fl1], 1)
        f2 = nunpack(ent[self.fl1 : self.fl1 + self.fl2])
        f3 = nunpack(ent[self.fl1 + self.fl2 :])
        if f1 == 1:  # not in an object stream
            return XRefPos(None, f2 + self.offset, f3)
        elif f1 == 2:  # in an object stream
            return XRefPos(f2, f3, 0)
        else:
            # this is a free object
            raise KeyError(objid)


PASSWORD_PADDING = (
    b"(\xbfN^Nu\x8aAd\x00NV\xff\xfa\x01\x08" b"..\x00\xb6\xd0h>\x80/\x0c\xa9\xfedSiz"
)


class PDFStandardSecurityHandler:
    """Basic security handler for basic encryption types."""

    supported_revisions: Tuple[int, ...] = (2, 3)

    def __init__(
        self,
        docid: Sequence[bytes],
        param: Dict[str, Any],
        password: str = "",
    ) -> None:
        self.docid = docid
        self.param = param
        self.password = password
        self.init()

    def init(self) -> None:
        self.init_params()
        if self.r not in self.supported_revisions:
            error_msg = "Unsupported revision: param=%r" % self.param
            raise PDFEncryptionError(error_msg)
        self.init_key()

    def init_params(self) -> None:
        self.v = int_value(self.param.get("V", 0))
        self.r = int_value(self.param["R"])
        self.p = uint_value(self.param["P"], 32)
        self.o = str_value(self.param["O"])
        self.u = str_value(self.param["U"])
        self.length = int_value(self.param.get("Length", 40))

    def init_key(self) -> None:
        self.key = self.authenticate(self.password)
        if self.key is None:
            raise PDFPasswordIncorrect

    @property
    def is_printable(self) -> bool:
        return bool(self.p & 4)

    @property
    def is_modifiable(self) -> bool:
        return bool(self.p & 8)

    @property
    def is_extractable(self) -> bool:
        return bool(self.p & 16)

    def compute_u(self, key: bytes) -> bytes:
        if self.r == 2:
            # Algorithm 3.4
            return Arcfour(key).encrypt(PASSWORD_PADDING)  # 2
        else:
            # Algorithm 3.5
            hash = md5(PASSWORD_PADDING)  # 2
            hash.update(self.docid[0])  # 3
            result = Arcfour(key).encrypt(hash.digest())  # 4
            for i in range(1, 20):  # 5
                k = b"".join(bytes((c ^ i,)) for c in iter(key))
                result = Arcfour(k).encrypt(result)
            result += result  # 6
            return result

    def compute_encryption_key(self, password: bytes) -> bytes:
        # Algorithm 3.2
        password = (password + PASSWORD_PADDING)[:32]  # 1
        hash = md5(password)  # 2
        hash.update(self.o)  # 3
        # See https://github.com/pdfminer/pdfminer.six/issues/186
        hash.update(struct.pack("<L", self.p))  # 4
        hash.update(self.docid[0])  # 5
        if self.r >= 4:
            assert isinstance(self, PDFStandardSecurityHandlerV4)
            if not self.encrypt_metadata:
                hash.update(b"\xff\xff\xff\xff")
        result = hash.digest()
        n = 5
        if self.r >= 3:
            n = self.length // 8
            for _ in range(50):
                result = md5(result[:n]).digest()
        return result[:n]

    def authenticate(self, password: str) -> Optional[bytes]:
        password_bytes = password.encode("latin1")
        key = self.authenticate_user_password(password_bytes)
        if key is None:
            key = self.authenticate_owner_password(password_bytes)
        return key

    def authenticate_user_password(self, password: bytes) -> Optional[bytes]:
        key = self.compute_encryption_key(password)
        if self.verify_encryption_key(key):
            return key
        else:
            return None

    def verify_encryption_key(self, key: bytes) -> bool:
        # Algorithm 3.6
        u = self.compute_u(key)
        if self.r == 2:
            return u == self.u
        return u[:16] == self.u[:16]

    def authenticate_owner_password(self, password: bytes) -> Optional[bytes]:
        # Algorithm 3.7
        password = (password + PASSWORD_PADDING)[:32]
        hash = md5(password)
        if self.r >= 3:
            for _ in range(50):
                hash = md5(hash.digest())
        n = 5
        if self.r >= 3:
            n = self.length // 8
        key = hash.digest()[:n]
        if self.r == 2:
            user_password = Arcfour(key).decrypt(self.o)
        else:
            user_password = self.o
            for i in range(19, -1, -1):
                k = b"".join(bytes((c ^ i,)) for c in iter(key))
                user_password = Arcfour(k).decrypt(user_password)
        return self.authenticate_user_password(user_password)

    def decrypt(
        self,
        objid: int,
        genno: int,
        data: bytes,
        attrs: Optional[Dict[str, Any]] = None,
    ) -> bytes:
        return self.decrypt_rc4(objid, genno, data)

    def decrypt_rc4(self, objid: int, genno: int, data: bytes) -> bytes:
        assert self.key is not None
        key = self.key + struct.pack("<L", objid)[:3] + struct.pack("<L", genno)[:2]
        hash = md5(key)
        key = hash.digest()[: min(len(key), 16)]
        return Arcfour(key).decrypt(data)


class PDFStandardSecurityHandlerV4(PDFStandardSecurityHandler):
    """Security handler for encryption type 4."""

    supported_revisions: Tuple[int, ...] = (4,)

    def __init__(self, *args, **kwargs) -> None:
        if default_backend is None:
            raise PDFEncryptionError(
                "Encryption type requires the "
                "optional `cryptography` package. "
                "You may install it with `pip install playa-pdf[crypto]`."
            )
        super().__init__(*args, **kwargs)

    def init_params(self) -> None:
        super().init_params()
        self.length = 128
        self.cf = dict_value(self.param.get("CF"))
        self.stmf = literal_name(self.param["StmF"])
        self.strf = literal_name(self.param["StrF"])
        self.encrypt_metadata = bool(self.param.get("EncryptMetadata", True))
        if self.stmf != self.strf:
            error_msg = "Unsupported crypt filter: param=%r" % self.param
            raise PDFEncryptionError(error_msg)
        self.cfm = {}
        for k, v in self.cf.items():
            dictv = dict_value(v)
            f = self.get_cfm(literal_name(dictv["CFM"]))
            if f is None:
                error_msg = "Unknown crypt filter method: param=%r" % self.param
                raise PDFEncryptionError(error_msg)
            self.cfm[k] = f
        self.cfm["Identity"] = self.decrypt_identity
        if self.strf not in self.cfm:
            error_msg = "Undefined crypt filter: param=%r" % self.param
            raise PDFEncryptionError(error_msg)

    def get_cfm(self, name: str) -> Optional[Callable[[int, int, bytes], bytes]]:
        if name == "V2":
            return self.decrypt_rc4
        elif name == "AESV2":
            return self.decrypt_aes128
        else:
            return None

    def decrypt(
        self,
        objid: int,
        genno: int,
        data: bytes,
        attrs: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
    ) -> bytes:
        if not self.encrypt_metadata and attrs is not None:
            t = attrs.get("Type")
            if t is not None and literal_name(t) == "Metadata":
                return data
        if name is None:
            name = self.strf
        return self.cfm[name](objid, genno, data)

    def decrypt_identity(self, objid: int, genno: int, data: bytes) -> bytes:
        return data

    def decrypt_aes128(self, objid: int, genno: int, data: bytes) -> bytes:
        assert self.key is not None
        key = (
            self.key
            + struct.pack("<L", objid)[:3]
            + struct.pack("<L", genno)[:2]
            + b"sAlT"
        )
        hash = md5(key)
        key = hash.digest()[: min(len(key), 16)]
        initialization_vector = data[:16]
        ciphertext = data[16:]
        cipher = Cipher(
            algorithms.AES(key),
            modes.CBC(initialization_vector),
            backend=default_backend(),
        )  # type: ignore
        return cipher.decryptor().update(ciphertext)  # type: ignore


class PDFStandardSecurityHandlerV5(PDFStandardSecurityHandlerV4):
    """Security handler for encryption types 5 and 6."""

    supported_revisions = (5, 6)

    def __init__(self, *args, **kwargs) -> None:
        if default_backend is None:
            raise PDFEncryptionError(
                "Encryption type requires the "
                "optional `cryptography` package. "
                "You may install it with playa[crypto]."
            )
        super().__init__(*args, **kwargs)

    def init_params(self) -> None:
        super().init_params()
        self.length = 256
        self.oe = str_value(self.param["OE"])
        self.ue = str_value(self.param["UE"])
        self.o_hash = self.o[:32]
        self.o_validation_salt = self.o[32:40]
        self.o_key_salt = self.o[40:]
        self.u_hash = self.u[:32]
        self.u_validation_salt = self.u[32:40]
        self.u_key_salt = self.u[40:]

    def get_cfm(self, name: str) -> Optional[Callable[[int, int, bytes], bytes]]:
        if name == "AESV3":
            return self.decrypt_aes256
        else:
            return None

    def authenticate(self, password: str) -> Optional[bytes]:
        password_b = self._normalize_password(password)
        hash = self._password_hash(password_b, self.o_validation_salt, self.u)
        if hash == self.o_hash:
            hash = self._password_hash(password_b, self.o_key_salt, self.u)
            cipher = Cipher(
                algorithms.AES(hash),
                modes.CBC(b"\0" * 16),
                backend=default_backend(),
            )  # type: ignore
            return cipher.decryptor().update(self.oe)  # type: ignore
        hash = self._password_hash(password_b, self.u_validation_salt)
        if hash == self.u_hash:
            hash = self._password_hash(password_b, self.u_key_salt)
            cipher = Cipher(
                algorithms.AES(hash),
                modes.CBC(b"\0" * 16),
                backend=default_backend(),
            )  # type: ignore
            return cipher.decryptor().update(self.ue)  # type: ignore
        return None

    def _normalize_password(self, password: str) -> bytes:
        if self.r == 6:
            # saslprep expects non-empty strings, apparently
            if not password:
                return b""
            from playa._saslprep import saslprep

            password = saslprep(password)
        return password.encode("utf-8")[:127]

    def _password_hash(
        self,
        password: bytes,
        salt: bytes,
        vector: Optional[bytes] = None,
    ) -> bytes:
        """Compute password hash depending on revision number"""
        if self.r == 5:
            return self._r5_password(password, salt, vector)
        return self._r6_password(password, salt[0:8], vector)

    def _r5_password(
        self,
        password: bytes,
        salt: bytes,
        vector: Optional[bytes] = None,
    ) -> bytes:
        """Compute the password for revision 5"""
        hash = sha256(password)
        hash.update(salt)
        if vector is not None:
            hash.update(vector)
        return hash.digest()

    def _r6_password(
        self,
        password: bytes,
        salt: bytes,
        vector: Optional[bytes] = None,
    ) -> bytes:
        """Compute the password for revision 6"""
        initial_hash = sha256(password)
        initial_hash.update(salt)
        if vector is not None:
            initial_hash.update(vector)
        k = initial_hash.digest()
        hashes = (sha256, sha384, sha512)
        round_no = last_byte_val = 0
        while round_no < 64 or last_byte_val > round_no - 32:
            k1 = (password + k + (vector or b"")) * 64
            e = self._aes_cbc_encrypt(key=k[:16], iv=k[16:32], data=k1)
            # compute the first 16 bytes of e,
            # interpreted as an unsigned integer mod 3
            next_hash = hashes[self._bytes_mod_3(e[:16])]
            k = next_hash(e).digest()
            last_byte_val = e[len(e) - 1]
            round_no += 1
        return k[:32]

    @staticmethod
    def _bytes_mod_3(input_bytes: bytes) -> int:
        # 256 is 1 mod 3, so we can just sum 'em
        return sum(b % 3 for b in input_bytes) % 3

    def _aes_cbc_encrypt(self, key: bytes, iv: bytes, data: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()  # type: ignore
        return encryptor.update(data) + encryptor.finalize()  # type: ignore

    def decrypt_aes256(self, objid: int, genno: int, data: bytes) -> bytes:
        initialization_vector = data[:16]
        ciphertext = data[16:]
        assert self.key is not None
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(initialization_vector),
            backend=default_backend(),
        )  # type: ignore
        return cipher.decryptor().update(ciphertext)  # type: ignore


SECURITY_HANDLERS = {
    1: PDFStandardSecurityHandler,
    2: PDFStandardSecurityHandler,
    4: PDFStandardSecurityHandlerV4,
    5: PDFStandardSecurityHandlerV5,
}


def read_header(fp: BinaryIO) -> Tuple[str, int]:
    """Read the PDF header and return the (initial) version string and
    its position.

    Sets the file pointer to after the header (this is not reliable).

    Note that this version can be overridden in the document catalog.

    """
    try:
        hdr = fp.read(8)
        start = 0
    except IOError as err:
        raise PDFSyntaxError("Failed to read PDF header") from err
    if not hdr.startswith(b"%PDF-"):
        # Try harder... there might be some extra junk before it
        fp.seek(0, 0)
        hdr = fp.read(4096)  # FIXME: this is arbitrary...
        start = hdr.find(b"%PDF-")
        if start == -1:
            raise PDFSyntaxError("Could not find b'%%PDF-', is this a PDF?")
        hdr = hdr[start : start + 8]
        fp.seek(start + 8)
        log.debug("Found header at position %d: %r", start, hdr)
    try:
        version = hdr[5:].decode("ascii")
    except UnicodeDecodeError as err:
        raise PDFSyntaxError(
            "Version number in %r contains non-ASCII characters" % hdr
        ) from err
    if not re.match(r"\d\.\d", version):
        raise PDFSyntaxError("Version number in  %r is invalid" % hdr)
    return version, start


class OutlineItem(NamedTuple):
    """The most relevant fields of an outline item dictionary.

    Danger: Deprecated
        This interface is deprecated.  It will be removed in PLAYA 1.0.
    """

    level: int
    title: str
    dest: Union[PSLiteral, bytes, list, None]
    action: Union[dict, None]
    se: Union[ObjRef, None]


class Document:
    """Representation of a PDF document on disk.

    Since PDF documents can be very large and complex, merely creating
    a `Document` does very little aside from opening the file and
    verifying that the password is correct and it is, in fact, a PDF.
    This may, however, involve a certain amount of file access since
    the cross-reference table and trailer must be read in order to
    determine this (we do not treat linearized PDFs specially for the
    moment).

    Some metadata, such as the structure tree and page tree, will be
    loaded lazily and cached.  We do not handle modification of PDFs.

    Args:
      fp: File-like object in binary mode.  Will be read using
          `mmap` if possible, otherwise will be read into memory.
      password: Password for decryption, if needed.
      space: the device space to use for interpreting content ("screen"
             or "page")

    """

    _fp: Union[BinaryIO, None] = None
    _pages: Union["PageList", None] = None
    _pool: Union[Executor, None] = None
    _destinations: Union["Destinations", None] = None

    def __enter__(self) -> "Document":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        # If we were opened from a file then close it
        if self._fp:
            self._fp.close()
            self._fp = None
        # Shutdown process pool
        if self._pool:
            self._pool.shutdown()
            self._pool = None

    def __init__(
        self,
        fp: BinaryIO,
        password: str = "",
        space: DeviceSpace = "screen",
        _boss_id: int = 0,
    ) -> None:
        if _boss_id:
            # Set this **right away** because it is needed to get
            # indirect object references right.
            _set_document(self, _boss_id)
            assert in_worker()
        self.xrefs: List[XRef] = []
        self.space = space
        self.info = []
        self.catalog: Dict[str, Any] = {}
        self.encryption: Optional[Tuple[Any, Any]] = None
        self.decipher: Optional[DecipherCallable] = None
        self._cached_objs: Dict[int, PDFObject] = {}
        self._parsed_objs: Dict[int, Tuple[List[PDFObject], int]] = {}
        self._cached_fonts: Dict[object, Font] = {}
        if isinstance(fp, io.TextIOBase):
            raise TypeError("fp is not a binary file")
        # The header is frequently mangled, in which case we will try to read the
        # file anyway.
        try:
            self.pdf_version, self.offset = read_header(fp)
        except PDFSyntaxError:
            log.warning("PDF header not found, will try to read the file anyway")
            self.pdf_version = "UNKNOWN"
            self.offset = 0
        try:
            self.buffer: Union[bytes, mmap.mmap] = mmap.mmap(
                fp.fileno(), 0, access=mmap.ACCESS_READ
            )
        except io.UnsupportedOperation:
            log.warning("mmap not supported on %r, reading document into memory", fp)
            fp.seek(0, 0)
            self.buffer = fp.read()
        except ValueError:
            raise
        self.is_printable = self.is_modifiable = self.is_extractable = True
        # Getting the XRef table and trailer is done non-lazily
        # because they contain encryption information among other
        # things.  As noted above we don't try to look for the first
        # page cross-reference table (for linearized PDFs) after the
        # header, it will instead be loaded with all the rest.
        self.parser = IndirectObjectParser(self.buffer, self)
        self.parser.seek(self.offset)
        try:
            pos = self._find_xref()
            log.debug("Found xref at %d", pos)
            self._read_xref_from(pos, self.xrefs)
        except (ValueError, IndexError, StopIteration, PDFSyntaxError) as e:
            log.debug("Using fallback XRef parsing: %s", e)
            newxref = XRefFallback(self.parser)
            self.xrefs.append(newxref)
        # Now find the trailer
        for xref in self.xrefs:
            trailer = xref.trailer
            if not trailer:
                continue
            # If there's an encryption info, remember it.
            if "Encrypt" in trailer:
                if "ID" in trailer:
                    id_value = list_value(trailer["ID"])
                else:
                    # Some documents may not have a /ID, use two empty
                    # byte strings instead. Solves
                    # https://github.com/pdfminer/pdfminer.six/issues/594
                    id_value = (b"", b"")
                self.encryption = (id_value, dict_value(trailer["Encrypt"]))
                self._initialize_password(password)
            if "Info" in trailer:
                try:
                    self.info.append(dict_value(trailer["Info"]))
                except TypeError:
                    log.warning("Info is a broken reference (incorrect xref table?)")
            if "Root" in trailer:
                # Every PDF file must have exactly one /Root dictionary.
                try:
                    self.catalog = dict_value(trailer["Root"])
                except TypeError:
                    log.warning("Root is a broken reference (incorrect xref table?)")
                    self.catalog = {}
                break
        else:
            log.warning("No /Root object! - Is this really a PDF?")
        if self.catalog.get("Type") is not LITERAL_CATALOG:
            log.warning("Catalog not found!")
        if "Version" in self.catalog:
            log.debug(
                "Using PDF version %r from catalog instead of %r from header",
                self.catalog["Version"],
                self.pdf_version,
            )
            self.pdf_version = self.catalog["Version"]
        self.is_tagged = False
        markinfo = resolve1(self.catalog.get("MarkInfo"))
        if isinstance(markinfo, dict):
            self.is_tagged = not not markinfo.get("Marked")

    def _initialize_password(self, password: str = "") -> None:
        """Initialize the decryption handler with a given password, if any.

        Internal function, requires the Encrypt dictionary to have
        been read from the trailer into self.encryption.
        """
        assert self.encryption is not None
        (docid, param) = self.encryption
        if literal_name(param.get("Filter")) != "Standard":
            raise PDFEncryptionError("Unknown filter: param=%r" % param)
        v = int_value(param.get("V", 0))
        # 3 (PDF 1.4) An unpublished algorithm that permits encryption
        # key lengths ranging from 40 to 128 bits. This value shall
        # not appear in a conforming PDF file.
        if v == 3:
            raise PDFEncryptionError("Unpublished algorithm 3 not supported")
        factory = SECURITY_HANDLERS.get(v)
        # 0 An algorithm that is undocumented. This value shall not be used.
        if factory is None:
            raise PDFEncryptionError("Unknown algorithm: param=%r" % param)
        handler = factory(docid, param, password)
        self.decipher = handler.decrypt
        self.is_printable = handler.is_printable
        self.is_modifiable = handler.is_modifiable
        self.is_extractable = handler.is_extractable
        assert self.parser is not None
        # Ensure that no extra data leaks into encrypted streams
        self.parser.strict = True

    def __iter__(self) -> Iterator[IndirectObject]:
        """Iterate over top-level `IndirectObject` (does not expand object streams)"""
        return (obj for pos, obj in IndirectObjectParser(self.buffer, self))

    @property
    def objects(self) -> Iterator[IndirectObject]:
        """Iterate over all indirect objects (including, then expanding object
        streams)"""
        for pos, obj in IndirectObjectParser(self.buffer, self):
            yield obj
            if (
                isinstance(obj.obj, ContentStream)
                and obj.obj.get("Type") is LITERAL_OBJSTM
            ):
                parser = ObjectStreamParser(obj.obj, self)
                for spos, sobj in parser:
                    yield sobj

    @property
    def tokens(self) -> Iterator[Token]:
        """Iterate over tokens."""
        return (tok for pos, tok in Lexer(self.buffer))

    @property
    def structtree(self) -> StructTree:
        """Return the PDF structure tree.

        Danger: Deprecated
            This interface is deprecated.  It will be removed in PLAYA 1.0.
        """
        warnings.warn(
            "The `structtree` property is deprecated and will be removed in PLAYA 1.0."
            "  Use `structure` instead. ",
            DeprecationWarning,
        )
        return StructTree(self)

    @property
    def structure(self) -> Union[Tree, None]:
        """Logical structure of this document, if any.

        In the case where no logical structure tree exists, this will
        be `None`.  Otherwise you may iterate over it, search it, etc.
        """
        if "StructTreeRoot" not in self.catalog:
            return None
        return Tree(self)

    @property
    def parent_tree(self) -> Union[NumberTree, None]:
        """Parent tree of this document.

        This is a somewhat obscure data structure that links marked
        content sections to their corresponding structure elements.
        If you don't know what that means, you probably don't need it,
        but if you do, here it is.
        """
        if "StructTreeRoot" not in self.catalog:
            return None
        st = dict_value(self.catalog["StructTreeRoot"])
        if "ParentTree" not in st:
            return None
        return NumberTree(st["ParentTree"])

    def _getobj_objstm(
        self, stream: ContentStream, index: int, objid: int
    ) -> PDFObject:
        if stream.objid in self._parsed_objs:
            (objs, n) = self._parsed_objs[stream.objid]
        else:
            (objs, n) = self._get_objects(stream)
            assert stream.objid is not None
            self._parsed_objs[stream.objid] = (objs, n)
        i = n * 2 + index
        try:
            obj = objs[i]
        except IndexError:
            raise PDFSyntaxError("index too big: %r" % index)
        return obj

    def _get_objects(self, stream: ContentStream) -> Tuple[List[PDFObject], int]:
        if stream.get("Type") is not LITERAL_OBJSTM:
            log.warning("Content stream Type is not /ObjStm: %r" % stream)
        try:
            n = int_value(stream["N"])
        except KeyError:
            log.warning("N is not defined in content stream: %r" % stream)
            n = 0
        except TypeError:
            log.warning("N is invalid in content stream: %r" % stream)
            n = 0
        parser = ObjectParser(stream.buffer, self)
        objs: List[PDFObject] = [obj for _, obj in parser]
        return (objs, n)

    def _getobj_parse(self, pos: int, objid: int) -> PDFObject:
        assert self.parser is not None
        self.parser.seek(pos)
        try:
            _, obj = next(self.parser)
            if obj.objid != objid:
                raise PDFSyntaxError(f"objid mismatch: {obj.objid!r}={objid!r}")
        except (ValueError, IndexError, PDFSyntaxError) as e:
            log.warning(
                "Indirect object %d not found at position %d: %r", objid, pos, e
            )
            # In case of malformed pdf files where the offset in the
            # xref table doesn't point exactly at the object
            # definition (probably more frequent than you think), just
            # use a regular expression to find the object because we
            # can do that.
            realpos = -1
            lastgen = -1
            for m in re.finditer(rb"%d\s+(\d+)\s+obj" % objid, self.buffer):
                genno = int(m.group(1))
                if genno > lastgen:
                    lastgen = genno
                    realpos = m.start(0)
            if realpos == -1:
                raise PDFSyntaxError(
                    f"Indirect object {objid!r} not found in document"
                ) from e
            self.parser.seek(realpos)
            (_, obj) = next(self.parser)
        if obj.objid != objid:
            raise PDFSyntaxError(f"objid mismatch: {obj.objid!r}={objid!r}")
        if self.decipher:
            return decipher_all(self.decipher, obj.objid, obj.genno, obj.obj)
        return obj.obj

    def __getitem__(self, objid: int) -> PDFObject:
        """Get an indirect object from the PDF.

        Note that the behaviour in the case of a non-existent object,
        while Pythonic, is not PDFic, as PDF 1.7 sec 7.3.10 states:

        > An indirect reference to an undefined object shall not be
        considered an error by a conforming reader; it shall be
        treated as a reference to the null object.

        Raises:
          ValueError: if Document is not initialized
          IndexError: if objid does not exist in PDF
        """
        if not self.xrefs:
            raise ValueError("Document is not initialized")
        if objid not in self._cached_objs:
            obj = None
            for xref in self.xrefs:
                try:
                    (strmid, index, genno) = xref.get_pos(objid)
                except KeyError:
                    continue
                try:
                    if strmid is not None:
                        stream = stream_value(self[strmid])
                        obj = self._getobj_objstm(stream, index, objid)
                    else:
                        obj = self._getobj_parse(index, objid)
                    break
                # FIXME: We might not actually want to catch these...
                except StopIteration:
                    log.debug("EOF when searching for object %d", objid)
                    continue
                except PDFSyntaxError as e:
                    log.debug("Syntax error when searching for object %d: %s", objid, e)
                    continue
            if obj is None:
                raise IndexError(f"Object with ID {objid} not found")
            self._cached_objs[objid] = obj
        return self._cached_objs[objid]

    def get_font(self, objid: object, spec: Mapping[str, object]) -> Font:
        if objid and objid in self._cached_fonts:
            return self._cached_fonts[objid]
        if spec.get("Type") is not LITERAL_FONT:
            log.warning("Font specification Type is not /Font: %r", spec)
        # Create a Font object.
        if "Subtype" in spec:
            subtype = literal_name(spec["Subtype"])
        else:
            log.warning("Font specification Subtype is not specified: %r", spec)
            subtype = ""
        if subtype in ("Type1", "MMType1"):
            # Type1 Font
            font: Font = Type1Font(spec)
        elif subtype == "TrueType":
            # TrueType Font
            font = TrueTypeFont(spec)
        elif subtype == "Type3":
            # Type3 Font
            font = Type3Font(spec)
        elif subtype == "Type0":
            # Type0 Font
            dfonts = list_value(spec["DescendantFonts"])
            assert dfonts
            if len(dfonts) != 1:
                log.debug("Type 0 font should have 1 descendant, has more: %r", dfonts)
            subspec = dict_value(dfonts[0]).copy()
            # Merge the root and descendant font dictionaries
            for k in ("Encoding", "ToUnicode"):
                if k in spec:
                    subspec[k] = resolve1(spec[k])
            font = CIDFont(subspec)
        else:
            log.warning("Invalid Font spec, creating dummy font: %r" % spec)
            # We need a dummy font object to be able to do *something*
            # (even if it's the wrong thing) with text objects.
            font = Font({}, {})
        if objid:
            self._cached_fonts[objid] = font
        return font

    @property
    def outline(self) -> Union[Outline, None]:
        """Document outline, if any."""
        if "Outlines" not in self.catalog:
            return None
        return Outline(self)

    @property
    def outlines(self) -> Iterator[OutlineItem]:
        """Iterate over the PDF document outline.

        Danger: Deprecated
            This interface is deprecated.  It will be removed in PLAYA 1.0.
        """
        warnings.warn(
            "The `outlines` property is deprecated and will be removed in PLAYA 1.0.",
            DeprecationWarning,
        )
        if "Outlines" not in self.catalog:
            raise KeyError

        def search(entry: object, level: int) -> Iterator[OutlineItem]:
            entry = dict_value(entry)
            if "Title" in entry:
                if "A" in entry or "Dest" in entry:
                    title = decode_text(str_value(entry["Title"]))
                    dest = entry.get("Dest")
                    action = entry.get("A")
                    se = entry.get("SE")
                    yield OutlineItem(
                        level, title, resolve1(dest), resolve1(action), se
                    )
            if "First" in entry and "Last" in entry:
                yield from search(entry["First"], level + 1)
            if "Next" in entry:
                yield from search(entry["Next"], level)

        return search(self.catalog["Outlines"], 0)

    @property
    def page_labels(self) -> Iterator[str]:
        """Generate page label strings for the PDF document.

        If the document includes page labels, generates strings, one per page.
        If not, raise KeyError.

        The resulting iterator is unbounded (because the page label
        tree does not actually include all the pages), so it is
        recommended to use `pages` instead.

        Raises:
          KeyError: No page labels are present in the catalog

        """
        assert self.catalog is not None  # really it cannot be None

        page_labels = PageLabels(self.catalog["PageLabels"])
        return page_labels.labels

    PageType = Dict[Any, Dict[Any, Any]]

    def _get_pages_from_xrefs(self) -> Iterator[Tuple[int, PageType]]:
        """Find pages from the cross-reference tables if the page tree
        is missing (note that this only happens in invalid PDFs, but
        it happens.)

        Returns:
          an iterator over (objid, dict) pairs.
        """
        for xref in self.xrefs:
            for object_id in xref.objids:
                try:
                    obj = self[object_id]
                    if isinstance(obj, dict) and obj.get("Type") is LITERAL_PAGE:
                        yield object_id, obj
                except IndexError:
                    pass

    def _get_page_objects(self) -> Iterator[Tuple[int, PageType]]:
        """Iterate over the flattened page tree in reading order, propagating
        inheritable attributes.  Returns an iterator over (objid, dict) pairs.

        Raises:
          KeyError: if there is no page tree.
        """
        if "Pages" not in self.catalog:
            raise KeyError("No 'Pages' entry in catalog")
        stack = [(self.catalog["Pages"], self.catalog)]
        visited = set()
        while stack:
            (obj, parent) = stack.pop()
            if isinstance(obj, ObjRef):
                # The PDF specification *requires* both the Pages
                # element of the catalog and the entries in Kids in
                # the page tree to be indirect references.
                object_id = int(obj.objid)
            elif isinstance(obj, int):
                # Should not happen in a valid PDF, but probably does?
                log.warning("Page tree contains bare integer: %r in %r", obj, parent)
                object_id = obj
            else:
                log.warning("Page tree contains unknown object: %r", obj)
            page_object = dict_value(self[object_id])

            # Avoid recursion errors by keeping track of visited nodes
            # (again, this should never actually happen in a valid PDF)
            if object_id in visited:
                log.warning("Circular reference %r in page tree", obj)
                continue
            visited.add(object_id)

            # Propagate inheritable attributes
            object_properties = page_object.copy()
            for k, v in parent.items():
                if k in INHERITABLE_PAGE_ATTRS and k not in object_properties:
                    object_properties[k] = v

            # Recurse, depth-first
            object_type = object_properties.get("Type")
            if object_type is None:
                log.warning("Page has no Type, trying type: %r", object_properties)
                object_type = object_properties.get("type")
            if object_type is LITERAL_PAGES and "Kids" in object_properties:
                for child in reversed(list_value(object_properties["Kids"])):
                    stack.append((child, object_properties))
            elif object_type is LITERAL_PAGE:
                yield object_id, object_properties

    @property
    def pages(self) -> "PageList":
        """Pages of the document as an iterable/addressable `PageList` object."""
        if self._pages is None:
            self._pages = PageList(self)
        return self._pages

    @property
    def names(self) -> Dict[str, Any]:
        """PDF name dictionary (PDF 1.7 sec 7.7.4).

        Raises:
          KeyError: if nonexistent.
        """
        return dict_value(self.catalog["Names"])

    @property
    def destinations(self) -> "Destinations":
        """Named destinations as an iterable/addressable `Destinations` object."""
        if self._destinations is None:
            self._destinations = Destinations(self)
        return self._destinations

    @property
    def dests(self) -> Iterable[Tuple[str, list]]:
        """Iterable of named destinations as (name, destination) tuples
        (PDF 1.7 sec 12.3.2).

        Note that we assume the names of destinations are either "name
        objects" (that's PDF for UTF-8) or "text strings", since the
        PDF spec says (p. 367):

        > The keys in the name tree may be treated as text strings for
        > display purposes.

        therefore, you get them as `str`.

        Danger: Deprecated
            This interface is deprecated.  It will be removed in PLAYA 1.0.

        Raises:
          KeyError: if no destination tree exists
        """
        warnings.warn(
            "The `dests` property is deprecated and will be removed in PLAYA 1.0.",
            DeprecationWarning,
        )
        try:
            # PDF-1.2 or later
            dests = (
                (decode_text(k), resolve1(v)) for k, v in NameTree(self.names["Dests"])
            )
        except KeyError:
            # PDF-1.1 or prior
            dests = (
                (k, resolve1(v)) for k, v in dict_value(self.catalog["Dests"]).items()
            )
        for name, dest in dests:
            if isinstance(dest, dict):
                yield name, resolve1(dest["D"])
            else:
                yield name, dest

    def _find_xref(self) -> int:
        """Internal function used to locate the first XRef."""
        # search the last xref table by scanning the file backwards.
        prev = b""
        for pos, line in reverse_iter_lines(self.buffer):
            line = line.strip()
            if line == b"startxref":
                if not prev.isdigit():
                    log.warning("Invalid startxref position: %r", prev)
                    continue
                start = int(prev)
                if not start >= 0:
                    log.warning("Invalid negative startxref position: %d", start)
                    continue
                elif start > pos:
                    log.warning("Invalid startxref position (> %d): %d", pos, start)
                    continue
                return start + self.offset
            elif line == b"xref":
                return pos
            elif line == b"endobj":
                # Okay, we're probably not in Kansas anymore...
                break
            if line:
                prev = line
        raise ValueError("No xref table found at end of file")

    # read xref table
    def _read_xref_from(
        self,
        start: int,
        xrefs: List[XRef],
    ) -> None:
        """Reads XRefs from the given location."""
        parser = ObjectParser(self.buffer, self, start)
        try:
            (pos, token) = parser.nexttoken()
        except StopIteration:
            raise ValueError("Unexpected EOF at {start}")
        if token is KEYWORD_XREF:
            parser.nextline()
            xref: XRef = XRefTable(parser, self.offset)
        else:
            # It might be an XRefStream, if this is an indirect object...
            _, token = parser.nexttoken()
            _, token = parser.nexttoken()
            if token is KEYWORD_OBJ:
                # XRefStream: PDF-1.5
                self.parser.seek(pos)
                self.parser.reset()
                xref = XRefStream(self.parser, self.offset)
            else:
                # Well, maybe it's an XRef table without "xref" (but
                # probably not)
                parser.seek(pos)
                xref = XRefTable(parser, self.offset)
        xrefs.append(xref)
        trailer = xref.trailer
        # For hybrid-reference files, an additional set of xrefs as a
        # stream.
        if "XRefStm" in trailer:
            pos = int_value(trailer["XRefStm"])
            self._read_xref_from(pos + self.offset, xrefs)
        # Recurse into any previous xref tables or streams
        if "Prev" in trailer:
            # find previous xref
            pos = int_value(trailer["Prev"])
            self._read_xref_from(pos + self.offset, xrefs)


def call_page(func: Callable[[Page], Any], pageref: PageRef) -> Any:
    """Call a function on a page in a worker process."""
    return func(_deref_page(pageref))


class PageList:
    """List of pages indexable by 0-based index or string label."""

    def __init__(
        self, doc: Document, pages: Union[Iterable[Page], None] = None
    ) -> None:
        self.docref = _ref_document(doc)
        if pages is not None:
            self._pages = list(pages)
            self._labels: Dict[str, Page] = {
                page.label: page for page in pages if page.label is not None
            }
        else:
            self._init_pages(doc)

    def _init_pages(self, doc: Document) -> None:
        try:
            page_labels: Iterable[Union[str, None]] = doc.page_labels
        except (KeyError, ValueError):
            page_labels = (str(idx) for idx in itertools.count(1))
        self._pages = []
        self._objids = {}
        self._labels = {}
        try:
            page_objects = list(doc._get_page_objects())
        except (KeyError, IndexError, TypeError):
            page_objects = list(doc._get_pages_from_xrefs())
        for page_idx, ((objid, properties), label) in enumerate(
            zip(page_objects, page_labels)
        ):
            page = Page(doc, objid, properties, label, page_idx, doc.space)
            self._pages.append(page)
            self._objids[objid] = page
            if label is not None:
                if label in self._labels:
                    log.info("Duplicate page label %s at index %d", label, page_idx)
                else:
                    self._labels[label] = page

    @property
    def doc(self) -> "Document":
        """Get associated document if it exists."""
        return _deref_document(self.docref)

    def __len__(self) -> int:
        return len(self._pages)

    def __iter__(self) -> Iterator[Page]:
        return iter(self._pages)

    @overload
    def __getitem__(self, key: int) -> Page: ...

    @overload
    def __getitem__(self, key: str) -> Page: ...

    @overload
    def __getitem__(self, key: slice) -> "PageList": ...

    @overload
    def __getitem__(self, key: Iterable[int]) -> "PageList": ...

    @overload
    def __getitem__(self, key: Iterator[Union[int, str]]) -> "PageList": ...

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._pages[key]
        elif isinstance(key, str):
            return self._labels[key]
        elif isinstance(key, slice):
            return PageList(_deref_document(self.docref), self._pages[key])
        else:
            return PageList(_deref_document(self.docref), (self[k] for k in key))

    def by_id(self, objid: int) -> Page:
        """Get a page by its indirect object ID.

        Args:
            objid: Indirect object ID for the page object.

        Returns:
            the page in question.
        """
        return self._objids[objid]

    def map(self, func: Callable[[Page], Any]) -> Iterator:
        """Apply a function over each page, iterating over its results.

        Args:
            func: The function to apply to each page.

        Note:
            This possibly runs `func` in a separate process.  If its
            return value is not serializable (by `pickle`) then you
            will encounter errors.
        """
        doc = _deref_document(self.docref)
        if doc._pool is not None:
            return doc._pool.map(
                call_page,
                itertools.repeat(func),
                ((id(doc), page.page_idx) for page in self),
            )
        else:
            return (func(page) for page in self)


class PageLabels(NumberTree):
    """PageLabels from the document catalog.

    See Section 12.4.2 in the PDF 1.7 Reference.
    """

    @property
    def labels(self) -> Iterator[str]:
        itor = iter(self)
        try:
            start, label_dict_unchecked = next(itor)
            # The tree must begin with page index 0
            if start != 0:
                log.warning("PageLabels tree is missing page index 0")
                # Try to cope, by assuming empty labels for the initial pages
                start = 0
        except StopIteration:
            log.warning("PageLabels tree is empty")
            start = 0
            label_dict_unchecked = {}

        while True:  # forever!
            label_dict = dict_value(label_dict_unchecked)
            style = label_dict.get("S")
            prefix = decode_text(str_value(label_dict.get("P", b"")))
            first_value = int_value(label_dict.get("St", 1))

            try:
                next_start, label_dict_unchecked = next(itor)
            except StopIteration:
                # This is the last specified range. It continues until the end
                # of the document.
                values: Iterable[int] = itertools.count(first_value)
            else:
                range_length = next_start - start
                values = range(first_value, first_value + range_length)
                start = next_start

            for value in values:
                label = self._format_page_label(value, style)
                yield prefix + label

    @staticmethod
    def _format_page_label(value: int, style: Any) -> str:
        """Format page label value in a specific style"""
        if style is None:
            label = ""
        elif style is LIT("D"):  # Decimal arabic numerals
            label = str(value)
        elif style is LIT("R"):  # Uppercase roman numerals
            label = format_int_roman(value).upper()
        elif style is LIT("r"):  # Lowercase roman numerals
            label = format_int_roman(value)
        elif style is LIT("A"):  # Uppercase letters A-Z, AA-ZZ...
            label = format_int_alpha(value).upper()
        elif style is LIT("a"):  # Lowercase letters a-z, aa-zz...
            label = format_int_alpha(value)
        else:
            log.warning("Unknown page label style: %r", style)
            label = ""
        return label


class Destinations:
    """Mapping of named destinations.

    These either come as a NameTree or a dict, depending on the
    version of the PDF standard, so this abstracts that away.
    """

    dests_dict: Union[Dict[str, PDFObject], None] = None
    dests_tree: Union[NameTree, None] = None

    def __init__(self, doc: Document) -> None:
        self._docref = _ref_document(doc)
        self.dests: Dict[str, Destination] = {}
        if "Dests" in doc.catalog:
            # PDF-1.1: dictionary
            self.dests_dict = dict_value(doc.catalog["Dests"])
        elif "Names" in doc.catalog:
            names = dict_value(doc.catalog["Names"])
            if "Dests" in names:
                self.dests_tree = NameTree(names["Dests"])

    def __iter__(self) -> Iterator[str]:
        if self.dests_dict is not None:
            yield from self.dests_dict
        elif self.dests_tree is not None:
            for kb, _ in self.dests_tree:
                ks = decode_text(kb)
                yield ks

    def __getitem__(self, name: Union[bytes, str, PSLiteral]) -> Destination:
        if isinstance(name, bytes):
            name = decode_text(name)
        elif isinstance(name, PSLiteral):
            name = literal_name(name)
        if name in self.dests:
            return self.dests[name]
        elif self.dests_dict is not None:
            # This will raise KeyError or TypeError if necessary, so
            # we don't have to do it explicitly
            destlist = list_value(self.dests_dict[name])
            self.dests[name] = Destination.from_list(self.doc, destlist)
        elif self.dests_tree is not None:
            # This is not the most efficient, but we need to decode
            # the keys (and we cache the result...)
            for k, v in self.dests_tree:
                if decode_text(k) == name:
                    dest = resolve1(v)
                    if isinstance(dest, list):
                        self.dests[name] = Destination.from_list(self.doc, dest)
                    elif isinstance(dest, dict):
                        dest = list_value(resolve1(dest["D"]))
                        self.dests[name] = Destination.from_list(self.doc, dest)
                    break
        # This will also raise KeyError if necessary
        return self.dests[name]

    @property
    def doc(self) -> "Document":
        """Get associated document if it exists."""
        return _deref_document(self._docref)
