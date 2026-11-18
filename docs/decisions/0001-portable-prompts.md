# Portable agent prompts without a runtime wrapper

Record: contemporaneous, 2026-11-18. Status: proposed adaptation; owner acceptance is separate.

Decision-makers: Codex / gpt-6.1-sol proposed and implemented this preparation's adaptation. Kemal (KarıncaAI) owns acceptance; this record does not assert the owner's acceptance of this candidate.

## Context

The source definitions included local-language working instructions, a local skill reference and a custom Explore name. Several nominally read-only roles had shell access. A public installation should not require the original person's policy files or silently override a built-in role.

## Options considered

- Copy the source files unchanged: rejected because of local references, language and built-in naming ambiguity.
- Build an installer and routing engine: rejected because Claude Code already loads Markdown definitions; a new runtime would add scope and dependencies.
- Adapt the definitions and document manual copy installation: selected for this preparation.

## Decision

Use English role names and self-contained instructions. Rename the wide-search role to broad-explorer. Omit shell/edit tools from read-only roles; limit executable work to the implementer under the caller's existing permissions. Model aliases are dated suggestions. K0–K3 describe work selection, not an automatic router; K3 remains with the caller.

## Consequences

Interpretation: static installation is easier to inspect, but read-only specialists now need caller-supplied command output for runtime diagnosis or calculations. Tool lists are not a complete security boundary. Tests check structure and installation, not the model's adherence to the instructions.

## Evidence

`agents/`, `tests/test_package.py`, [TIERS.md](../TIERS.md), and the [official custom-subagent format](https://code.claude.com/docs/en/sub-agents), accessed 2026-11-18.
