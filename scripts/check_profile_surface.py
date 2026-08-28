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

REQUIRED_ASSETS = ("docs/brand/zentropy-banner.png",)

REQUIRED_DOCS = (
    "docs/research/2026-07-01-enterprise-profile-research.md",
    "docs/research/2026-07-01-profile-template-research.md",
    "docs/research/2026-07-01-index-scope-assessment.md",
    "docs/research/2026-08-27-profile-capability-integration-review.md",
    "docs/superpowers/specs/2026-07-01-github-profile-site-aligned-design.md",
    "docs/superpowers/plans/2026-07-01-github-profile-site-aligned.md",
)

REQUIRED_README_TERMS = (
    "Zain Dana Harper",
    "Available for paid work",
    "## Three ways to work together",
    "https://harperz9.github.io/hire.html#engineering-path",
    "https://harperz9.github.io/hire.html#public-service-field-path",
    "https://harperz9.github.io/research.html",
    "https://harperz9.github.io/resume.html",
    "https://harperz9.github.io/cv.html",
    "https://harperz9.github.io/portfolio.html",
    "## Evidence accepted upstream",
    "https://github.com/dgenio/agentfence/pull/261",
    "https://github.com/freelawproject/litigant-portal/pull/820",
    "https://github.com/sjh9714/mergewarden/pull/107",
    "## Capability constellation",
    "Flywheel is the sole primary platform",
    "mothership",
    "Project Telos",
    "https://github.com/HarperZ9/flywheel/releases/tag/v0.3.10",
    "Agent systems",
    "Evaluation and verification",
    "Security and privacy",
    "Developer infrastructure",
    "Graphics and retro systems",
    "data visualization",
    "Research and education",
    "https://github.com/HarperZ9/terminal-state-fixtures",
    "https://github.com/HarperZ9/phantom/releases/tag/v1.1.0",
    "Layer 2 identity surfaces",
    "https://harperz9.github.io/security.html",
    "coordinated disclosure",
    "## Retro Systems Lab",
    "play → preserve → verify",
    "https://harperz9.github.io/retro.html",
    "https://github.com/HarperZ9/engine-revival/releases/tag/v0.1.0",
    "https://github.com/HarperZ9/brender-archival/releases/tag/v0.1.1",
)

DISALLOWED_README_TERMS = (
    "docs/brand/evidence-map.svg",
    "https://github.com/HarperZ9/aleph",
    "https://github.com/HarperZ9/orca",
    "fourteen flagship engines",
    "0.1.0 source prototype",
    "Phantom v1.0.0",
    "any work can occur within third-party provider terms of service",
    "guarantees provider compliance",
    "guaranteed provider compliance",
    "compliant with every provider",
    "live jailbreak corpora",
    "exploit chains",
    "target-specific techniques",
    "bypass payloads",
    "What you are buying",
    "Why you want me in the room.",
    "Buy the pattern.",
    "Do not buy me",
    "I am a cheater",
    "I am a liar",
    "get fucked up",
    "I get fucked up",
    "Build with a model",
    "Peer into the frontier",
    "Build it to be checked, or do not ship it.",
    "eight flagships",
    "Eight engines",
    "fourteen flagship engines under one Flywheel thesis",
    "Together, the two tables name all fourteen flagships.",
    "Standalone products held apart from the fourteen engines.",
    "1.0.0 on default public main and the local release tag",
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

EXPECTED_PATH_LABELS = (
    "Technical and evaluation",
    "Public, union, and field",
    "Education and research",
)

EXPECTED_PROOF_URLS = (
    "https://github.com/dgenio/agentfence/pull/261",
    "https://github.com/freelawproject/litigant-portal/pull/820",
    "https://github.com/sjh9714/mergewarden/pull/107",
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
        fail(f"README missing required architecture or truth terms: {', '.join(missing)}")

    casefolded = text.casefold()
    forbidden = [term for term in DISALLOWED_README_TERMS if term.casefold() in casefolded]
    if forbidden:
        fail(f"README contains disallowed public terms: {', '.join(forbidden)}")
    if "\u2014" in text:
        fail("README contains an em dash glyph")

    word_count = len(re.findall(r"\b[\w'-]+\b", re.sub(r"<[^>]+>", " ", text)))
    if word_count > 1000:
        fail(f"README exceeds 1000-word hiring-surface limit: {word_count}")

    paths_at = text.index("## Three ways to work together")
    proof_at = text.index("## Evidence accepted upstream")
    capability_at = text.index("## Capability constellation")
    if not paths_at < proof_at < capability_at:
        fail("hiring paths and third-party proofs must precede owned-product breadth")

    paths_section = text[paths_at:proof_at]
    path_rows = re.findall(r"^\| \*\*([^*]+)\*\* \|", paths_section, re.MULTILINE)
    if tuple(path_rows) != EXPECTED_PATH_LABELS:
        fail(
            "hiring table must contain exactly the three approved paths in order: "
            f"{', '.join(EXPECTED_PATH_LABELS)}"
        )

    proof_section = text[proof_at:capability_at]
    proof_urls = re.findall(
        r"^- \[[^\]]+\]\((https://github\.com/([^/]+)/[^/]+/pull/\d+)\):",
        proof_section,
        re.MULTILINE,
    )
    observed_proof_urls = tuple(url for url, _owner in proof_urls)
    if observed_proof_urls != EXPECTED_PROOF_URLS:
        fail("upstream evidence section must contain exactly the three approved PR proofs")
    if any(owner.casefold() == "harperz9" for _url, owner in proof_urls):
        fail("upstream evidence must come from repositories outside HarperZ9")

    if "Flywheel v0.3.10" not in text:
        fail("Flywheel must be identified at verified release v0.3.10")
    if re.search(r"Flywheel.{0,80}(?:v|version )?0\.1\.0", text, re.IGNORECASE | re.DOTALL):
        fail("Flywheel must not be described as version 0.1.0")

    if not re.search(r"authorized security", text, re.IGNORECASE):
        fail("README must include one bounded authorized-security aggregate")
    if not re.search(r"public (?:surface|pages?).{0,160}(?:sanitized|bounded)", text, re.IGNORECASE | re.DOTALL):
        fail("README must distinguish the sanitized public security surface")
    if not re.search(r"approved\s+private or embargoed\s+channels", text, re.IGNORECASE):
        fail("README must route controlled material through approved private or embargoed channels")

    markdown_targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    bad_targets = [target for target in markdown_targets if not target.startswith(("https://", "mailto:"))]
    if bad_targets:
        fail(f"README contains non-public link targets: {', '.join(bad_targets)}")


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
