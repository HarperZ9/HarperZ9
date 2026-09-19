# Zain Dana Harper / ZentropyLabs.ai

<!-- markdownlint-disable MD013 MD033 -->

<img src="docs/brand/zentropy-banner.png" alt="Zentropy Labs: Work you can walk away from." width="100%">

## Mission: re-derivable verification

AI now shapes decisions about money, health, safety, and the work that builds the
next AI. When a model produces an answer that matters, the person on the receiving
end usually has to trust whoever ran it. I build tools that remove that
requirement. An accepted result carries a receipt, and a skeptic re-runs the
recorded check on their own machine, offline, and reaches the same verdict without
trusting me, my company, or my lab.

That property is what capture and conflict of interest cannot survive. A captured
auditor or a self-interested lab cannot fake a verdict a skeptic re-runs for
themselves, so accountability stops depending on who you trust and starts
depending on a check anyone can repeat. The same holds across any actor, company,
lab, or nation: given the same check, evidence, and assumptions, a correct
implementation returns the same verdict. The end I work toward is trustworthy AI
that reaches individuals without asking them to trust a party they cannot inspect.

A public evaluation claim should expose its claim, boundary, evidence, source
version, execution assumptions, false-success controls, and correction path, so
another reviewer can rerun or challenge the verdict. A receipt proves a check
reproduces. It does not prove the answer is true of the world. That bound stays
attached to every claim here.

## Flagship: Flywheel v1.0.1

Flywheel runs a task with any model you choose, local or frontier, behind one
OpenAI-compatible surface, and runs a gated coding agent over your own folders.
Every accepted answer emits a proof receipt anyone can re-run offline for the same
verdict, with no learned model on the accept path. Ten native evaluation lanes
bundle from hash-pinned source and launch on a clean machine. It also ships a
native desktop app.

