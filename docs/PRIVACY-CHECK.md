# Privacy and secret check

Check date: 2026-11-18. Record: contemporaneous preparation checks; the state after publication is in section 7. Raw scanner streams and private source paths are excluded from this repository. Scope hashes and tool-generated counts below describe the checked candidate; they are not a guarantee of absence.

## 1. Publication method

A fresh repository contains adapted definitions and new documentation/tests rather than the source setup's history. Only the selected agent files were read as package inputs; the owner's standing exclusion list dated 2026-11-18 was applied. No excluded source directory was traversed. Private policy agents, raw conversations, credentials, host configuration and tool output are not bundled. Source file hashes are compared before and after preparation outside this tree.

The commit identity is the maintainer's GitHub noreply identity, using `users.noreply.github.com`. No remote was added during preparation; the repository was published afterwards (section 7).

## 2. Secret scanning

| Scanner/version | Scope | Finding count | Result |
|---|---|---|---|
| betterleaks 1.10.1 | full history at `fad74180779ade2102ba9d1f63a40193986e8728` | 0 | completed |
| trufflehog 3.99.9 | full history at `fad74180779ade2102ba9d1f63a40193986e8728` | 0 | completed |
| betterleaks 1.10.1 | working directory at that commit, including an ignored installed-layout example | 0 | exit 0 |
| trufflehog 3.99.9 | working directory at that commit, including an ignored installed-layout example | 0 | exit 0 |

The table shows the first checked candidate. The same scans, with the same scanner versions and with verification disabled, were repeated on later candidates over the full history and the working directory, each with 0 findings. Those results are kept outside the package.

Positive-control findings (git / directory): Betterleaks 1 / 1; TruffleHog 1 / 2. Filesystem scanning can include Git object data, so these are findings, not unique credential counts.
TruffleHog git mode produced a Windows termination warning; the instrumented Git event check recorded complete start/end coverage and zero command failures. No detector/scan error category was reported. The warning is not silently discarded.

Positive control: a separate synthetic repository contains a randomly generated token-shaped string, not a credential. The control stays outside this repository. Verification and update features are disabled; no credential is sent to a provider. Scans retain only allowlisted metadata and counts, never secret values or raw output.

## 3. Personal data and local references

A private static checker (version 2.1), run in strict mode, recorded 0 missing standard files and 0 path/e-mail/template findings. Raw transcript files, secret-like filenames and excluded-name files were all 0 according to that tool. Its only initial documentation warning was the deliberately empty metrics file; metrics are generated after the content commit. Final strict-check results are retained in the external preparation record.

All agent definitions were read manually for local instructions, policy references and paths. Intentional maintainer-name occurrences belong to copyright/AI-use attribution and the project GitHub URLs. The source collection's origin date is unknown (not recorded); file timestamps are not treated as proof of origin.

## 4. Legal and naming checks

| Check | Result | Evidence/date |
|---|---|---|
| Name and trademark | The GitHub exact-name check found no other-owner repository named subagent-tiers. A web search found a differently named scoped package, @pure01fx/dsh-subagent-tiers-hu. Registry API results are recorded below. No official trademark database was searched. Interpretation: this is a practical naming search, not trademark clearance or legal advice. | 2026-11-18; GitHub name search and web search for the exact phrase |
| Dependency/license inventory | Agent definitions are plain Markdown. Tests import only Python standard-library modules. CI references checkout and setup-python by full commit SHA; these are not bundled. Contributor Covenant attribution is preserved in the conduct document and NOTICE. No third-party runtime library is bundled. | 2026-11-18; imports in tests/test_package.py and workflow source |
| Employer/client IP | The maintainer's standing statement is that this is personal work without employer/client code, data or working time. This records the maintainer's statement; the AI cannot attest ownership independently. | Maintainer's standing answer, 2026-11-18 |
| Encryption/export note | No cryptographic implementation is bundled. Tests use the standard library's hash function to compare copied file bytes. Interpretation: this is not a formal export-law assessment. | 2026-11-18; test imports and agent files |

Registry API reads on 2026-11-18: npm exact package subagent-tiers returned HTTP 404; PyPI exact project subagent-tiers returned HTTP 404. No package registry publication is part of this project.

## 5. Independent reading

The final full candidate SHA must be read by an independent AI reviewer distinct from the producer. This additional AI read is not a human review or owner acceptance. The result and exact SHA belong to the external preparation record; the publication-day result belongs to section 7. Automated checks do not certify owner acceptance.

## 6. Limits

Interpretation: static checks can miss private information and scanners can miss secret types. A positive control proves one synthetic pattern can be detected; it does not prove complete coverage. Operating-system network isolation is not established. No live Claude Code/model call or end-to-end delegation was tested. Tests establish offline structure and installation only. The source origin date and exact earlier authoring-tool history are not established. Changelog generation requires the documented git-cliff tool; its actual execution is recorded in section 7.

## 7. State at publication

Read from GitHub and from the scanners on 2026-11-18, after the repository was published. This section is the one place for statements about the hosted repository; other files link here.

Published 2026-11-18 as https://github.com/KemalG-u/subagent-tiers (visibility public). The first push was `df1f099aaac00409fd6abf17e7088f24903a902f` (read back with `git ls-remote`).

| Item | State |
|---|---|
| Independent final reading | passed at `df1f099aaac00409fd6abf17e7088f24903a902f`: a delta read on top of the read that passed at `f894fc8`, by an independent AI reviewer (Claude), not a human sign-off. The failed and passed reads of earlier candidates are recorded outside the package |
| Release authorization | given by the maintainer on 2026-11-18 (publish today; the message itself is not published) |
| Owner acceptance of the exact release SHA | no separate sign-off on this SHA is recorded here; the maintainer's authorization to publish is the recorded decision. AI reads and automated checks do not stand in for owner acceptance |
| CI (`.github/workflows/ci.yml`): first run on the public repository | success on `df1f099`: https://github.com/KemalG-u/subagent-tiers/actions/runs/44373818308 . The action SHAs in the workflow were resolved again on 2026-11-18 with `git ls-remote` for the pinned tags (checkout v7.0.1, setup-python v7.1.0) and did not change |
| GitHub secret scanning, push protection, private vulnerability reporting, Dependabot alerts | enabled (read back from the GitHub API on 2026-11-18; Dependabot alerts: API status 204). Dependabot security updates: disabled. Secret scanning of non-provider patterns and validity checks: disabled. Dependabot version updates for the actions are configured in `.github/dependabot.yml` |
| GitHub dependency graph SBOM export | export available; the dependency graph lists 3 packages. This row records only that the export is available and its package count |
| Scans repeated on published history | at `df1f099`: Betterleaks 1.10.1 and TruffleHog 3.99.9, git history and working directory, 0 findings each; verification and update features off |
| Repository description and topics | description equals the first sentence of the README; topics: agent-skills, ai-agents, claude-code, model-routing, subagents |
| Profile page | the maintainer's profile README lists this repository ("New: subagent-tiers", commit `57993f6` in the profile repository), and the repository is pinned (GraphQL `pinnedItems` read: look-before-you-code, prove-it-review, subagent-tiers) |
| Release and tag | none: no `v0.1.0` tag and no GitHub release exist, while `CHANGELOG.md` has a 0.1.0 section |
| `CHANGELOG.md` | generated for `v0.1.0` with git-cliff 2.14.2 during preparation. It was not regenerated after publication: the tool was not run in the publication update, and the commits after publication are `docs:` commits, which `cliff.toml` skips (an inference from the configuration, not a run) |
