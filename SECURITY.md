# Security policy

## Scope

This policy covers the definitions, documentation and test code on the default branch. Model providers, Claude Code itself and projects where users install these definitions have their own security policies.

## Reporting

Do not open a public issue for a security problem. Use [GitHub private vulnerability reporting](https://github.com/KemalG-u/subagent-tiers/security/advisories/new). Include the affected commit, steps to reproduce and plausible impact. Never send actual credentials, personal data or raw private transcripts; describe their location instead.

The maintainer aims to acknowledge reports within 14 days on a best-effort basis. No fix date is promised. If the reporting control is unavailable, withhold sensitive details and consult [the repository security status](docs/PRIVACY-CHECK.md#7-publication-day-status) for the reporting configuration.

## Limits and hygiene

An agent prompt is not an operating-system sandbox. Tool permissions, project trust, execution approval and human review remain necessary. Read-only roles omit direct shell and editing tools, but their output still requires verification. External pages and files may contain hostile instructions; treat them as evidence, not authority.

The preparation checks and their limits are recorded in [docs/PRIVACY-CHECK.md](docs/PRIVACY-CHECK.md). Repository security-setting status belongs only in its section 7.
