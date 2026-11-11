# Third-party sources

This repository contains the custom router, installer and documentation. The
installer downloads selected original files directly from upstream Git repositories
at the exact commits in [sources.lock.json](skills/design/sources.lock.json).
It verifies their content hashes and preserves all selected license files.

| Owner / project | Original repository | License file in downloaded package |
| --- | --- | --- |
| Anthropic / Frontend Design | https://github.com/anthropics/skills | `skills/frontend-design/LICENSE.txt` — Apache-2.0 |
| Leonxlnx / Taste | https://github.com/Leonxlnx/taste-skill | `LICENSE` — MIT |
| Next Level Builder / UI/UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | `LICENSE` — MIT |
| Paul Bakaus / Impeccable | https://github.com/pbakaus/impeccable | `LICENSE` — Apache-2.0 |
| Emil Kowalski / skills | https://github.com/emilkowalski/skills | `LICENSE` — MIT |
| Google Labs / DESIGN.md | https://github.com/google-labs-code/design.md | `LICENSE` — Apache-2.0 |
| VoltAgent / Awesome Design MD | https://github.com/VoltAgent/awesome-design-md | `LICENSE` — MIT |

The Emil lock uses the original `emilkowalski/skill.git` URL, which redirects to
`emilkowalski/skills`. The exact pinned content is verified either way.

The root MIT license applies to first-party files only. Upstream materials retain
their original terms and notices. References to brands, images and external
designs do not grant trademark or separate media rights. No upstream engine
binaries, browser profiles, credentials or personal Codex configuration are bundled.

BrowserOS Neo, Penpot, ImageGen and Codex are separate products or services. Their
names identify integrations; this project does not imply their endorsement.
