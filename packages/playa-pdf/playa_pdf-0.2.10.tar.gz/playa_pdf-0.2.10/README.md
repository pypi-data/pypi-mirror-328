# **P**arallel and **LA**z**Y** **A**nalyzer for **PDF** 🏖️

## About

There are already too many PDF libraries, unfortunately none of which
does everything that everybody wants it to do, and we probably don't
need another one. It is not recommended that you use this library for
anything at all, but if you were going to use it for something, it
would be specifically one of these things and nothing else:

1. Accessing the document catalog, page tree, structure tree, content
   streams, cross-reference table, XObjects, and other low-level PDF
   metadata.
2. Obtaining the absolute position and attributes of every character,
   line, path, and image in every page of a PDF.
   
If you just want to extract text from a PDF, there are a lot of better
and faster tools and libraries out there, see [these
benchmarks](https://github.com/py-pdf/benchmarks) for a summary (TL;DR
pypdfium2 is probably what you want, but pdfplumber does a nice job of
converting PDF to ASCII art).

The purpose of PLAYA is to provide an efficent, parallel and
parallelizable, pure-Python and Pythonic (for its author's definition
of the term), lazy interface to the internals of PDF files.

But yes, you *can* also extract text with PLAYA now.  This is fast compared
to other pure-Python libraries, slow compared to anything else, and I
can't guarantee that the output is any good.  On my Thinkpad X250
(Core i5-5300U circa 2015) I get these speeds when extracting the
zoning bylaw of my town (486 pages of tagged PDF), using `playa --text` on
the command-line:

| Tool | Time |
|------|------|
| pdfminer.six | 36.6s |
| pypdf | 17.7s |
| PLAYA (1 CPU) | 18.2s |
| PLAYA (1 CPU, PyPy 3.9) | 10.8s |
| PLAYA (2 CPUs) | 10.5s |
| pypdfium2 | 1.7s |
| Poppler | 1.6s |

Soon, this will get faster.  You will also be able to use
[PAVÉS](https://github.com/dhdaines/paves) for this and other
higher-level tasks, and it will be better, maybe.

## Installation

Installing it should be really simple as long as you have Python 3.8
or newer:

    pipx install playa-pdf

Yes it's not just "playa".  Sorry about that.  If you wish to read
certain encrypted PDFs then you will need the `crypto` add-on:

    pipx install playa-pdf[crypto]

## Usage

Do you want to get stuff out of a PDF?  You have come to the right
place!  Let's open up a PDF and see what's in it:

```python
pdf = playa.open("my_awesome_document.pdf")
raw_byte_stream = pdf.buffer
a_bunch_of_tokens = list(pdf.tokens)
a_bunch_of_indirect_objects = list(pdf)
```

The raw PDF tokens and objects are probably not terribly useful to
you, but you might find them interesting.  Note that these are
"indirect objects" where the actual object is accompanied by an object
number and generation number:

```python
for objid, genno, obj in pdf:
    ...
# or also
for obj in pdf:
    obj.objid, obj.genno, obj.obj
```

Also, these will only be the top-level objects and not those found
inside object streams (the streams are themselves indirect objects).
You can iterate over all indirect objects including object streams
using the `objects` property:

```python
for obj in pdf.objects:
    obj.objid, obj.genno, obj.obj
```

In this case it is possible you will encounter multiple objects with
the same `objid` due to the "incremental updates" feature of PDF.
Currently, iterating over the objects in a particular stream is
possible, but complicated.  It may be simplified in PLAYA 0.3.

You can also access indirect objects by number (this will return the
object with most recent generation number):

```python
a_particular_object = pdf[42]
```

Your PDF document probably has some pages.  How many?  What are their
numbers/labels?  They could be things like "xvi" (pronounced
"gzvee"), 'a", or "42", for instance!

```python
npages = len(pdf.pages)
page_numbers = [page.label for page in pdf.pages]
```

What's in the table of contents?  (NOTE: this API is deprecated and
will change soon as it is not Lazy nor does it properly represent the
hierarchy of the document outline)

