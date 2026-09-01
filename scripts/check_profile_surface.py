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
    "## What I built",
    "https://github.com/dgenio/agentfence/pull/261",
    "https://github.com/freelawproject/litigant-portal/pull/820",
    "https://github.com/sjh9714/mergewarden/pull/107",
    "Zain Dana Harper and Zentropy Labs are the front door",
    "## Systems, grouped by the work they do",
    "sole primary platform",
    "https://github.com/HarperZ9/flywheel/releases/tag/v0.3.10",
    "Agent execution and memory",
    "Evaluation and verification",
    "Security and privacy",
    "Developer infrastructure",
    "Graphics and runtime systems",
    "Preservation and retro systems",
    "Research and education",
    "https://github.com/HarperZ9/terminal-state-fixtures",
    "https://github.com/HarperZ9/phantom/releases/tag/v1.1.0",
    "Layer 2 identity surfaces",
    "https://harperz9.github.io/security.html",
    "### Operational security systems",
    "Array",
    "Seed",
    "Sofer",
    "Isomorph",
    "Bounds",
    "ORCA",
    "Gate",
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
    "mothership",
    "### Authorized security, kept bounded",
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

EXPECTED_PROJECT_DESCRIPTIONS = (
    (
        "Flywheel",
        "https://github.com/HarperZ9/flywheel",
        "Flywheel runs an AI task with the local or hosted model and tools you choose. "
        "It checks what happened, saves a receipt you can inspect or replay, "
        "and includes a native desktop app.",
    ),
    (
        "Index",
        "https://github.com/HarperZ9/index",
        "Index maps repositories and multi-repo workspaces so you can see how the code fits together. "
        "It reads manifests, imports, symbols, and local documentation, then builds offline wikis, "
        "dependency maps, context packets, and architecture checks with file-and-line evidence.",
    ),
    (
        "Gather",
        "https://github.com/HarperZ9/gather",
        "Gather collects research material from sources that basic scrapers often miss. "
        "It handles JavaScript-rendered pages, authenticated APIs, scholarly records, PDFs, OCR, "
        "audio, video, feeds, and local documents, then saves each item in a content-addressed corpus "
        "with provenance you can recheck.",
    ),
    (
        "BuildLang",
        "https://github.com/HarperZ9/buildlang",
        "BuildLang is a systems programming language and compiler that makes programs declare what they are allowed "
        "to touch. It checks those permissions and memory rules before producing native code through C. "
        "Experimental shader output, two-way C integration, a CLI, editor support, and re-checkable "
        "build receipts are included.",
    ),
    (
        "Phantom",
        "https://github.com/HarperZ9/phantom",
        "Phantom helps you inspect and, when authorized, change the hardware identifiers a computer exposes. "
        "It works on owned or expressly authorized Windows and Linux systems, saves a backup before "
        "changes, and can restore the original values.",
    ),
    (
        "Accountable Surface",
        "https://github.com/HarperZ9/accountable-surface",
        "Accountable Surface lets an AI agent take only the file, command, web, or browser action a person has approved. "
        "It checks the request and authorization, blocks or pauses when needed, verifies the outcome, "
        "rolls back reversible failures, and records every step in a hash-chained journal.",
    ),
)


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def normalized_project_table(section: str) -> tuple[str, ...]:
    lines = section.splitlines()
    try:
        start = lines.index("| Project | What it does |")
    except ValueError:
        return ()

    block: list[str] = []
    for line in lines[start:]:
        if not line.strip():
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        block.append(f"| {' | '.join(cells)} |")
    return tuple(block)


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

    visible_text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    visible_text = re.sub(r"<[^>]+>", " ", visible_text)
    word_count = len(re.findall(r"\b[\w'-]+\b", visible_text))
    if word_count > 1000:
        fail(f"README exceeds 1000-word hiring-surface limit: {word_count}")

    paths_at = text.index("## Three ways to work together")
    proof_at = text.index("## Evidence accepted upstream")
    projects_at = text.index("## What I built")
    capability_at = text.index("## Systems, grouped by the work they do")
    if not paths_at < proof_at < projects_at < capability_at:
        fail("hiring paths, third-party proofs, and plain-language projects must precede product breadth")

    paths_section = text[paths_at:proof_at]
    path_rows = re.findall(r"^\| \*\*([^*]+)\*\* \|", paths_section, re.MULTILINE)
    if tuple(path_rows) != EXPECTED_PATH_LABELS:
        fail(
            "hiring table must contain exactly the three approved paths in order: "
            f"{', '.join(EXPECTED_PATH_LABELS)}"
        )

    proof_section = text[proof_at:projects_at]
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

    projects_section = text[projects_at:capability_at]
    expected_table = (
        "| Project | What it does |",
        "| --- | --- |",
    ) + tuple(
        f"| [{name}]({url}) | {description} |"
        for name, url, description in EXPECTED_PROJECT_DESCRIPTIONS
    )
    observed_table = normalized_project_table(projects_section)
    if observed_table != expected_table:
        fail("plain-language project table must contain exactly the six approved descriptions in order")

    if "Flywheel v0.3.10" not in text:
        fail("Flywheel must be identified at verified release v0.3.10")
    if re.search(r"Flywheel.{0,80}(?:v|version )?0\.1\.0", text, re.IGNORECASE | re.DOTALL):
        fail("Flywheel must not be described as version 0.1.0")

    required_security_systems = ("Array", "Seed", "Sofer", "Isomorph", "Bounds", "ORCA", "Gate")
    missing_security_systems = [name for name in required_security_systems if name not in text]
    if missing_security_systems:
        fail(f"README must name distinct operational security systems: {', '.join(missing_security_systems)}")
    security_start = text.find("### Operational security systems")
    security_end = text.find("## Retro Systems Lab", security_start)
    if security_start < 0 or security_end < 0:
        fail("README must contain the operational-security section before the retro section")
    security_section = text[security_start:security_end]
    if not re.search(
        r"controlled-private systems\s+with public capability descriptions",
        security_section,
        re.IGNORECASE,
    ):
        fail("operational security systems must be labeled controlled-private with public descriptions")
    if "They are not public releases or downloads." not in security_section:
        fail("operational security section must state that controlled-private systems are not public releases")
    if not re.search(
        r"Public pages describe each\s+system's job,\s+evidence, maturity, and limits",
        security_section,
        re.IGNORECASE,
    ):
        fail("README must describe the public security pages as system-specific evidence surfaces")
    if not re.search(r"approved\s+private or embargoed\s+channels", security_section, re.IGNORECASE):
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
