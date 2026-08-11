```yaml
skill_reference: $galax-new-chat-bootstrap-guardian
skill_id: GALAX-SKILL-08
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 8: Galax New Chat Bootstrap Guardian

## 1. Purpose

Skill 8 reconstructs enough repository-backed state for a new/unverified Galax chat to continue safely without asking the Human Owner to restate repository history.

## 2. Mandatory bootstrap chain

```text
fetch Router
→ fetch Skill 8
→ fetch only required dependencies
→ fetch Context Engineer
→ fetch Prompt Engineer only when Cline-facing packaging is required
→ reconstruct current repository/task/executor/lock state
→ produce bootstrap receipt
→ PASS only when safe_to_continue=true
→ start separate normal routing cycle for original request
```

## 3. Highest-priority permanent CrewAI remediation rule to recover

A safe bootstrap must recover this canonical permanent lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

and understand:

```yaml
permanent_CrewAI_remediation_set:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md

unlock_path: NONE
Human_Owner_unlock: prohibited
ChatGPT_unlock: prohibited
Cline_unlock: prohibited
Skill_9_override: prohibited
Skill_12_override: prohibited
mutation_result: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

Allowed interaction is only read/check/non-mutating validation and commit/push when the protected set remains unchanged.

Bootstrap must not PASS if this permanent rule is unknown or interpreted as an ordinary owner-unlockable `LOCKED_ACCEPTED` artifact.

## 4. Mandatory recovered ChatGPT jobs

A safe bootstrap must also recover these exact standing ChatGPT repository jobs:

```text
1. update length problem in repo → Skill 5 → ChatGPT direct execution/publication.
2. edit/update ChatGPT skills and rules only → Skill 9 → ChatGPT direct execution/publication only under docs/skills/chatgpt/** and docs/rules/**, excluding permanent CrewAI remediation artifacts/rules.
3. update achievement in repo → Skill 5 → ChatGPT direct execution/publication.
```

It must also recover:

- zero-coding-owner rule;
- Cline-default execution for all other repository work when Cline is capable;
- `BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE` outside standing Skill 5/Skill 9 scopes;
- Skill 12 as fallback for other direct ChatGPT execution, never for permanent remediation mutation;
- Context Engineer role and fast-path boundaries;
- Prompt Engineer role for Cline-facing work;
- NEW/STAY and mode mappings;
- PLAN_ONLY before ACT_BOUNDED when planning is required;
- `execute the approved plan here` only in ACT_BOUNDED;
- commit/push separation for Cline work;
- ordinary LOCKED_ACCEPTED and do-not-repeat state.

## 5. Prompt support

Prompt Engineer is not required for direct Skill 5 or allowed direct Skill 9 actions because Cline is not executor for those scopes.

For Cline tasks:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

The Human Owner must not be asked to choose NEW/STAY or PLAN/ACT.

No Cline prompt may be emitted for a permanent remediation mutation/unlock request.

## 6. Bootstrap receipt

```yaml
GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V5:
  repository:
  router_loaded: true | false
  Context_Engineer_loaded: true | false
  Prompt_Engineer_loaded_when_required: true | false
  branch_or_ref:
  verified_HEAD_SHA:
  active_assignment:
  current_stage:
  completed_work: []
  LOCKED_ACCEPTED: []
  do_not_repeat: []
  blockers: []
  permanent_CrewAI_remediation_lock_recovered: true | false
  permanent_CrewAI_remediation_unlock_path_NONE_recovered: true | false
  Human_Owner_cannot_unlock_permanent_remediation_set_recovered: true | false
  Skill_5_ChatGPT_length_problem_rule_recovered: true | false
  Skill_9_ChatGPT_skill_rule_update_rule_recovered: true | false
  Skill_5_ChatGPT_achievement_rule_recovered: true | false
  Cline_default_other_work_rule_recovered: true | false
  Skill_12_fallback_rule_recovered: true | false
  zero_coding_owner_rule_recovered: true | false
  NEW_STAY_rule_recovered: true | false
  mode_mapping_recovered: true | false
  safe_to_continue: true | false
```

## 7. Stop discipline

Bootstrap itself does not execute the original technical task. After PASS, route the preserved Human Owner request through a separate Router cycle.

A request to mutate/unlock the permanent CrewAI remediation set does not proceed to another route; it returns `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK` and stops.
