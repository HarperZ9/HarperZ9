# Usage Guide

This repository publishes the `HarperZ9` GitHub profile README. The design,
scope and claim rules are in `PRODUCT.md`.

The README uses only what GitHub renders: generated SVG plates in light and
dark variants, collapsed sections, tables, one Mermaid diagram, and links to
live pages. Richer interactive pages live on the site.

## Regenerate the art

```powershell
python scripts/profile_art.py
```

Output is deterministic, and CI fails if the committed SVGs differ from a
fresh run.

## Refresh the live blocks

```powershell
python scripts/refresh_profile.py
python scripts/refresh_profile.py --check
```

The first command rewrites the release table, the latest-writing list and the
badges. The second exits 1 when a rewrite would change files. The scheduled
`Refresh profile` workflow runs the same script daily and commits only when
something changed.

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
- `PRODUCT.md` records scope, art rules and claim rules.
- `AGENTS.md` is the local handoff contract.
- `scripts/check_profile_surface.py` is the CI gate. Its rules, including the
  word limit and the reason it was set, live in `scripts/profile_surface.toml`.
- `scripts/art_kit.py` and `scripts/profile_art.py` draw the plates in
  `docs/art`.
- `scripts/refresh_profile.py` writes the generated README blocks and badges.
- `docs/research` keeps earlier research records behind the profile.
- `CHANGELOG.md` records public-facing profile updates.
