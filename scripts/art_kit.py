"""Shared drawing kit for the profile art.

Every figure is generated from code. The drawing uses the standard library;
the lettering is set by type_kit.py, which needs fontTools and the Accession
files in docs/brand/fonts. The output is deterministic: the same seed, palette
and font files give the same bytes, so a reviewer can regenerate any panel and
diff it.

Palette values and faces come from the site's shared kit: wall, ink,
soft, line, verdict colours and the three primaries from system/kit/kit.css,
and the six platform inks from world/site/crossover/colour-tokens.json. The
primaries appear only as the single flare on the aperture rim.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from type_kit import outline


@dataclass(frozen=True)
class Palette:
    name: str
    ground: str
    ink: str
    soft: str
    line: str
    verified: str
    drift: str
    unverifiable: str
    glow: str
    primaries: tuple[str, str, str]
    platforms: tuple[str, ...]


DARK = Palette(
    name="dark",
    ground="#0a0a0c",
    ink="#ece5d6",
    soft="#b8b0a0",
    line="#2e2c31",
    verified="#63d4ce",
    drift="#e29472",
    unverifiable="#b3b1e6",
    glow="#f6e7c4",
    primaries=("#e2584a", "#e3b25a", "#8e9be6"),
    platforms=("#c8ab90", "#99b4d1", "#adb885", "#81bfb7", "#aea6f0", "#e395bb"),
)

LIGHT = Palette(
    name="light",
    ground="#e8e3d9",
    ink="#16130f",
    soft="#4a443b",
    line="#c4baa6",
    verified="#0a6b61",
    drift="#8f3a19",
    unverifiable="#4e4d85",
    glow="#16130f",
    primaries=("#c8322b", "#d79e35", "#1d2562"),
    platforms=("#7a6047", "#405871", "#889261", "#427f78", "#8a81c8", "#bb7196"),
)

PALETTES = (DARK, LIGHT)

# Platform order for Palette.platforms: The Flywheel, Articulate, The Commons,
# The Playground, BuildLang, Research.

# Lettering follows the site's face roles: Accession Display for the name,
# Accession Text for running words, Accession Mono for addresses and labels.
# GitHub shows the art through <img>, where no font loads, so every letter is
# drawn as an outline taken from the font files (see type_kit.py).


class Rng:
    """Small linear congruential generator so output never depends on random."""

    def __init__(self, seed: int) -> None:
        self.state = seed & 0xFFFFFFFF

    def next(self) -> float:
        self.state = (1664525 * self.state + 1013904223) & 0xFFFFFFFF
        return self.state / 0x100000000


def field(theta: float, phases: list[float]) -> float:
    """A smooth closed field around the circle, in the range 0 to 1."""
    total = 0.0
    for k, phase in enumerate(phases, start=2):
        total += math.sin(k * theta + phase) / k
    norm = sum(1 / k for k in range(2, len(phases) + 2))
    return 0.5 + 0.5 * total / norm


def f(value: float) -> str:
    """Format a coordinate compactly."""
    text = f"{value:.1f}"
    return text[:-2] if text.endswith(".0") else text


def style_block(extra: str = "") -> str:
    """Motion lives in CSS so prefers-reduced-motion can stop all of it.

    SMIL animation ignores that media query, so the art uses CSS keyframes.
    """
    return (
        "<style>"
        "@keyframes spin{to{transform:rotate(360deg)}}"
        "@keyframes spinr{to{transform:rotate(-360deg)}}"
        "@keyframes breathe{0%,100%{opacity:.55}50%{opacity:1}}"
        "@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}"
        ".spin{transform-box:view-box;animation:spin 240s linear infinite}"
        ".spinr{transform-box:view-box;animation:spinr 360s linear infinite}"
        ".breathe{animation:breathe 7s ease-in-out infinite}"
        ".drift{animation:drift 9s ease-in-out infinite}"
        f"{extra}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
        "</style>"
    )


def defs(p: Palette, uid: str) -> str:
    """Grain veil, scanlines and the core glow."""
    return (
        "<defs>"
        f'<filter id="grain-{uid}" x="0" y="0" width="100%" height="100%">'
        '<feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/>'
        '<feColorMatrix type="saturate" values="0"/>'
        '<feComponentTransfer><feFuncA type="table" tableValues="0 .09"/></feComponentTransfer>'
        "</filter>"
        f'<pattern id="scan-{uid}" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="1" fill="{p.ink}" opacity=".045"/></pattern>'
        f'<radialGradient id="glow-{uid}">'
        f'<stop offset="0" stop-color="{p.glow}" stop-opacity="0"/>'
        f'<stop offset=".42" stop-color="{p.glow}" stop-opacity="0"/>'
        f'<stop offset=".5" stop-color="{p.glow}" stop-opacity=".85"/>'
        f'<stop offset=".62" stop-color="{p.glow}" stop-opacity=".18"/>'
        f'<stop offset="1" stop-color="{p.glow}" stop-opacity="0"/>'
        "</radialGradient>"
        "</defs>"
    )


def veil(p: Palette, uid: str, w: int, h: int) -> str:
    """Scanlines plus grain over the whole plate."""
    return (
        f'<rect width="{w}" height="{h}" fill="url(#scan-{uid})"/>'
        f'<rect width="{w}" height="{h}" filter="url(#grain-{uid})" opacity=".9"/>'
    )


def crop_marks(p: Palette, w: int, h: int, inset: int = 14, size: int = 12) -> str:
    """Print crop marks in the four corners."""
    out = []
    for x, sx in ((inset, 1), (w - inset, -1)):
        for y, sy in ((inset, 1), (h - inset, -1)):
            out.append(
                f'<path d="M{x} {y + sy * size}V{y}H{x + sx * size}" '
                f'fill="none" stroke="{p.soft}" stroke-width=".8"/>'
            )
    return "".join(out)


def corona(cx: float, cy: float, r0: float, reach: float, count: int, seed: int,
           stroke: str, opacity: float, width: float = 0.5) -> str:
    """Radial line-mesh whose length follows a hidden smooth field."""
    rng = Rng(seed)
    phases = [rng.next() * math.tau for _ in range(9)]
    parts = []
    for i in range(count):
        theta = math.tau * i / count
        length = reach * (0.18 + 0.82 * field(theta, phases) ** 2.4)
        jitter = 1 + (rng.next() - 0.5) * 0.12
        r1 = r0 + length * jitter
        c, s = math.cos(theta), math.sin(theta)
        parts.append(f"M{f(cx + r0 * c)} {f(cy + r0 * s)}L{f(cx + r1 * c)} {f(cy + r1 * s)}")
    return (
        f'<path d="{"".join(parts)}" fill="none" stroke="{stroke}" '
        f'stroke-width="{width}" stroke-opacity="{opacity}" stroke-linecap="round"/>'
    )


def rings(cx: float, cy: float, radii: list[float], stroke: str, opacity: float) -> str:
    return "".join(
        f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="{stroke}" '
        f'stroke-width=".6" stroke-opacity="{opacity}"/>'
        for r in radii
    )


def halftone(cx: float, cy: float, r_in: float, r_out: float, step: float,
             fill: str, light: tuple[float, float] = (-0.6, -0.8)) -> str:
    """Dot-screen annulus shaded as if lit from one side, like a halftone moon."""
    dots = []
    lx, ly = light
    y = cy - r_out
    while y <= cy + r_out:
        x = cx - r_out
        while x <= cx + r_out:
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy)
            if r_in <= d <= r_out:
                lit = max(0.0, (dx * lx + dy * ly) / d)
                size = step * 0.42 * (0.15 + 0.85 * lit) * (1 - (d - r_in) / (r_out - r_in)) ** 0.5
                if size > 0.35:
                    dots.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{size:.2f}"/>')
            x += step
        y += step
    return f'<g fill="{fill}" fill-opacity=".55">{"".join(dots)}</g>'


def flare(p: Palette, cx: float, cy: float, r: float, start_deg: float, span_deg: float) -> str:
    """The single colour mark: one rim arc split into the site's three primaries."""
    out = []
    for k, color in enumerate(p.primaries):
        off = (k - 1) * 1.6
        a0, a1 = math.radians(start_deg), math.radians(start_deg + span_deg)
        x0, y0 = cx + off + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + off + r * math.cos(a1), cy + r * math.sin(a1)
        out.append(
            f'<path d="M{f(x0)} {f(y0)}A{f(r)} {f(r)} 0 0 1 {f(x1)} {f(y1)}" fill="none" '
            f'stroke="{color}" stroke-width="2.2" stroke-opacity=".85" stroke-linecap="round"/>'
        )
    return "".join(out)


