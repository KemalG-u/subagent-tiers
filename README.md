# Subagent Tiers

Reusable Claude Code agent definitions with a guide for matching work to evidence, risk and review needs.

[![CI](https://github.com/KemalG-u/subagent-tiers/actions/workflows/ci.yml/badge.svg)](https://github.com/KemalG-u/subagent-tiers/actions/workflows/ci.yml)

Use this when one assistant keeps switching between finding files, writing changes and judging its own work. For example: ask `discovery` to locate a broken setting, assign a bounded fix to `implementer`, then give `reviewer` the diff and acceptance criteria. You remain responsible for permissions, execution and acceptance.

## Install

Requires Claude Code with custom Markdown subagents. The definitions use documented model aliases; availability and supported effort levels depend on your account and runtime. See [the official documentation](https://code.claude.com/docs/en/sub-agents). Python 3.11 or newer is needed only for the offline package tests, with no third-party Python dependencies.

From the cloned repository, copy the definitions into a **new, empty** project agent directory. Inspect existing project agents first; do not overwrite them.

PowerShell:

```powershell
if (Test-Path -LiteralPath 'example-project/.claude/agents') {
  Write-Error 'example-project/.claude/agents already exists; choose a new empty project directory'
} else {
  $target = Join-Path $PWD 'example-project/.claude/agents'
  New-Item -ItemType Directory -Path $target -Force | Out-Null
  Copy-Item -LiteralPath (Get-ChildItem -LiteralPath ./agents -Filter '*.md').FullName -Destination $target
  Get-ChildItem -LiteralPath $target -Filter '*.md' | Sort-Object Name | Select-Object -ExpandProperty Name
}
```

POSIX shell (also from the cloned repository):

```sh
if [ -e example-project/.claude/agents ]; then
  echo 'example-project/.claude/agents already exists; choose a new empty project directory' >&2
else
  mkdir -p example-project/.claude/agents &&
    cp agents/*.md example-project/.claude/agents/ &&
    ls example-project/.claude/agents/
fi
```

Each block is a single `if`/`else` command, so nothing is copied when the target already exists, even if the lines are pasted one at a time.

Expected filenames (ordering may vary):

```text
broad-explorer.md
data-analyst.md
diagnostician.md
discovery.md
implementer.md
research-scout.md
reviewer.md
security-auditor.md
```

Start Claude Code in `example-project`. If the directory was created after an existing session started, restart that session. Example request:

```text
Use discovery to find where retries are configured. Read only. Return file:line
evidence and unknowns; do not choose a fix or run project commands.
```

The answer depends on your project; the filename listing above is the reproducible installation output. Installing these files does not install tools, configure a provider or grant new account permissions. The package does not replace the built-in `Explore` agent.

## Pick the work, then the tier

| Need | Agent | Default model alias |
|---|---|---|
| Narrow facts and locations | `discovery` | `haiku` |
| Wide read-only search | `broad-explorer` | `haiku` |
| Bounded implementation with a check | `implementer` | `sonnet` |
| Current external evidence | `research-scout` | `sonnet` |
| Diagnosis from supplied evidence | `diagnostician` | `sonnet` |
| Security review from supplied evidence | `security-auditor` | `sonnet` |
| Structured-data evidence analysis | `data-analyst` | `sonnet` |
| Independent final review | `reviewer` | `opus` |

The [K0–K3 guide](docs/TIERS.md) explains escalation, a complete handoff example and role overlap. Model choices are dated defaults, not a measured quality or speed guarantee. Read-only roles have no shell tool; ask the caller to obtain runtime evidence. The implementer can run commands under your existing permissions. Prompt text alone is not a security boundary.

## Tests

```sh
python -B -m unittest discover -s tests -v
```

Tests check the packaged definitions, project-scoped installation from a clean copy, name/tool boundaries and relative documentation links. They do not invoke an AI service or prove model behavior. Generated measurements: [docs/METRICS.md](docs/METRICS.md).

## How it was built

These definitions were adapted from a personal agent setup. The adaptation translates the prompts, removes local policy references, narrows read-only tools and documents the handoff discipline. The original creation date is not established by the available evidence. The preparation record describes what was actually checked and what remains unknown.

- [Process and limitations](docs/PROCESS.md)
- [AI use](docs/AI-USE.md)
- [Design decision](docs/decisions/0001-portable-prompts.md)
- [Preparation log](docs/devlog/2026-11-18-portable-package.md)
- [Privacy checks](docs/PRIVACY-CHECK.md)

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) and [CHANGELOG.md](CHANGELOG.md).

Apache-2.0: [LICENSE](LICENSE), [NOTICE](NOTICE).
