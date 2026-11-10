# Implementation plan

1. Audit the installed Design router, its upstream sources, exact versions, licenses and environment dependencies. Verify current official Codex and BrowserOS setup documentation.
2. Port the custom router to English. Keep the four-stage workflow, targeted routing, motion across stages, preservation of project style and explicit exclusions. Put compatibility constraints in our layer; preserve upstream files unchanged.
3. Build a Python standard-library installer for macOS/Linux. Install a project-local bundle by default, with optional user scope. Fetch exact Git commits, select the original package paths, verify expected content hashes and preserve licenses. Keep upstream files outside automatic skill discovery; expose the Design entry point.
4. Add an install prompt, README, routing catalog, model recommendations, MCP setup and attribution. Explain optional runtimes and manual app/account setup. Do not change a recipient's model, approvals, global instructions or existing configuration.
5. Test against a clean temporary target, repeat the install, verify all packages and prove conflict and tamper detection. Keep network and live-app verification separate from filesystem tests.
6. Prepare the exact initial commit scope for review. After commit authorization, create the public repository, publish the tested files and verify anonymous access and the install prompt link.

V1 uses pinned releases. Updates are deliberate manifest changes followed by tests; no upstream version changes during an active design stage. BrowserOS, pen.dev and Penpot setup is handled by the receiving agent using official setup instructions and the user's own local endpoints.
