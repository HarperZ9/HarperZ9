"""CI gate for the HarperZ9 profile surface.

Rules live in scripts/profile_surface.toml; structural checks live here.
Run from anywhere: python scripts/check_profile_surface.py
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CONFIG = ROOT / "scripts" / "profile_surface.toml"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "AUTHORS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "USAGE.md",
    "CHANGELOG.md",
    "PRODUCT.md",
    "scripts/art_kit.py",
    "scripts/profile_art.py",
    "scripts/refresh_profile.py",
)

SECRET_SHAPES = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY"),
)


def fail(message: str) -> None:
    print(f"profile surface: {message}", file=sys.stderr)
    raise SystemExit(1)


def word_count(text: str) -> int:
    visible = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    visible = re.sub(r"```.*?```", " ", visible, flags=re.DOTALL)
    visible = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", visible)
    visible = re.sub(r"<[^>]+>", " ", visible)
    return len(re.findall(r"\b[\w'-]+\b", visible))


def check_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).exists()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def check_terms(text: str, config: dict) -> None:
    missing = [term for term in config["required_terms"] if term not in text]
    if missing:
        fail(f"README missing required terms: {', '.join(missing)}")
    found = [
        term for term in config["disallowed_terms"]
        if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text, re.IGNORECASE)
    ]
    if found:
        fail(f"README contains disallowed terms: {', '.join(found)}")
    if "—" in text:
        fail("README contains an em dash")


def check_structure(text: str, config: dict) -> None:
    positions = []
    for heading in config["section_order"]:
        match = re.search(rf"^{re.escape(heading)}$", text, re.MULTILINE)
        if not match:
            fail(f"README missing section: {heading}")
        positions.append(match.start())
    if positions != sorted(positions):
        fail("README sections are out of order")
    for name in config["generated_blocks"]:
        block = re.search(rf"<!-- {name}:start -->\n(.*?)<!-- {name}:end -->", text, re.DOTALL)
        if not block or "| --- |" not in block.group(1):
            fail(f"generated block '{name}' is missing or empty; run scripts/refresh_profile.py")
    if text.count("<details>") != text.count("</details>"):
        fail("unbalanced <details> sections")


def check_words(text: str, config: dict) -> None:
    limit = config["max_words"]
    count = word_count(text)
    if count > limit:
        fail(f"README has {count} visible words, over the limit of {limit} set in {CONFIG.name}")
    print(f"profile surface: {count} visible words (limit {limit})")


def check_images(text: str) -> None:
    sources = re.findall(r'(?:src|srcset)="([^"]+)"', text)
    for source in sources:
        if source.startswith("https://"):
            fail(f"README loads a remote image: {source}")
        path = ROOT / source.split("#", 1)[0]
        if not path.is_file():
            fail(f"README references a missing image: {source}")
    for dark in re.findall(r'srcset="(docs/art/[\w-]+)-dark\.svg"', text):
        if f'srcset="{dark}-light.svg"' not in text:
            fail(f"{dark} has a dark variant without a light one")
    for svg in (ROOT / "docs" / "art").glob("*.svg"):
        body = svg.read_text(encoding="utf-8")
        if "animation:" in body and "prefers-reduced-motion" not in body:
            fail(f"{svg.name} animates without honoring prefers-reduced-motion")
        if "<script" in body or "href=\"http" in body:
            fail(f"{svg.name} contains a script or a remote reference")


def check_links(text: str) -> None:
    targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    targets += re.findall(r'<a href="([^"]+)"', text)
    bad = [t for t in targets if not t.startswith(("https://", "mailto:", "#"))]
    if bad:
        fail(f"README contains non-public link targets: {', '.join(bad)}")
    headings = {
        re.sub(r"[^\w\- ]", "", h).strip().lower().replace(" ", "-")
        for h in re.findall(r"^#{2,3} (.+)$", text, re.MULTILINE)
    }
    broken = [t for t in targets if t.startswith("#") and t[1:] not in headings]
    if broken:
        fail(f"README has in-page links with no matching heading: {', '.join(broken)}")


def check_secrets() -> None:
    paths = [ROOT / name for name in REQUIRED_FILES if (ROOT / name).is_file()]
    paths += [CONFIG, Path(__file__).resolve()]
    paths += list((ROOT / "docs").glob("**/*.md"))
    paths += list((ROOT / ".github").glob("**/*.yml"))
    for path in paths:
        content = path.read_text(encoding="utf-8")
        if any(pattern.search(content) for pattern in SECRET_SHAPES):
            fail(f"credential-shaped text found in {path.relative_to(ROOT)}")


def main() -> int:
    config = tomllib.loads(CONFIG.read_text(encoding="utf-8"))["readme"]
    text = README.read_text(encoding="utf-8")
    check_files()
    check_terms(text, config)
    check_structure(text, config)
    check_words(text, config)
    check_images(text)
    check_links(text)
    check_secrets()
    print("profile surface: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
