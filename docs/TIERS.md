# Work tiers and handoffs

Interpretation: these tiers express a working method, not measured model rankings. Defaults were chosen on 2026-11-18; aliases can resolve to different models over time. Review them against your account and the [Claude Code model reference](https://code.claude.com/docs/en/sub-agents#choose-a-model).

| Tier | Work | Suggested role and route | Evidence before moving on |
|---|---|---|---|
| K0 | Facts that can be checked directly | `discovery` or `broad-explorer`, haiku | Paths and lines, scope and unknowns |
| K1 | Bounded production or specialist evidence | `implementer`, `research-scout`, `diagnostician`, `data-analyst`, sonnet | Concrete output with its acceptance check or evidence gaps |
| K2 | Independent review of an important result | `reviewer`, opus; security-specific evidence may first go to `security-auditor`, sonnet | Findings tied to the actual candidate, not the producer's report |
| K3 | Architecture, uncertain high-impact cause, destructive or irreversible choice | Caller retains control; escalate to an appropriately capable model and a human decision where needed | Alternatives, consequences, explicit authorization and a verification plan |

These are not automatic routing rules. No K3 agent is bundled: a more expensive agent is not permission to delete data, change accounts, publish or spend money. Do not parallelize work that edits the same files. Independent read-only evidence gathering can run in parallel if your environment permits it.

## Brief example

```text
Goal: stop a retry setting being ignored.
Owned files: src/retry.py and tests/test_retry.py only.
Input: discovery's file:line evidence and the failing test output.
Preserve: other contributors' edits and the public function signature.
Acceptance: the regression test fails before the patch, then passes with the
existing retry tests. Report exact commands and executed test counts.
Boundaries: no publishing, account changes or destructive commands.
Delivery: diff summary, command -> result, remaining risks.
```

Interpretation: a useful sequence is discovery → caller diagnosis → bounded implementation → independent review → caller acceptance. It is an example, not an executed success story. If a cause is uncertain, use `diagnostician` for competing hypotheses before assigning a fix. The same model may serve different roles, but the producer must not certify its own work.

## Similar roles

`discovery` is a narrow lookup; `broad-explorer` searches a wider surface. `diagnostician` reasons about failure causes from evidence; `reviewer` compares a candidate against acceptance criteria. `security-auditor` specializes in security surfaces; it does not replace a complete security assessment. `data-analyst` requests deterministic computation when the supplied data cannot support a result directly.

## Tools and limits

Read-only definitions omit `Bash`, `Write` and `Edit`. This deliberately limits their direct runtime work: the caller executes tests and supplies redacted evidence. The implementer explicitly receives a shell and editing tools, subject to the host's permission system. Do not treat these lists as an operating-system sandbox. Research tools can contact external sites; do not put sensitive inputs in searches.

If a model alias or effort level is unavailable, choose an available route before use. Do not silently downgrade a high-impact review. There are no fixed token/turn quotas in these definitions: the caller controls the task budget and stops repeated unproductive attempts.
