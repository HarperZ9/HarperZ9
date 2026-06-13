# AGENTS.md - GitHub Profile

## Scope

This file applies to the `HarperZ9/HarperZ9` profile repository. Root workspace
instructions still apply; this repository is a public GitHub profile surface.

## Product Boundary

The profile README is a public positioning surface. It should point readers to
stable public repos, portfolio pages, and safe release-candidate products.

Publishable surfaces:

- `README.md` - public profile content.
- `AUTHORS.md` - authorship and release ownership note.

Never publish:

- `.env`, `.env.*`, credentials, API tokens, private notes, browser profiles,
  generated local logs, or protected corpus material.
- Details from private repositories unless they have been deliberately split
  into public, scrubbed product surfaces.

## Editing Rules

- Keep links pointed at public repositories or public pages.
- Keep claims concrete and checkable.
- When adding a product, use the same maturity language used by the portfolio
  site: public work, release candidate, sample, research, or archived.
- Keep the profile short enough to scan from GitHub's first screen.

## Verification

For profile edits:

```powershell
git diff --check
```

Before committing or pushing, scan changed files for credential-shaped content
and confirm no local-only files are staged.
