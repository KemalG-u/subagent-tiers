# Adapting a personal agent collection

Record: contemporaneous, 2026-11-18.

## Problem and diagnosis

The source collection could not be reused verbatim: a diagnostic prompt depended on a local skill, several instructions were local-language policies, and the broad-search agent used the built-in Explore name. Shell access also weakened the meaning of read-only roles.

## Resolution

The package translates and generalizes the prompts, gives broad search a distinct name, removes local dependencies and omits shell/edit tools from read-only roles. Manual copy installation uses Claude Code's existing project agent directory rather than a custom installer.

## Failed attempts and omissions

No live model behavior check was attempted; no failure or success is inferred. Offline installation testing cannot validate real model selection, account availability or prompt adherence. The package's parser has an explicit negative fixture to prove it rejects missing frontmatter.

## Evidence

`DefinitionTests.test_no_builtin_override`, `DefinitionTests.test_read_only_tool_boundaries`, `InstallationTests.test_copy_to_clean_project`, `InstallationTests.test_positive_control_rejects_bad_definition`, and [the preparation record](../PROCESS.md).