```python
for entry in pdf.outlines:
    level, title, dest, action, struct_element = entry
    # or
    entry.level, entry.title, entry.dest, entry.action, entry.se
    ...
```

If you are lucky it has a "logical structure tree".  The elements here
might even be referenced from the table of contents!  (or, they might
not... with PDF you never know).  (NOTE: this API is deprecated and
will change soon as it is not Lazy at all)

```python
structure = pdf.structtree
for element in structure:
   for child in element:
       ...
```

Now perhaps we want to look at a specific page.  Okay!  You can also
look at its contents, more on that in a bit:

```python
page = pdf.pages[0]        # they are numbered from 0
page = pdf.pages["xviii"]  # but you can get them by label (a string)
page = pdf.pages["42"]     # or "logical" page number (also a string)
print(f"Page {page.label} is {page.width} x {page.height}")
```

## Accessing content

What are these "contents" of which you speak, which were surely
created by a Content Creator?  Well, you can look at the stream of
tokens or mysterious PDF objects:

```python
for token in page.tokens:
    ...
for object in page.contents:
    ...
```

But that isn't very useful, so you can also access actual textual and
graphical objects (if you wanted to, for instance, do layout
analysis).

```python
for item in page:
    ...
```

Because it is quite inefficient to expand, calculate, and copy every
possible piece of information, PLAYA gives you some options here.
Wherever possible this information can be computed lazily, but this
involves some more work on the user's part.

## Using multiple CPUs

You may be wondering, what does "Parallel and Lazy" really mean?
PLAYA allows you to take advantage of multiple CPUs, which can greatly
speed up some operations on large documents.  This parallelism
currently operates at the page level since this is the most logical
way to split up a PDF.  To enable it, pass the `max_workers` argument
to `playa.open` with the number of cores you wish to use (you can also
explicitly pass `None` to use the maximum):

```python
with playa.open(path, max_workers=4) as pdf:
    ...
```

Now, you can apply a function across the pages of the PDF in parallel
using the `map` method of `pdf.pages`, for example:

```python
def get_page_size(page: Page) -> Tuple[int, int]:
    return page.width, page.height

page_sizes = pdf.pages.map(get_page_size)
```

You could also just do this for certain pages by subscripting
`pdf.pages`:

```python
some_page_sizes = pdf.pages[2:5].map(get_page_size)
```

There are some limitations to this, because it uses `multiprocessing`.
The function you pass to `map` must be serializable by `pickle`, which
in practice means that an inner function or lambda generally doesn't
work.  You can get around this in a very Java-like way by passing a
callable object that encapsulates the necessary state.  If you wish to
avoid traumatising readers of your code, then use `functools.partial`
instead:

```python
pdf.pages.map(partial(myfunc, arg1=value1, arg2=value2))
```

Also, any value returned by your function must also be serializable.
There is a bit of magic that enables this to work for PDF objects
containing indirect object references, so you should be able to, for
instance, get the `dests` or `annots` from every page without any
trouble.  But if you have your own complex objects that you return you
may encounter problems (or slowness).

## Dictionary-based API

