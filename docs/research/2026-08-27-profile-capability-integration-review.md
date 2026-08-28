# Profile capability integration review

Date: 2026-08-27

## Scope

This review covers only `README.md` and `scripts/check_profile_surface.py` from
the profile update based on `origin/main` at `3a48bfe`. `CHANGELOG.md` and all
other existing profile files remain unchanged.

## Public design decision

The first screen now routes readers through three hiring paths before showing
owned products. Three merged third-party pull requests follow as externally
reviewed evidence. The owned work then appears as one primary platform,
Flywheel, with capability families, lanes, extensions, and bounded standalone
systems. The profile does not maintain a fixed flagship count.

The security summary is deliberately aggregate. Public material is limited to
sanitized tests, schemas, detectors, and bounded findings. Material that could
enable misuse remains outside the public profile and uses approved private or
embargoed handling.

## Ground-truth sources

- Flywheel `pyproject.toml` identifies version `0.3.10`, and the public
  [v0.3.10 release](https://github.com/HarperZ9/flywheel/releases/tag/v0.3.10)
  is published.
- The public
  [Phantom v1.1.0 release](https://github.com/HarperZ9/phantom/releases/tag/v1.1.0)
  is published. The public capability registry limits the shipped surface to
  Layer 2 identity controls and states that kernel and firmware layers are not
  shipped end to end.
- The public
  [Engine Revival v0.1.0](https://github.com/HarperZ9/engine-revival/releases/tag/v0.1.0)
  and
  [BRender Archival v0.1.1](https://github.com/HarperZ9/brender-archival/releases/tag/v0.1.1)
  releases are published. Their proof boundaries remain separate from the
  browser Retro Engine.
- [AgentFence PR 261](https://github.com/dgenio/agentfence/pull/261),
  [Free Law Project PR 820](https://github.com/freelawproject/litigant-portal/pull/820),
  and [Mergewarden PR 107](https://github.com/sjh9714/mergewarden/pull/107)
  are merged after third-party review.

## Test-first receipt

1. The revised verifier ran against the old profile and failed on the missing
   hiring paths, proof section, capability architecture, current versions, and
   Retro Systems Lab boundaries.
2. The hiring-first profile made the verifier pass.
3. Independent review found that a fourth path or fourth proof could still pass.
4. Temporary mutations added one extra path and one extra proof. Each mutation
   failed for the intended invariant before the temporary content was removed.
5. The clean profile then returned `profile surface: ok`.

The verifier now checks the exact three path labels and order, the exact three
external pull-request proofs, proof ownership outside `HarperZ9`, section order,
the current Flywheel and Phantom identities, the Retro route, controlled
security handling, public link shapes, a 1,000-word ceiling, and
credential-shaped text.

## Verification

- Profile verifier: pass.
- Markdown lint for the repository CI file set: pass with zero issues.
- README word count: 774.
- Public link probe: all GitHub and site links returned HTTP 200. LinkedIn
  returned its automated-client block code, so that URL was verified by shape
  but not by an unauthenticated automated fetch.
- Hiring-page fragment check: `engineering-path` and
  `public-service-field-path` both exist in the live page.
- Credential-shaped scan of changed files: no matches.
- `git diff --check`: pass.
- Independent re-review after the mutation-gate fix: pass with no material
  findings.

These checks establish profile consistency and current public-link state. They
do not establish product adoption, employer endorsement, or suitability for
every role.
