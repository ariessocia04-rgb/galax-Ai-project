```yaml
skill_reference: $galax-chatgpt-technical-fallback-executor-guardian
skill_id: GALAX-SKILL-12
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 12: Galax ChatGPT Technical Fallback Executor Guardian

## 1. Purpose

Skill 12 is the only exception that may temporarily make ChatGPT the repository executor.

Normal rule:

```text
Cline capable → Cline executes.
ChatGPT authors/specifies/supervises/reviews.
Human Owner controls consequential stages.
```

If Cline is capable of the exact bounded action, Skill 12 must return:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 2. Activation evidence

A fallback candidate exists only when at least one is factually proven:

```yaml
fallback_reason:
  - CLINE_CAPABILITY_BLOCKED
  - CLINE_REPEATED_COMMAND_MISMATCH
  - OTHER_OWNER_APPROVED_VERIFIED_BLOCKER
```

`CLINE_REPEATED_COMMAND_MISMATCH` requires:

```text
first material mismatch
→ ChatGPT gives exact corrected command
→ Human Owner authorizes corrected retry
→ Cline materially mismatches the same bounded goal again
```

One mistake is not enough.

## 3. Mandatory gate

Before any ChatGPT repository execution:

```yaml
GALAX_CHATGPT_TECHNICAL_FALLBACK_GATE_V2:
  Human_Owner_request:
  repository:
  target_branch:
  current_HEAD_SHA:
  exact_bounded_action:
  exact_target_files: []

  normal_executor: Cline
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

ChatGPT may execute only when `gate_result == PASS_CHATGPT_TECHNICAL_FALLBACK`.

## 4. Owner authorization

The Human Owner approves the exact fallback action/stages in plain language. The Human Owner is never required to code or perform Git commands manually.

## 5. Stage authority

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

The Human Owner may explicitly combine exact bounded stages. Do not infer combined authority from vague language.

## 6. GitHub direct-write truthfulness

```yaml
CONNECTED_GITHUB_DIRECT_WRITE:
  creates_remote_commit_directly: true
  separate_local_commit: false
  separate_push: false
  required_owner_authority: exact_remote_write_or_publication_authorization
```

Do not falsely report a separate push when the connected GitHub write created the remote commit directly.

## 7. Scope limits

Fallback must touch only the exact owner-authorized target.

Prohibited without separate authority:

- unrelated scope expansion;
- LOCKED_ACCEPTED modification;
- main direct write;
- force push/history rewrite;
- secrets/security changes by inference;
- merge;
- deploy;
- simultaneous overlapping Cline + ChatGPT writers.

## 8. Result and resume

After execution, verify exact remote evidence and return:

```yaml
GALAX_CHATGPT_TECHNICAL_FALLBACK_RESULT_V2:
  repository:
  fallback_gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
  Human_Owner_authorized_stages: []
  execution_mechanism:
  target_branch:
  starting_HEAD_SHA:
  files_created: []
  files_modified: []
  files_deleted: []
  resulting_commit_or_remote_SHA:
  remote_diff_verified: true | false
  unrelated_changes_detected: []
  LOCKED_ACCEPTED_preserved: true | false
  status: PASS | CHANGES_REQUIRED | BLOCKED
```

Successful fallback work becomes current repository truth. Cline resumes from it and must not redo/revert/overwrite it without new Human Owner authority.

## 9. Final contract

```text
Cline can perform exact action
→ BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE

Cline cannot perform exact action / qualifying repeated mismatch / verified blocker
+ ChatGPT exact capability proven
+ Human Owner explicitly authorizes exact fallback stages
+ no lock/scope/writer conflict
→ PASS_CHATGPT_TECHNICAL_FALLBACK
→ ChatGPT performs only authorized action
→ verify result
→ Cline resumes from new repository truth
```
