# GitHub Profile Template Research Receipt

## Scope

This receipt records the public research used to shape the `HarperZ9` GitHub
profile README. The target is the personal GitHub profile page rendered from
`HarperZ9/HarperZ9`, not the portfolio site.

## Sources Reviewed

- GitHub Docs, profile README requirements:
  <https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme>
- GitHub Blog, accessible profile guidance:
  <https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/>
- GitHub Community accessibility discussion:
  <https://github.com/orgs/community/discussions/64778>
- Reddit `r/github`, profile README examples and community reactions:
  <https://www.reddit.com/r/github/comments/uulygm/what_are_some_really_nice_github_profile_readmes/>
- DEV Community, standout profile README examples:
  <https://dev.to/github/10-standout-github-profile-readmes-h2o>
- DEV Community, profile README publication traps:
  <https://dev.to/uya0526design/i-built-a-github-profile-readme-the-it-wont-show-up-traps-and-tips-to-stand-out-4pba>
- `awesome-github-profile-readme`, curated examples and add-ons:
  <https://github.com/abhisheknaiidu/awesome-github-profile-readme>
- `awesome-github-profile-readme-templates`, curated template collection:
  <https://github.com/durgeshsamariya/awesome-github-profile-readme-templates>
- GitHub topics, `github-profile-readme` collections:
  <https://github.com/topics/github-profile-readme>
- Live Project Telos site and brand system:
  <https://harperz9.github.io>

## Pattern Findings

- The common standout toolkit is now predictable: visitor counters, typing SVGs,
  GitHub stats cards, trophy cards, animated badges, skill icon walls, and
  GitHub Actions-driven dynamic blocks.
- Reddit and developer examples show those dynamic patterns can be technically
  clever, but they often compete with the first job of the profile: making the
  person, work, and best inspection path obvious.
- GitHub's own profile README requirements are mechanical: exact username repo,
  public visibility, root `README.md`, and non-empty content. Older special
  repositories may still require pressing `Share to Profile`.
- Accessibility guidance consistently favors descriptive image alt text,
  meaningful links, plain language, and logical headings over decorative visual
  density.
- Template collections are useful for inventory, but the strongest direction
  for this profile comes from the existing Project Telos brand: a canonical
  flagship card, restrained copy, one iris-accent visual system, and proof-first
  language.

## Decisions Applied

- Use one canonical flagship card image instead of a bespoke profile diagram.
- Avoid badge walls, typing SVGs, stats cards, visitor counters, and dynamic
  GitHub Actions widgets.
- Lead with identity, thesis, and public inspection paths.
- Show projects as mobile-readable flagship rows, not a wide table.
- Include skills through concrete domains: AI accountability, systems and
  compilers, graphics/reverse engineering, color/calibration, and public
  product shipping.
- Keep tester threads and local verifier commands visible.
- Preserve plain Markdown readability when images do not load.
- Add a verifier guard against stale private/public-boundary links.

## Publication Note

The repository satisfied GitHub's documented special-repository requirements,
but the actual profile page did not render the README until GitHub's
`Share to Profile` control was used from the repository page. The live profile
page was then checked in-browser for the Project Telos title, hero image,
thesis, eight-engine section, range section, and tester threads.
