# Contributing to Subagent Tiers

Keep changes focused on a concrete delegation problem. Discuss larger changes in an issue first, and follow the [Code of Conduct](CODE_OF_CONDUCT.md). For security reports, see [SECURITY.md](SECURITY.md).

## Development

Use Python 3.11 or newer. No extra Python packages are needed.

```sh
python -B -m unittest discover -s tests -v
```

Tests run offline and create scratch installation directories under your operating system's temporary directory, which are removed when each test ends; they never copy credentials or invoke a model. Check the changed role in a project-scoped agent directory before claiming runtime compatibility. Do not overwrite existing definitions. Include the Claude Code version and model route if you report a runtime check.

Update the role, tier guide, tests and installation instructions together when behavior changes. Use Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`); `git-cliff` generates the changelog from these subjects.

## Pull requests

Describe the problem, solution, scope and command → result. State which checks were omitted. Keep secrets, personal data, local machine paths and raw agent transcripts out of the repository and reports.

## AI use

- You are responsible for understanding and verifying your contribution, including AI-written output. Do not submit bulk unreviewed content or invented compatibility claims.
- Disclose substantial AI assistance in the PR and add `Assisted-by: Tool:model` to the commit message. Ordinary autocomplete needs no declaration.
- An AI must never add `Signed-off-by` or certify human review. Only a human can make that certification.
- Do not supply private data or code you cannot relicense to an AI service.
- Copyright depends on human creative contribution; purely generated text may not qualify. Explain your contribution honestly.

The project's own declaration is [docs/AI-USE.md](docs/AI-USE.md). This policy draws on the [LLVM AI policy](https://llvm.org/docs/AIToolPolicy.html) and [Linux coding assistant guidance](https://docs.kernel.org/process/coding-assistants.html).

## License

Contributions are submitted under Apache-2.0, section 5; see [LICENSE](LICENSE). Optional source header: `SPDX-License-Identifier: Apache-2.0`.
