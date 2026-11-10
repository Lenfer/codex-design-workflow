# Stage handoffs

## Concept: pen.dev

Start from the product scenario, real copy, brand materials, existing decisions and
constraints. For an ongoing project the direction is already selected. Offer a
proportionate number of directions only if a material choice remains unresolved.

Use Frontend Design as the default lead, or select Taste after checking its strong
layout constraints. UI/UX Pro Max can answer specific questions; Awesome Design MD
can supply references. Their suggestions must fit the product.

In pen.dev show composition and character at target sizes. Distinguish reference
images, photographs and concept renders from final UI assets. Keep provenance,
resolution and licenses for important resources. Do not invent product facts from
stock images or another company's website.

Define what motion communicates and how it responds to the user. Key states or a
small reproducible prototype may suffice; a static board does not prove animation.
For icons and complex procedural animation read pen.dev's current icons/Generate
and scripts-and-shaders instructions when those capabilities are available.

Hand off the chosen composition, size relationships, colors, typography, original
assets, target sizes/states, motion character, decisions and open questions.
Save an editable .pen or a confirmed managed draft, IDs and preview in the project's
artifact location. Confirm export/save before claiming a native file is ready.

## System and assets: Penpot

Confirm the current file, page, libraries and authorized scope. Use the latest
concept and user decisions. Reuse and extend an existing system.

- Tokens: semantic colors/themes, type scale, spacing, dimensions, radii, borders
  and depth. A stored numeric value does not prove a token binding.
- Assets: originals and derivatives, roles/states, sizing, scaling, transparency,
  provenance and license. Raster assets are valid; UI text and controls stay editable.
- Components: reusable parts, instances, actual states and variants. Theme, Size
  and State are separate axes; a color variant does not replace hover/error.
- Pages: shell, navigation, meaningful empty/loading/error/success states, long
  content and target sizes. Themes should preserve geometry and shared grid anchors.
- Motion: states, triggers, direction, timing/easing or spring, interruption and
  reduced-motion alternative.

Check instance restrictions before reparenting/removing; do not detach a whole
library to work around one operation. Resolve the correct Penpot instance before
writes. Check exported renders, actual fonts and character coverage, overflow,
baselines and themes. Verify persistence by readback/reopening after major changes.
A native archive may omit fonts; do not assume portability.

Hand off current screen/component IDs, viewport and state, tokens, source assets,
responsive rules, motion specification and exceptions. Use existing project records.

## Implementation

Use the latest system and user decisions with the existing stack. Map semantic
tokens and reusable components into code. Use original assets rather than similar
symbols or stretched screen captures. Include relevant safe areas, keyboard,
text scaling and platform conventions. Implement motion as specified, including
interruption, cancellation, repeated input and reduced motion.

## Verification

1. Run appropriate project checks. A build confirms compilation, not visual fidelity.
2. Compare actual rendering to the current reference with matching viewport, theme
   and data: geometry, typography, spacing, assets, states and responsive behavior.
3. Use BrowserOS Neo for web and the platform's native environment for native UI.
4. Exercise meaningful user actions; screenshots do not prove submission, animation
   playback or persistence. Scale checks to the change.
5. Fix observed problems, repeat affected checks and report unverified conditions.

Impeccable, break-ui and motion skills are targeted helpers. Separate agents are
unnecessary unless authorized. Pixel fidelity applies to named states and sizes;
font rasterization differences are not automatically grid drift. Do not turn a
comparison score into a percentage of project completion.
