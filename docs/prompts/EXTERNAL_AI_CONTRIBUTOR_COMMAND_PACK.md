# External AI Contributor Command-Pack Router

```yaml
document_status: ACTIVE_COMPATIBILITY_ROUTER
repository: ariessocia04-rgb/galax-Ai-project
Cline_prompt_creation_status: SUPERSEDED_BY_CANONICAL_GUIDE
canonical_Cline_prompt_creation_rule: docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
old_generic_Cline_Stage_A_prompt_active: false
old_generic_Cline_Stage_B_prompt_active: false
non_Cline_contributor_guidance_status: PRESERVED_AT_PINNED_HISTORICAL_REF
non_Cline_pinned_ref: 0a145d7d3ff770160e528a1fe170f301f878f7d4
non_Cline_pinned_path: docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
historical_content_deleted: false
```

> [!IMPORTANT]
> **For every Cline prompt, do not use the former generic Stage A or Stage B commands from this file's history.**
>
> Read and follow:
>
> `docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md`

## 1. Cline routing rule

Any ChatGPT session, new chat, or repository-aware assignment author creating, correcting, reviewing, or approving a prompt for Cline must read:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ the latest applicable checkpoint
→ docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
→ the exact active plan and assignment
→ docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
→ current live repository and owner-supplied evidence
```

The active Cline format is the Human Owner's flat, strict, sectioned `GALAX_AI_ASSIGNMENT_V1` pattern.

The following old Cline patterns are retired:

```text
- generic one-line Stage A Plan prompt
- generic one-line Stage B Act prompt
- automatic Plan-to-Act continuation
- deeply nested generic assignment as the primary prompt
- combined edit, validation, commit, and push authority
```

## 2. Non-Cline contributor preservation

This path previously also contained bounded guidance for:

```text
OpenHands Core
mini-SWE-agent
Aider
PR-Agent
Human coordination commands
```

Those non-Cline sections were not rejected by the Human Owner's Cline prompt-format decision and must not be treated as deleted or superseded merely because the Cline method changed.

Until a separately authorized migration creates new canonical non-Cline files, use the exact pinned historical content at:

```yaml
repository: ariessocia04-rgb/galax-Ai-project
ref: 0a145d7d3ff770160e528a1fe170f301f878f7d4
path: docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
allowed_historical_sections:
  - Section_4_OpenHands_Core
  - Section_5_mini_SWE_agent
  - Section_6_Aider
  - Section_7_PR_Agent
  - Section_8_Human_coordination_commands
  - Section_9_Current_command_pack_status
```

Do not use historical Section 3 for Cline.

Before using any pinned non-Cline section:

```text
verify the current repository and branch
→ verify the current exact assignment
→ verify current tool versions and command syntax
→ preserve the current Foundation and Agent 01 architecture
→ replace every placeholder
→ obtain exact Human Owner authorization
→ stop on any stale or conflicting instruction
```

A historical command is evidence, not automatic authority. If the pinned command conflicts with current repository rules, return `BLOCKED_SUPERSESSION_CONFLICT` and do not execute it.

## 3. Shared safety boundary

For every contributor:

```yaml
main_write: prohibited
force_push: prohibited
merge: prohibited_without_Human_Owner_authorization
deployment: prohibited_without_Human_Owner_authorization
secrets_access: prohibited
Agents_02_to_15: prohibited
simultaneous_writers: prohibited
unsupported_success_claims: prohibited
```

No contributor may infer authorization from vague language such as `continue`, `finish`, `improve`, or `fix everything`.

## 4. Final routing decision

```yaml
when_contributor_is_Cline:
  read: docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
  use_old_generic_Cline_prompt: false

when_contributor_is_OpenHands_mini_SWE_Aider_or_PR_Agent:
  use_pinned_non_Cline_sections_only: true
  pinned_ref: 0a145d7d3ff770160e528a1fe170f301f878f7d4
  current_repository_verification_required: true
  separate_Human_Owner_authorization_required: true
```

This router changes prompt-construction authority only. It grants no implementation, validation, commit, push, reviewer-trigger, merge, deployment, or production authority.