There used to be a "dictionary-based" API here.  You can now find it
in [PAVÉS](https://github.com/dhdaines/paves).

## An important note about coordinate spaces

Wait, what is this "absolute position" of which you speak, and which
PLAYA gives you?  It's important to understand that there is no
definition of "device space" in the PDF standard, and I quote (PDF 1.7
sec 8.3.2.2):

> A particular device’s coordinate system is called its device
space. The origin of the device space on different devices can fall in
different places on the output page; on displays, the origin can vary
depending on the window system. Because the paper or other output
medium moves through different printers and imagesetters in different
directions, the axes of their device spaces may be oriented
differently.

You may immediately think of CSS when you hear the phrase "absolute
position" and this is exactly what PLAYA gives you as its default
device space, specifically:

- Units are default user space units (1/72 of an inch).
- `(0, 0)` is the top-left corner of the page, as defined by its
  `MediaBox` after rotation is applied.
- Coordinates increase from the top-left corner of the page towards
  the bottom-right corner.

However, for compatibility with `pdfminer.six`, you can also pass
`space="page"` to `playa.open`.  In this case, `(0, 0)` is the
bottom-left corner of the page as defined by the `MediaBox`, after
rotation, and coordinates increase from the bottom-left corner of the
page towards the top-right, as they do in PDF user space.

If you don't care about absolute positioning, you can use
`space="default"`, which may be somewhat faster in the future (currently
it isn't).  In this case, no translation or rotation of the default
user space is done (in other words any values of `MediaBox` or
`Rotate` in the page dictionary are simply ignored).  This is **definitely**
what you want if you wish to take advantage of the coordinates that
you may find in `outlines`, `dests`, tags and logical structure
elements.

## Lazy object API

Fundamentally you may just want to know *what* is *where* on the page,
and PLAYA has you covered there (note that the bbox is normalized, and
in the aforementioned interpretation of "device space"):

```python
for obj in page:
    print(f"{obj.object_type} at {obj.bbox}")
    left, top, right, bottom = obj.bbox
    print(f"  top left is {left, top}")
    print(f"  bottom right is {right, botom}")
```

Another important piece of information (which `pdfminer.six` does not
really handle) is the relationship between layout and logical
structure, done using *marked content sections*:

```python
for obj in page:
    print(f"{obj.object_type} is in marked content section {obj.mcs.mcid}")
    print(f"    which is tag {obj.mcs.tag.name}")
    print(f"    with properties {obj.mcs.tag.props}")
```

The `mcid` here is the same one referenced in elements of the
structure tree as shown above (but remember that `tag` has nothing to
do with the structure tree element, because Reasons).  A marked
content section does not necessarily have a `mcid` or `props`, but it
will *always* have a `tag`.

PDF also has the concept of "marked content points". PLAYA suports
these with objects of `object_type == "tag"`.  The tag name and
properties are also accessible via the `mcs` attribute.

### Form XObjects

A PDF page may also contain "Form XObjects" which are like tiny
embedded PDF documents (they have nothing to do with fillable forms).
The lazy API (because it is lazy) **will not expand these for you**
which may be a source of surprise.  You can identify them because they
have `object_type == "xobject"`.  The layout objects inside them are
accessible by iteration, as with pages (but **not** documents):

```python
for obj in page:
    if obj.object_type == "xobject":
        for item in obj:
            ...
```

You can also iterate over them in the page context with `page.xobjects`:

```python
for xobj in page.xobjects:
    for item in xobj:
        ...
```

Exceptionally, these have a few more features than the ordinary
`ContentObject` - you can look at their raw stream contents as well as
the tokens, and you can also see raw, mysterious PDF objects with
`contents`.

### Graphics state

You may also wish to know what color an object is, and other aspects of
what PDF refers to as the *graphics state*, which is accessible
through `obj.gstate`.  This is a mutable object, and since there are
quite a few parameters in the graphics state, PLAYA does not create a
copy of it for every object in the layout - you are responsible for
saving them yourself if you should so desire.  This is not
particularly onerous, because the parameters themselves are immutable:

```python
for obj in page:
    print(f"{obj.object_type} at {obj.bbox} is:")
    print(f"    {obj.gstate.scolor} stroking color")
    print(f"    {obj.gstate.ncolor} non-stroking color")
    print(f"    {obj.gstate.dash} dashing style")
    my_stuff = (obj.dash, obj.gstate.scolor, obj.gstate.ncolor)
    other_stuff.append(my_stuff)  # it's safe there
```

For compatibility with `pdfminer.six`, PLAYA, even though it is not a
layout analyzer, can do some basic interpretation of paths.  Again,
this is lazy.  If you don't care about them, you just get objects with
`object_type` of `"path"`, which you can ignore.  PLAYA won't even
compute the bounding box (which isn't all that slow, but still).  If
you *do* care, then you have some options.  You can look at the actual
path segments in user space (fast):

```python
for seg in path.raw_segments:
   print(f"segment: {seg}")
```

Or in PLAYA's "device space" (not so fast):

```python
for seg in path.segments:
   print(f"segment: {seg}")
```

This API doesn't try to interpret paths for you.  You only get
`PathSegment`s.  But for convenience you can get them grouped by
subpaths as created using the `m` or `re` operators:

```python
for subpath in path:
   for seg in subpath.segments:
       print(f"segment: {seg}")
```

### Text Objects

Since most PDFs consist primarily of text, obviously you may wish to
know something about the actual text (or the `ActualText`, which you
can sometimes find in `obj.mcs.tag.props["ActualText"]`).  This is
more difficult than it looks, as fundamentally PDF just positions
arbitrarily numbered glyphs on a page, and the vast majority of PDFs
embed their own fonts, using *subsetting* to include only the glyphs
actually used.

Whereas `pdfminer.six` would break down text objects into their
individual glyphs (which might or might not correspond to characters),
this is not always what you want, and moreover it is computationally
quite expensive.  So PLAYA, by default, does not do this.  If you
don't need to know the actual bounding box of a text object, then
don't access `obj.bbox` and it won't be computed.  If you don't need
to know the position of each glyph but simply want the Unicode
characters, then just look at `obj.chars`.

It is also important to understand that `obj.chars` may or may not
correspond to the actual text that a human will read on the page.  To
actually extract *text* from a PDF necessarily involves Heuristics or
Machine Learning (yes, capitalized, like that) and PLAYA does not do
either of those things.

This is because PDFs, especially ones produced by OCR, don't organize
text objects in any meaningful fashion, so you will want to actually
look at the glyphs.  This becomes a matter of iterating over the item,
giving you, well, more items, which are the individual glyphs:

```python
for glyph in item:
    print("Glyph has CID {glyph.cid} and Unicode {glyph.text}")
```

Note that the actual positioning of the glyphs is only done once you
actually look at their `bbox` property, so for instance, if you wish
to ignore glyphs with `textstate.render_mode == 3` (which means
"invisible") or `gstate.scolor.values == (1.0,)` (which means "written
in white ink") then you could do that.

PDF has the concept of a *text state* which determines some aspects of
how text is rendered.  You can obviously access this though
`glyph.textstate` - note that the text state, like the graphics state,
is mutable, so you will have to copy it or save individual parameters
that you might care about.  This may be a major footgun so watch out.

PLAYA doesn't guarantee that text objects come at you in anything
other than the order they occur in the file (but it does guarantee
that).

### An important note about text objects

But wait!  What do we mean by "Text Objects"?  What is "text", anyway?
While philosophers have debated this question for millennia, PDF has a
somewhat more precise definition (PDF 1.7, sec 9.4.1):

> A PDF text object consists of operators that may show text strings,
move the text position, and set text state and certain other
parameters ... A text object begins with the `BT` operator and ends with
the `ET` operator ... specific categories of text-related operators may
appear in a text object ...

Except that this is not entirely true!  Many *other* operators may
also appear in a text object (PDF 1.7, sec 8.2, table 9):

> Text object: Allowed operators:
>
> - General graphics state
> - Color
> - Text state
> - Text-showing
> - Text-positioning
> - Marked-content

In other words, as usual:

![Adobe is Spiderman](./docs/adobe-spiderman.jpg)

In particular, we care **a lot** about marked content operators, because
of the abovementioned `ActualText` property.  For this reason a
`TextObject` in PLAYA **does not** and **will never** correspond to a
PDF text object as defined by the `BT` and `ET` operators.  For the
moment, every text-showing operator triggers a new `TextObject`.  It
is possible (though unlikely) that in the future, only changes in marked
content or graphics state will do this.

## Conclusion

As mentioned earlier, if you really just want to do text extraction,
there's always pdfplumber, pymupdf, pypdfium2, pikepdf, pypdf, borb,
etc, etc, etc.

## Acknowledgement

This repository obviously includes code from `pdfminer.six`.  Original
license text is included in
[LICENSE](https://github.com/dhdaines/playa/blob/main/LICENSE).  The
license itself has not changed!
