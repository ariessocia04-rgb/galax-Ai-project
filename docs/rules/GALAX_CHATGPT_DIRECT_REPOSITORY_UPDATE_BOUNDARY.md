# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Final authority:** Human Owner

## 1. Canonical rule

Galax uses a capability-first, Cline-default execution model.

```text
Human Owner
→ ChatGPT decides WHAT should be done
→ Router selects one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines exact authority/scope/mode
→ Prompt Engineer packages the instruction
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

This applies to repository work generally, including CrewAI implementation, documentation, ChatGPT skills, router, supervisory rules, Context Engineer, Prompt Engineer, new-chat rules, length-problem records, and achievement records whenever Cline can perform the exact bounded action.

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
  technical_fallback_executor: true_only_after_Skill_12_PASS_and_explicit_Human_Owner_authorization

Cline:
  role: default_repository_executor_when_capable
  edit_save_executor: true_when_authorized
  validation_executor: true_when_separately_authorized
  commit_executor: true_when_separately_authorized
  push_executor: true_when_separately_authorized
  may_mechanically_apply_ChatGPT_authored_governance: true
  may_independently_change_governance_meaning: false
  self_authorization: prohibited
```

## 3. Global ChatGPT takeover blocker

If Cline is factually capable of the exact bounded task, ChatGPT must not take over repository execution merely because ChatGPT has GitHub access, authored the content, or would be faster.

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

This blocker applies to edit/save, validation, commit, push/remote publication, governance, continuity, and implementation work.

## 4. Skill 12 fallback exception

ChatGPT may directly execute only when all required conditions are proven:

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

Connected GitHub direct-write actions create remote commits directly. When used under valid Skill 12 fallback, ChatGPT must report that mechanism truthfully and must not invent a separate local commit/push step.

After fallback, the verified remote result becomes current repository truth; Cline resumes from it and must not redo/revert/overwrite it without new Human Owner authority.

## 5. Human Owner zero-coding rule

Never require the Human Owner to write code, patch files, type terminal/Git commands, resolve syntax, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording when an authorized AI actor can do it.

## 6. Consequential-stage separation

Default separation:

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

## 7. Prompt and context support

Canonical support files:

```text
docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
```

Context Engineer supplies verified minimum context. Prompt Engineer supplies the mandatory owner-facing and Cline-facing package. Neither is a primary/dependency skill and neither changes authority.

## 8. Supersession

This file supersedes prior rules that:

- made ChatGPT the normal direct Skill 9 supervisory writer;
- made ChatGPT the normal direct Skill 5 continuity/achievement uploader;
- prohibited Cline from mechanically applying ChatGPT-authored governance or continuity changes;
- limited Cline-default execution only to CrewAI source implementation.

Current exact rule:

```text
Cline capable → Cline executes.
ChatGPT authors/specifies/reviews.
Human Owner controls consequential gates.
ChatGPT executes only through verified, explicitly authorized Skill 12 fallback.
```
