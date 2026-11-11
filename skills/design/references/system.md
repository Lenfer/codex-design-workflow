# Penpot system and asset management

Confirm the intended file, page, libraries and task scope. Read the latest concept
and user decisions. Extend the existing system and preserve working IDs.

## Decompose the concept

- Tokens: semantic colors and themes, typography, spacing, dimensions, radii,
  borders and depth. Distinguish a real token binding from a stored numeric value.
- Assets: logos, icons, illustrations, photos, backgrounds, characters and scenes.
  Keep originals and derivatives, roles and states, dimensions, scaling rules,
  transparency, provenance and licenses. Raster artwork is valid; keep UI text,
  actions and components editable rather than flattening a screen into an image.
- Components: reusable masters and instances, meaningful variants and actual
  interaction states. Theme, Size and State are independent axes. A color variant
  does not cover hover or error behavior.
- Screens: shared shell, content, navigation, scenario-specific empty, loading,
  error and success states, long content and target viewports. Preserve shared
  grid anchors and geometry across light and dark themes.
- Motion: initial, intermediate and final states, trigger, direction, duration
  and easing or spring parameters, interruption and reduced-motion alternative.

Use native libraries and layouts where they serve the design. Check instance
restrictions before reparenting or removal; keep library connections intact when
one operation fails. Resolve the intended Penpot instance before writing.

Check screen renders, actual fonts and character coverage, overflow, baselines
and themes. API coordinates and font names do not prove correct rendering.
Read back or reopen after substantial changes to verify persistence. Native
archives may omit fonts; verify portability before claiming it.

## Maintain the system during each task

Before editing, find the current reference for the scenario, state, theme and
viewport. Keep one clear source for each supported combination; a responsive
design can cover several combinations. Preserve existing codes and IDs, and
clarify names that obstruct navigation. From the project entry point, link to
the system, screens, open proposals and archive. Reuse the existing index or
project map; four separate pages and a second registry are unnecessary.

Continue on the appropriate page and within the existing shell. Apply a requested
small correction with an unambiguous outcome to the main design. When a new
decision needs a choice, create a temporary Review with the current reference,
the decision question and affected screens or components. A board on the existing
page usually suffices for one alternative. A new edit does not require a new page.

After presenting each iteration, request and wait for explicit operator acceptance
under the [Design acceptance rule](../SKILL.md#explicit-operator-acceptance).
Keep an unresolved proposal open until the operator answers.

On acceptance, update the agreed part of the main system and its working links.
Prefer editing in place. An accepted board can also become the main reference at
its existing location and ID: update its role and mark the previous reference as
replaced. Check the route to the current source, close the resolved Review and
remove it from open proposals. Keep history accessible through an archive link
without presenting it as another current reference.

On rejection, retain the current reference, close the Review and record the
decision in the project's existing records. On partial acceptance, integrate the
accepted part, close the resolved and rejected parts, and leave only the specific
open question linked to the updated reference.

For shared changes, edit the existing master and meaningful variants. Check
affected themes, states and representative consuming screens. Avoid copying the
same correction into individual instances. Before moving, merging or deleting,
check masters, instances, nested objects, prototype links and known direct links.
Closing a Review does not require deleting its objects. An unknown dependency
blocks that physical operation: preserve the material and name the remaining
check. Matching names, or a name such as Empty or Preview, do not establish that
an object is disposable.

Before finishing, check navigation from the project entry point to the changed
reference, persistence and rendering of affected states. Cover the edit and its
dependencies; a full-file audit is unnecessary for each task. Report design
acceptance, implementation and execution checks separately. If an accepted change
has not reached the main system or navigation, name the remaining operation;
the design handoff is incomplete. A concept-only assignment ends at that stage.

Organize pages by stable product areas and boards by screens and states. Consider
a separate file when an area has an independent work cycle, and identify the
source of shared components. Screen count alone does not require a file split.

## Example: camera menu

A Review proposes a new camera-switch position and a new menu label. The operator
accepts the position and leaves the label open. Update the current menu master;
check open and closed states in light and dark themes and instances on capture
and preview screens. Close the resolved Review part. Leave the label question
linked to the current menu, with accepted and rejected material in history.
Report code implementation and checks according to their actual status. Reflect
later agreed code refinements in the main design as well.

## Handoff to code

Provide current component and screen links/IDs, reference viewport and state,
tokens, source assets and retrieval rules, responsive behavior, motion specification
and known exceptions. Use the project's existing documents and memory. DESIGN.md
can serve as a concise map of the system.
