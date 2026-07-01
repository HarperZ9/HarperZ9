# GitHub Profile Site-Aligned Design

## Goal

Align the `HarperZ9` GitHub profile with the live Project Telos site and the
canonical flagship artwork while keeping the README useful as plain GitHub
Markdown. The profile must frame Telos as a cross-domain research lab and
product ecosystem, with evidence/accountability as the method rather than the
whole mission.

## Research Takeaways

- GitHub profile guidance rewards immediate clarity: who the person is, what
  they build, and which projects are worth inspecting.
- Hiring managers need a faster first screen than researchers: role signal,
  strongest artifacts, and inspection path must appear before deep theory.
- Common template patterns such as badge walls, typing SVGs, stats cards, and
  visitor counters are visually loud but weak as proof surfaces.
- Reddit and developer-forum examples reward novelty, but the durable lesson is
  clarity: the visitor should understand the person, best projects, and first
  inspection path before noticing any dynamic trick.
- Accessibility guidance favors descriptive alt text, meaningful links, logical
  heading order, and plain language.
- The Project Telos site already has the right design language: clean editorial
  structure, restrained typography, the iris accent, and a repeatable flagship
  card.
- The canonical brand file retires bespoke heroes and says repo heroes should
  use the flagship card system.
- `index map` and `index router` over the public workspace show a broad repo
  set, with `build-ui` and `proof-surface` as structural hubs and docs spanning
  compilers, rendering, color, AI4Science, agent systems, and research packets.
- Publication must include the actual GitHub profile page. If GitHub does not
  auto-render the special README, use `Share to Profile` from the repo page.
- GitHub-native interaction is limited to Markdown/HTML affordances that GitHub
  renders: tables, `<details>`, links, images, and Mermaid diagrams. Full
  JavaScript maps belong on the site and should be linked from the profile.

## Direction

Use the Telos flagship card as the only visual anchor. Write the profile as a
GitHub-native route map from identity to research-lab scope, site, engines,
domain lanes, tester threads, and developer verification. Add interaction only
where it improves reader routing: hiring-manager fast path, collapsible reader
paths, Mermaid ecosystem map, direct live-surface links, and a clearly labeled
non-traffic route chart.

## Voice

- Clean, professional, and direct.
- Ambitious about the system, precise about what readers can inspect.
- Personality shows through working style: self-taught, proof-first, skeptical
  of unverifiable claims, and willing to build across domains.
- Avoid reducing the work to evidence/accountability alone.

## Content Architecture

1. Flagship card hero and the main site thesis.
2. Zain Dana Harper identity, hiring signal, and Project Telos positioning.
3. Site, flagship, and career links.
4. Hiring-manager fast path and collapsible reader paths.
5. Mermaid ecosystem map, live-surface links, and route chart.
6. Eight-engine flagship rows mirroring the site architecture.
7. Domain lanes drawn from the indexed public docs and Telos dogfood packets.
8. Public-safe private-line note routed through the main site.
9. Range and working-style section.
10. Tester threads and local verifier commands.

## Constraints

- Keep all links public and avoid private-repo GitHub URLs.
- Use the canonical `docs/brand/profile-hero.png` card asset.
- Do not introduce bespoke visual systems.
- Avoid dynamic external badge services and visitor counters.
- Use Mermaid and `<details>` only when the same meaning remains available as
  plain text.
- Do not publish secrets, private repo details, protected corpus material, or
  local-only paths.
- Keep the README readable when rendered as plain Markdown.
