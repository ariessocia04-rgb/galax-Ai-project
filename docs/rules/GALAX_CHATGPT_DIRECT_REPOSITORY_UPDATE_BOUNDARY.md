# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Final authority:** Human Owner

## 1. Canonical rule

Galax uses a capability-first, Cline-default execution model **with one explicit Skill 5 continuity exception**.

General repository work:

```text
Human Owner
→ ChatGPT decides WHAT should be done
→ Router selects one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines exact authority/scope/mode
→ Prompt Engineer packages the instruction when Cline is the executor
→ Cline executes whenever Cline is capable
→ Cline edits/saves locally
→ Cline runs only separately authorized validation
→ ChatGPT reviews Cline evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
→ Human Owner separately authorizes COMMIT
→ Cline commits
→ STOP
→ Human Owner separately authorizes PUSH
→ Cline pushes
→ STOP
→ GitHub provides remote evidence
→ ChatGPT independently reviews exact remote diff
→ Human Owner final acceptance
```

**Exact Skill 5 exception:** `update_length_problem`, `update_achievement`, and qualifying Skill 5 achievement persistence are executed and published directly by ChatGPT under Skill 5. Cline is not required for that exact continuity scope.

## 2. Responsibility split

```yaml
Human_Owner:
  final_authority: true
  coding_knowledge_required: false
  authorizes_scope: true
  authorizes_validation: true
  authorizes_commit: true
  authorizes_push: true
  final_acceptance: true

ChatGPT:
  role: architect_specification_supervisor_reviewer
  default_repository_executor: false
  default_commit_executor: false
  default_push_executor: false
  may_author_exact_change: true
  may_review_local_evidence: true
  may_review_remote_diff: true
  Skill_5_direct_continuity_executor: true
  Skill_5_direct_continuity_publisher: true_when_connected_GitHub_capability_available
  technical_fallback_executor_for_other_work: true_only_after_Skill_12_PASS_and_explicit_Human_Owner_authorization

Cline:
  role: default_repository_executor_when_capable_except_exact_Skill_5_continuity_scope
  edit_save_executor: true_when_authorized
  validation_executor: true_when_separately_authorized
  commit_executor: true_when_separately_authorized
  push_executor: true_when_separately_authorized
  may_mechanically_apply_ChatGPT_authored_governance: true
  may_independently_change_governance_meaning: false
  Skill_5_length_or_achievement_executor: false_by_default
  self_authorization: prohibited
```

## 3. Skill 5 direct ChatGPT continuity exception

Skill 5 is the only standing non-fallback direct ChatGPT repository-write exception.

```yaml
SKILL_5_CHATGPT_DIRECT_CONTINUITY_EXCEPTION:
  applies_to:
    - update_length_problem
    - update_achievement
    - qualifying_terminal_PASS_achievement_persistence
  executor: ChatGPT
  normal_publisher: ChatGPT_connected_GitHub_app_when_available
  Cline_required: false
  Prompt_Engineer_Cline_package_required: false
  main_write: prohibited
  unrelated_scope_expansion: prohibited
```

Required path:

```text
Router selects Skill 5
→ Context Engineer supplies verified continuity evidence
→ Skill 5 determines exact content/target/dedupe/numbering/timestamp/evidence class
→ ChatGPT directly persists the exact authorized continuity record
→ ChatGPT verifies resulting remote evidence
→ Human Owner final acceptance
→ stop
```

Do not route exact Skill 5 continuity persistence to Cline merely because Cline can edit Markdown.

When the connected GitHub contents API is used, it creates a remote commit directly. ChatGPT must report that exact mechanism and must not invent a separate local commit or push.

## 4. Global ChatGPT takeover blocker for non-Skill-5 work

If Cline is factually capable of an exact bounded task outside the standing Skill 5 continuity exception, ChatGPT must not take over repository execution merely because ChatGPT has GitHub access, authored the content, or would be faster.

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

This blocker applies to general edit/save, validation, commit, push/remote publication, governance, documentation, and implementation work.

## 5. Skill 12 fallback exception for other work

Outside the standing Skill 5 exception, ChatGPT may directly execute only when all required Skill 12 conditions are proven:

```yaml
GALAX_CHATGPT_TECHNICAL_FALLBACK_GATE:
  exact_action_known: true
  one_of:
    - Cline_capability_limit_factually_proven
    - repeated_material_Cline_mismatch_after_one_corrected_retry_proven
    - other_exact_owner_approved_verified_blocker
  ChatGPT_current_tool_capability_proven: true
  Human_Owner_explicit_fallback_authorization: true
  exact_authorized_stages_known: true
  LOCKED_ACCEPTED_conflict: false
  unrelated_scope_expansion: false
  simultaneous_overlapping_writer: false
  gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake does not authorize takeover.

After a valid fallback, the verified remote result becomes current repository truth; Cline resumes from it and must not redo/revert/overwrite it without new Human Owner authority.

## 6. Human Owner zero-coding rule

Never require the Human Owner to write code, patch files, type terminal/Git commands, resolve syntax, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording when an authorized AI actor can do it.

## 7. Consequential-stage separation

For Cline-executed work:

```text
PLAN ≠ ACT
ACT ≠ VALIDATE
VALIDATE ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
MERGE ≠ DEPLOY
```

No PASS automatically authorizes commit or push.

Direct Skill 5 connected-GitHub persistence is different: the repository write creates the remote commit directly, so no separate Cline commit/push stage exists for that exact action.

## 8. Prompt and context support

Canonical support files:

```text
docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
```

Context Engineer supplies verified minimum context.

Prompt Engineer supplies mandatory owner-facing and Cline-facing packaging only when a Cline instruction is required. It is not required for direct Skill 5 continuity persistence.

Neither support component changes authority.

## 9. Supersession

This file supersedes prior interpretations that either:

- made Cline the executor for exact Skill 5 length/achievement persistence; or
- made ChatGPT a broad direct repository writer outside Skill 5 without a valid Skill 12 fallback.

Current exact rule:

```text
Exact Skill 5 continuity/achievement persistence
→ ChatGPT executes and publishes directly.

Other repository work and Cline capable
→ Cline executes.
→ ChatGPT authors/specifies/reviews.
→ Human Owner controls consequential gates.

Other direct ChatGPT execution
→ Skill 12 only after verified gate + explicit Human Owner authorization.
```
