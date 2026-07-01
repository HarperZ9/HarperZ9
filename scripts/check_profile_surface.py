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
    "https://harperz9.github.io",
    "https://github.com/HarperZ9/telos",
    "https://github.com/HarperZ9/index",
    "https://github.com/HarperZ9/gather",
    "https://github.com/HarperZ9/forum",
    "https://github.com/HarperZ9/crucible",
    "https://github.com/HarperZ9/emet",
    "https://github.com/HarperZ9/buildlang",
    "https://github.com/HarperZ9/learn",
    "This is a workbench, not a trophy case.",
    "artistic",
    "restless",
    "fallible",
    "wrong turns",
    "Choose a door.",
    "I have 30 seconds.",
    "I am hiring for AI tooling or platform work.",
    "I am an engineer and want proof.",
    "I want the weird human part.",
    "I want to break it.",
    "Showcases and demos.",
    "Open something visual.",
    "Run a tiny demo from source.",
    "Inspect the demo surfaces.",
    "Pick a mood.",
    "The instruments.",
    "https://harperz9.github.io/catalog.html",
    "https://harperz9.github.io/overview.html",
    "https://harperz9.github.io/buildlang/",
    "examples/atlas-demo.html",
    "examples/gather-demo.html",
    "examples/forum-demo.html",
    "AI tooling or platform work",
    "The map.",
    "https://harperz9.github.io/studio.html",
    "```mermaid",
    "Intentional profile routing mix, not traffic data",
    "Domain lanes.",
    "What I am unusually good at.",
    "Bench notes.",
    "Things I keep reaching for.",
    "Things I am still learning in public.",
    "Things that usually mean I am doing the right work.",
    "What I am not pretending.",
    "Open traps.",
    "A receipt is not truth.",
    "Build it to be checked, or do not ship it.",
    "proof-surface",
    "How this profile is built.",
    "enterprise profile receipt",
)

PROFILE_CONTRACT_TERMS = (
    "Zain Dana Harper",
    "Project Telos",
    "Build with a model. Take nothing on faith.",
    "research lab and product ecosystem",
    "ambiguous technical",
    "strongest where the problem",
    "is underspecified",
    "turn ambiguous technical work into instruments",
    "model output as authority",
    "docs/brand/profile-hero.png",
)

DISALLOWED_README_TERMS = (
    "docs/brand/evidence-map.svg",
    "Recent public dogfood",
    "https://github.com/HarperZ9/aleph",
    "https://github.com/HarperZ9/orca",
    "https://github.com/HarperZ9/behavior-transform",
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
    expected_terms = REQUIRED_README_TERMS + PROFILE_CONTRACT_TERMS
    missing = [term for term in expected_terms if term not in text]
    if missing:
        fail(f"README missing required public terms: {', '.join(missing)}")
    forbidden = [term for term in DISALLOWED_README_TERMS if term in text]
    if forbidden:
        fail(f"README contains disallowed public terms: {', '.join(forbidden)}")


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
