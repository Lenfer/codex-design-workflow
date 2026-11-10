# README figures

The three figures use the workflow's previously selected Corporate style: pale
paper, navy ink and one indigo focal accent. They are original vector diagrams,
with English labels, accessible titles/descriptions and no external assets or
network font requests. Typography uses Arial/Helvetica and Georgia system stacks;
rendering can vary slightly by platform.

| Figure | Editable source | README image |
| --- | --- | --- |
| Process and model recommendations | [workflow.html](workflow.html) | [workflow.svg](../images/workflow.svg) |
| Task-to-skill routing | [routing.html](routing.html) | [routing.svg](../images/routing.svg) |
| Installation and live verification | [setup.html](setup.html) | [setup.svg](../images/setup.svg) |

Regenerate the HTML with `python3 -B scripts/build_figures.py` from the repository
root. The SVGs are exported from those sources with Diagram Design's
`export_svg.py --system-fonts` helper. Diagram Design was used to author the
documentation illustrations; it is independent of the installed Design workflow
and is not installed as one of its dependencies.

The diagrams summarize the workflow. Detailed routing and compatibility constraints
remain in the skill's reference documents. The Google DESIGN.md and Awesome Design
MD nodes describe resources, not additional executable tools.
