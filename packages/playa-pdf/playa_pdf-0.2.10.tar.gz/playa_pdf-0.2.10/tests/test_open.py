"""
Test basic opening and navigation of PDF documents.
"""

from csv import DictWriter
from io import StringIO
from pathlib import Path

import pytest

try:
    import pdfminer
except ImportError:
    pdfminer = None  # type: ignore
import playa
from playa.exceptions import PDFEncryptionError
from .data import TESTDIR, BASEPDFS, PASSWORDS, XFAILS, CONTRIB

# We know pdfminer.six gives different output for these and we don't
# care (generally because of PLAYA's better rectangle detection and
# correct bboxes for rotated glyphs)
PDFMINER_BUGS = {
    "issue-449-vertical.pdf",
    "issue_495_pdfobjref.pdf",
    "issue-886-xref-stream-widths.pdf",
    "issue-1004-indirect-mediabox.pdf",
    "issue-1008-inline-ascii85.pdf",
    "issue-1059-cmap-decode.pdf",
    "issue-1062-filters.pdf",
    "rotated.pdf",
    "issue-1114-dedupe-chars.pdf",
    "malformed-from-issue-932.pdf",
    "mcid_example.pdf",
    "utf8_tounicode.pdf",
    "utf16_tounicode.pdf",
    "ascii_tounicode.pdf",
    "duplicate_encoding_tounicode.pdf",
}


# Only do "base" PDFs as we know pdfminer has issues with others
# warnings.capture_warnings does not work in pytest because Reasons
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.skipif(pdfminer is None, reason="pdfminer.six is not installed")
@pytest.mark.parametrize("path", BASEPDFS, ids=str)
def test_open(path: Path) -> None:
    """Open all the documents and compare with pdfminer"""
    if path.name in XFAILS:
        pytest.xfail("Intentionally corrupt file: %s" % path.name)
    from pdfminer.converter import PDFPageAggregator
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser

    def convert_miner(layout):
        for ltitem in layout:
            itype = type(ltitem).__name__.lower()[2:]
            if itype == "figure":
                yield from convert_miner(ltitem)
            else:
                yield (itype, ltitem.bbox)

    passwords = PASSWORDS.get(path.name, [""])
    for password in passwords:
        miner = []
        with open(path, "rb") as infh:
            if path.name in PDFMINER_BUGS:
                pytest.skip("pdfminer.six has a bug, skipping %s" % path.name)
                break
            try:
                rsrc = PDFResourceManager()
                agg = PDFPageAggregator(rsrc, pageno=1)
                interp = PDFPageInterpreter(rsrc, agg)
                pdf = PDFDocument(PDFParser(infh), password=password)
                for pdfpage in PDFPage.create_pages(pdf):
                    interp.process_page(pdfpage)
                    layout = agg.result
                    if layout is not None:
                        miner.extend(convert_miner(layout))
            except Exception:
                continue

        beach = []
        try:
            with playa.open(path, password=password, space="page") as doc:
                for page in doc.pages:
                    for item in page.layout:
                        bbox = (item["x0"], item["y0"], item["x1"], item["y1"])
                        beach.append((item["object_type"], bbox))
        except PDFEncryptionError:
            pytest.skip("cryptography package not installed")

        assert beach == miner


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.skipif(not CONTRIB.exists(), reason="contrib samples not present")
def test_inline_data() -> None:
    with playa.open(CONTRIB / "issue-1008-inline-ascii85.pdf") as doc:
        page = doc.pages[0]
        items = list(page.layout)
        assert len(items) == 456


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.skipif(not CONTRIB.exists(), reason="contrib samples not present")
def test_redundant_h() -> None:
    with playa.open(CONTRIB / "issue-1008-inline-ascii85.pdf") as doc:
        page = doc.pages[0]
        rects = [item for item in page.layout if item["object_type"] == "rect"]
        assert len(rects) == 6


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_multiple_contents() -> None:
    with playa.open(TESTDIR / "jo.pdf") as doc:
        page = doc.pages[0]
        assert len(list(page.contents)) > 1
        items = list(page.layout)
        assert len(items) == 898


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.skipif(not CONTRIB.exists(), reason="contrib samples not present")
def test_xobjects() -> None:
    with playa.open(CONTRIB / "basicapi.pdf") as doc:
        objs = [obj for obj in doc.layout if obj.get("xobjid")]
    assert objs
    assert objs[0]["xobjid"] == "XT5"


def test_weakrefs() -> None:
    """Verify that PDFDocument really gets deleted even if we have
    PDFObjRefs hanging around."""
    with playa.open(TESTDIR / "simple5.pdf") as doc:
        ref = doc.catalog["Pages"]
    del doc
    with pytest.raises(RuntimeError):
        _ = ref.resolve()


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_write_csv() -> None:
    """Verify that we can easily write to a CSV file."""
    with playa.open(TESTDIR / "simple1.pdf") as doc:
        out = StringIO()
        writer = DictWriter(out, fieldnames=playa.fieldnames)
        writer.writeheader()
        writer.writerows(doc.layout)
        assert out.getvalue()
        # print(out.getvalue())


@pytest.mark.skipif(not CONTRIB.exists(), reason="contrib samples not present")
def test_spaces() -> None:
    """Test different coordinate spaces."""
    with playa.open(CONTRIB / "issue-1181.pdf", space="page") as doc:
        page = doc.pages[0]
        page_box = next(iter(page)).bbox
    with playa.open(CONTRIB / "issue-1181.pdf", space="default") as doc:
        page = doc.pages[0]
        user_box = next(iter(page)).bbox
    assert page_box[1] == pytest.approx(user_box[1] - page.mediabox[1])
    with playa.open(CONTRIB / "issue-1181.pdf", space="screen") as doc:
        page = doc.pages[0]
        screen_box = next(iter(page)).bbox
    # BBoxes are normalied, so top is 1 for screen and 3 for page
    assert screen_box[3] == pytest.approx(page.height - page_box[1])
    assert screen_box[3] == pytest.approx(page.height - page_box[1])


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_glyph_offsets() -> None:
    """Verify that glyph_offset is what we say it is."""
    # screen space
    with playa.open(TESTDIR / "simple3.pdf", space="screen") as doc:
        glyph_x = 0.0
        glyph_y = 0.0
        for dic in doc.layout:
            if dic["text"] == "e":  # e as in Hello
                assert dic["glyph_offset_x"] > glyph_x
            elif dic["text"] == "い":  # あ as in あいうえお
                assert dic["glyph_offset_y"] > glyph_y
            glyph_x = dic["glyph_offset_x"]
            glyph_y = dic["glyph_offset_y"]
    # page / user space
    with playa.open(TESTDIR / "simple3.pdf", space="page") as doc:
        glyph_x = 0.0
        glyph_y = 0.0
        for dic in doc.layout:
            if dic["text"] == "e":  # e as in Hello
                assert dic["glyph_offset_x"] > glyph_x
            elif dic["text"] == "い":  # あ as in あいうえお
                assert dic["glyph_offset_y"] < glyph_y
            glyph_x = dic["glyph_offset_x"]
            glyph_y = dic["glyph_offset_y"]


def test_tiff_predictor() -> None:
    with playa.open(TESTDIR / "test_pdf_with_tiff_predictor.pdf") as doc:
        image = next(doc.pages[0].images)
        # Decoded TIFF: 600 x 600 + a header
        assert len(image.stream.buffer) == 360600
