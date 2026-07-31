# Hybrid Atomic Prompting — Three Real Task Experiment

**Status:** `EXPERIMENTAL`  
**Activation token:** `HYBRID_ATOMIC_TRIAL_TASK_<N>_OF_3`

This rule is dormant unless the Human Owner's current task contains the activation token.

When active, follow:

```text
one goal
→ minimum necessary context
→ efficient authorized read or targeted search
→ one bounded result
→ explicit stop
```

## Priority

This experiment does not override:

- Human Owner authority;
- locked accepted work protection;
- exact task scope;
- no direct write to `main`;
- approval requirements for edits, commands, dependencies, and Git writes;
- stop-on-unexpected-result rules;
- architecture, schema, security, workflow, deployment, credential, and MCP restrictions.

Where this rule conflicts with a safety boundary in `00-galax-governance.md`, the safety boundary wins.

## Investigation behavior

For diagnosis, inspection, comparison, or failure classification:

```yaml
preferred_mode: PLAN
allowed:
  - native file reads within named scope
  - targeted native searches within named files or named directory scope
  - evidence-backed analysis
forbidden:
  - edits
  - terminal commands
  - tests
  - Git writes
```

Do not reread the same file range without a material reason.

Do not replace an efficient targeted native search with repeated full-file reads merely to satisfy an imagined tool sequence.

## Implementation behavior

For an already diagnosed correction:

```yaml
preferred_mode: ACT
required:
  - one concrete goal
  - exact authorized path or paths
  - one bounded conceptual correction
  - visible reviewable diff
  - stop after the authorized endpoint
forbidden:
  - unrelated refactor
  - extra files
  - automatic testing unless authorized
  - automatic retry
  - automatic continuation
  - Git writes unless separately authorized
```

## Command behavior

For an authorized test or command:

```yaml
maximum_commands: as_stated_by_current_task
source_edits: prohibited_unless_separately_authorized
automatic_retry: prohibited
follow_on_commands: prohibited
required_result:
  - exact command
  - complete output
  - exit code
  - stop
```

## Response discipline

Do not restate the entire repository governance file in every response.

Do not generate oversized receipts unless the current task requires that evidence.

Return only the evidence necessary to prove the current goal, including blockers and the exact next action.

## Trial measurement

The Human Owner is testing three completed real tasks with zero `Reject` actions.

For each activated task, include this final compact scorecard:

```yaml
hybrid_atomic_trial:
  task_number:
  human_rejects:
  duplicate_reads:
  unauthorized_actions:
  automatic_continuation:
  correct_result:
  bounded_result:
  provisional_result: PASS_or_FAIL_or_NO_SCORE
```

Do not self-award final experimental adoption. ChatGPT and the Human Owner review the scorecard after each task.
