# Project Telos

![Project Telos profile hero](docs/brand/profile-hero.png)

> Public map of the tools, demos, receipts, and status behind the Telos work.

This profile is the front door for the public Project Telos tool system:
research intake, codebase indexing, agent routing, claim checking, creative
workspaces, release hygiene, and receipt-backed demos.

## Why it matters

The public portfolio should make it clear what can be opened, tested, and
verified today. This profile keeps the flagship repos, current status, and
tester entry points in one place instead of relying on scattered claims.

## Try it

```bash
git clone https://github.com/HarperZ9/HarperZ9.git
python -m webbrowser https://harperz9.github.io
```

## What to test first

- Open the five flagship repos and run their `doctor`, `status`, or demo commands.
- Use the tester issues linked below to report real workflow gaps.
- Check claims against repo tests, release notes, receipts, or explicit limits.

## Current status

Public profile and live project map. The largest claims remain pre-proof until
external testers reproduce them; the profile should point to evidence, not ask
for trust.

## Developer notes

This repository is the GitHub profile README. Licenses and runnable commands live
in the linked tool repositories; this page routes readers to those surfaces.

## Existing public profile
### The surface every domain launches from. Let's have a look.

**Main site:** [harperz9.github.io](https://harperz9.github.io)

One operation makes any claim, action, or creation **checkable**, so a person and an AI can do real work together and verify every step. Accountability is not the brake; it is the runway. Security is one domain on it, not the point.

**Field guide:** [harperz9.github.io/field-guide.html](https://harperz9.github.io/field-guide.html)

I am **Zain Dana Harper**, self-taught, building in the open since 2023, with AI directed as a coordinated teammate. Everything here is public, local-first where possible, and honest about where it stands: **every claim ships beside its test, or its limit.** Do not trust it, check it.

## The Flagships

One operation runs through all of them: perceive into a witnessed form, check it against a criterion it did not author, carry a re-checkable proof, and say UNVERIFIABLE when it cannot.

| Flagship | What it does | Status |
|---|---|---|
| [gather](https://github.com/HarperZ9/gather) | research intake with provenance receipts | PyPI `gather-engine` 1.5.0, fair-source |
| [index](https://github.com/HarperZ9/index) | workspace maps and context graphs for repos, docs, and assets | PyPI `index-graph` 2.8.0, fair-source |
| [forum](https://github.com/HarperZ9/forum) | accountable multi-agent orchestration on a witnessed causal ledger | PyPI `forum-engine` 1.12.0, fair-source |
| [crucible](https://github.com/HarperZ9/crucible) | judgment/refinement organ that steelmans, measures, and refines claims | public repo; `crucible-bench` 1.1.0 local package metadata; no PyPI claim here |
| [the telos engine](https://github.com/HarperZ9/telos) | shared perceive-and-make studio for human-AI work, MCP, and creative/science demos | source registry 0.1.0, active |

## Where to test it

- **Doctor / clinical admin:** keep source fragments, routing decisions, and uncertainty visible before a model summary becomes action.
- **Artist / studio:** preserve prompts, source assets, transforms, chosen branches, and export gates instead of losing the trail in a pile of outputs.
- **Media / newsroom:** map each public claim back to witnessed sources, conflict notes, and a decision ledger.
- **Token economy / routing:** spend model calls where they buy evidence, not where they merely create confident prose.
- **Reasoning:** let the model perceive and propose, but keep final authority outside the model and inside a checkable record.

Solo, pre-revenue, pre-proof on the largest claims, and built to be inspected. I am looking for verification, testing against real workflows, early traction from people willing to inspect the receipts, and possibly modest grassroots research funding.

## Recent public dogfood

- [SmallHarness external fixture loading](https://github.com/GetSmallAI/SmallHarness/pull/13) merged: data-only external eval fixtures with path-safety handling.
- [Pydantic AI turn index](https://github.com/pydantic/pydantic-ai/pull/6135) is open: stable chat span names with `gen_ai.turn.index` for agent trace evaluation.
- [AutoGen scankii receipt feedback](https://github.com/microsoft/autogen/discussions/7890#discussioncomment-17474671) is live: replayable scan-receipt dogfood across static-only, file-side, and unverifiable-boundary fixtures.

## Open tester threads

- [Test gather intake](https://github.com/HarperZ9/gather/issues/1)
- [Test index maps](https://github.com/HarperZ9/index/issues/13)
- [Test forum ledgers](https://github.com/HarperZ9/forum/issues/1)
- [Test crucible checks](https://github.com/HarperZ9/crucible/issues/1)
- [Test the telos surface](https://github.com/HarperZ9/telos/issues/2)

## For developers

Keep the public README, examples, and repository metadata aligned with current behavior. Before opening a PR or publishing a release, verify the working tree and any documented commands for this repo.

```bash
git status --short
```
