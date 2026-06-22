# Zain Dana Harper

I build open-source tools that let an AI check its own work - and let *you* re-run the check yourself.

The core is small and hard to corrupt: it perceives an artifact as a witnessed reading, checks it against a standard it didn't set for itself, and keeps a proof anyone can re-run to the identical answer. When there's nothing solid to check against, it says **UNVERIFIABLE** instead of pretending. Accountability is the floor, not the ceiling - once the proof holds, the limits are free to move.

**Don't trust it - check it -> [harperz9.github.io](https://harperz9.github.io/)**

The core is small on purpose, so it composes three ways:

**Bounded agents** - [accountable-surface](https://github.com/HarperZ9/accountable-surface): an MCP server where a model perceives and acts *only* through a witness and a default-deny gate. Awareness is not authority. *(129 tests; filesystem / web / command effectors, inert until the gate allows. In progress - advisory until a runtime enforces it.)* Composed from [coherence-membrane](https://github.com/HarperZ9/coherence-membrane) (perception) + [proof-surface](https://github.com/HarperZ9/proof-surface) (the gate).

**Accountable shipping** - the release toolkit that runs on every release and says *no* by default: [public-surface-sweeper](https://github.com/HarperZ9/public-surface-sweeper), [repo-proof-index](https://github.com/HarperZ9/repo-proof-index), [model-provenance-validator](https://github.com/HarperZ9/model-provenance-validator), [secret-redact-io](https://github.com/HarperZ9/secret-redact-io), [provenance-sensorium](https://github.com/HarperZ9/provenance-sensorium), [workspace-repo-map](https://github.com/HarperZ9/workspace-repo-map). **Six on PyPI; the rest public on GitHub - and I keep those two words apart.**

**Accountable creativity** - [studio-engine](https://github.com/HarperZ9/studio-engine): a zero-dependency creative engine with a grounded critic; every result grows from a single number, so anyone re-runs it to the identical thing - stronger than a signature, because it never asks you to trust the signer. Drawing on [raw](https://github.com/HarperZ9/raw), the real-time rendering eye.

**The witness, the language, the products**
- [EMET](https://github.com/HarperZ9/emet) - external byte-witness: `MATCH` / `DRIFT` / `UNVERIFIABLE`, never *trusted*. *(Honest limit: three language implementations, one author - implementable from the spec, not yet independently re-derived.)*
- [QuantaLang](https://github.com/HarperZ9/quantalang) - a typed effects language; what a function may *do* is part of its type, checked through to C. *(999 tests; C backend end-to-end; other targets experimental.)*
- [Quanta Color](https://github.com/HarperZ9/quanta-color) / [Calibrate Pro](https://github.com/HarperZ9/calibrate-pro) - the standalone products that fund the work. Color and calibration, measured rather than guessed.

**A private tier - by inquiry.** ORCA, an accountable assessment runner that cannot reach the target, and Aleph, a self-red-team for hardening your own models, are private capabilities I run by inquiry, not public releases. In the current climate, that's how capability keeps advancing without forfeiting trust. - [zaindharper@gmail.com](mailto:zaindharper@gmail.com)

## The Through-Line

Before software or a model makes a claim, the state behind it should be visible enough to inspect. Public repos expose the safe product and research surfaces; private repos keep unpublished, proprietary, operational, or reverse-engineering material out of public paths. When a private system holds a harmless reusable part, I split that piece into a small public package instead of publishing the bundle. Every release carries its maturity verdict - the shipped say shipped, the conceptual say conceptual.

## Stack

Rust / Python / C++ / HLSL / Lua / TypeScript / CMake / D3D11 / Linux / Windows.

## Attribution

Some tooling work includes Claude Code as an AI build partner; I review, test, edit, and own the public release surface myself. The standard I ask to be held to: **judge the action, never the worth.**

Independent since 2023 / Seattle / [harperz9.github.io](https://harperz9.github.io/)
