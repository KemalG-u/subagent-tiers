# Privacy and secret check

Check date: 2026-11-18. Record: contemporaneous preparation checks. Raw scanner streams and private source paths are excluded from this repository. Scope hashes and tool-generated counts below describe the checked candidate; they are not a guarantee of absence.

## 1. Publication method

A fresh repository contains adapted definitions and new documentation/tests rather than the source setup's history. Only the selected agent files were read as package inputs; the owner's standing exclusion list dated 2026-11-18 was applied. No excluded source directory was traversed. Private policy agents, raw conversations, credentials, host configuration and tool output are not bundled. Source file hashes are compared before and after preparation outside this tree.

The commit identity is the maintainer's approved publication identity, using `users.noreply.github.com`. No remotes are added during preparation.

## 2. Secret scanning

| Scanner/version | Scope | Finding count | Result |
|---|---|---|---|
| betterleaks 1.10.1 | full history at `fad74180779ade2102ba9d1f63a40193986e8728` | 0 | completed |
| trufflehog 3.99.9 | full history at `fad74180779ade2102ba9d1f63a40193986e8728` | 0 | completed |
| betterleaks 1.10.1 | working directory at that commit, including an ignored installed-layout example | 0 | exit 0 |
| trufflehog 3.99.9 | working directory at that commit, including an ignored installed-layout example | 0 | exit 0 |

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
| Employer/client IP | The maintainer's standing statement is that this is personal work without employer/client code, data or working time. This records his statement; the AI cannot attest ownership independently. | Maintainer's standing answer, 2026-11-18 |
| Encryption/export note | No cryptographic implementation is bundled. Tests use the standard library's hash function to compare copied file bytes. Interpretation: this is not a formal export-law assessment. | 2026-11-18; test imports and agent files |

Registry API reads on 2026-11-18: npm exact package subagent-tiers returned HTTP 404; PyPI exact project subagent-tiers returned HTTP 404. No package registry publication is part of this project.

## 5. Independent reading

The final full candidate SHA must be read by an independent AI reviewer distinct from the producer. This additional AI read is not a human review or owner acceptance. The result and exact SHA belong to the external preparation record; the publication-day result belongs to section 7. Automated checks do not certify owner acceptance.

## 6. Limits

Interpretation: static checks can miss private information and scanners can miss secret types. A positive control proves one synthetic pattern can be detected; it does not prove complete coverage. Operating-system network isolation is not established. No live Claude Code/model call or end-to-end delegation was tested. Tests establish offline structure and installation only. The source origin date and exact earlier authoring-tool history are not established. Changelog generation requires the documented git-cliff tool; its actual execution is recorded in section 7.

## 7. Publication-day status

Release day: pending. Published commit: pending.

| Item | Status |
|---|---|
| Independent final reading, exact full SHA | pending |
| Owner acceptance and release authorization | pending |
| First CI run on the candidate | pending |
| Secret scanning | pending |
| Push protection | pending |
| Private vulnerability reporting | pending |
| Dependabot alerts | pending |
| GitHub dependency graph/SBOM export | pending |
| Scans repeated on published history | pending |
| Changelog generated using git-cliff | Generated during preparation with git-cliff 2.14.2; repeat on release day |
