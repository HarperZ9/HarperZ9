# Zain Dana Harper

Independent software engineer working on **AI accountability**: making the
intent that goes *into* model-assisted work and the work record that comes
*back out* both visible enough to inspect. The through-line is bilateral
provenance &mdash; trusted context carried inward, a verifiable work record carried
outward &mdash; and live-state awareness: small programmatic organs that give a model
or a reviewer moment-to-moment ground truth instead of a remembered
representation.

The flagship is **EMET**, an external byte-witness. **proof-surface** is the
shared contract those tools agree on. The **QuantaLang / Quanta** portfolio is
the engineering-depth proof behind the thesis.

**Portfolio: [harperz9.github.io](https://harperz9.github.io/)**

## The accountability spine

- **[EMET](https://github.com/HarperZ9/emet)** &mdash; an external witness for
  source/view consistency. It re-derives a SHA-256 over raw source bytes and
  reports one of three deliberately limited verdicts: `MATCH`, `DRIFT`, or
  `UNVERIFIABLE`. Trust comes from re-derivation &mdash; same bytes, same answer &mdash; not
  from authority: the verdict lattice is *structurally closed*, so `governed()`
  raises at construction time before any `TRUSTED`/`APPROVED`/`AUTHORIZED` token
  could reach output. It keeps a hash-chained, tamper-evident audit log.
  Reference implementation in Python plus from-scratch Rust and Node
  re-implementations that pass the same 19 conformance vectors in CI. (The three
  implementations are same-author, so cross-language agreement here is
  re-derivability *in principle*; a different-author conformance implementation
  is future work.)

- **[proof-surface](https://github.com/HarperZ9/proof-surface)** &mdash; the shared,
  stdlib-only contract family the accountability tools agree on: a neutral
  evidence **packet**, a hard-pinned **work-record receipt** (a verifiable
  record that flows outward for review &mdash; the structural inverse of an
  authorization-suppression "prefire"), and a **witness-receipt** validator that
  mirrors EMET's closed verdict lattice without importing EMET. Every validator
  rejects authority-shaped content. 21 tests.

- **[proof-surface-report](https://github.com/HarperZ9/proof-surface-report)** &mdash;
  a reviewer-facing Markdown adapter for packets and receipts. It renders
  evidence for a human and rejects authority-shaped language on the way out.

- **[repo-proof-index](https://github.com/HarperZ9/repo-proof-index)** &mdash; a
  reviewer-ready aggregator/indexer over proof packets and receipts. It indexes
  the evidence; it does not decide whether the evidence is enough.

## Provenance, hygiene, and agent review

- **[model-provenance-validator](https://github.com/HarperZ9/model-provenance-validator)**
  &mdash; validates provenance envelopes and redacts secret-shaped values out of its
  own output.
- **[agent-audit](https://github.com/HarperZ9/agent-audit)** &mdash; a dependency-light
  Python SDK/CLI that audits an AI-agent session by checking a declared-intent +
  action-ledger against a scope policy. It flags intent drift, scope violations,
  and prior-work claims the ledger does not support &mdash; making agent behavior
  transparent and reviewable.
- **[provenance-sensorium](https://github.com/HarperZ9/provenance-sensorium)** &mdash;
  a fully-tested local CLI/library that turns project files, git state, and
  Markdown claims into hash-stamped JSON provenance receipts and flags secrets,
  private-path leaks, and unevidenced or human-only claims before you publish.
- **[release-surface-scanner](https://github.com/HarperZ9/release-surface-scanner)**
  &mdash; a dependency-free CLI that turns a repository into a reviewable release
  packet: required-file checks, `.env` exclusion, secret-shape detection that
  never echoes the value, per-file hashing, and JSON/Markdown reports plus a
  compact proof index.
- **[public-surface-sweeper](https://github.com/HarperZ9/public-surface-sweeper)**
  &mdash; a pre-release repo-hygiene scanner for required files and secret-shaped
  values. Release hygiene, not a vulnerability scanner.
- **[secret-redact-io](https://github.com/HarperZ9/secret-redact-io)** &mdash; a tiny
  stdlib-only SDK and CLI that wraps file, fetch, and subprocess IO to strip
  common secret shapes (API keys, tokens, PEM keys) and emit hash-only audit
  receipts (byte counts, SHA-256, redaction counts) without ever storing the raw
  values.

## Live-state organs and signal kernels

- **[signal-kernels](https://github.com/HarperZ9/signal-kernels)** &mdash; a
  header-only C++23 signal / information-theory library: entropy, mutual
  information / transfer entropy, KL / Jensen-Shannon / Hellinger / Wasserstein
  divergence, Granger causality, PELT change-point detection, FFT, and
  SARIMA / VAR forecasting. Tests green.
- **[anomaly-kernels](https://github.com/HarperZ9/anomaly-kernels)** &mdash; C++23
  statistical anomaly-detection kernels: baseline profiling, z-score / IQR /
  percentile scoring, and multi-signal temporal correlation.
- **[gpu-trace-validator](https://github.com/HarperZ9/gpu-trace-validator)** &mdash;
  validates GPU trace JSON against a schema and emits bounded, redacted
  receipts. An early state-aware organ for graphics work that needs inspectable
  frame/pass receipts.

## QuantaLang and the Quanta portfolio

- **[QuantaLang](https://github.com/HarperZ9/quantalang)** &mdash; an effects-oriented
  compiler built in Rust. It compiles `.quanta` source to **C** as the primary,
  end-to-end **verified** execution path, and emits **HLSL** and **GLSL** for
  shader work. SPIR-V, LLVM IR, WebAssembly, Rust source, x86-64, and ARM64
  backends are plainly labeled experimental research surfaces. QuantaLang is the
  effects-language side of the same live-state thesis: typed effect receipts and
  policy gates that make what code touched and emitted inspectable. Editor
  support ships as
  [quantalang-vscode](https://github.com/HarperZ9/quantalang-vscode) and
  [quantalang-tmLanguage](https://github.com/HarperZ9/quantalang-tmLanguage).
- **[Quanta Color](https://github.com/HarperZ9/quanta-color)** &mdash; Python
  color-science tooling: color spaces, tone mapping, appearance models, spectral
  workflows, and ICC/LUT work.
- **[Calibrate Pro](https://github.com/HarperZ9/calibrate-pro)** &mdash; Windows
  display-calibration tooling with measured workflows, DDC/CI, LUT/ICC output,
  and verification reports (including reverse-engineered colorimeter drivers).
- **Quanta finance / oracle / engine / ui** &mdash; source-visible proprietary
  fintech and forecasting surfaces.

## Agent-dev utilities

Small, deterministic helpers extracted from larger workflow patterns:
[agent-routing-kit](https://github.com/HarperZ9/agent-routing-kit),
[context-curator-lite](https://github.com/HarperZ9/context-curator-lite),
[workflow-harness-lite](https://github.com/HarperZ9/workflow-harness-lite),
[workspace-repo-map](https://github.com/HarperZ9/workspace-repo-map), and
[agent-hook-pack](https://github.com/HarperZ9/agent-hook-pack).

## Services

**Harper Compliance** offers compliance consulting: document kits, policy
templates, and process guidance for teams navigating regulatory and operational
requirements. Work is delivered through a private-repo service site with
browser-side document flows. Live at
[harpercompliance.llc](https://harpercompliance.llc).

**Harper Advocates / SendMyLetter** is a consumer-rights letter service: it
generates demand letters and rights-assertion documents for individuals.
Delivered through a responsive frontend with browser-side document workflows.
Live at [harperadvocates.com](https://harperadvocates.com).

Both services run on privately-held repos. The public proof is the live site
itself.

## Through-line

AI accountability has two directions, and most tooling only covers one. Build
provenance proves *how* an artifact was produced; it does not catch a system
vouching for itself in-band, a presented view drifting from its source, or an
agent claiming prior work its ledger never recorded. The spine here closes that
gap on both sides: **inward**, trusted context and scope; **outward**, a
verifiable work record a reviewer can re-derive. EMET is the byte-level witness
that refuses to certify itself; proof-surface is the contract its consumers
share; the Quanta/QuantaLang portfolio is where the same idea &mdash; make messy work
inspectable &mdash; shows up as compiler, color, and signal engineering.

Where a private system contains a reusable, harmless part, I split that piece
into a smaller public package rather than publishing the whole bundle.

## Stack

Rust, Python, C++23, HLSL/GLSL, TypeScript, CMake, Linux, Windows.

## Areas

AI accountability and provenance, compiler design, signal / information theory,
color science, display calibration, systems programming, conformance testing,
and agent workflow tooling.

## Style

Small tools with explicit edges: typed inputs, visible state, reproducible
tests, and public claims that can be checked. The standard is plain &mdash; ship
useful pieces, keep sensitive systems compartmentalized, and leave enough
evidence for someone else to re-derive the reasoning.

## Contributor attribution

Some recent tooling work includes Claude Code as an AI coding contributor. I use
it as a build partner, then review, test, edit, and own the public release
surface myself.
