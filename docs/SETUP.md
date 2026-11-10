# Apps, MCP and live checks

## Codex

Install and sign into Codex using the [official setup documentation](https://developers.openai.com/codex/quickstart).
The bundle installs skills into the supported [`.agents/skills` locations](https://developers.openai.com/codex/skills).
It does not install Codex itself or transfer another person's account.

For MCP, follow [official Codex MCP documentation](https://developers.openai.com/codex/mcp).
Servers may use HTTP URLs or local stdio commands. Use the app's current integration
instructions and the recipient's own values. For an HTTP integration, the CLI form is:

```bash
codex mcp add server-name --url YOUR_OWN_MCP_URL
```

This is a command template, not a ready endpoint. Avoid putting token-bearing URLs
in logs, screenshots or shared prompts. OAuth-enabled servers may require
`codex mcp login server-name`. App-specific pairing may be different. Preserve the
existing `~/.codex/config.toml`; do not replace it with the author's configuration.

## BrowserOS Neo

The [official repository](https://github.com/browseros-ai/BrowserOS) documents
macOS Homebrew installation:

```bash
brew tap browseros-ai/tap
brew install --cask browseros-neo
```

The receiving agent may run these when installing this requested environment if
Homebrew is already available. The Python skill installer does not run them.
For macOS, Windows and Linux x64, use the direct downloads linked by the same
official repository. Do not install a browser build from an unrelated mirror.

Launch Neo, complete any necessary local account setup, then select Codex on its
MCP connection board. Prefer that one-click connection. Otherwise use the current
Manual Setup instructions and the endpoint displayed by your own instance.
Do not guess a port or reuse the author's URL. Install/read the official Neo skill
offered by that integration when available.

If the tools do not appear, reconnect MCP or start a new Codex session. Verify by
listing tabs, opening a temporary public page, reading it and closing only that
task's tab. Record the URL, date, action and outcome locally. Keep profile contents,
cookies and sensitive raw logs out of Git.

The [Neo manual setup page](https://docs.browseros.com/neo/mcp/manual) is the
vendor's linked reference. During preparation on 2026-11-10 it returned an empty
page in Neo; the repository's installation and connection instructions were
readable. Consult the current in-app connection board if the documentation remains
unavailable. No endpoint or unattended pairing behavior is assumed by this package.

## pen.dev

Install from [pen.dev](https://www.pen.dev/) yourself, then follow its supported
Codex/agent integration. In the receiving session, confirm that its tools appear;
read the native design instructions and current app state before any writes.
The authoring environment uses a `pencil`-named MCP integration, but integration
names may differ. A tool namespace alone does not establish a live app connection.

## Penpot

Set up [Penpot](https://penpot.app/) yourself, using its hosted service or your own
deployment. See the [official Penpot repository](https://github.com/penpot/penpot).
Connect the supported integration for your instance and account. Confirm the
intended workspace/file with a read-only overview before writing. This bundle
does not install a Penpot server, invent a universal MCP endpoint or assume direct
lossless import from pen.dev.

## Setup report

Report each layer separately:

| Layer | Proof |
| --- | --- |
| Files installed | `install.py doctor` succeeds; all seven sources resolve |
| Skill discovered | Codex can load `design` in the intended project/session |
| MCP configured | The recipient's integration is listed in Codex |
| Neo connected | A real read-only browser task succeeds |
| pen.dev connected | Native instructions/state can be read from the correct app |
| Penpot connected | Overview/file state can be read from the intended instance |

Mark unavailable tools as pending. File installation does not establish live app
connectivity, and an author's successful setup does not verify a recipient's setup.
