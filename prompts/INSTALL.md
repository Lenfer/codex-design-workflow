# Installation prompt

Paste this into Codex in the project where you want to try the workflow. Codex
will inspect the installer, install the skills and guide you through app pairing.
You will set up Penpot yourself.

```text
Set up the Design workflow from https://github.com/Lenfer/codex-design-workflow.

Start with the task and plan, then implementation:
1. Read README.md, docs/TASK.md, docs/IMPLEMENTATION_PLAN.md, install.py and
   skills/design/sources.lock.json. Explain the install scope briefly.
2. Detect my OS, Python, Git and Codex setup. Default to the current project's
   scope. If no project is selected, ask for a project directory or personal scope.
   Reuse an existing checkout after checking its origin; do not overwrite it.
3. Run install.py plan, install and doctor with the selected target. Fetch every
   pinned original. Preserve existing skills and settings; report conflicts rather
   than overwrite them. Never replace my AGENTS.md, approvals or model configuration.
4. Set up BrowserOS Neo using docs/SETUP.md and current official instructions.
   On macOS with Homebrew available, install the official browseros-neo cask if
   missing. For other platforms use the official download instructions; do not
   invent an unattended installer. Ask me only for necessary app/account interaction.
   Connect Codex from Neo's MCP connection board using my own local setup. If Neo
   is not yet connected, request that pairing instead of using another browser.
   Read Neo's official skill when available. Never copy anyone's browser profile,
   credentials or MCP secrets.
5. I will set up Penpot myself. Show its official links and the
   remaining integration steps. If already connected, use read-only state calls to
   verify the correct workspace/file; do not alter open design files during setup.
6. Verify the installed Design skill and library resolution. Verify Neo with a
   real read-only browser action in your own temporary tab, then close that tab.
   Report filesystem installation, MCP configuration and live connectivity as
   separate results. Do not claim unavailable tools were tested. If a Codex restart
   is needed, say exactly what to verify in the next session.

Use the Design router for subsequent UI work: concept and system/assets in Penpot,
implementation and verification. Create vector assets as SVG; use ImageGen for
raster assets when available and preserve source files. Start at the stage my request needs.
Load only relevant upstream originals and preserve the project's approved style.
Diagram Design stays independent. Model choices are optional recommendations;
do not switch settings or start subagents without authorization.

Finish with installed paths, verified versions, live checks and concrete remaining
manual steps. Do not commit or publish anything as part of this installation.
```
