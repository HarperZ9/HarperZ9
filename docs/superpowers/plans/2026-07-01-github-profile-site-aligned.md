# GitHub Profile Site-Aligned Implementation Plan

<!-- markdownlint-disable MD013 -->

**Goal:** Revise the public `HarperZ9/HarperZ9` GitHub profile repository so it
matches the Project Telos site design, clean professional tone, and canonical
flagship artwork.

**Architecture:** Keep `README.md` as the shipped public profile. Replace the
bespoke profile visual with the canonical Project Telos flagship card and
update the verifier so site-aligned copy and public project links stay present.

**Tech Stack:** GitHub Flavored Markdown, static PNG hero asset, Python 3
standard library, GitHub Actions Markdown lint.

## Global Constraints

- Public links only.
- No credentials, `.env` files, private notes, browser state, local logs, or
  protected corpus material.
- Keep claims concrete and checkable.
- Keep the profile short enough to scan from GitHub's first screen.
- Preserve required links to the main site and the eight public engines.
- Use `docs/brand/profile-hero.png`; do not add bespoke README diagrams.

---

### Task 1: Brand Asset Alignment

**Files:**

- Replace: `docs/brand/profile-hero.png`
- Modify: `docs/brand/README.md`

**Steps:**

- [x] Copy the canonical Telos flagship card from the site repo.
- [x] Remove the custom evidence map asset.
- [x] Document the card source and accessibility boundary.

### Task 2: README Rewrite

**Files:**

- Modify: `README.md`

**Steps:**

- [x] Open with the flagship card and site thesis.
- [x] Introduce Zain Dana Harper and Project Telos in the site's professional
      tone.
- [x] Mirror the eight-engine site architecture with mobile-readable rows.
- [x] Keep tester issues and developer verification commands.

### Task 3: Verification Contract

**Files:**

- Modify: `scripts/check_profile_surface.py`
- Modify: `.github/workflows/ci.yml`
- Modify: `USAGE.md`

**Steps:**

- [x] Require site-aligned terms, public project links, and the hero asset.
- [x] Remove the obsolete custom SVG requirement.
- [x] Keep credential-shaped text scanning in the local verifier.

### Task 4: Verification

**Files:**

- Read: `README.md`
- Read: `scripts/check_profile_surface.py`

**Steps:**

- [ ] Run `python scripts/check_profile_surface.py`.
- [ ] Run Markdown lint against the documented files.
- [ ] Render the README through GitHub Markdown.
- [ ] Run a credential-shaped text scan.
- [ ] Amend the local profile commit after checks pass.
