# Project Telos Profile Brand Assets

<!-- markdownlint-disable MD013 -->

This directory contains the public README artwork for the `HarperZ9` GitHub
profile.

- Hero image: `profile-hero.png`
- Source artwork: `HarperZ9.github.io/img/og/telos.png`
- Source system: Project Telos flagship card template, `img/og/_card.html`
- Brand rule: one flagship card, one iris accent, no bespoke repo hero.
- Accessibility floor: the README must keep the product name, thesis, project
  links, and verification commands available as real text outside the image.
- Provenance boundary: source fonts and local rendering inputs remain in the
  site project; this repo commits only the exported PNG used by GitHub.

## Fonts (2026-11-14)

`fonts/` holds the four Accession files the art is set in, with their licence,
`fonts/OFL.txt` (SIL Open Font License 1.1, copyright Zain Dana Harper):

- `AccessionDisplay-Bold.ttf`: the name on the hero.
- `AccessionText-Regular.ttf`: running words.
- `AccessionMono-Regular.ttf`: the site address and the badges.
- `AccessionMono-Bold.ttf`: the verdict labels.

All four are version 0.1.0, copied unchanged from `system/fonts/accession/static/`
in the HarperZ9.github.io repository. `scripts/type_kit.py` reads them with
fontTools and writes each letter as an outline.

## Generated art (2026-10-01)

The README now uses the generated plates in `docs/art`, drawn by
`scripts/profile_art.py`. `banner.png` and `profile-hero.png` remain for
external uses and are no longer referenced by the README.
