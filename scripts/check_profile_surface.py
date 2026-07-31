from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "AUTHORS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "USAGE.md",
    "CHANGELOG.md",
    "PRODUCT.md",
)

REQUIRED_ASSETS = ("docs/brand/profile-hero.png",)

REQUIRED_DOCS = (
    "docs/research/2026-07-01-enterprise-profile-research.md",
    "docs/research/2026-07-01-profile-template-research.md",
    "docs/research/2026-07-01-index-scope-assessment.md",
    "docs/superpowers/specs/2026-07-01-github-profile-site-aligned-design.md",
    "docs/superpowers/plans/2026-07-01-github-profile-site-aligned.md",
)

REQUIRED_README_TERMS = (
    "Zain Dana Harper",
    "Project Telos",
    "Work you can walk away from.",
    "run anywhere",
    "https://harperz9.github.io",
    "https://github.com/HarperZ9/flywheel",
    "https://github.com/HarperZ9/telos",
    "https://github.com/HarperZ9/index",
    "https://github.com/HarperZ9/gather",
    "https://github.com/HarperZ9/forum",
    "https://github.com/HarperZ9/crucible",
    "https://github.com/HarperZ9/emet",
    "https://github.com/HarperZ9/buildlang",
    "https://github.com/HarperZ9/learn",
    "## The flagships",
    "The receipt that matters",
    "fourteen flagship engines under one Flywheel thesis",
    "1.1.0 package and release; frozen 1.0.0 core spec.",
    "Plexus 0.2.0 public source",
    "poster design",
    "measured critique",
    "seeded neural graphics",
    "AI-assisted design workflows",
    "managed access",
    "term licensing",
    "continued learning",
    "practical IT",
    "```mermaid",
)

REQUIRED_LIVE_SHIELDS = (
    # name, version_needle, ci_needle, downloads_needle
    ("index",     "img.shields.io/pypi/v/index-graph",         "img.shields.io/github/actions/workflow/status/HarperZ9/index/ci.yml",          "img.shields.io/pypi/dm/index-graph"),
    ("gather",    "img.shields.io/pypi/v/gather-engine",       "img.shields.io/github/actions/workflow/status/HarperZ9/gather/ci.yml",         "img.shields.io/pypi/dm/gather-engine"),
    ("forum",     "img.shields.io/pypi/v/forum-engine",        "img.shields.io/github/actions/workflow/status/HarperZ9/forum/ci.yml",          "img.shields.io/pypi/dm/forum-engine"),
    ("crucible",  "img.shields.io/pypi/v/crucible-bench",      "img.shields.io/github/actions/workflow/status/HarperZ9/crucible/ci.yml",       "img.shields.io/pypi/dm/crucible-bench"),
    ("emet",      "img.shields.io/pypi/v/emet",                "img.shields.io/github/actions/workflow/status/HarperZ9/emet/conformance.yml", "img.shields.io/pypi/dm/emet"),
    ("buildlang", "img.shields.io/crates/v/buildlang",         "img.shields.io/github/actions/workflow/status/HarperZ9/buildlang/ci.yml",      "img.shields.io/crates/dv/buildlang"),
)

DISALLOWED_README_TERMS = (
    "docs/brand/evidence-map.svg",
    "https://github.com/HarperZ9/aleph",
    "https://github.com/HarperZ9/orca",
    "https://github.com/HarperZ9/behavior-transform",
    "What you are buying",
    "translation pressure",
    "Why you want me in the room.",
    "Buy the pattern.",
    "Buy me when",
    "Do not buy me",
    "How to evaluate the bet.",
    "that is the buying signal",
    "What this buys you.",
    "Your team gets less hidden state",
    "I am a cheater",
    "I am a liar",
    "no spine",
    "get fucked up",
    "I get fucked up",
    "Build with a model",
    "Peer into the frontier",
    "Build it to be checked, or do not ship it.",
    "eight flagships",
    "Eight engines",
    "1.0.0 on default public main and the local release tag",
)

FLAGSHIP_REPO_SLUGS = (
    "flywheel",
    "telos",
    "index",
    "gather",
    "forum",
    "crucible",
    "emet",
    "buildlang",
    "learn",
    "relay",
    "plexus",
    "mneme",
    "studio-engine",
    "build-color",
)

DISALLOWED_README_CASEFOLD_TERMS = (
    "cali" + "brate",
)

SECRET_SHAPES = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY"),
)


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def assert_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).exists()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def assert_required_assets() -> None:
    missing = [name for name in REQUIRED_ASSETS if not (ROOT / name).exists()]
    if missing:
        fail(f"missing required assets: {', '.join(missing)}")


def assert_required_docs() -> None:
    missing = [name for name in REQUIRED_DOCS if not (ROOT / name).exists()]
    if missing:
        fail(f"missing required docs: {', '.join(missing)}")


def assert_readme_contract() -> None:
    text = README.read_text(encoding="utf-8")
    missing = [term for term in REQUIRED_README_TERMS if term not in text]
    if missing:
        fail(f"README missing required terms: {', '.join(missing)}")
    for name, version_n, ci_n, downloads_n in REQUIRED_LIVE_SHIELDS:
        for label, needle in (("version", version_n), ("CI", ci_n), ("downloads", downloads_n)):
            if needle not in text:
                fail(
                    f"README missing live {label} badge for {name} "
                    "(versions, CI status, and downloads must come from the "
                    "registry/GitHub on page load, never hand-typed)"
                )
    forbidden = [term for term in DISALLOWED_README_TERMS if term in text]
    if forbidden:
        fail(f"README contains disallowed public terms: {', '.join(forbidden)}")
    casefolded = text.casefold()
    forbidden_casefolded = [
        term for term in DISALLOWED_README_CASEFOLD_TERMS if term in casefolded
    ]
    if forbidden_casefolded:
        fail(
            "README contains disallowed public terms: "
            f"{', '.join(forbidden_casefolded)}"
        )
    if "\u2014" in text:
        fail("README contains an em dash glyph")
    flagship_section = text.split("## The flagships", 1)[1].split(
        "## How the workshop fits together", 1
    )[0]
    flagship_rows = re.findall(
        r"^\| \[[^\]]+\]\(https://github\.com/HarperZ9/([^)]+)\) \|",
        flagship_section,
        flags=re.MULTILINE,
    )
    if tuple(flagship_rows) != FLAGSHIP_REPO_SLUGS:
        fail(
            "flagship tables must name the exact fourteen-engine roster in order: "
            f"{', '.join(FLAGSHIP_REPO_SLUGS)}"
        )


def assert_no_secret_shapes() -> None:
    paths = [ROOT / name for name in REQUIRED_FILES if (ROOT / name).is_file()]
    paths.append(ROOT / "scripts" / "check_profile_surface.py")
    paths.extend((ROOT / "docs").glob("**/*.md"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_SHAPES:
            if pattern.search(text):
                fail(f"credential-shaped text found in {path.relative_to(ROOT)}")


def main() -> int:
    assert_required_files()
    assert_required_assets()
    assert_required_docs()
    assert_readme_contract()
    assert_no_secret_shapes()
    print("profile surface: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
