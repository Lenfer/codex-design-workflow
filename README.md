# Codex Design Workflow

A portable design workflow for Codex: **pen.dev → Penpot → code → verification**.

One Design skill routes each task to the relevant original specialist, keeps the
project's visual direction consistent and carries motion through every stage.

![Design routes the brief through pen.dev, Penpot, project code and BrowserOS Neo verification.](docs/images/workflow.svg)

## How the workflow works

Start with the brief and the current project. Design selects a lead skill for the
task, then adds specialists only where they help. A new interface begins with its
concept; an existing screen can start with a focused system or code correction.
Motion moves through concept, specification, implementation and real playback.

1. **pen.dev:** establish the composition and visual direction; create concepts,
   icons, source assets and complex procedural-motion prototypes.
2. **Penpot:** turn the direction into tokens, editable components, states,
   responsive screens and a motion specification.
3. **Code:** implement that system in the project's existing stack using the actual
   assets and components.
4. **Verify:** compare real rendering and exercise user scenarios. Return a
   discrepancy to the relevant stage while keeping the approved style.

Suggested model placement is shown above. Astra Medium is the owner's selected
route for icons and complex pen.dev animation; the other placements are
recommendations. See [model details](skills/design/references/models.md).

## Give this to Codex

Copy [the installation prompt](prompts/INSTALL.md), or paste:

> Set up https://github.com/Lenfer/codex-design-workflow using its prompts/INSTALL.md.
> Read the task and plan first, inspect the installer, then install the Design
> workflow and all pinned sources. Configure my own BrowserOS Neo connection and
> verify it. I will install pen.dev and Penpot myself. Preserve my existing skills
> and Codex settings, and report any remaining manual setup.

## What you get

- An English Design router with concept, system, implementation and verification
  handoffs; targeted skill selection; motion guidance and compatibility rules.
- Seven pinned upstream skill/resource families, including all 17 Emil skills.
- A standard-library Python installer with content verification and preserved licenses.
- BrowserOS Neo setup instructions, pen.dev/Penpot handoff guidance and optional
  model recommendations. Diagram Design is separate and excluded.

The external originals are downloaded into a library outside skill auto-discovery.
The visible `design` skill loads the relevant original when needed. This keeps
overlapping design instructions from competing. Google DESIGN.md and Awesome Design
MD are resources rather than executable skills.

## Install

V1 supports macOS and Linux with **Python 3.9+ and Git**. Windows users can inspect
the package, but native Windows/WSL app connections have not been validated.
Codex must already be installed and signed in. The installer has no pip/npm dependencies.

```bash
git clone https://github.com/Lenfer/codex-design-workflow.git
cd codex-design-workflow
python3 -B install.py plan --target /absolute/path/to/your-project
python3 -B install.py install --target /absolute/path/to/your-project
python3 -B install.py doctor --target /absolute/path/to/your-project
```

For personal installation across projects, use `--user` instead of `--target` on
each command. Project scope is recommended for a first trial.

The installer writes only:

```text
<target>/.agents/skills/design/        # discoverable router and helpers
<target>/.design-workflow/library/     # pinned, unmodified upstream files
```

It leaves existing `AGENTS.md`, MCP settings, model settings and credentials alone.
Different existing files cause a conflict; identical files are reusable. Repeating
the same install verifies and reuses the same versions. Keep local library content
out of your application's Git repository, for example with these project ignore rules:

```gitignore
.design-workflow/
.agents/skills/design/installation.json
```

Codex discovers project skills under `.agents/skills`; restart Codex if the new
skill does not appear. See [official Codex skills documentation](https://developers.openai.com/codex/skills).
Try: `Use $design to improve this screen while preserving its current visual style.`

## Apps and MCP

![Install the pinned skill library, connect the recipient's own tools, then verify both files and live access.](docs/images/setup.svg)

Follow [setup and live verification](docs/SETUP.md) after installing skills.

| Component | Setup |
| --- | --- |
| BrowserOS Neo | On macOS, the receiving agent can use the official Homebrew cask; launch, account sign-in and Codex pairing happen locally. Direct platform downloads are also available. |
| pen.dev | Install manually; connect its supported agent integration. |
| Penpot | Set up manually; connect the intended workspace and supported MCP integration. |
| Codex MCP | Use the recipient's own endpoints. The installer never imports the author's configuration. |

`doctor` verifies files. A configured MCP server still needs an actual tool call
before it is considered connected. Optional Node, ffmpeg, Swift/Expo, Impeccable's
engine and the Google DESIGN.md npm CLI are not bundled or required for installation.

## Routing and sources

![Design routes new direction to Frontend Design or Taste, UX questions to UI/UX Pro Max, refinement to Impeccable, motion to Emil, and system references to DESIGN.md resources.](docs/images/routing.svg)

| Source | Purpose | License |
| --- | --- | --- |
| [Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Distinctive visual direction and interface composition | Apache-2.0 |
| [Taste](https://github.com/Leonxlnx/taste-skill) | Selected corporate/product website workflow | MIT |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Focused UX and stack guidance/search | MIT |
| [Impeccable](https://github.com/pbakaus/impeccable) | Critique, refinement, adaptation and UI hardening | Apache-2.0 |
| [Emil Kowalski's skills](https://github.com/emilkowalski/skills) | Motion and interaction specialists; 17 original skills | MIT |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | Design-system specification format | Apache-2.0 |
| [Awesome Design MD](https://github.com/VoltAgent/awesome-design-md) | Optional design references | MIT |

See [full routing](skills/design/references/routing.md),
[stage handoffs](skills/design/references/stages.md),
[compatibility](skills/design/references/compatibility.md) and
[model recommendations](skills/design/references/models.md).
Exact commits, selected paths, licenses and tree hashes are in
[sources.lock.json](skills/design/sources.lock.json). Originals retain their own
terms; see [attribution](THIRD_PARTY.md).

## Verify and update

```bash
python3 -B /path/to/installed/design/scripts/library.py status
python3 -B /path/to/installed/design/scripts/library.py resolve emil
python3 -B /path/to/installed/design/scripts/library.py check-updates
python3 -B -m unittest discover -s tests -v
```

`check-updates` compares upstream HEAD without replacing files. Review source and
license changes, update pins and tree hashes, then test a clean target before
releasing a new bundle. Keep versions fixed during an active design stage.

There is no automatic overwrite/update command. Install an updated bundle into a
fresh project first. If replacing a personal install, retain a backup of the old
router and library and resolve the reported conflict deliberately.

Offline installs can use `--source-cache /path/to/releases`, with the same
`<id>/<commit>` layout and the same hash verification. A partial failed install can
be retried; existing verified releases are reused. If interrupted by process death,
inspect the reported lock and remove that lock only after confirming no installer
is running. Preserve any conflicting or modified source tree for investigation.

To uninstall, remove only this bundle's installed router and library after checking
for local edits. No Codex configuration changes need reverting.

The [task](docs/TASK.md) and [implementation plan](docs/IMPLEMENTATION_PLAN.md) describe
the package scope. First-party code and documentation use the [MIT License](LICENSE).

The README diagrams have [editable HTML sources](docs/figures/README.md).
See [validation and tested limits](docs/VALIDATION.md).
