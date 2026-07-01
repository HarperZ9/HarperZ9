# Usage Guide

This repository publishes the `HarperZ9` GitHub profile README. It is a public
front door to the Project Telos site, cross-domain research lab, flagship
engines, tester threads, and verification surfaces.

The README uses only GitHub-native interaction: collapsible sections, tables,
Mermaid diagrams, and links to live site surfaces. Real JavaScript maps and
dashboards should live on the site, with the profile linking out to them.

Hiring-oriented sections should stay concrete: each claim needs a public
artifact, a first inspection path, or an explicit boundary.

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
- Keep the time-budgeted hiring path and proof-of-work matrix close to the top.
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
- `docs/research/2026-07-01-index-scope-assessment.md` records the index-backed
  scope correction that keeps Telos framed as a research lab across domains.
- `CHANGELOG.md` records public-facing profile updates.
