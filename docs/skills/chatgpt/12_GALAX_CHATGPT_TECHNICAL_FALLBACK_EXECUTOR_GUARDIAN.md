```yaml
skill_reference: $galax-chatgpt-technical-fallback-executor-guardian
skill_id: GALAX-SKILL-12
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 12: Galax ChatGPT Technical Fallback Executor Guardian

## 1. Purpose

Skill 12 is the fallback for **direct ChatGPT repository execution outside the standing Skill 5 and Skill 9 scopes**.

Standing direct ChatGPT scopes that do not require Skill 12:

```yaml
standing_non_fallback_ChatGPT_scopes:
  Skill_5:
    - update_length_problem_in_repo
    - update_achievement_in_repo
    - qualifying_achievement_persistence
  Skill_9:
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
    actions:
      - edit_skill_rule_content
      - update_skill_rule_content
```

For all other repository work:

```text
Cline capable → Cline executes.
ChatGPT authors/specifies/supervises/reviews.
Human Owner controls consequential stages.
```

If Cline is capable outside the standing Skill 5/Skill 9 scopes:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 2. Activation evidence

A Skill 12 fallback candidate exists only when at least one is factually proven:

```yaml
fallback_reason:
  - CLINE_CAPABILITY_BLOCKED
  - CLINE_REPEATED_COMMAND_MISMATCH
  - OTHER_OWNER_APPROVED_VERIFIED_BLOCKER
```

Repeated mismatch requires one exact corrected retry to have also failed materially on the same bounded goal.

## 3. Mandatory gate

```yaml
GALAX_CHATGPT_TECHNICAL_FALLBACK_GATE_V3:
  Human_Owner_request:
  repository:
  target_branch:
  current_HEAD_SHA:
  exact_bounded_action:
  exact_target_files: []

  action_inside_standing_Skill_5_scope: true | false
  action_inside_standing_Skill_9_scope: true | false

  normal_executor_outside_standing_scopes: Cline
  Cline_capable_of_exact_action: true | false
  fallback_reason:
  Cline_failure_or_blocker_evidence: []
  corrected_retry_evidence_when_required: []

  ChatGPT_current_tool_capability_verified: true | false
  ChatGPT_exact_execution_mechanism:
  ChatGPT_can_complete_exact_action: true | false

  LOCKED_ACCEPTED_conflict: true | false
  unrelated_scope_expansion: true | false
  simultaneous_writer_risk: true | false

  Human_Owner_fallback_authorization_received: true | false
  authorized_stages: []

  gate_result:
    PASS_CHATGPT_TECHNICAL_FALLBACK |
    BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE |
    BLOCKED_CLINE_FAILURE_NOT_PROVEN |
    BLOCKED_CHATGPT_CAPABILITY_NOT_PROVEN |
    BLOCKED_OWNER_AUTHORIZATION_REQUIRED |
    BLOCKED_LOCK_CONFLICT |
    BLOCKED_SCOPE_EXPANSION |
    BLOCKED_SIMULTANEOUS_WRITER_RISK
```

Skill 12 is not needed when the action is already authorized directly by Skill 5 or Skill 9.

## 4. Stage authority

Possible fallback stages:

```yaml
fallback_stages:
  - read_or_verify
  - edit_or_save
  - validation
  - commit
  - push_or_remote_publication
```

Default separation:

```text
EDIT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH_OR_REMOTE_PUBLICATION
```

## 5. GitHub direct-write truthfulness

```yaml
CONNECTED_GITHUB_DIRECT_WRITE:
  creates_remote_commit_directly: true
  separate_local_commit: false
  separate_push: false
```

Do not falsely report a separate push when a connected GitHub write created the remote commit directly.

## 6. Scope limits

Fallback must touch only the exact owner-authorized target. No unrelated scope expansion, LOCKED_ACCEPTED changes, main direct write, force push, history rewrite, secret changes by inference, merge, deploy, or overlapping Cline + ChatGPT writers without separate authority.

## 7. Final contract

```text
Skill 5 length/achievement work
→ ChatGPT executes directly under Skill 5.

Skill 9 ChatGPT skill/rule edit/update work
→ ChatGPT executes directly under Skill 9.

Other work and Cline capable
→ Cline executes.

Other work where fallback is factually justified
+ ChatGPT capability proven
+ Human Owner explicitly authorizes exact stages
→ Skill 12 may authorize only those stages.
```
