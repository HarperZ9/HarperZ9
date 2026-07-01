# Enterprise GitHub Profile Research and Telemetry Receipt

<!-- markdownlint-disable MD013 -->

Date: 2026-07-01

Purpose: rebuild the `HarperZ9` GitHub profile as an enterprise-grade flagship
surface, using public market data, GitHub profile constraints, developer-forum
signals, repository telemetry, and `index` workspace scope.

## Scope

This receipt covers the actual GitHub profile repository:
`HarperZ9/HarperZ9`. It does not redesign the portfolio site. The profile is a
GitHub Markdown surface, so interactivity is limited to GitHub-supported
elements such as links, tables, collapsible `<details>` sections, and Mermaid
diagrams.

## External Research

- **GitHub profile mechanics (high):** GitHub displays a profile README when
  the repository name matches the username, the repo is public, the root has a
  non-empty `README.md`, and the account is not a managed user account.
  Source: <https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme>
- **GitHub diagram support (high):** GitHub renders Mermaid diagrams from
  fenced Markdown blocks using the `mermaid` language identifier; supported
  examples include flowcharts and pie charts. Source:
  <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams>
- **GitHub accessibility guidance (high):** GitHub's accessibility guidance for
  profile READMEs emphasizes descriptive link text, image alt text, heading
  hierarchy, plain language, and careful emoji use. Source:
  <https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/>
- **GitHub Octoverse 2025 market context (high):** GitHub reported more than
  230 new repositories per minute, 43.2 million pull requests merged per month
  on average, nearly 1 billion commits in 2025, and more than 1.1 million
  public repositories using an LLM SDK. Source:
  <https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/>
- **Stack Overflow 2025 AI usage context (high):** 84% of survey respondents
  were using or planning to use AI tools in development, and 51% of
  professional developers used AI tools daily. Positive sentiment toward AI
  tools dropped to 60%, which supports positioning around judgment and
  verification rather than AI enthusiasm alone. Source:
  <https://survey.stackoverflow.co/2025/ai>
- **Stack Overflow 2025 model context (high):** OpenAI GPT models led reported
  LLM use for development work; the survey also reported substantial Claude
  Sonnet usage among professional developers. Source:
  <https://survey.stackoverflow.co/2025/technology>
- **LinkedIn 2026 SWE labor note (moderate):** LinkedIn's Economic Graph report
  describes a software-engineering labor market transformed by AI, with AI
  roles expanding in SWE-adjacent hiring and entry pathways tightening. Source:
  <https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/us-software-engineer-talent-landscape-2026.pdf>
- **Dice 2026 tech jobs report (moderate):** Dice reported U.S. tech postings
  up 23% year over year in May 2026 and AI skill requirements in 73% of U.S.
  tech job postings. Source:
  <https://www.dice.com/hiring/recruitment/reports/dice-tech-job-report>
- **Developer-forum signal (moderate):** Hacker News hiring-manager comments
  repeatedly value clear READMEs, passion, real problem-solving, collaboration
  behavior, issue/PR quality, and communication over ornamental profile polish.
  Sources:
  <https://news.ycombinator.com/item?id=19413348>,
  <https://news.ycombinator.com/item?id=16224401>,
  <https://news.ycombinator.com/item?id=14530134>
- **Profile-template/forum signal (moderate):** Reddit and curated template
  collections show a saturated toolkit of stats cards, visitor counters,
  typing SVGs, badge walls, Actions-driven profile blocks, and skill icon
  grids. These can be clever, but they are not the right primary signal for
  this profile. Sources:
  <https://www.reddit.com/r/github/comments/uulygm/what_are_some_really_nice_github_profile_readmes/>,
  <https://github.com/durgeshsamariya/awesome-github-profile-readme-templates>

## GitHub Telemetry

Collected with `gh` on 2026-07-01. GitHub traffic endpoints cover a recent
rolling window, not all-time traffic.

- **Public account surface (high):** `gh api users/HarperZ9` returned 69 public
  repositories, `hireable: true`, location Seattle, WA, and public bio language
  centered on AI accountability, Project Telos, Rust, Python, and C++23.
