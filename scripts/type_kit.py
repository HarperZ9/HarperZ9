"""Set text as vector outlines from the Accession font files.

GitHub shows the profile art through <img>, where no web font loads, so a
font-family name alone falls back to the viewer's system face. This module
reads glyph outlines, advances and pair kerning from the Accession files in
docs/brand/fonts (SIL Open Font License 1.1, OFL.txt beside them). Each glyph
a picture uses is written once as a path in <defs>, and each run of text
places those glyphs with <use>, so every viewer sees the same letters.

Needs fontTools (pinned in the workflows). Output is deterministic: the same
font files and the same text give the same bytes.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from fontTools.pens.basePen import BasePen
from fontTools.ttLib import TTFont

FONTS = Path(__file__).resolve().parents[1] / "docs" / "brand" / "fonts"

# Role to file. The roles follow the site's face tokens: Display for the name,
# Text for running words, Mono for addresses, labels and badges.
FACES = {
    "display": "AccessionDisplay-Bold.ttf",
    "text": "AccessionText-Regular.ttf",
    "mono": "AccessionMono-Regular.ttf",
    "mono-bold": "AccessionMono-Bold.ttf",
}


def num(value: float) -> str:
    """Two decimals at most, with trailing zeros and a bare minus zero removed."""
    out = f"{value:.2f}".rstrip("0").rstrip(".")
    return "0" if out in ("-0", "") else out


class _PathPen(BasePen):
    """Collects one glyph as relative SVG path commands in font units, y down."""

    def __init__(self, glyph_set) -> None:
        super().__init__(glyph_set)
        self.parts: list[str] = []
        self.at = (0.0, 0.0)

    def _rel(self, points: list[tuple[float, float]]) -> str:
        """Each point relative to the current point, with no spare separators."""
        out = ""
        for x, y in points:
            for value in (x - self.at[0], self.at[1] - y):
                text = num(value)
                out += text if text.startswith("-") or not out else " " + text
        self.at = points[-1]
        return out

    def _moveTo(self, pt) -> None:
        self.parts.append(f"M{num(pt[0])} {num(-pt[1])}")
        self.at = pt

    def _lineTo(self, pt) -> None:
        self.parts.append("l" + self._rel([pt]))

    def _qCurveToOne(self, pt1, pt2) -> None:
        self.parts.append("q" + self._rel([pt1, pt2]))

    def _curveToOne(self, pt1, pt2, pt3) -> None:
        self.parts.append("c" + self._rel([pt1, pt2, pt3]))

    def _closePath(self) -> None:
        self.parts.append("z")

    def _endPath(self) -> None:
        self.parts.append("z")


class Face:
    """One font file: character map, advances, outlines and pair kerning."""

    def __init__(self, path: Path) -> None:
        if not path.is_file():
            raise FileNotFoundError(f"font file missing: {path}")
        self.font = TTFont(str(path))
        self.upm = self.font["head"].unitsPerEm
        self.cmap = self.font.getBestCmap()
        self.glyphs = self.font.getGlyphSet()
        self.advances = self.font["hmtx"].metrics
        self.pair_tables = self._pair_tables()
        self._kern_cache: dict[tuple[str, str], int] = {}
        self._path_cache: dict[str, str] = {}

    def _pair_tables(self) -> list:
        """PairPos subtables reached from the kern feature, in lookup order."""
        if "GPOS" not in self.font:
            return []
        table = self.font["GPOS"].table
        if not table.FeatureList or not table.LookupList:
            return []
        indices = sorted({
            index
            for record in table.FeatureList.FeatureRecord
            if record.FeatureTag == "kern"
            for index in record.Feature.LookupListIndex
        })
        out = []
        for index in indices:
            lookup = table.LookupList.Lookup[index]
            subtables = [
                sub.ExtSubTable if lookup.LookupType == 9 else sub
                for sub in lookup.SubTable
            ]
            pairs = [sub for sub in subtables if type(sub).__name__ == "PairPos"]
            if pairs:
                out.append(pairs)
        return out

    def kern(self, left: str, right: str) -> int:
        """Horizontal adjustment between two glyphs, in font units."""
        key = (left, right)
        if key not in self._kern_cache:
            self._kern_cache[key] = sum(self._lookup_kern(subs, left, right) for subs in self.pair_tables)
        return self._kern_cache[key]

    @staticmethod
    def _lookup_kern(subtables: list, left: str, right: str) -> int:
        # Within one lookup the first subtable that covers the pair decides.
        for sub in subtables:
            if left not in sub.Coverage.glyphs:
                continue
            if sub.Format == 1:
                pair_set = sub.PairSet[sub.Coverage.glyphs.index(left)]
                for record in pair_set.PairValueRecord:
                    if record.SecondGlyph == right:
                        value = record.Value1
                        return (value.XAdvance or 0) if value is not None else 0
                continue
            class1 = sub.ClassDef1.classDefs.get(left, 0)
            class2 = sub.ClassDef2.classDefs.get(right, 0)
            value = sub.Class1Record[class1].Class2Record[class2].Value1
            return (getattr(value, "XAdvance", 0) or 0) if value is not None else 0
        return 0

    def glyph_names(self, body: str) -> list[str]:
        names = []
        for char in body:
            name = self.cmap.get(ord(char))
            if name is None:
                raise ValueError(f"Accession has no glyph for {char!r} in {body!r}")
            names.append(name)
        return names

    def layout(self, body: str, size: float, spacing: float = 0) -> tuple[list[tuple[str, float]], float]:
        """Glyph names with their x offsets in font units, and the width in pixels."""
        scale = size / self.upm
        names = self.glyph_names(body)
        placed, x = [], 0.0
        for i, name in enumerate(names):
            if i:
                x += self.kern(names[i - 1], name) + spacing / scale
            placed.append((name, x))
            x += self.advances[name][0]
        return placed, x * scale

    def glyph_path(self, name: str) -> str:
        """One glyph as path data in font units, baseline at y = 0."""
        if name not in self._path_cache:
            pen = _PathPen(self.glyphs)
            self.glyphs[name].draw(pen)
            self._path_cache[name] = "".join(pen.parts)
        return self._path_cache[name]


@lru_cache(maxsize=None)
def face(role: str) -> Face:
    return Face(FONTS / FACES[role])


def width(body: str, size: float, role: str = "text", spacing: float = 0) -> float:
    return face(role).layout(body, size, spacing)[1]


# Glyphs used since the last glyph_defs() call, as (role, glyph name) -> id.
_used: dict[tuple[str, str], str] = {}


def _glyph_id(role: str, name: str) -> str:
    key = (role, name)
    if key not in _used:
        _used[key] = f"a{len(_used)}"
    return _used[key]


def outline(body: str, x: float, y: float, size: float, fill: str, *, role: str = "text",
            anchor: str = "start", spacing: float = 0, opacity: float = 1) -> str:
    """One <g> placing the glyphs of a run of text, baseline at y.

    The picture must also carry glyph_defs(), called once after its last text.
    """
    font = face(role)
    placed, total = font.layout(body, size, spacing)
    if anchor == "middle":
        x -= total / 2
    elif anchor == "end":
        x -= total
    scale = size / font.upm
    extra = f' fill-opacity="{opacity}"' if opacity != 1 else ""
    uses = "".join(
        f'<use href="#{_glyph_id(role, name)}"' + (f' x="{num(offset)}"' if offset else "") + "/>"
        for name, offset in placed
        if font.glyph_path(name)
    )
    return (
        f'<g transform="translate({num(x)} {num(y)}) scale({scale:.5f})" '
        f'fill="{fill}"{extra}>{uses}</g>'
    )


def glyph_defs() -> str:
    """<defs> for every glyph placed since the last call; empty when none were."""
    if not _used:
        return ""
    paths = "".join(
        f'<path id="{glyph_id}" d="{face(role).glyph_path(name)}"/>'
        for (role, name), glyph_id in _used.items()
    )
    _used.clear()
    return f"<defs>{paths}</defs>"
