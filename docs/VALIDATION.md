# Validation

## Penpot-only workflow: 2026-11-11

Concepts and the design system now share Penpot. Vector assets use SVG; raster
assets can use ImageGen when available. The router, README, setup prompt, model
guidance and workflow/setup figures describe this path.

Checks on macOS:

- All eight installer tests passed.
- Clean installation and repeated installation from the existing source cache
  passed. `doctor` verified the router and all seven pinned sources. Installed
  router files matched this checkout byte for byte.
- Public text and private-path checks, local Markdown links, Python/JSON parsing,
  required skill frontmatter and `git diff --check` passed.
- Both changed HTML figures passed Diagram Design's offline self-check. Their
  exported SVGs were opened and visually checked through BrowserOS Neo: labels
  were readable and no overlapping or clipped content was observed.

The Skill Creator validator could not run in the default Python environment
because PyYAML is absent. Required frontmatter was checked separately. No live
Penpot design or image-generation task was executed for this documentation change.
These checks cover local preparation; Git history and the remote branch identify
the published revision.

## Penpot documentation update: 2026-11-11

The English router now includes explicit acceptance of each presented design
iteration and a dedicated Penpot reference covering tokens, source assets,
components, screens, motion, navigation and Review resolution. The README adds
an explanation and an offline SVG with its HTML source.

Checks on macOS:

- All eight installer tests passed.
- A clean temporary installation from the existing source cache, repeated
  installation and `doctor` passed for all seven pinned sources. The installed
  Penpot reference matched this checkout byte for byte.
- First-party text passed an English-only and private-path scan. Local Markdown
  file targets existed; Python and JSON files parsed. `git diff --check` passed.
- Diagram Design's self-check passed for `penpot.html`. BrowserOS Neo opened the
  exported `penpot.svg`; full-page visual inspection found no clipped labels or
  overlapping content. The SVG uses system fonts and requests no web fonts.

The Skill Creator validator still cannot run in the default Python environment:
`ModuleNotFoundError: No module named 'yaml'`. No dependency was installed for
this documentation update. The operator accepted the illustrated README and
authorized its commit and publication to `main` on 2026-11-11, with local
development continuing on `dev`. The checks above cover preparation; Git history
and the remote branch identify the published revision. No live Penpot file was
edited or tested during this work.

Preparation date: 2026-11-10. Executed on macOS; Linux support follows the portable
Python/Git implementation but has not been exercised on a separate Linux machine.

## Passed

- Downloaded all seven exact commits from public GitHub repositories using the
  production Git fetch/archive path. Selected trees matched all seven locked
  SHA-256 hashes, including entrypoints, license files and executable flags.
- Installed the final router and downloaded sources into a clean temporary target
  using the verified source cache. Repeated installation, then ran `doctor`.
- Resolved and verified all seven sources and 23 original entrypoints, including
  all 17 Emil skills.
- Eight automated tests: repeat installation/configuration preservation, existing
  router conflicts, bad source cache, modified installed originals, symlinked
  releases, preflight of all sources, unsafe paths/unpinned sources, concurrent lock.
- Checked first-party files for English-only text and machine-specific paths;
  parsed Python and JSON and checked local Markdown links.
- Checked the skill's required name and description. The Skill Creator validator
  could not run because its PyYAML dependency was absent in the local Python
  environments; no dependency was added to the recipient's installer.
- Generated three Corporate HTML diagrams and exported offline SVGs. Diagram
  Design's self-check passed for every source. BrowserOS Neo inspection of the
  local README and all three exported images found an export selector issue;
  SVG-qualified selectors fixed it, and the corrected images were rechecked.

The initial test run exposed rejection of macOS's system `/var` alias. The
installer now canonicalizes the selected target before checking for symlinks inside
its own installation paths; all eight tests passed after the correction.

## Live tools and publication

BrowserOS Neo was exercised during preparation: public source reading, GitHub
repository creation and readback. The empty public repository
`https://github.com/Lenfer/codex-design-workflow` was created without an automatic
README/license commit. The owner authorized the initial publication on 2026-11-10,
including illustrated documentation. Public content and the installation-prompt
link are verified after the initial push; the Git history identifies that release.

The recipient's Codex discovery, fresh BrowserOS installation/pairing and
Penpot connection have not been tested on another machine. Follow
[SETUP.md](SETUP.md) for the receiving environment's live checks. File hashes do
not establish those connections.

## Reproduce

```bash
python3 -B -m unittest discover -s tests -v
python3 -B install.py install --target /path/to/a/clean/project
python3 -B install.py install --target /path/to/a/clean/project
python3 -B install.py doctor --target /path/to/a/clean/project
python3 -B /path/to/a/clean/project/.agents/skills/design/scripts/library.py status
```
