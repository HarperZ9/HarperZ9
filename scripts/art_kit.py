"""Shared drawing kit for the profile art.

Every figure is generated from code with the standard library only. The output
is deterministic: the same seed and palette give the same bytes, so a reviewer
can regenerate any panel and diff it.

Palette values come from the site's design tokens (void and bone grounds,
verdict colors). The spectrum appears only as the single flare on the aperture.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


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


DARK = Palette(
    name="dark",
    ground="#060608",
    ink="#ece5d6",
    soft="#b8b0a0",
    line="#29282c",
    verified="#63d4ce",
    drift="#e29472",
    unverifiable="#b3b1e6",
    glow="#f6e7c4",
)

LIGHT = Palette(
    name="light",
    ground="#ebe5d8",
    ink="#16130f",
    soft="#4a443b",
    line="#c9bfab",
    verified="#0a6b61",
    drift="#8f3a19",
    unverifiable="#4e4d85",
    glow="#16130f",
)

PALETTES = (DARK, LIGHT)

# The one spectral flare: refraction on the aperture rim, never used in text.
FLARE = ("#3fd3e6", "#e2489f", "#f0b23c")

SANS = "'Hanken Grotesk','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "Conso,'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace"


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


def flare(cx: float, cy: float, r: float, start_deg: float, span_deg: float) -> str:
    """The single spectral mark: one rim arc split into three offset channels."""
    out = []
    for k, color in enumerate(FLARE):
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
        + flare(cx, cy, 150 * s, -58, 34)
    )


def svg_open(w: int, h: int, title: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-labelledby="t d"><title id="t">{title}</title><desc id="d">{desc}</desc>'
    )


def text(x: float, y: float, body: str, size: float, fill: str, *, mono: bool = False,
         weight: int = 400, anchor: str = "start", spacing: float = 0, opacity: float = 1) -> str:
    family = MONO if mono else SANS
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    extra += f' fill-opacity="{opacity}"' if opacity != 1 else ""
    return (
        f'<text x="{f(x)}" y="{f(y)}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{body}</text>'
    )
