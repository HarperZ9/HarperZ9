"""Refresh the live parts of the profile README.

Reads two public sources and rewrites the README blocks between markers:

- the site's Atom feed (https://harperz9.github.io/feed.xml) for the latest writing;
- the GitHub releases API for the current release of each flagship.

It also redraws the version badges in docs/art. Standard library only. A
GITHUB_TOKEN in the environment raises the API rate limit; nothing else is used.

    python scripts/refresh_profile.py           # rewrite README and badges
    python scripts/refresh_profile.py --check   # exit 1 if a rewrite would change files
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from art_kit import MONO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ART = ROOT / "docs" / "art"
FEED = "https://harperz9.github.io/feed.xml"
ATOM = "{http://www.w3.org/2005/Atom}"
WRITING_COUNT = 6

FLAGSHIPS = (
    ("flywheel", "Flywheel", "AI workstation and coding harness: any model, gated agent, rerunnable receipts"),
    ("articulate", "Articulate", "Local writing checker and editor with content-free receipts"),
    ("telos", "Telos", "Accountable actuation: senses, actions and hardware control in permission tiers"),
    ("accountable-surface", "Accountable Surface", "Gates agent actions on explicit grants, with a hash-chained journal"),
    ("forum", "Forum", "Coordinates agent teams with a replayable ledger"),
    ("relay", "Relay", "Permission-checked coding agent for any model endpoint"),
    ("gather", "Gather", "Research intake from the web, papers, video, scans and audio, with provenance"),
    ("index", "Index", "Offline repository and workspace maps with file and line evidence"),
    ("mneme", "Mneme", "Agent memory where every recall can be rechecked"),
    ("canon", "Canon", "One memory and personality record shared across models and tools"),
    ("crucible", "Crucible", "Tests falsifiable claims and records MATCH, DRIFT or UNVERIFIABLE"),
    ("emet", "EMET", "Checks that bytes reaching a model still match their source"),
    ("learn", "Learn", "Turns your own material into a course that never takes the test for you"),
    ("plexus", "Plexus", "Finds and wires compatible tools in an agent toolchain"),
    ("phantom", "Phantom", "Reversible hardware-identity privacy for owned Windows and Linux machines"),
)

BADGES = (("flywheel", "Flywheel"), ("articulate", "Articulate"), ("telos", "Telos"))


def fetch(url: str, accept: str) -> bytes:
    headers = {"User-Agent": "HarperZ9-profile-refresh", "Accept": accept}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except OSError as exc:
        print(f"fetch failed for {url}: {exc}", file=sys.stderr)
        raise


def latest_writing() -> list[tuple[str, str, str]]:
    root = ET.fromstring(fetch(FEED, "application/atom+xml"))
    items = []
    for entry in root.findall(f"{ATOM}entry"):
        title = (entry.findtext(f"{ATOM}title") or "").strip()
        link = entry.find(f"{ATOM}link")
        href = link.get("href", "") if link is not None else ""
        date = (entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated") or "")[:10]
        if title and href.startswith("https://"):
            items.append((date, title, href))
    items.sort(key=lambda item: item[0], reverse=True)
    return items[:WRITING_COUNT]


def latest_release(repo: str) -> tuple[str, str, str]:
    url = f"https://api.github.com/repos/HarperZ9/{repo}/releases/latest"
    data = json.loads(fetch(url, "application/vnd.github+json"))
    return data["tag_name"], data["published_at"][:10], data["html_url"]


def writing_block(items: list[tuple[str, str, str]]) -> str:
    lines = ["| Date | Piece |", "| --- | --- |"]
    lines += [f"| {date} | [{title}]({href}) |" for date, title, href in items]
    return "\n".join(lines)


def releases_block(releases: dict[str, tuple[str, str, str]]) -> str:
    lines = ["| Tool | What it does | Release |", "| --- | --- | --- |"]
    for repo, name, note in FLAGSHIPS:
        tag, date, url = releases[repo]
        lines.append(f"| [{name}](https://github.com/HarperZ9/{repo}) | {note} | [{tag}]({url}) ({date}) |")
    return "\n".join(lines)


def badge(label: str, value: str) -> str:
    """A square-cornered chip that reads on both GitHub themes."""
    lw = 12 + 7.2 * len(label)
    vw = 12 + 7.2 * len(value)
    w = round(lw + vw)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="22" viewBox="0 0 {w} 22" '
        f'role="img" aria-label="{label} {value}"><title>{label} {value}</title>'
        f'<rect x=".5" y=".5" width="{w - 1}" height="21" fill="#060608" stroke="#6f6a61"/>'
        f'<rect x="{lw:.1f}" y=".5" width="{vw - .5:.1f}" height="21" fill="#ece5d6"/>'
        f'<g font-family="{MONO}" font-size="12">'
        f'<text x="6" y="15" fill="#ece5d6">{label}</text>'
        f'<text x="{lw + 6:.1f}" y="15" fill="#060608">{value}</text></g></svg>\n'
    )


def replace_block(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:start -->\n).*?(<!-- {name}:end -->)", re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"README is missing the {name} markers")
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def planned_files() -> dict[Path, str]:
    releases = {repo: latest_release(repo) for repo, _name, _note in FLAGSHIPS}
    text = README.read_text(encoding="utf-8")
    writing = latest_writing()
    text = replace_block(text, "writing", writing_block(writing))
    text = replace_block(text, "releases", releases_block(releases))
    files = {README: text}
    for repo, label in BADGES:
        files[ART / f"badge-{repo}.svg"] = badge(label, releases[repo][0])
    files[ART / "badge-writing.svg"] = badge("Writing", f"latest {writing[0][0]}")
    files[ART / "badge-feed.svg"] = badge("Atom feed", "subscribe")
    return files


def main(argv: list[str]) -> int:
    files = planned_files()
    changed = [p for p, body in files.items() if not p.exists() or p.read_text(encoding="utf-8") != body]
    if "--check" in argv:
        for path in changed:
            print(f"would change {path.relative_to(ROOT).as_posix()}")
        return 1 if changed else 0
    for path in changed:
        path.write_text(files[path], encoding="utf-8", newline="\n")
        print(f"updated {path.relative_to(ROOT).as_posix()}")
    if not changed:
        print("profile is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