- Install: `pip install flywheel-verify`
- Release: [Flywheel v1.0.1](https://github.com/HarperZ9/flywheel/releases/tag/v1.0.1), with the Windows installer attached
- Honest null: on the shipped benchmark the verified loop shows no measured
  accuracy uplift over single-shot, and the interval includes zero. The value it
  delivers is the re-derivable receipt and the containment.

[Inspect Flywheel](https://github.com/HarperZ9/flywheel) ·
[Read publications](https://harperz9.github.io/publications.html) ·
[See the evidence](https://harperz9.github.io/demonstrations.html) ·
[Portfolio](https://harperz9.github.io/portfolio.html)

## Evidence accepted upstream

These results show the work surviving another maintainer's scope and review.

- [AgentFence PR 261](https://github.com/dgenio/agentfence/pull/261): an
  owner-approved and merged Go engine optimization with deterministic rule
  selection, allocation coverage, and green cross-platform checks.
- [Free Law Project PR 820](https://github.com/freelawproject/litigant-portal/pull/820):
  approved and merged documentation for running the fast DB-free test suite.
- [Mergewarden PR 107](https://github.com/sjh9714/mergewarden/pull/107):
  replay fixtures for reusable-workflow pinning, revised after owner review,
  approved, merged, and CI-checked.

## What I built

Six representative projects, described by what the code does. Flywheel is the
primary platform; the others solve narrower problems and can be used on their
own.

| Project | What it does |
| --- | --- |
| [Flywheel](https://github.com/HarperZ9/flywheel) | Flywheel runs a task with any model you choose, local or frontier, behind one OpenAI-compatible surface, and runs a gated coding agent over your own folders. Every accepted answer emits a proof receipt anyone can re-run offline for the same verdict, with no learned model on the accept path. It also ships a native desktop app. |
| [Index](https://github.com/HarperZ9/index) | Index maps repositories and multi-repo workspaces so you can see how the code fits together. It reads manifests, imports, symbols, and local documentation, then builds offline wikis, dependency maps, context packets, and architecture checks with file-and-line evidence. |
| [Gather](https://github.com/HarperZ9/gather) | Gather collects research material from sources that basic scrapers often miss. It handles JavaScript-rendered pages, authenticated APIs, scholarly records, PDFs, OCR, audio, video, feeds, and local documents, then saves each item in a content-addressed corpus with provenance you can recheck. |
| [BuildLang](https://github.com/HarperZ9/buildlang) | BuildLang is a systems programming language and compiler that makes programs declare what they are allowed to touch. It checks those permissions and memory rules before producing native code through C. Experimental shader output, two-way C integration, a CLI, editor support, and re-checkable build receipts are included. |
| [Phantom](https://github.com/HarperZ9/phantom) | Phantom helps you inspect and, when authorized, change the hardware identifiers a computer exposes. It works on owned or expressly authorized Windows and Linux systems, saves a backup before changes, and can restore the original values. |
| [Accountable Surface](https://github.com/HarperZ9/accountable-surface) | Accountable Surface lets an AI agent take only the file, command, web, or browser action a person has approved. It checks the request and authorization, blocks or pauses when needed, verifies the outcome, rolls back reversible failures, and records decisions and outcomes in a journal. Persisted journals are hash-chained so later edits, deletions, or reordering are detected. |

## Systems, grouped by the work they do

The current verified release of
[Flywheel v1.0.1](https://github.com/HarperZ9/flywheel/releases/tag/v1.0.1):
a self-hostable, model-agnostic agent workstation and coding harness for
routing, gated tool use, ten native evaluation lanes, receipts, memory, context,
and reproducible workflows. The backbone is re-derivable verification: nothing is
accepted without a receipt, and no learned model sits on the accept path. It is
the sole primary platform, not a label for everything else in the workshop.

| Family | Representative public work |
| --- | --- |
| **Agent execution and memory** | [Flywheel](https://github.com/HarperZ9/flywheel), [Forum](https://github.com/HarperZ9/forum), [Relay](https://github.com/HarperZ9/relay), [Mneme](https://github.com/HarperZ9/mneme), [Plexus](https://github.com/HarperZ9/plexus) |
| **Evaluation and verification** | [Terminal State Fixtures](https://github.com/HarperZ9/terminal-state-fixtures), [Crucible](https://github.com/HarperZ9/crucible), [Emet](https://github.com/HarperZ9/emet), [Bounds](https://harperz9.github.io/bounds.html) |
| **Security and privacy** | Shipped public work: [Phantom](https://github.com/HarperZ9/phantom). Controlled-private systems with public capability descriptions: [Array](https://harperz9.github.io/array.html), [Seed](https://harperz9.github.io/seed.html), [Sofer](https://harperz9.github.io/sofer.html), [Isomorph](https://harperz9.github.io/isomorph.html), [Bounds](https://harperz9.github.io/bounds.html), [ORCA and Gate](https://harperz9.github.io/private-practice.html) |
| **Developer infrastructure** | [BuildLang](https://github.com/HarperZ9/buildlang), [Index](https://github.com/HarperZ9/index), [Gather](https://github.com/HarperZ9/gather), [Chorus](https://github.com/HarperZ9/chorus) |
| **Graphics and runtime systems** | [RAW](https://github.com/HarperZ9/RAW), [SkyrimBridge](https://github.com/HarperZ9/SkyrimBridge), [Studio Engine](https://github.com/HarperZ9/studio-engine), [Truth ENB](https://harperz9.github.io/truth-enb.html), [Elder ENB](https://harperz9.github.io/elder-enb.html) |
| **Preservation and retro systems** | [Retro Engine](https://harperz9.github.io/retro.html), [Engine Revival](https://github.com/HarperZ9/engine-revival), [BRender Archival](https://github.com/HarperZ9/brender-archival) |
| **Research and education** | [Learn](https://github.com/HarperZ9/learn), [research records](https://harperz9.github.io/research.html), [publications](https://harperz9.github.io/publications.html), and [measured analytics](https://harperz9.github.io/analytics/current-cross-harness-pilot.html) |

### Phantom's boundary

[Phantom v1.1.0](https://github.com/HarperZ9/phantom/releases/tag/v1.1.0)
ships reversible hardware-identity privacy controls for Windows and Linux. It
covers **Layer 2 identity surfaces**. Kernel and firmware layers are modeled but
not shipped end to end. Use is limited to machines the operator owns or is
expressly authorized to test.

### Operational security systems

[Phantom](https://github.com/HarperZ9/phantom) is shipped public work. Array,
Seed, Sofer, Isomorph, Bounds, ORCA, and Gate are controlled-private systems
with public capability descriptions. They are not public releases or downloads.

[The security catalog](https://harperz9.github.io/security.html) documents each
system separately. Phantom changes and restores hardware-identity surfaces.
Array coordinates approval-gated offensive campaigns. Seed runs assessment and
detection-engineering modules. Sofer coordinates agents, models, probes, and
multi-stage workflows. Isomorph tests AI classifier and refusal behavior at
authorized inference boundaries. Bounds checks actions, observations, and
releases. ORCA manages private findings and reports; Gate makes fail-closed
integration and release decisions. Public pages describe each system's job,
evidence, maturity, and limits. Targets, credentials, live payloads, client
data, and engagement-specific findings stay in approved private or embargoed
channels.

## Retro Systems Lab

The lab follows **play → preserve → verify** while keeping each proof boundary
clear:

- [Retro Engine](https://harperz9.github.io/retro.html) is the interactive
  browser studio for owned pixel, palette, shader, and CRT experiments.
- [Engine Revival v0.1.0](https://github.com/HarperZ9/engine-revival/releases/tag/v0.1.0)
  is the public preservation and restoration-evidence spine.
- [BRender Archival v0.1.1](https://github.com/HarperZ9/brender-archival/releases/tag/v0.1.1)
  carries the specific BRender restoration record. Generic retro visuals are
  not presented as BRender evidence.

## How I work

Map the real state, build the missing surface, verify it, and leave an artifact
another person can inspect and maintain.

For a role-specific view, use the [hiring page](https://harperz9.github.io/hire.html).
For the deeper record, use the [portfolio](https://harperz9.github.io/portfolio.html)
or [public capability atlas](https://harperz9.github.io/catalog.html).

## Work with me

Available for paid work: full-time, contract, project, onsite, hybrid, or remote.
Based in Seattle, Washington.

| Path | Where I fit | Start here |
| --- | --- | --- |
| **Technical and evaluation** | Agent and model evaluation, developer infrastructure, systems integration, CI, security testing, technical support, and documentation. | [Engineering path](https://harperz9.github.io/hire.html#engineering-path) |
| **Public, union, and field** | Public service, ports, facilities, parks and grounds, arboriculture, client operations, scheduling, safety judgment, and physical work. | [Public-service and field path](https://harperz9.github.io/hire.html#public-service-field-path) |
| **Education and research** | Fellowships, labs, research operations, mentorship, continued learning, open-source work, and evidence-centered technical writing. | [Research and education](https://harperz9.github.io/research.html) |

[Hire / work](https://harperz9.github.io/hire.html) ·
[Resume](https://harperz9.github.io/resume.html) ·
[CV](https://harperz9.github.io/cv.html) ·
[Security boundary](https://harperz9.github.io/security.html) ·
[Retro Systems Lab](https://harperz9.github.io/retro.html) ·
[LinkedIn](https://www.linkedin.com/in/zaindanaharper/) ·
[Email](mailto:zaindharper@gmail.com)
