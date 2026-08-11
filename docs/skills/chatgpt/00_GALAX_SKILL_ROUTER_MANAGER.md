# Galax ChatGPT Skill Router Manager

**Status:** `ACTIVE_CHATGPT_ROUTING_CONTROL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Final authority:** Human Owner

## 1. Purpose

Select exactly one repository-backed primary Galax skill for the current bounded request, plus no more than two genuinely required dependency skills.

Repository evidence overrides chat memory.

## 2. Canonical executor architecture

```text
Human Owner
→ Router selects one primary skill
→ Context Engineer builds minimum verified context
→ selected skill decides exact authority/scope/mode
→ use the executor required by that selected skill
```

Normal repository execution rule:

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

**Mandatory Skill 5 exception:** exact `update_length_problem`, `update_achievement`, and qualifying Skill 5 achievement persistence are executed and published directly by ChatGPT through Skill 5. Cline is not required for that exact continuity scope.

For all other repository work, Cline remains the default executor whenever factually capable, including governance, skills, router, documentation, and CrewAI implementation.

ChatGPT must not directly execute general repository work merely because it authored the content or has GitHub access.

If Cline is capable for a non-Skill-5 task:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Only Skill 12 may permit ChatGPT technical/repository execution outside the exact Skill 5 continuity exception after its full fallback gate passes and the Human Owner explicitly authorizes the exact stages.

## 3. Skill registry

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

## 4. Non-skill support

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

Context Engineer is required for minimum verified context. Prompt Engineer is mandatory whenever ChatGPT must issue or package a Cline task, approval, rejection, correction, validation, Git, or review instruction.

Prompt Engineer is **not required** for direct Skill 5 continuity persistence because that exact path does not use Cline.

Unavailable results:

```text
BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE
BLOCKED_PROMPT_ENGINEER_UNAVAILABLE
```

## 5. Routing categories

```yaml
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
CHATGPT_SUPERVISORY_CONTROL_UPDATE:
  primary: $galax-owner-direct-repository-update-guardian
OWNER_RULE_SKILL_REQUIREMENTS_OR_FEASIBILITY:
  primary: $galax-owner-rule-skill-requirements-feasibility-guardian
CHATGPT_TECHNICAL_FALLBACK_AFTER_VERIFIED_CLINE_FAILURE:
  primary: $galax-chatgpt-technical-fallback-executor-guardian
UNKNOWN_OR_MULTI_TASK:
  result: BLOCKED_UNTIL_ONE_SAFE_PRIMARY_SCOPE_IS_PROVEN
```

## 6. Skill 2 and Skill 10 relationship

Skill 2 controls Cline prompt/execution packaging for repository work generally.

Skill 10 is mandatory only when the Cline task is active CrewAI remediation-blueprint implementation. Governance, documentation, router, and ChatGPT-support-file edits executed by Cline do not become CrewAI blueprint work merely because Cline performs them.

Skill 5 continuity/achievement direct persistence does not use Skill 2 because Cline is not the executor for that exact scope.

## 7. Skill 5 and Skill 9 executor rules

Skill 5 controls continuity/achievement content, evidence, dedupe, numbering, correctness, **and direct ChatGPT persistence** for its exact scope.

Skill 9 controls exact supervisory/router/skill/context/prompt governance specifications. Skill 9 does not make ChatGPT the normal governance publisher; Cline executes Skill 9 work when capable unless Skill 12 fallback is separately proven and authorized.

Exact Skill 5 path:

```text
Skill 5 selected
→ Context Engineer supplies verified continuity evidence
→ Skill 5 determines exact content/target
→ ChatGPT directly creates/updates the exact continuity record using the connected GitHub app when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner final acceptance
→ stop
```

General non-Skill-5 path when Cline can perform the action:

```text
selected skill defines exact change
→ Context Engineer supplies verified context
→ Prompt Engineer creates exact Cline package
→ Cline edits/saves
→ ChatGPT reviews
→ Human Owner COMMIT authorization
→ Cline commit
→ STOP
→ Human Owner PUSH authorization
→ Cline push
→ STOP
→ ChatGPT remote review
→ Human Owner final acceptance
```

## 8. Prompt package requirement

Every **Cline-facing** instruction must state outside the prompt box:

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

ChatGPT chooses exactly one session and one mode. Do not ask the Human Owner to choose.

Exact mapping:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

`execute the approved plan here` is an ACT/ACT_BOUNDED instruction, never a PLAN_ONLY instruction.

## 9. Consequential action separation

For Cline-executed work:

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
```

No automatic next stage.

For direct Skill 5 connected-GitHub persistence, the GitHub write itself creates the remote commit; do not invent a separate local commit or push step.

## 10. Mandatory new-chat recovery

New/unverified chats must recover and understand:

- this Router;
- the execution role separator;
- Context Engineer;
- Prompt Engineer;
- Cline-default execution for general repository work;
- **Skill 5 direct ChatGPT continuity/achievement persistence exception**;
- Skill 12 fallback for other ChatGPT execution;
- zero-coding-owner rule;
- NEW/STAY rules;
- mode mappings;
- approval/rejection packaging;
- commit/push separation for Cline work;
- LOCKED_ACCEPTED and do-not-repeat state.

## 11. Final rule

```text
Exact Skill 5 length-problem / achievement persistence
→ ChatGPT executes and publishes directly under Skill 5.

Other repository work and Cline capable
→ Cline executes.
→ ChatGPT authors/specifies/reviews.
→ Human Owner authorizes consequential stages.

Other ChatGPT execution
→ only through a separately proven and owner-authorized Skill 12 fallback.
```
