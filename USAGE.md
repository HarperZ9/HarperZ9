# Usage Guide

This repository publishes the `HarperZ9` GitHub profile README. It is a public
front door to the Project Telos site, cross-domain research lab, flagship
engines, tester threads, and verification surfaces.

The README uses only GitHub-native interaction: collapsible sections, tables,
Mermaid diagrams, and links to live site surfaces. Real JavaScript maps and
dashboards should live on the site, with the profile linking out to them.

The current concept is a public lab bench. Keep it vivid: reader doors,
instruments, maps, traps, and proof paths. Hiring signal should be present, but
it should be embedded in how the work can be inspected rather than framed as a
generic resume page.

The opening should be personal and grounded. Lead with what Zain likes, what
work he repeatedly returns to, and the actual project/life history behind the
public repos: graphics, color, compilers, field operations, technical writing,
support work, AI systems, and research tooling. Avoid sales-page framing.

The voice should match the recent Codex and Claude Code session pattern without
quoting private transcripts: scan the actual state, dogfood tools against real
work, adversarially test them, keep the first useful failure, merge what holds,
push public-safe artifacts, and raise the bar again.

Keep the project-history layer near the top. It should make the profile easier
to trust by connecting claims to public artifacts and lived work instead of
trying to optimize a pitch.

Interactive elements should stay GitHub-native: expandable showcase drawers,
quest-style interactions, demo links, runnable snippets, Mermaid diagrams, and
links to richer live surfaces on the site.

The workbench quests are the highest-friction interaction layer allowed inside
GitHub Markdown. Keep them concrete, runnable, and public. A visitor should be
able to choose a route, copy a command, inspect an artifact, or ask a better
interview question from that section alone.

Voice should stay human. The profile should preserve the artistic,
mistake-making, fallible person behind the clean engineering surface.

The enterprise profile pass is market-aware and telemetry-informed. Keep exact
market numbers and traffic snapshots in research receipts unless publishing
them directly helps the reader make a better hiring or collaboration decision.

## View

Open:

```text
https://github.com/HarperZ9
```

Primary site:

```text
https://harperz9.github.io
```

## Verify

Run the local profile-surface check:

```powershell
python scripts/check_profile_surface.py
```

Run the Markdown style check used by CI:

```powershell
$markdownFiles = @(
  "README.md",
  "CHANGELOG.md",
  "USAGE.md",
  "PRODUCT.md",
  "docs/brand/README.md",
  "docs/research/2026-07-01-enterprise-profile-research.md",
  "docs/research/2026-07-01-profile-template-research.md",
  "docs/research/2026-07-01-index-scope-assessment.md",
  "docs/superpowers/specs/2026-07-01-github-profile-site-aligned-design.md",
  "docs/superpowers/plans/2026-07-01-github-profile-site-aligned.md"
)
npx.cmd --yes markdownlint-cli2 @markdownFiles
```

Run the public delivery sweep when `public-surface-sweeper` is available
locally:

```powershell
python -m public_surface_sweeper . --workspace --json
```

Before publishing:

- Keep links pointed at public repositories or public pages.
- Keep maturity and funding language concrete.
- Keep the profile short enough to scan from GitHub's first screen.
- Keep the reader doors and showcase/demo drawers close to the top.
- Keep GitHub-native interaction readable when collapsed sections and Mermaid
  diagrams are unavailable.
- Confirm the profile README renders through GitHub Markdown before pushing.
- Do not stage `.env`, local logs, private notes, browser state, credentials,
  or protected corpus material.
- If the profile page does not show the README even though the special repo is
  valid, open the repository page on GitHub and use `Share to Profile`.

## Developer Notes

- `README.md` is the shipped profile surface.
- `PRODUCT.md` records the profile's public product purpose and anti-patterns.
- `AGENTS.md` is the local handoff contract.
- `scripts/check_profile_surface.py` is the CI gate for required public links,
  required repo docs, and credential-shaped text.
- `docs/brand/profile-hero.png` is the canonical Project Telos flagship card
  used by the profile README.
- `docs/research/2026-07-01-profile-template-research.md` records the public
  profile-template and forum research behind the direction.
- `docs/research/2026-07-01-enterprise-profile-research.md` records the
  market, telemetry, forum, and index signals behind the enterprise-profile
  rewrite.
- `docs/research/2026-07-01-index-scope-assessment.md` records the index-backed
  scope correction that keeps Telos framed as a research lab across domains.
- `CHANGELOG.md` records public-facing profile updates.
