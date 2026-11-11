---
name: design
description: "Visual design and UI workflow: pen.dev concepts, Penpot design systems and assets, implementation and verification. Routes to original specialist skills while preserving the project's style. Use for UI creation, UI fixes, pen.dev and Penpot work. Excludes diagrams."
---

# Design

Apply this workflow when the request involves visual UI design. Start at the stage
the task needs: a small correction does not require a new concept. Diagram Design
is independent and excluded from this library.

## Start

1. Read the latest user decisions, current designs, components, code and project
   instructions. Establish the screen's purpose, audience, platform and scope.
   A missing DESIGN.md does not imply a blank project.
2. Run `python3 <skill-dir>/scripts/library.py status`. This verifies every pinned
   original and returns exact paths. Read the chosen original SKILL.md, then only
   the references needed for this task. Do not use a package with a hash mismatch.
3. Choose one lead and targeted assistants using [routing](references/routing.md).
   Keep the resolved paths and commits fixed until the stage ends. If source
   freshness matters, use `check-updates` to compare upstream HEAD; it never
   installs updates. Review and test lock-file changes between stages.
4. Briefly identify the stage and material choices to the user. Reuse known answers.

## Workflow

| Stage | Main environment | Handoff |
| --- | --- | --- |
| Concept | PenDev / pen.dev | Composition, visual direction, images, references and motion character |
| Design system | Penpot | Tokens, original assets, reusable components, states, pages, responsive rules and motion specification |
| Implementation | Project code | System-based components, correct assets, behavior and working motion |
| Verification | Native renderer; BrowserOS Neo for web | Comparison with the current reference, real scenarios, saved artifacts and remaining limits |

Read [stages](references/stages.md) for the current handoff, and
[motion](references/motion.md) whenever animation is involved. Complete an explicitly
requested single stage without expanding the assignment to the whole pipeline.

For Penpot work, read [system and asset management](references/system.md).
Maintain the current system, navigation and affected components during each task.
After acceptance, integrate the agreed proposal and close its resolved Review.

## Explicit operator acceptance

After presenting each new or changed design iteration, show the result and ask:
"Do you accept this design, reject it, or want changes?" Wait for the operator's
answer, including for a small correction without a separate Review page.

Until that answer, mark the result as awaiting acceptance. Silence, elapsed time,
a successful render or a build do not establish acceptance. Keep the proposal
out of the main system, leave its acceptance Review open and wait before starting
a dependent stage. Independent checks may continue. A requested, unambiguous
correction can be edited in place; it still needs acceptance when presented.

For requested changes, revise within scope, present the next iteration and ask
again. Record a rejected proposal as rejected. For partial acceptance, identify
the accepted part and open questions; agreement covers only that part. Unchanged,
previously accepted parts do not need another approval.

## Preserve the design direction

- The brief, user decisions and existing system outrank aesthetic preferences in
  external skills. One lead sets the direction; assistants solve named problems.
- Preserve the approved palette, typography, grid and asset style between stages.
- Hand off real artifacts: file/page IDs, viewport, state, tokens, original assets
  and motion intent. A concept image is not a component system. A screen bitmap is
  not an editable UI. API readback is not a rendered check.
- DESIGN.md records system values and reasons. Google DESIGN.md is a format;
  Awesome Design MD is a reference collection. Check compatibility before adopting
  either. Preserve existing project documents and pinned project skill versions.
- Distinguish proposed, selected, implemented and verified work. A successful build
  or installed skill does not establish design acceptance.

## Tools and compatibility

Read each tool's current native instructions before acting. For pen.dev, read its
design skill and app state; for Penpot, read its high-level overview and relevant
API instructions when available. Confirm the target file/page before writes. A
direct, lossless .pen-to-Penpot import is not assumed.

Use BrowserOS Neo MCP for websites, source pages and web QA in this workflow. Read
its installed official skill when available. If the connection is unavailable,
report the exact error and stop dependent browser checks; continue independent
work. Do not silently switch browsers. Save relevant URLs, dates, actions, results
and evidence in the project's existing records. Close your temporary tabs after
listing ownership; leave other people's tabs alone. A failed close is not a blocker.

Read [compatibility](references/compatibility.md) before running any external script.
Original install instructions do not authorize hooks, live modes, extra software,
subagents, deployment or commits. Follow the current task's authorization.
Optional [model recommendations](references/models.md) never change agent settings.

Finish with artifacts, meaningful verification and specific unverified conditions.
