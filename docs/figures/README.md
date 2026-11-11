# README diagrams

The process diagram follows the artifacts you carry between tools. The routing
diagram maps a task to its specialist. The setup diagram separates files on disk
from the apps you connect through MCP.

| Diagram | HTML source | README image |
| --- | --- | --- |
| Concept, system, code and checks | [workflow.html](workflow.html) | [workflow.svg](../images/workflow.svg) |
| Task-to-skill routing | [routing.html](routing.html) | [routing.svg](../images/routing.svg) |
| Installed files and app connections | [setup.html](setup.html) | [setup.svg](../images/setup.svg) |
| Penpot system and Review lifecycle | [penpot.html](penpot.html) | [penpot.svg](../images/penpot.svg) |

These are schematic illustrations, not screenshots of the apps. They use the
project's Corporate palette, English labels, accessible titles and descriptions.
System fonts keep them usable offline: Arial/Helvetica for labels, Georgia for
titles and a system monospace face for code. The figures make no font requests;
type metrics can vary by platform.

The Penpot figure shows how reusable parts support current screens and how an
operator decision resolves a proposal. The accompanying README section covers
partial acceptance, rejection, navigation and persistence checks. Detailed rules
live in [system and asset management](../../skills/design/references/system.md).

Run `python3 -B scripts/build_figures.py` from the repository root to regenerate
the HTML. Export the SVGs with Diagram Design's `export_svg.py --system-fonts`
helper. Diagram Design is a separate authoring tool for these illustrations; the
Design workflow installer does not install it.

The Google DESIGN.md and Awesome Design MD entries are reference resources.
See the skill's routing and compatibility documents for the full instructions.
