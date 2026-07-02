# Project Telos

![Project Telos profile hero](docs/brand/profile-hero.png)

> A shared workspace where a person and an AI see the same live state, make
> things together, and can re-check every step.

I am **Zain Dana Harper**: a self-taught systems engineer, building in the
open since 2023, with AI directed as a coordinated teammate. The public work
spans an accountable human-AI workspace, a systems compiler, real-time
rendering, color science, and release tooling. One operation runs through all
of it: perceive into a witnessed form, check it against a criterion it did not
author, carry a re-checkable proof, and say UNVERIFIABLE when it cannot.
Verification is the floor the work launches from, not the headline.

**Main site: [harperz9.github.io](https://harperz9.github.io)** ·
[Field guide](https://harperz9.github.io/field-guide.html) ·
[How this profile is verified](USAGE.md)

## The flagships

Eight public engines: peers, built to compose. Each stands alone; together
they are the larger project. Seven ship fair-source; emet is MPL-2.0. The
workspace behind them, mapped by index itself on 2026-07-01:
147 repositories, 70 public on GitHub.

| Engine | What it is | Release |
|---|---|---|
| **[telos](https://github.com/HarperZ9/telos)** | The engine: a shared perceive-and-make studio for human-AI creation, simulation, MCP tools, and replayable receipts. The public repo is a demo slice of the native engine. | `v0.1.0` demo |
| **[index](https://github.com/HarperZ9/index)** | The map: workspace inventory and dependency graphs for many-repo work. | ![PyPI](https://img.shields.io/pypi/v/index-graph?label=index-graph) |
| **[forum](https://github.com/HarperZ9/forum)** | The orchestrator: multi-agent runs recorded in a witnessed causal ledger. | ![PyPI](https://img.shields.io/pypi/v/forum-engine?label=forum-engine) |
| **[gather](https://github.com/HarperZ9/gather)** | The intake: research ingestion with provenance receipts and a re-verifiable corpus. | ![PyPI](https://img.shields.io/pypi/v/gather-engine?label=gather-engine) |
| **[crucible](https://github.com/HarperZ9/crucible)** | The judgment: register, steelman, measure, refine. Verdicts are MATCH, DRIFT, or UNVERIFIABLE. | ![PyPI](https://img.shields.io/pypi/v/crucible-bench?label=crucible-bench) |
| **[emet](https://github.com/HarperZ9/emet)** | The byte witness: re-derives a file's bytes and reports MATCH, DRIFT, or UNVERIFIABLE. Reproduced in four independent languages. | ![PyPI](https://img.shields.io/pypi/v/emet) |
| **[buildlang](https://github.com/HarperZ9/buildlang)** | The authoring language: a typed-effects compiler with a verified C path, shader output, and re-checkable accountability receipts. `cargo install buildlang`. | ![crates.io](https://img.shields.io/crates/v/buildlang) |
| **[learn](https://github.com/HarperZ9/learn)** | The learning aid: retrieval practice and self-explanation checked by crucible; every graded step halts for the human and is witnessed. Zero-dep Node. | ![npm](https://img.shields.io/npm/v/%40harperz9%2Flearn?label=%40harperz9%2Flearn) |

The release badges read live from the package registries, so those rows
cannot silently go stale; the telos demo tag is the one hand-pinned value.

## The substrate

The engines stand on a wider base, built native and dependency-light:

- **[coherence-membrane](https://github.com/HarperZ9/coherence-membrane)**:
  receipt-backed perception of files, images, and screens for AI agents.
- **[accountable-surface](https://github.com/HarperZ9/accountable-surface)**:
  gates agent actions behind explicit grants and durable journals.
- **[proof-surface](https://github.com/HarperZ9/proof-surface)**: stdlib-only
  contracts for evidence packets, receipts, gates, and verdicts.
- **[studio-engine](https://github.com/HarperZ9/studio-engine)**: replayable
  creative worlds: shaders, sound, motion timelines, receipts.
- **The Build family**: [build-color](https://github.com/HarperZ9/build-color)
  color science, [calibrate-pro](https://github.com/HarperZ9/calibrate-pro)
  display calibration, [build-oracle](https://github.com/HarperZ9/build-oracle)
  forecasting, [build-engine](https://github.com/HarperZ9/build-engine)
  prediction, [build-ui](https://github.com/HarperZ9/build-ui) shared UI.
  ![PyPI](https://img.shields.io/pypi/v/build-color?label=build-color)

## Where it fits

- **Doctor / clinical admin**: keep source fragments, routing decisions, and
  uncertainty visible before a model summary becomes action.
- **Artist / studio**: preserve prompts, source assets, transforms, chosen
  branches, and export gates instead of losing the trail in a pile of outputs.
- **Media / newsroom**: map each public claim back to witnessed sources,
  conflict notes, and a decision ledger.
- **Token economy / routing**: spend model calls where they buy evidence, not
  where they merely create confident prose.
- **Reasoning**: let the model perceive and propose, but keep final authority
  outside the model and inside a checkable record.

## Recent public dogfood

- [SmallHarness external fixture loading](https://github.com/GetSmallAI/SmallHarness/pull/13)
  merged: data-only external eval fixtures with path-safety handling.
- [Pydantic AI turn index](https://github.com/pydantic/pydantic-ai/pull/6135)
  open: stable chat span names with `gen_ai.turn.index` for agent trace
  evaluation.
- [AutoGen scankii receipt feedback](https://github.com/microsoft/autogen/discussions/7890#discussioncomment-17474671)
  live: replayable scan-receipt dogfood across static-only, file-side, and
  unverifiable-boundary fixtures.

## Open tester threads

The fastest way to help: run one tool against a real workflow and report what
breaks.

- [Test gather intake](https://github.com/HarperZ9/gather/issues/1)
- [Test index maps](https://github.com/HarperZ9/index/issues/13)
- [Test forum ledgers](https://github.com/HarperZ9/forum/issues/1)
- [Test crucible checks](https://github.com/HarperZ9/crucible/issues/1)
- [Test the telos surface](https://github.com/HarperZ9/telos/issues/2)

## Status, honestly

Solo, independent, and pre-revenue. Every claim here ships beside its test, its receipt, or
its explicit limit; the largest claims still await external reproduction, and
this page points to evidence rather than asking for trust. I am looking for
testers with real workflows, collaborators who inspect receipts, and modest
grassroots research funding.

## For developers

This repository is the GitHub profile README; licenses and runnable commands
live in the linked repos. Before publishing changes here:

```bash
git status --short
python scripts/check_profile_surface.py
```
