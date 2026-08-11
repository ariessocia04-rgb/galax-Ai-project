# Galax ChatGPT Skill Router Manager

**Status:** `ACTIVE_CHATGPT_ROUTING_CONTROL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Final authority:** Human Owner except the owner-established permanent CrewAI remediation immutable set, which has no unlock path.

## 1. Purpose

Select exactly one repository-backed primary Galax skill for the current bounded request, plus no more than two genuinely required dependency skills.

Repository evidence overrides chat memory.

Before normal routing, apply the permanent CrewAI remediation mutation precheck in Section 2.

For material factual claims, also apply the lightweight factual-claim gate in Section 13 without creating a new primary skill or forcing duplicate reads.

## 2. Highest-priority permanent CrewAI remediation immutable gate

Canonical permanent lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Protected technical center:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

If any request from any actor, including the Human Owner, would directly or indirectly edit, rewrite, delete, rename, reformat, replace, supersede, reinterpret, weaken, unlock, or change the technical meaning of this permanent set:

```text
primary: $galax-locked-artifact-guardian
result: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
stop: true
```

This permanent gate preempts Skill 9, Skill 12, Cline execution, ordinary Human Owner unlock authority, and every other route.

Allowed operations on the permanent set are only:

```yaml
allowed:
  - read
  - inspect
  - check
  - diff
  - status
  - validate_non_mutating
  - verify_hash_or_blob_identity
  - verify_blueprint_mapping
  - commit_other_authorized_changes_when_protected_set_unchanged
  - push_other_authorized_changes_when_protected_set_unchanged
```

Commit/push is permitted only when the protected set and its technical meaning remain unchanged.

## 3. Canonical executor architecture

```text
Human Owner
→ Router selects one primary skill
→ Context Engineer builds minimum verified context
→ selected skill decides exact authority/scope/mode
→ use the executor required by that selected skill
```

### Standing ChatGPT direct repository jobs

These are the only standing non-fallback direct ChatGPT repository-write responsibilities, and none may override Section 2:

```yaml
CHATGPT_STANDING_DIRECT_REPOSITORY_JOBS:
  update_length_problem_in_repo:
    primary_skill: GALAX-SKILL-05
    executor: ChatGPT

  edit_or_update_ChatGPT_skills_and_rules_only:
    primary_skill: GALAX-SKILL-09
    executor: ChatGPT
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
    permanent_remediation_lock_override: prohibited

  update_achievement_in_repo:
    primary_skill: GALAX-SKILL-05
    executor: ChatGPT
```

Skill 5 and Skill 9 are standing direct ChatGPT exceptions only for their exact allowed scopes.

### General repository execution

For repository work outside those exact standing ChatGPT scopes:

```text
Cline executes whenever capable
→ ChatGPT reviews evidence
→ Human Owner authorizes consequential stages
→ Cline commits only after COMMIT authorization
→ STOP
→ Cline pushes only after separate PUSH authorization
→ STOP
→ ChatGPT reviews exact remote diff
→ Human Owner final acceptance
```

If Cline is capable for work outside Skill 5/Skill 9 standing scopes:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Only Skill 12 may permit other ChatGPT repository execution after its full fallback gate passes and the Human Owner explicitly authorizes the exact stages, but Skill 12 cannot override Section 2.

## 4. Skill registry

```yaml
GALAX_REPOSITORY_SKILL_REGISTRY:
  $galax-repository-state-scope-guardian:
    skill_id: GALAX-SKILL-01
    path: docs/skills/chatgpt/01_GALAX_REPOSITORY_STATE_SCOPE_GUARDIAN.md
  $galax-strict-cline-prompt-guardian:
    skill_id: GALAX-SKILL-02
    path: docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md
  $galax-evidence-validation-acceptance-guardian:
    skill_id: GALAX-SKILL-03
    path: docs/skills/chatgpt/03_GALAX_EVIDENCE_VALIDATION_ACCEPTANCE_GUARDIAN.md
  $galax-draft-pr-exact-diff-reviewer:
    skill_id: GALAX-SKILL-04
    path: docs/skills/chatgpt/04_GALAX_DRAFT_PR_EXACT_DIFF_REVIEWER.md
  $galax-continuity-achievement-guardian:
    skill_id: GALAX-SKILL-05
    path: docs/skills/chatgpt/05_GALAX_CONTINUITY_ACHIEVEMENT_GUARDIAN.md
  $galax-locked-artifact-guardian:
    skill_id: GALAX-SKILL-06
    path: docs/skills/chatgpt/06_GALAX_LOCKED_ARTIFACT_GUARDIAN.md
  $galax-repository-cleanup-auditor:
    skill_id: GALAX-SKILL-07
    path: docs/skills/chatgpt/07_GALAX_REPOSITORY_CLEANUP_AUDITOR.md
  $galax-new-chat-bootstrap-guardian:
    skill_id: GALAX-SKILL-08
    path: docs/skills/chatgpt/08_GALAX_NEW_CHAT_BOOTSTRAP_GUARDIAN.md
  $galax-owner-direct-repository-update-guardian:
    skill_id: GALAX-SKILL-09
    path: docs/skills/chatgpt/09_GALAX_OWNER_DIRECT_REPOSITORY_UPDATE_GUARDIAN.md
  $galax-cline-blueprint-scope-blocker:
    skill_id: GALAX-SKILL-10
    path: docs/skills/chatgpt/10_GALAX_CLINE_BLUEPRINT_SCOPE_BLOCKER.md
  $galax-owner-rule-skill-requirements-feasibility-guardian:
    skill_id: GALAX-SKILL-11
    path: docs/skills/chatgpt/11_GALAX_OWNER_RULE_SKILL_REQUIREMENTS_FEASIBILITY_GUARDIAN.md
  $galax-chatgpt-technical-fallback-executor-guardian:
    skill_id: GALAX-SKILL-12
    path: docs/skills/chatgpt/12_GALAX_CHATGPT_TECHNICAL_FALLBACK_EXECUTOR_GUARDIAN.md
