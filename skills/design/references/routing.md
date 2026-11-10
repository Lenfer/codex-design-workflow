# Routing

Resolve a source with `python3 <skill-dir>/scripts/library.py resolve <id>`.
Every resolution verifies integrity and prints exact original entrypoints. Read
the selected original completely before following its relevant references.
The originals live outside Codex's automatic skill-discovery directories, so this
router can choose deliberately without activating overlapping skills together.

| ID | Source | Route here for |
| --- | --- | --- |
| frontend | Anthropic Frontend Design | A new visual direction, distinctive composition and intentional interface design; default concept lead |
| taste | Leonxlnx Taste | A deliberately chosen corporate/product website workflow; first check its strong layout and content constraints |
| uiux | UI/UX Pro Max | A specific UX question, stack guidance or alternatives; validate relevance to the product |
| impeccable | Impeccable | Diagnosis, critique, refinement, adaptation, polish and hardening of existing UI; read the relevant playbook and craft floor |
| emil | Emil Kowalski's skills | Motion, interactions, native/mobile design and the related focused tasks below |
| design-md | Google Labs DESIGN.md | Design-system document format and rationale; a specification, not a visual style |
| awesome | VoltAgent Awesome Design MD | Optional design references; a collection, not an executable skill or the user's brand |

For a new landing page choose frontend, or taste when appropriate. For an existing
screen use its current system with the relevant Impeccable playbook. Penpot system
work follows the native API and the approved direction. Do not let every assistant
choose a new palette or redefine the brief.

## Emil family: choose the actual task

| Original skill | Task |
| --- | --- |
| animate | Implement web animation |
| animate-expo | Implement React Native / Expo animation |
| animation-performance | Investigate reproduced animation jank and performance problems |
| animation-vocabulary | Describe and communicate animation precisely |
| apple-design | Apple-platform interface design |
| ask-sonner | Sonner-specific guidance |
| break-ui | Exercise relevant edge cases and stressful UI content |
| choreograph | Coordinate motion sequences and relationships |
| emil-design-eng | General interaction and design engineering decisions |
| find-animation-opportunities | Identify purposeful motion when that exploration is requested |
| improve-animations | Improve existing motion |
| mobile-native | Native mobile interaction and interface work |
| pick-ui-library | Choose a UI library when explicitly requested |
| prototype | Produce a prototype when explicitly requested |
| remove-animations | Remove unnecessary motion in the requested scope |
| review-animations | Review motion when explicitly requested |
| write-swift | Swift implementation tasks |

Preserve original explicit-only metadata and read current instructions. Installing
the family does not install or authorize Swift, Expo, Sonner or a UI library.

## Local helpers

UI/UX Pro Max's Python search uses the standard library. After resolving `uiux`,
run its original `scripts/search.py --help`, then use a focused query. A search
result is guidance, not user research. Taste runtime helpers may need Node 22+;
they are optional. Google DESIGN.md's npm validator is optional and is not bundled.
Impeccable is provided as instructions/playbooks with direct-context fallback;
its binary engine and rendered detector are not installed by this bundle.
