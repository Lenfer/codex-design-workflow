# Connect the apps to Codex

Install the Design skill first. Then connect the apps you plan to use and test a
read-only action in each. The skill installer manages files; each MCP connection
gives Codex access to an app on your computer or in your account.

## Codex

Install and sign into Codex using the [official setup documentation](https://developers.openai.com/codex/quickstart).
Codex reads the installed Design skill from the supported
[`.agents/skills` locations](https://developers.openai.com/codex/skills).

Follow the [Codex MCP documentation](https://developers.openai.com/codex/mcp) and
the app's integration instructions. A server may use an HTTP endpoint or a local
stdio command. For an HTTP integration, substitute the URL from your own app:

```bash
codex mcp add server-name --url YOUR_OWN_MCP_URL
```

OAuth integrations may also need `codex mcp login server-name`. Some apps handle
pairing through their own interface. Preserve your existing
`~/.codex/config.toml`, and keep token-bearing URLs out of shared logs or screenshots.

## BrowserOS Neo

On macOS with Homebrew available, Codex can install Neo as described in the
[official repository](https://github.com/browseros-ai/BrowserOS):

```bash
brew tap browseros-ai/tap
brew install --cask browseros-neo
```

Use that repository's download links for macOS, Windows or Linux x64 if you prefer
a direct download. The Python skill installer does not install the browser.

Open Neo and select Codex on its MCP connection board. Complete the local account
setup you need for your work. If you need manual configuration, use Neo's
[manual setup instructions](https://docs.browseros.com/neo/mcp/manual) and the
endpoint shown by your own instance. The in-app board also has the connection
instructions. Read the official Neo skill offered by the integration.

Reconnect MCP or start a new Codex session if the tools have not appeared. To test
the connection, ask Codex to list tabs, open a public page in a temporary tab, read
it and close that tab. Record the URL, date and result in your project's existing
notes. Keep profiles, cookies and sensitive raw logs out of Git.

## pen.dev

Install [pen.dev](https://www.pen.dev/) yourself. Configuring its Codex integration
is a manual step; this bundle does not configure it. Follow the app's current
Codex setup instructions, then ask Codex to read the native design instructions
and current app state. Some integrations expose these tools under the name `pencil`.
Confirm the intended app and file before making design changes.

## Penpot

Set up [Penpot](https://penpot.app/) through its hosted service or your own
deployment. The [official repository](https://github.com/penpot/penpot) has the
server source and setup information.

Choosing and configuring a Penpot MCP integration is a manual step. Select one
that supports your deployment and follow that integration's documentation; this
bundle does not choose, install or configure it. Once its tools appear in Codex,
read the overview and confirm the workspace and file before making changes. The
bundle does not install a Penpot server. A transfer from pen.dev to Penpot still needs
editable components and assets; inspect the result instead of assuming a lossless
file import.

## Verify the setup

| Check | Evidence |
| --- | --- |
| Installed files | `install.py doctor` succeeds and all seven sources resolve. |
| Skill discovery | Codex can read `design` in the intended project and session. |
| MCP configuration | Codex lists the integration you configured. |
| Neo access | Codex opens and reads a public page through Neo. |
| pen.dev access | Codex reads the design instructions and state of the intended app. |
| Penpot access | Codex reads the overview and file state in the intended instance. |

Mark a check as pending if the tool is unavailable. Run these checks on each
recipient's computer; a successful installation elsewhere does not verify their
connections.
