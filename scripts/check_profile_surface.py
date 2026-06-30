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
)

REQUIRED_README_TERMS = (
    "https://harperz9.github.io",
    "https://github.com/HarperZ9/gather",
    "https://github.com/HarperZ9/index",
    "https://github.com/HarperZ9/forum",
    "https://github.com/HarperZ9/crucible",
    "https://github.com/HarperZ9/telos",
    "Open tester threads",
    "Recent public dogfood",
)

SECRET_SHAPES = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{36,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
)


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def assert_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).exists()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def assert_readme_contract() -> None:
    text = README.read_text(encoding="utf-8")
    missing = [term for term in REQUIRED_README_TERMS if term not in text]
    if missing:
        fail(f"README missing required public terms: {', '.join(missing)}")


def assert_no_secret_shapes() -> None:
    paths = [ROOT / name for name in REQUIRED_FILES if (ROOT / name).is_file()]
    paths.append(ROOT / "scripts" / "check_profile_surface.py")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_SHAPES:
            if pattern.search(text):
                fail(f"credential-shaped text found in {path.relative_to(ROOT)}")


def main() -> int:
    assert_required_files()
    assert_readme_contract()
    assert_no_secret_shapes()
    print("profile surface: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
