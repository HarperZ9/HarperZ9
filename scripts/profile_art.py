"""Generate the profile art panels in light and dark variants.

Run from the repository root:

    python scripts/profile_art.py

Writes docs/art/<panel>-<dark|light>.svg. Output is deterministic.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from art_kit import (  # noqa: E402
    PALETTES,
    Palette,
    aperture,
    corona,
    crop_marks,
    defs,
    f,
    flare,
    rings,
    style_block,
    svg_open,
    text,
    veil,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "art"
SEED = 20261001


def mini_aperture(p: Palette, cx: float, cy: float, s: float, seed: int,
                  accent: str, spin: bool = True) -> str:
    """A small aperture for figures: corona, rings, void core, accent rim."""
    cls = ' class="spin"' if spin else ""
    return (
        f'<g{cls} style="transform-origin:{f(cx)}px {f(cy)}px">'
        + corona(cx, cy, 34 * s, 70 * s, 120, seed, p.ink, 0.55, 0.5)
        + "</g>"
        + rings(cx, cy, [34 * s, 40 * s], p.ink, 0.3)
        + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(26 * s)}" fill="{p.ground}" '
        f'stroke="{accent}" stroke-width="2"/>'
    )


def hero(p: Palette) -> str:
    w, h, uid = 1280, 420, f"hero-{p.name}"
    body = [
        svg_open(w, h, "Zain Dana Harper",
                 "A luminous aperture drawn in fine radial lines beside the name "
                 "Zain Dana Harper and the line: tools and investigations that let "
                 "anyone recheck what an AI system did."),
        style_block(), defs(p, uid),
        f'<rect width="{w}" height="{h}" fill="{p.ground}"/>',
        aperture(p, uid, 1010, 210, 1.0, SEED),
        text(64, 118, "INDEPENDENT AI EVALUATION  /  ACCOUNTABILITY  /  INVESTIGATIONS",
             12, p.soft, mono=True, spacing=2.2),
        text(60, 196, "Zain Dana Harper", 68, p.ink, weight=700, spacing=-1.5),
        f'<path d="M64 226H600" stroke="{p.ink}" stroke-width="1"/>',
        text(64, 270, "Tools and investigations that let anyone", 25, p.soft),
        text(64, 304, "recheck what an AI system did, and who knew first.", 25, p.soft),
        text(64, 362, "harperz9.github.io", 14, p.ink, mono=True),
        veil(p, uid, w, h), crop_marks(p, w, h), "</svg>",
    ]
    return "".join(body)


def verdicts(p: Palette) -> str:
    w, h, uid = 1280, 300, f"verdicts-{p.name}"
    cols = (
        (240, p.verified, "MATCH", "the rerun agrees with the record"),
        (640, p.drift, "DRIFT", "the rerun disagrees, and says where"),
        (1040, p.unverifiable, "UNVERIFIABLE", "the record cannot be checked"),
    )
    body = [
        svg_open(w, h, "Three verdicts",
                 "Three apertures labelled MATCH, DRIFT and UNVERIFIABLE: the only "
                 "outcomes an independent recheck of a Flywheel receipt can return."),
        style_block(), defs(p, uid), f'<rect width="{w}" height="{h}" fill="{p.ground}"/>',
    ]
    for i, (cx, accent, label, note) in enumerate(cols):
        body.append(mini_aperture(p, cx, 118, 1.0, SEED + 10 + i, accent))
        body.append(text(cx, 232, label, 17, accent, mono=True, weight=600, anchor="middle", spacing=2))
        body.append(text(cx, 260, note, 15, p.soft, anchor="middle"))
    body.append(f'<path d="M320 118H560M720 118H960" stroke="{p.line}" stroke-width="1" stroke-dasharray="2 5"/>')
    body += [veil(p, uid, w, h), crop_marks(p, w, h), "</svg>"]
    return "".join(body)


def incidents(p: Palette) -> str:
    w, h, uid = 1280, 280, f"incidents-{p.name}"
    body = [
        svg_open(w, h, "Who told the public first",
                 "Nine small apertures for nine 2026 AI agent incidents. Six carry an "
                 "outer mark: in those six, someone outside the organization that ran "
                 "the model told the public first."),
        style_block(), defs(p, uid), f'<rect width="{w}" height="{h}" fill="{p.ground}"/>',
    ]
    for i in range(9):
        cx = 120 + i * 130
        outside = i < 6
        body.append(mini_aperture(p, cx, 120, 0.62, SEED + 30 + i, p.ink if outside else p.soft, spin=False))
        if outside:
            body.append(f'<circle cx="{f(cx)}" cy="62" r="4.5" fill="{p.ink}"/>')
            body.append(f'<path d="M{f(cx)} 68V84" stroke="{p.ink}" stroke-width="1"/>')
    body.append(f'<path d="M80 196H850" stroke="{p.ink}" stroke-width="1"/>')
    body.append(f'<path d="M890 196H1160" stroke="{p.soft}" stroke-width="1" stroke-dasharray="2 4"/>')
    body.append(text(80, 226, "Six of nine: someone outside the organization told the public first.", 17, p.ink))
    body.append(text(890, 226, "The other three.", 17, p.soft))
    body.append(text(80, 254, "WHO KNEW FIRST  /  NINE CASE LEDGERS  /  2026", 12, p.soft, mono=True, spacing=2))
    body += [veil(p, uid, w, h), crop_marks(p, w, h), "</svg>"]
    return "".join(body)


def monitor(p: Palette) -> str:
    w, h, uid = 1280, 300, f"monitor-{p.name}"
    gx, gy = 700, 130
    ticks = "".join(f"M{x} {gy - 9}V{gy + 9}" for x in range(90, 600, 22))
    body = [
        svg_open(w, h, "A check before the action",
                 "A trace of observed steps runs into an aperture, the pre-action "
                 "check. One path continues to an action with a receipt; the other "
                 "stops at a bar before the action runs."),
        style_block(), defs(p, uid), f'<rect width="{w}" height="{h}" fill="{p.ground}"/>',
        f'<g class="drift"><path d="{ticks}" stroke="{p.soft}" stroke-width="1.2"/></g>',
        f'<path d="M80 {gy}H{gx - 60}" stroke="{p.ink}" stroke-width="1"/>',
        mini_aperture(p, gx, gy, 0.8, SEED + 50, p.ink),
        flare(gx, gy, 52, -60, 30),
        f'<path d="M{gx + 58} {gy}C{gx + 160} {gy} {gx + 180} 70 {gx + 290} 70H1150" '
        f'fill="none" stroke="{p.verified}" stroke-width="1.6"/>',
        f'<circle cx="1158" cy="70" r="7" fill="none" stroke="{p.verified}" stroke-width="1.6"/>',
        f'<path d="M{gx + 58} {gy}C{gx + 140} {gy} {gx + 160} 196 {gx + 240} 196H{gx + 300}" '
        f'fill="none" stroke="{p.drift}" stroke-width="1.6"/>',
        f'<path d="M{gx + 304} 180V212" stroke="{p.drift}" stroke-width="3"/>',
        text(80, 186, "trace observed, step by step", 16, p.soft),
        text(gx, 236, "checked before it acts", 16, p.ink, anchor="middle"),
        text(1150, 50, "runs, with a receipt", 16, p.verified, anchor="end"),
        text(gx + 320, 202, "halted before it runs", 16, p.drift),
        text(80, 270, "DIRECTION IN PROGRESS  /  NOT A RELEASE", 12, p.soft, mono=True, spacing=2),
        veil(p, uid, w, h), crop_marks(p, w, h), "</svg>",
    ]
    return "".join(body)


def rule(p: Palette) -> str:
    """A thin divider: a hairline with a small aperture at its center."""
    w, h, uid = 1280, 64, f"rule-{p.name}"
    cx, cy = w / 2, h / 2
    ticks = "".join(
        f"M{f(cx + 18 * math.cos(a))} {f(cy + 18 * math.sin(a))}"
        f"L{f(cx + 27 * math.cos(a))} {f(cy + 27 * math.sin(a))}"
        for a in (math.tau * i / 48 for i in range(48))
    )
    return "".join([
        svg_open(w, h, "Section divider", "A hairline with a small aperture at its center."),
        style_block(), defs(p, uid),
        f'<path d="M24 {cy}H{cx - 40}M{cx + 40} {cy}H{w - 24}" stroke="{p.soft}" stroke-width=".8"/>',
        f'<g class="spin" style="transform-origin:{f(cx)}px {f(cy)}px">'
        f'<path d="{ticks}" stroke="{p.ink}" stroke-width=".6"/></g>',
        f'<circle cx="{f(cx)}" cy="{f(cy)}" r="11" fill="none" stroke="{p.ink}" stroke-width="1"/>',
        "</svg>",
    ])


PANELS = {"hero": hero, "verdicts": verdicts, "incidents": incidents, "monitor": monitor, "rule": rule}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, build in PANELS.items():
        for p in PALETTES:
            path = OUT / f"{name}-{p.name}.svg"
            path.write_text(build(p) + "\n", encoding="utf-8", newline="\n")
            print(f"wrote {path.relative_to(ROOT).as_posix()} ({path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