def aperture(p: Palette, uid: str, cx: float, cy: float, scale: float, seed: int) -> str:
    """The recurring form: a line-mesh corona swept to a luminous void core."""
    s = scale
    return (
        halftone(cx, cy, 150 * s, 196 * s, 7 * s, p.soft)
        + f'<g class="spinr" style="transform-origin:{f(cx)}px {f(cy)}px">'
        + corona(cx, cy, 70 * s, 150 * s, 96, seed + 1, p.soft, 0.5, 0.45)
        + "</g>"
        + f'<g class="spin" style="transform-origin:{f(cx)}px {f(cy)}px">'
        + corona(cx, cy, 40 * s, 112 * s, 220, seed, p.ink, 0.62, 0.4)
        + "</g>"
        + rings(cx, cy, [r * s for r in (40, 44, 52, 66, 150)], p.ink, 0.35)
        + f'<circle class="breathe" cx="{f(cx)}" cy="{f(cy)}" r="{f(62 * s)}" fill="url(#glow-{uid})"/>'
        + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(30 * s)}" fill="{p.ground}"/>'
        + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(30 * s)}" fill="none" stroke="{p.ink}" stroke-width="1.2"/>'
        + flare(p, cx, cy, 150 * s, -58, 34)
    )


def svg_open(w: int, h: int, title: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-labelledby="t d"><title id="t">{title}</title><desc id="d">{desc}</desc>'
    )


def inks(p: Palette, x_end: float, cy: float, r: float = 8, step: float = 13) -> str:
    """Six flat overlapping discs, one per platform ink, ending at x_end."""
    count = len(p.platforms)
    x0 = x_end - r - step * (count - 1)
    return "".join(
        f'<circle cx="{f(x0 + step * i)}" cy="{f(cy)}" r="{f(r)}" fill="{color}" fill-opacity=".88"/>'
        for i, color in enumerate(p.platforms)
    )


def text(x: float, y: float, body: str, size: float, fill: str, *, mono: bool = False,
         display: bool = False, weight: int = 400, anchor: str = "start",
         spacing: float = 0, opacity: float = 1) -> str:
    """Text as Accession outlines. The words stay readable in <title> and <desc>."""
    if mono:
        role = "mono-bold" if weight >= 600 else "mono"
    else:
        role = "display" if display else "text"
    return outline(body, x, y, size, fill, role=role, anchor=anchor, spacing=spacing, opacity=opacity)
