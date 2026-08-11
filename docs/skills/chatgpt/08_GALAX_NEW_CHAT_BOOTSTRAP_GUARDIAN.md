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
→ fetch Prompt Engineer
→ read new-chat operating manual
→ reconstruct current repository/task/executor state
→ produce bootstrap receipt
→ PASS only when safe_to_continue=true
→ start separate normal routing cycle for the original request
```

## 3. Mandatory recovered rules

A safe bootstrap must recover and preserve:

- Human Owner final authority;
- zero-coding-owner rule;
- Cline-default repository execution whenever Cline is capable;
- ChatGPT architect/specification/supervisor/reviewer role by default;
- `BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE`;
- Skill 12 as the only verified owner-authorized ChatGPT execution fallback;
- Context Engineer role and fast-path boundaries;
- Prompt Engineer role;
- exact `NEW` versus `STAY` rule;
- exact mode mappings;
- owner-facing header requirement;
- approval and rejection packaging;
- `PLAN_ONLY` before implementation when planning is required;
- `execute the approved plan here` only in `ACT_BOUNDED`;
- edit/validation/commit/push separation;
- exact remote review after push/publication;
- LOCKED_ACCEPTED protections;
- completed work and do-not-repeat state;
- current assignment, branch/ref, HEAD and blockers.

## 4. Mandatory prompt support

Canonical support files:

```text
docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
```

If either is required and unavailable:

```text
BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE
BLOCKED_PROMPT_ENGINEER_UNAVAILABLE
```

## 5. Prompt-mode recovery

Bootstrap must understand:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

The Human Owner must not be asked to choose NEW/STAY or PLAN/ACT.

## 6. Bootstrap receipt

```yaml
GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V2:
  repository:
  router_loaded: true | false
  Context_Engineer_loaded: true | false
  Prompt_Engineer_loaded: true | false
  branch_or_ref:
  verified_HEAD_SHA:
  active_assignment:
  current_stage:
  last_completed_action:
  completed_work: []
  LOCKED_ACCEPTED: []
  rejected_or_superseded_work: []
  do_not_repeat: []
  blockers: []
  Cline_default_executor_rule_recovered: true | false
  Skill_12_fallback_rule_recovered: true | false
  zero_coding_owner_rule_recovered: true | false
  NEW_STAY_rule_recovered: true | false
  mode_mapping_recovered: true | false
  approval_rejection_package_recovered: true | false
  commit_push_separation_recovered: true | false
  safe_to_continue: true | false
```

## 7. Stop discipline

Bootstrap itself does not execute the technical task. After PASS, route the original Human Owner request through a separate normal Router cycle.