- **Profile repo views (high):** `gh api repos/HarperZ9/HarperZ9/traffic/views`
  returned 3 views and 2 unique viewers in the available traffic window.
- **Profile repo clones (high):** `gh api repos/HarperZ9/HarperZ9/traffic/clones`
  returned 208 clones and 85 unique cloners in the available traffic window.
  This is not a hiring-read metric; it is a repository interaction signal.
- **Profile popular path (high):** `gh api repos/HarperZ9/HarperZ9/traffic/popular/paths`
  returned `/HarperZ9/HarperZ9` with 3 views and 2 uniques.
- **Flagship repo views (high):** recent traffic returned `telos` at 48 views /
  33 uniques, `index` at 34 views / 19 uniques, and `gather` at 18 views / 10
  uniques.
- **Public repo inventory (high):** `gh repo list HarperZ9 --limit 100 --json`
  confirmed active public flagships across Telos, index, gather, forum,
  crucible, emet, buildlang, learn, proof-surface, the Build ecosystem, color,
  calibration, graphics/native systems, provenance, release scanning, and agent
  workflow tooling.

## Index Telemetry

Collected with `index_map` and `index_context` over `C:\dev\public` on
2026-07-01.

- **Workspace scale (high):** `index_map` found 65 repositories: 61 public and
  4 local.
- **Profile role (high):** `index_focus` for `profile` classified the profile
  repo as a leaf with no dependency neighborhood. The profile is a front door,
  not the structural center.
- **Structural hubs (moderate):** `index_context` identified `build-ui` and
  `proof-surface` as hubs. The public ecosystem is not one evidence repo; UI
  surfaces and proof contracts both carry the architecture.
- **Scope correction (high):** the public workspace spans accountability,
  source intake, agent routing, compilers, color, graphics/native systems,
  research operations, workflow harnesses, finance/oracle work, and site/profile
  surfaces.

## Strategic Reading

- AI skill alone is no longer enough. The profile should sell judgment around
  AI work: verification, boundaries, source handling, routing, and product
  taste.
- The first screen has to be a decision surface for a busy reader: identity,
  thesis, fit, and first inspection links.
- The strongest profile pattern is not maximal decoration. It is a guided
  inspection route that makes the work easy to evaluate.
- The personal voice should stay visible. The profile is stronger when rigor is
  framed as a response to fallibility and ambition, not as sterile posturing.
- GitHub-native interaction should be used where it helps scan: details panels,
  Mermaid maps, and route charts. Live dashboards belong on the site.

## Decisions Applied

- Rebuilt the README around a market-aware opening: AI fluency is becoming
  table stakes; the differentiated lane is systems judgment and verifiable
  toolmaking.
- Kept the canonical Project Telos flagship artwork instead of adding a new
  badge-heavy or animated profile hero.
- Moved hiring signal, role fit, and inspection routes above the long ecosystem
  catalog.
- Added an adversarial-tester route to make the profile feel more alive and to
  reinforce the dogfood/testing posture.
- Kept the eight flagship engines visible while adding `proof-surface` as the
  contract floor in maps and engineer routes.
- Kept human voice in the opening and `The human part` section: artistic,
  restless, fallible, mistake-making, and still serious about checks.
- Recorded telemetry here rather than using low recent profile traffic as
  in-profile social proof.

## Reapproach Note

The first enterprise-profile rewrite was rejected as too close to corporate
positioning. The profile direction was then reapproached as a public lab bench:
reader doors, instruments, maps, open traps, and a more visible human voice.
The market and telemetry research still inform the routing, but the README no
longer leads with a market-report frame. Hiring signal is carried through
inspectable work instead of resume-page posture.

## Residual Limits

- GitHub traffic data is recent-window telemetry only. It should inform routing,
  not be treated as market validation.
- Developer-forum evidence is qualitative and historically mixed. It supports
  clear inspection paths, but it cannot prove what a specific hiring manager
  will value.
- Market reports are current as of 2026-07-01 but may change. The profile should
  not depend on exact market percentages in its reader-facing copy.
