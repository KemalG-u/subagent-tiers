# Adapting a personal agent collection

Record: contemporaneous, 2026-11-18.

## Problem and diagnosis

The source collection could not be reused verbatim: a diagnostic prompt depended on a local skill, several instructions were local-language policies, and the broad-search agent used the built-in Explore name. Shell access also weakened the meaning of read-only roles.

## Resolution

The package translates and generalizes the prompts, gives broad search a distinct name, removes local dependencies and omits shell/edit tools from read-only roles. Manual copy installation uses Claude Code's existing project agent directory rather than a custom installer.

## Failed attempts and omissions

- The first offline test run had one failure: the documentation links check found a link to the metrics file, which did not exist yet. It was fixed and the tests were rerun.
- Changelog generation was blocked until the closing preparation round because `git-cliff` was not available to the preparation. It was generated in that round with git-cliff 2.14.2.
- An independent AI reading found two documentation gaps (the independent reader was not listed in the AI-use record, and the design decision did not state who proposed it); both were closed in `a5f1776`.
- A second independent AI read of the candidate found further documentation and test-hygiene issues; they were fixed before release.
- A read of those fixes found that the POSIX installation guard did not stop the following copy commands, so files in an existing target could be overwritten; the PowerShell snippet had the same problem when pasted line by line. Both snippets were rewritten as a single if/else command and run against an empty and an occupied target before release.
- No live model behavior check was attempted; no failure or success is inferred. Offline installation testing cannot validate real model selection, account availability or prompt adherence. The package's parser has an explicit negative fixture to prove it rejects missing frontmatter.

## Evidence

`DefinitionTests.test_no_builtin_override`, `DefinitionTests.test_read_only_tool_boundaries`, `InstallationTests.test_copy_to_clean_project`, `InstallationTests.test_positive_control_rejects_bad_definition`, and [the preparation record](../PROCESS.md).
