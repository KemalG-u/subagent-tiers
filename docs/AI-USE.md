# AI use in Subagent Tiers

Maintainer: Kemal (KarıncaAI). Record: reconstructed on 2026-11-18 from the source definitions and this preparation's files and checks. This is a curated summary, not a raw transcript.

## Standing declaration

The maintainer's standing statement is that he does not write code: AI tools write code and documents. He sets the direction and rules and reviews and checks every change. This is a personal project, without employer or client code, data or working time. That statement describes his working arrangement; it is not evidence that he has personally read this exact candidate. Review depth per change is not measured, and candidate-specific acceptance must be recorded separately.

## Work in this package

| Tool / model | Work |
|---|---|
| Codex / gpt-6.1-sol | Adapted the source definitions, translated and generalized prompts, wrote documentation and offline tests, executed local checks |
| Independent AI reviewer: Codex / gpt-6.1-sol, high effort | Read-only review of candidate `6456d614ff85cab8ae807968334c0209d002e068` against the preparation standard and source evidence. Ran the non-writing test classes, reported documentation gaps and did not write package files. This is an additional AI read, not human review or owner acceptance. Coverage of the final candidate is recorded separately outside the package. |
| Earlier source-authoring tools | The source definitions were supplied from a personal AI-agent setup; precise tool/model provenance is not established by the available source files |

The maintainer chose the publication scope and the use of tier guidance. The AI translated local instructions, renamed roles for general use, removed local policy dependencies, narrowed read-only tools and drafted this package. No raw agent logs are included.

## Verification

| Claim | Evidence |
|---|---|
| Definition format and tool boundaries | `python -B -m unittest discover -s tests -v`, [generated measurements](METRICS.md) |
| Definitions can be copied into a clean project agent directory | `InstallationTests.test_copy_to_clean_project`; byte equality and parsed installed frontmatter |
| Privacy and scanner checks | [PRIVACY-CHECK.md](PRIVACY-CHECK.md) |

The AI, not the human maintainer, ran these preparation checks. Tests do not call Claude Code or a model service. They do not prove prompt compliance, delegation quality or current account/model compatibility. No measured speed or cost advantage is claimed.

## Unknowns

- KEMAL-VERIFY: when did this particular source agent collection first begin? File timestamps are not accepted as proof of its origin.
- Exact creation history and authorship of individual source passages are not reconstructed from transcripts.
- The standing human-review declaration is the maintainer's statement; the exact candidate's human review must not be inferred from automated checks.

## Commit and copyright practice

Commits record AI assistance with `Assisted-by: Codex`. AI tools do not add `Signed-off-by` or attest human acceptance. The public history is a fresh preparation history rather than a copy of private setup history.

Interpretation: the human contribution is direction, specification, selection and arrangement, and review under the standing declaration. Purely machine-generated passages may lack copyright protection. AI-written share and review depth are not measured. This record is not a quality guarantee.
