# GitHub Profile Site-Aligned Implementation Plan

<!-- markdownlint-disable MD013 -->

**Goal:** Revise the public `HarperZ9/HarperZ9` GitHub profile repository so it
matches the Project Telos site design, clean professional tone, and canonical
flagship artwork, while presenting Telos as a research lab across domains.

**Architecture:** Keep `README.md` as the shipped public profile. Replace the
bespoke profile visual with the canonical Project Telos flagship card and
update the verifier so site-aligned copy, research-lab scope, and public
project links stay present.

**Tech Stack:** GitHub Flavored Markdown, static PNG hero asset, Python 3
standard library, GitHub Actions Markdown lint.

## Global Constraints

- Public links only.
- No credentials, `.env` files, private notes, browser state, local logs, or
  protected corpus material.
- Keep claims concrete and checkable.
- Keep the profile short enough to scan from GitHub's first screen.
- Preserve required links to the main site and the eight public engines.
- Preserve the broader research-lab framing from the index-backed scope
  assessment.
- Preserve GitHub-native interaction that helps hiring managers route through
  the work quickly.
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

- [x] Run `python scripts/check_profile_surface.py`.
- [x] Run Markdown lint against the documented files.
- [x] Render the README through GitHub Markdown.
- [x] Run a credential-shaped text scan.
- [x] Push the profile repo to `origin/main`.
- [x] Use GitHub's `Share to Profile` control when the special README does not
      auto-render on the actual profile page.
- [x] Verify the actual profile page renders the Project Telos README.

### Task 5: Research Lab Scope Correction

**Files:**

- Modify: `README.md`
- Modify: `scripts/check_profile_surface.py`
- Add: `docs/research/2026-07-01-index-scope-assessment.md`

**Steps:**

- [x] Run `index map`, `index context`, `index router`, and a focused Telos
      context envelope over the public workspace.
- [x] Compare the indexed repo/doc surface against the narrower profile copy.
- [x] Reframe evidence/accountability as the lab method, not the whole mission.
- [x] Add domain lanes covering formal systems, AI4Science, infrastructure
      risk, perception/media, and agent/product surfaces.
- [x] Update the profile verifier and docs so the correction persists.

### Task 6: Hiring Signal and GitHub-Native Interaction

**Files:**

- Modify: `README.md`
- Modify: `scripts/check_profile_surface.py`

**Steps:**

- [x] Add a hiring-manager fast path before the deep flagship inventory.
- [x] Add collapsible reader paths for hiring managers, engineers, and
      research collaborators.
- [x] Add Mermaid ecosystem map and route chart blocks that GitHub can render.
- [x] Add direct links to live site surfaces for richer interaction.
- [x] Label charts that are editorial routing aids rather than traffic data.
- [x] Update the verifier and docs so these interactive affordances persist.