```

Do not invent another skill or load all skills by default.

## 5. Non-skill support

```yaml
Context_Engineer:
  path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
  registered_skill: false
  dependency_skill: false
  counts_toward_limits: false

Prompt_Engineer:
  path: docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
  registered_skill: false
  dependency_skill: false
  counts_toward_limits: false
```

Context Engineer is required for minimum verified context.

Prompt Engineer is mandatory only when ChatGPT must issue or package a Cline task, approval, rejection, correction, validation, Git, or review instruction.

Prompt Engineer is not required for direct Skill 5 or direct Skill 9 repository actions because Cline is not the executor for those exact scopes.

## 6. Routing categories

```yaml
PERMANENT_CREWAI_REMEDIATION_MUTATION_OR_UNLOCK_ATTEMPT:
  primary: $galax-locked-artifact-guardian
  result: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK

NEW_CHAT_BOOTSTRAP:
  primary: $galax-new-chat-bootstrap-guardian
REPOSITORY_STATE:
  primary: $galax-repository-state-scope-guardian
CLINE_EXECUTION_COMMAND_OR_PERMISSION:
  primary: $galax-strict-cline-prompt-guardian
EVIDENCE_REVIEW:
  primary: $galax-evidence-validation-acceptance-guardian
DRAFT_PR_REVIEW:
  primary: $galax-draft-pr-exact-diff-reviewer
CONTINUITY_OR_ACHIEVEMENT:
  primary: $galax-continuity-achievement-guardian
LOCKED_ARTIFACT:
  primary: $galax-locked-artifact-guardian
CLEANUP_AUDIT:
  primary: $galax-repository-cleanup-auditor
CHATGPT_SKILL_OR_RULE_UPDATE:
  primary: $galax-owner-direct-repository-update-guardian
OWNER_RULE_SKILL_REQUIREMENTS_OR_FEASIBILITY:
  primary: $galax-owner-rule-skill-requirements-feasibility-guardian
CHATGPT_TECHNICAL_FALLBACK_AFTER_VERIFIED_CLINE_FAILURE:
  primary: $galax-chatgpt-technical-fallback-executor-guardian
UNKNOWN_OR_MULTI_TASK:
  result: BLOCKED_UNTIL_ONE_SAFE_PRIMARY_SCOPE_IS_PROVEN
