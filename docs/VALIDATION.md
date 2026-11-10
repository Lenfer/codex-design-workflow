# Validation

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

The recipient's Codex discovery, fresh BrowserOS installation/pairing, pen.dev and
Penpot connections have not been tested on another machine. Follow
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
