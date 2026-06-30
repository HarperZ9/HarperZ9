# Usage Guide

This repository publishes the `HarperZ9` GitHub profile README. It is a public
map to Project Telos tools, demos, tester threads, and evidence surfaces.

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

Run the public delivery sweep when `public-surface-sweeper` is available
locally:

```powershell
python -m public_surface_sweeper . --workspace --json
```

Before publishing:

- Keep links pointed at public repositories or public pages.
- Keep maturity and funding language concrete.
- Keep the profile short enough to scan from GitHub's first screen.
- Do not stage `.env`, local logs, private notes, browser state, credentials,
  or protected corpus material.

## Developer Notes

- `README.md` is the shipped profile surface.
- `AGENTS.md` is the local handoff contract.
- `scripts/check_profile_surface.py` is the CI gate for required public links,
  required repo docs, and credential-shaped text.
- `CHANGELOG.md` records public-facing profile updates.