```

## 7. Skill 2 and Skill 10 relationship

Skill 2 controls Cline prompt/execution packaging only when Cline is the executor.

Skill 10 is mandatory for active CrewAI remediation-blueprint implementation.

Neither Skill 2 nor Skill 10 may authorize mutation of the permanent remediation set.

Direct Skill 5 and direct Skill 9 work do not use Skill 2 because Cline is not the executor for those exact standing scopes.

## 8. Skill 5 and Skill 9 direct execution rules

### Skill 5

```text
Skill 5 selected for length problem / achievement
→ Context Engineer supplies verified continuity evidence
→ Skill 5 determines exact content/target
→ ChatGPT directly creates/updates the exact continuity record using the connected GitHub app when available
→ ChatGPT verifies resulting remote evidence
→ Human Owner final acceptance
→ stop
```

### Skill 9

```text
Skill 9 selected for create/edit/update of an eligible ChatGPT skill or rule
→ Context Engineer supplies verified repository evidence
→ apply permanent CrewAI remediation immutable precheck
→ if permanent lock collision: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ otherwise verify target is under docs/skills/chatgpt/** or docs/rules/**
→ for new supervisory rules, require explicit Human Owner approval of the bounded purpose/scope
→ ChatGPT directly creates/edits/updates the exact allowed skill/rule
→ ChatGPT verifies resulting remote evidence
→ Human Owner final acceptance
→ stop
```

## 9. Prompt package requirement for Cline work

Every Cline-facing instruction must state outside the prompt box:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
OWNER ACTION: <exact action>
DO NOT: <exact prohibitions>
EXPECTED CLINE STOP: <exact stop>
AFTER CLINE STOPS: <exact return evidence>
CLINE PROMPT REQUIRED: YES | NO
```

ChatGPT chooses exactly one session and one mode.

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

`execute the approved plan here` is an ACT/ACT_BOUNDED instruction, never a PLAN_ONLY instruction.

## 10. Consequential action separation

For Cline-executed work:

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
```

For connected-GitHub direct Skill 5 or Skill 9 writes, the write creates the remote commit directly; do not invent a separate local commit or push.

The permanent remediation set is different: no direct write is allowed at all after the permanent lock publication.

## 11. Mandatory new-chat recovery

New/unverified chats must recover:

- permanent CrewAI remediation immutable set and `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK`;
- no Human Owner unlock path for that set;
- read/check/non-mutating validation only for protected remediation artifacts;
- commit/push allowed only when protected set remains unchanged;
- Cline-default execution for general repository work;
- Skill 5 direct ChatGPT length-problem/achievement persistence;
- Skill 9 direct ChatGPT create/edit/update authority for eligible `docs/skills/chatgpt/**` and `docs/rules/**`, excluding permanent remediation artifacts;
- Skill 12 fallback for other direct ChatGPT execution, never for the permanent remediation set;
- Context Engineer;
- Prompt Engineer for Cline work;
- zero-coding-owner rule;
- NEW/STAY and mode mappings;
- approval/rejection packaging;
- commit/push separation for Cline work;
- ordinary LOCKED_ACCEPTED and do-not-repeat state;
- factual claim gate: `docs/rules/GALAX_CHATGPT_FACTUAL_CLAIM_GATE.md`.

## 12. Final rule

```text
Permanent CrewAI remediation blueprint/rule/canonical narrow supersession mutation request
→ Skill 6
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ STOP.

Allowed protected-set operations
→ read / check / non-mutating validation only.
→ commit/push only when protected set remains unchanged.

ChatGPT standing jobs outside permanent lock:
1. Update length problem in repo → Skill 5.
2. Create owner-approved supervisory rules and edit/update ChatGPT skills/rules only → Skill 9.
3. Update achievement in repo → Skill 5.

Everything else and Cline capable
→ Cline executes.

Other direct ChatGPT execution
→ Skill 12 only after verified gate + explicit Human Owner authorization, but never to override the permanent remediation lock.
```

## 13. Global factual claim gate

Canonical rule:

```text
docs/rules/GALAX_CHATGPT_FACTUAL_CLAIM_GATE.md
```

This is supervisory support, not a registered skill and not a routing destination.

For a material factual claim:

```text
fresh verified evidence already exists
→ reuse it; do not re-fetch merely to repeat the same proof.

current verification is materially required and the required source/tool is available
→ verify only the missing/current fact.

required evidence is missing or conflicting
→ UNKNOWN / UNVERIFIED / applicable existing blocker.

unsupported guessing
→ prohibited.
```

This gate must not trigger a full repository scan, full skill load, automatic web search, or duplicate reads. The Context Engineer applies the evidence classification and fast-path rules.

The permanent CrewAI remediation immutable gate in Section 2 remains higher authority than this factual-claim gate.
