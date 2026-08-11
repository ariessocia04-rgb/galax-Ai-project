```yaml
skill_reference: $galax-cline-blueprint-scope-blocker
skill_id: GALAX-SKILL-10
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 10: Galax Cline Blueprint Scope Blocker

## 1. Purpose

Skill 10 is the mandatory scope gate for real active CrewAI remediation-blueprint implementation tasks.

It allows implementation **from** the frozen remediation blueprint while permanently forbidding mutation **of** the remediation blueprint, its permanent lock rule, or the canonical Foundation narrow supersession.

## 2. Permanent immutable precondition

Before returning any implementation PASS, verify the proposed action does not directly or indirectly mutate:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

Mutation includes edit, rewrite, delete, rename, move, reformat, replace, supersede, reinterpret, weaken, unlock, or indirect technical-meaning change.

If any such mutation is proposed:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and stop.

Human Owner approval does not override this permanent gate.

## 3. PASS condition

Return:

```text
PASS_CLINE_BLUEPRINT_ONLY
```

only when all are proven:

```yaml
repository_matches: true
active_blueprint_verified: true
active_assignment_verified: true
branch_verified: true
HEAD_verified: true
proposed_action_traces_to_active_blueprint: true
permanent_CrewAI_remediation_set_unchanged: true
no_indirect_remediation_semantic_mutation: true
LOCKED_ACCEPTED_preserved: true
completed_work_not_repeated: true
scope_is_bounded: true
```

Otherwise return the exact factual blocker.

## 4. Allowed interaction with frozen remediation artifacts

During implementation work, protected remediation artifacts may only be:

```yaml
allowed:
  - read
  - inspect
  - check
  - diff
  - validate_non_mutating
  - verify_hash_or_blob_identity
  - verify_blueprint_mapping
```

Commit/push may proceed only when those protected artifacts remain unchanged.

## 5. Non-blueprint work

Skill 10 is not the general executor router.

For work that is not active CrewAI remediation implementation, return:

```text
NOT_A_SKILL_10_BLUEPRINT_TASK
```

Then the Router applies the correct route:

```text
Skill 5 exact length-problem/achievement persistence → ChatGPT direct under Skill 5.
Allowed Skill 9 ChatGPT skill/rule update → ChatGPT direct under Skill 9.
Other non-protected repository work and Cline capable → Cline execution through Skill 2.
```

Skill 10 must not classify protected remediation mutation as ordinary non-blueprint work; that always returns `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK`.

## 6. Executor rule

For active CrewAI implementation work that passes this gate:

```text
Cline executes the bounded implementation.
ChatGPT supervises/reviews.
Human Owner controls consequential stages.
```

Direct ChatGPT technical fallback outside standing Skill 5/Skill 9 scopes requires Skill 12, but Skill 12 cannot override the permanent remediation lock.

## 7. Final contract

```text
Implement exact frozen blueprint requirement
+ protected remediation artifacts remain unchanged
→ PASS_CLINE_BLUEPRINT_ONLY may be possible.

Edit/unlock/supersede/change remediation blueprint or protected technical meaning
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK.

Read/check/non-mutating validation of protected set
→ allowed when narrowly required.

Commit/push
→ allowed only when protected set remains unchanged.
```
