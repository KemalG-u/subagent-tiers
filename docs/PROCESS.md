# Preparation process

Record: contemporaneous preparation record, 2026-11-18; original development history is not reconstructed. The original source creation date is unknown.

## Export choice

A fresh repository preserves the selected source concepts rather than the private setup's history. Only the selected agent definitions were inputs; private policy agents, credentials, configuration, transcripts and operational logs were excluded. No remote was needed to prepare or test this tree; the repository was published afterwards. The publication identity uses the maintainer's GitHub noreply address.

## Preparation stages

| Date | Stage | Evidence |
|---|---|---|
| 2026-11-18 | Name check and bounded source selection | Legal/naming table in [PRIVACY-CHECK.md](PRIVACY-CHECK.md) |
| 2026-11-18 | Translate roles, remove local references and narrow tools | [Decision](decisions/0001-portable-prompts.md), `agents/` |
| 2026-11-18 | Offline structure and installed-layout checks | `tests/test_package.py`; [METRICS.md](METRICS.md) |
| 2026-11-18 | Security/privacy checks and limitations | [PRIVACY-CHECK.md](PRIVACY-CHECK.md) |

The source-to-public role mapping is discovery, implementer, reviewer, research-scout, security-auditor, diagnostician, data-analyst and broad-explorer. The broad search agent has a distinct name so the package does not shadow Claude Code's built-in Explore agent. Local-language policy references and machine-specific instructions are not dependencies of the installed prompts.

## Validation and limits

Offline tests validate frontmatter, names, tools, links and installation into an otherwise empty project agent directory. A deliberately malformed definition exercises the parser's rejection path. The read-only definitions are deliberately unable to run shell diagnostics or data scripts; the caller supplies runtime evidence.

No paid model calls or live agent delegations were performed during preparation. The tests establish an offline package property, not end-to-end model behavior. Setbacks during preparation are listed in the [preparation log](devlog/2026-11-18-portable-package.md). No runtime failure story is invented: no live model check was attempted. The preparation log records concrete changes and constraints rather than reconstructing a narrative from unknown history.

Interpretation: tier guidance may improve task assignment, but this package provides no measured performance or quality comparison. Recheck dated aliases and supported tool names when using a different Claude Code version.
