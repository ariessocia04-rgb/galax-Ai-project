# Operation Length Problem Solve — Canonical Chat Continuity Protocol

**Canonical path:** `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md`  
**Status:** `ACTIVE_CANONICAL_CHAT_CONTINUITY_PROTOCOL`  
**Created:** `2026-07-21`  
**Applies to:** ChatGPT, Codex, Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Claude Code, GitHub Copilot, Jules, and any repository-aware AI or human continuing the Galax project.  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Protected branch:** `main`  
**Current authorized scope:** Governance Foundation and Agent 01 only  
**Merge/deployment:** prohibited unless separately and explicitly authorized by the human owner.

> The filename intentionally preserves the owner's requested label `OPERATIION LENGTH PROBLEM SOLVE` so that the phrase is easy to search exactly. Do not create a corrected-name duplicate or alias unless every reference is deliberately migrated under the no-exact-duplicates rule.

---

## 1. Problem this protocol solves

A long ChatGPT conversation can exceed the practical context available to the active model. A new chat, a different model, or another AI may also receive only partial history, an automatically selected subset of past context, or a lossy summary.

This creates predictable risks:

```text
- missing an earlier owner decision;
- reviving an obsolete plan;
- following the wrong branch or SHA;
- repeating completed research;
- creating duplicate files or roles;
- treating paper qualification as runtime approval;
- starting a later contributor before its entry gate;
- guessing what happened in the previous chat;
- claiming implementation or tests that never occurred;
- asking the owner questions already answered in the repository.
```

The solution is not to make one conversation infinitely long. The solution is to make the repository the durable, structured, auditable continuity source and require every new chat or AI to reconstruct the current state from it before answering or acting.

---

## 2. Official ChatGPT research findings

The following findings were verified from official OpenAI sources on `2026-07-21`.

### 2.1 Model context is finite

OpenAI documents that each model has a maximum combined token limit for input and output. When content exceeds the usable limit, the supported remedies include shortening, pre-processing, summarizing, or splitting the work into smaller segments.

Official source:

- https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-

Galax decision:

```yaml
single_chat_as_permanent_project_memory: prohibited
repository_checkpointing: required
bounded_context_reconstruction: required
```

### 2.2 Chat history memory does not retain every detail

OpenAI states that ChatGPT may reference past chats when the setting is enabled, but it does not remember every detail from past conversations. Saved memory is intended for important durable personal details, not as an exact software-project ledger.

Official sources:

- https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work
- https://help.openai.com/en/articles/8590148-memory-faq

Galax decision:

```yaml
ChatGPT_memory: convenience_context_only
ChatGPT_memory_as_exact_project_truth: prohibited
repository_as_exact_project_truth: required
```

### 2.3 ChatGPT Projects are the preferred conversation workspace

OpenAI documents that Projects keep related chats, files, and project instructions together and are intended for long-running, repeated, and evolving work. Project instructions apply inside the project and override global custom instructions. A moved chat inherits the project instructions and file context.

Official sources:

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://openai.com/academy/projects/

Galax decision:

```yaml
recommended_ChatGPT_workspace: dedicated_Galax_AI_Project
project_instructions: required
project_memory: helpful_not_authoritative
GitHub_repository: authoritative
```

### 2.4 Project-only memory improves separation but is not a substitute for Git history

OpenAI documents that project-only memory can restrict reference context to chats within the same project. It can help keep unrelated conversations out of the Galax context. It still does not replace branch state, commits, issue status, PR state, tests, hashes, or source records.

Galax decision:

```yaml
project_only_memory: recommended_when_available_for_a_new_project
branch_and_issue_verification: always_required
```

### 2.5 Current Project and file limits can change

As of the verified date, OpenAI documents unlimited Projects, with current per-project file limits varying by plan and only ten files uploadable at once. OpenAI also documents separate file-size and document-token limits. These are operational limits, not continuity guarantees, and must be revalidated when they matter.

Official sources:

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt

Galax decision:

```yaml
upload_entire_repository_as_project_files: prohibited
minimum_reference_pack_when_connector_unavailable: allowed_but_not_dynamic
GitHub_connector_or_repository_access: preferred
```

---

## 3. Core continuity rule

```text
When the owner says “length chat problem” or an equivalent trigger,
do not answer from remembered conversation fragments.
First inspect and reconstruct the exact Galax state from the repository.
```

The repository records decisions, status, movement, evidence, and the next allowed action. Chat memory may help locate the project, but it cannot override the current repository.

---

## 4. Trigger phrases

Treat any of these phrases, including spelling variations, as the same command:

```text
length chat problem
chat length problem
conversation length problem
conversation length limit
chat reached length limit
new chat continue Galax
continue from the repo
continue exact Galax flow
operation length problem solve
operatiion length problem solve
backread the repo because the chat is full
```

A message may contain only the trigger or may include another request. The trigger activates the repository reconstruction procedure before the other request is answered.

Do not respond first with a generic explanation of context windows. Do not ask, “What were we working on?” when repository access exists.

---

## 5. Mandatory immediate behavior after a trigger

The AI must perform this sequence:

```text
DETECT TRIGGER
→ identify the exact Galax repository
→ obtain repository access
→ verify current branch and branch heads
→ read canonical continuity and project records
→ inspect open PR and assignment issues
→ reconstruct the current stage
→ detect conflicts, stale records, and missing evidence
→ produce OPERATION_LENGTH_CONTINUITY_RECEIPT
→ answer or act only when safe_to_continue=true
```

### 5.1 Repository access available

Use the connected GitHub repository tools or an authorized local checkout. Read current files and repository metadata directly.

### 5.2 Repository access unavailable

Do not guess from chat memory or an old summary. Return exactly:

```yaml
status: BLOCKED_REPOSITORY_ACCESS_REQUIRED
repository: ariessocia04-rgb/galax-Ai-project
reason: exact_current_state_cannot_be_verified
safe_remedy:
  - connect_or_authorize_GitHub_repository_read_access
  - or provide_a_current_repository_checkout
  - then_rerun_the_length_chat_problem_trigger
work_started: false
claims_about_current_state: prohibited
```

A manually uploaded snapshot may support reading, but it cannot prove current branch, issue, PR, or live repository state unless its commit SHA is independently verified.

---

## 6. Mandatory reading order for continuity reconstruction

Read every item completely where applicable, in this order:

1. `README.md`
2. `AGENTS.md`
3. `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md`
4. `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
5. The canonical audit target named by the alias above
6. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
7. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
8. Every applicable file under `docs/rules/`
9. Every applicable file under `docs/plan/`
10. `docs/sources/SOURCE_INDEX.md`
11. Exact source cards for every active framework, LLM, tool, gateway, contributor, and agent involved
12. The exact current agent research records under `docs/research/agents/`
13. The current authorized prompt or exact assignment
14. Draft PR `#1`, or its current replacement if the repository later records one
15. Current assignment issues, presently `#2` through `#6`, or their current replacements
16. Current research and implementation branch comparison
17. Current `main` head, research head, implementation head, open PR head, and assignment starting SHA

If a path has been superseded, preserve its historical evidence but follow the higher-priority canonical replacement.

---

## 7. Canonical decision priority

```text
README current readiness
→ this continuity protocol for reconstruction procedure
→ final conflict audit and its canonical target
→ Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ validated LLM routing and assignment records
→ source index and exact source cards
→ exact current GitHub assignment
→ historical records
→ ChatGPT memory or old conversation summary
```

Rules:

- Chat memory never overrides a repository record.
- An old assistant summary never overrides the current branch or issue.
- A lower-priority file cannot reactivate an explicitly superseded design.
- A materially new owner decision received in chat must be recorded in the repository before it is treated as durable cross-chat truth.
- When two active records conflict and priority does not resolve them, return `BLOCKED_SUPERSESSION_CONFLICT`; do not choose by intuition.

---

## 8. Current Galax movement ledger

This ledger records the important decision movement that led to the current path. It is not a verbatim chat transcript. Raw conversation wording is intentionally not the canonical project record.

### `MOVE-001` — External contributor qualification

```yaml
selected_for_controlled_trial:
  Cline: 86
  OpenHands_Core: 84
  mini_SWE_agent: 83
  Aider: 82
  PR_Agent: 82
declined_or_deferred:
  OpenCode: 74
  goose: 77
fully_qualified: 0
score_meaning: Galax_paper_compatibility_not_accuracy
```

Canonical records:

- `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
- `docs/sources/EXTERNAL_AI_CONTRIBUTOR_INDEX.md`
- individual contributor source cards

### `MOVE-002` — Contributor sequencing and permission boundary

```text
Cline primary supervised work
→ Aider one exact reproducible repair when needed
→ mini-SWE-agent isolated patch comparison when needed
→ OpenHands Docker-isolated blocker reproduction when needed
→ PR-Agent read-only review
→ human decision
```

```yaml
simultaneous_overlapping_writers: prohibited
direct_agent_to_agent_MCP_mesh: prohibited
main_write: prohibited
merge: prohibited
deployment: prohibited
```

### `MOVE-003` — Foundation implementation branch and assignments

```yaml
research_branch: agent/agent-01-tool-inspection
implementation_branch: implementation/foundation-agent-01
Cline_assignment: issue_2
OpenHands_assignment: issue_3
mini_SWE_assignment: issue_4
Aider_assignment: issue_5
PR_Agent_assignment: issue_6
```

The exact starting SHA must always be read dynamically from the active assignment and verified against the implementation branch head. Do not trust a SHA copied from an old conversation.

### `MOVE-004` — Agent 01 architecture conflict reconciliation

The direct-Agent-tool design was superseded for this exact Foundation architecture.

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  calls_per_run: 1

engineering_manager:
  tools: []
  direct_tool_calls: 0
  receives: trusted_RepositoryPreflightResult
  produces: AgentTaskResult

Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_router_per_branching_stage: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Canonical record:

- `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`

### `MOVE-005` — Current authorized stage before this protocol

```yaml
current_stage: CLINE_PLAN_ONLY_READY_FOR_HUMAN_LAUNCH
repository_implementation: NOT_PERFORMED
controlled_trials_run: false
live_provider_tests_run: false
live_GitHub_permission_validation_run: false
Agent_01_runtime_approved: false
Agents_02_to_15_enabled: false
production_ready: false
```

The active source for the exact plan-only SHA and command is GitHub Issue `#2`.

### `MOVE-006` — Conversation-length continuity protocol

```yaml
problem: long_or_new_chat_may_lack_exact_history
solution: mandatory_repo_first_state_reconstruction
canonical_file: docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
raw_chat_as_source_of_truth: false
repository_as_source_of_truth: true
```

---

## 9. Current-stage state machine

The AI must classify the current stage from repository evidence. Use the first stage whose conditions are fully satisfied.

### `RESEARCH_OR_RECONCILIATION_REQUIRED`

Use when canonical conflicts remain unresolved, mandatory files are missing, or research and implementation branches are not in the expected relationship.

### `CLINE_PLAN_ONLY_READY_FOR_HUMAN_LAUNCH`

Required evidence:

```text
- Issue #2 or its replacement says plan-only ready;
- assignment starting SHA matches implementation branch head;
- research and implementation branches are synchronized as required;
- no blocking canonical conflict remains;
- no plan-only run output has been accepted yet.
```

Allowed next action: launch Cline in plan-only mode with auto-approval disabled.

### `CLINE_PLAN_OUTPUT_PENDING_HUMAN_REVIEW`

Use only when an actual Cline plan-only output exists and the human has not accepted or rejected it.

Allowed next action: compare the output against the assignment and canonical records.

### `CLINE_ACT_NOT_AUTHORIZED`

Use whenever there is no explicit recorded human authorization for Act mode. A valid plan by itself does not authorize implementation.

### `CLINE_ACT_AUTHORIZED`

Required evidence:

```text
- accepted plan artifact;
- exact allowed paths;
- exact commands and tests;
- explicit human Act authorization;
- clean/specified worktree state;
- matching starting SHA;
- no new blocker.
```

### `FOUNDATION_IMPLEMENTATION_IN_PROGRESS`

Use only when actual implementation files, command evidence, and current branch changes exist under an authorized Act assignment.

### `AIDER_EXACT_REPAIR_READY`

Use only when one reproducible failure, exact command, failure output, starting SHA, editable files, and success command are recorded.

### `MINI_SWE_COMPARISON_READY`

Use only when one exact bounded issue and isolated comparison assignment exist.

### `OPENHANDS_REPRODUCTION_READY`

Use only when a real Cline blocker or explicit reproduction assignment exists with a Docker-isolated workspace contract.

### `PR_AGENT_REVIEW_READY`

Use only when a stable draft PR contains actual Foundation implementation and evidence reports.

### `HUMAN_DECISION_PENDING`

Use when a valid review or human-review request exists and only the human owner can approve, revise, stop, merge, or accept risk.

### `BLOCKED_*`

Use an exact blocker whenever a required repository, branch, SHA, permission, credential, dependency, profile, sandbox, test, or evidence condition is absent.

Never skip directly to a later state because it appears more useful.

---

## 10. Mandatory continuity receipt

Before giving a substantive project answer or performing a repository mutation after a length trigger, return or internally construct this exact evidence structure and show its important fields to the owner:

```yaml
OPERATION_LENGTH_CONTINUITY_RECEIPT:
  trigger_detected:
  reconstructed_at_utc:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:
  default_branch:
  main_head_sha:
  research_branch:
  research_head_sha:
  implementation_branch:
  implementation_head_sha:
  research_and_implementation_comparison:
  active_pr:
    number:
    state:
    draft:
    merged:
    head_branch:
    head_sha:
    base_branch:
  active_assignments:
    - issue_number:
      contributor:
      state:
      starting_sha:
      entry_gate_satisfied:
  files_read:
    - path:
      blob_sha:
      authority:
  canonical_decisions_confirmed: []
  superseded_decisions_rejected: []
  last_confirmed_movement:
  current_stage:
  next_allowed_action:
  prohibited_next_actions: []
  unresolved_blockers: []
  assumptions: []
  facts_from_repository: []
  facts_only_from_chat_memory: []
  safe_to_continue: false
```

Validation rules:

```text
- safe_to_continue cannot be true when repository access is missing;
- safe_to_continue cannot be true when a mandatory file was not read;
- safe_to_continue cannot be true when starting SHA mismatches;
- safe_to_continue cannot be true when an unresolved canonical conflict exists;
- facts_only_from_chat_memory must be empty for any decision that changes repository work;
- assumptions must never be silently converted into facts;
- the next action must match the current stage.
```

---

## 11. Response contract for the new chat or AI

After reconstruction, answer the owner in this order:

```text
1. Confirmed current stage.
2. Last completed movement.
3. Exact next allowed action.
4. Exact blocked or prohibited actions.
5. Repository/branch/issue/PR evidence.
6. Any true conflict or missing proof.
7. Perform the requested task only if it is authorized by the resolved stage.
```

Language and clarity rules:

- Use direct Tagalog with precise technical English terms where helpful.
- Do not use vague phrases such as `continue the project`, `fix everything`, or `should be okay` without exact scope.
- Do not repeat questions already answered by the repository.
- Do not claim to have read a file that was not retrieved.
- Do not claim a contributor is working merely because an issue exists.
- Separate `documented`, `implemented`, `tested`, `live-tested`, `approved`, `merged`, `deployed`, and `production-ready`.
- When a fact changed after the last repository record, verify it from the current authoritative source and record the result before using it as a durable project decision.

---

## 12. Rules for recording new conversation decisions

A new owner instruction in chat is not yet durable cross-chat state until it is recorded in the repository.

For every material decision:

```text
owner instruction
→ inspect current canonical records
→ determine whether it adds, updates, or supersedes a decision
→ update the existing canonical file when the responsibility is already represented
→ create a new file only when the record has a materially distinct purpose
→ update README/AGENTS/indices only where discovery requires it
→ update active issue and PR state when affected
→ synchronize the implementation branch when required
→ verify branch comparison
→ report exact commit SHA and remaining blockers
```

Material decisions include:

```text
- scope change;
- architecture change;
- role or contributor change;
- branch or assignment change;
- permission change;
- model/provider/tool change;
- test or evidence requirement change;
- current-stage transition;
- human approval or rejection;
- blocker resolution;
- merge or deployment decision.
```

Do not store raw private chain-of-thought. Store only observable decisions, rationale summaries, evidence, commands, results, hashes, and blockers.

---

## 13. No-duplication behavior

This file owns only:

```text
- conversation-length trigger handling;
- repository continuity reconstruction;
- the movement ledger;
- current-stage determination;
- continuity receipt schema;
- new-chat response and checkpoint behavior.
```

It does not replace:

```text
README.md
AGENTS.md
Foundation Flow execution contract
CrewAI remediation blueprint
external contributor execution plan
source cards
exact platform command pack
GitHub assignment issues
```

When another file already owns a detailed design, link to it and record only the continuity-relevant decision here. Do not copy the whole design into another file.

An exact duplicate may be removed only under `docs/rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md`. A near duplicate or historical record must not be deleted automatically.

---

## 14. Required checkpoint after every material stage transition

When the current stage changes, the responsible repository-aware AI must update all affected canonical surfaces in one coherent handoff:

```text
1. Update the owning canonical plan/rule/decision file.
2. Update the active assignment issue state and starting or ending SHA.
3. Update the draft PR body when its status summary changed.
4. Update this movement ledger only when a new material movement occurred.
5. Fast-forward or otherwise synchronize the implementation branch when authorized and safe.
6. Compare research and implementation branches.
7. Verify no direct main write occurred.
8. Report the exact new head SHA.
```

Do not update this file for every minor wording change or every ordinary commit. Update it only when the continuity state, decision path, trigger procedure, or stage changes.

---

## 15. Recommended ChatGPT Project setup

Create or use one dedicated ChatGPT Project named:

```text
Galax AI — Canonical Repository Continuity
```

Recommended setup:

```text
1. Use project-only memory when available and appropriate.
2. Move the current Galax conversation into the Project when the UI permits.
3. Connect the GitHub repository or ensure the new chat can access it.
4. Do not upload the entire repository as Project files.
5. Keep Project instructions short and point to this canonical file.
6. Start a new Project chat before the current chat becomes unusably long.
7. In the new chat, say: “length chat problem — continue exact Galax flow from repo.”
```

### Project Instructions text

Paste this into the Galax ChatGPT Project instructions:

```text
For every Galax request, treat GitHub repository ariessocia04-rgb/galax-Ai-project as the authoritative project record. When the user says “length chat problem,” “conversation length problem,” “continue exact Galax flow,” or an equivalent phrase, do not rely on remembered chat fragments and do not ask what the previous work was. Access the repository, read README.md, AGENTS.md, and docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md, then follow the complete mandatory reading order in that file. Verify the current branch heads, draft PR, active assignment issues, canonical decisions, current stage, and exact next allowed action. Produce an OPERATION_LENGTH_CONTINUITY_RECEIPT before acting. Never guess missing state, never revive superseded records, never create duplicate plans, never claim implementation or tests without evidence, never write to main, and never proceed beyond the currently authorized stage.
```

Project memory is helpful context only. The repository remains authoritative.

---

## 16. Minimal new-chat command

The owner can use this exact command in a new ChatGPT chat or another repository-aware AI:

```text
Length chat problem. Open ariessocia04-rgb/galax-Ai-project and follow docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md exactly. Reconstruct the current Galax state from README, AGENTS, canonical plans/rules, current branch heads, PR, and assignment issues. Return the OPERATION_LENGTH_CONTINUITY_RECEIPT, tell me the exact current stage and next allowed action, then continue only the authorized work. Do not guess, do not duplicate, and do not rely on old chat memory as project truth.
```

---

## 17. Current continuity status

```yaml
protocol_documented: true
ChatGPT_Project_recommended: true
repository_first_reconstruction_required: true
raw_chat_transcript_required: false
exact_decision_movement_ledger_required: true
current_stage_at_creation: CLINE_PLAN_ONLY_READY_FOR_HUMAN_LAUNCH
current_starting_SHA_source: active_GitHub_Issue_2
Cline_Act_authorized: false
repository_implementation: NOT_PERFORMED
controlled_trials_run: false
external_contributors_fully_qualified: 0
Agent_01_runtime_approved: false
Agents_02_to_15_enabled: false
production_ready: false
```

The exact branch heads, PR head, and assignment starting SHA must be read dynamically whenever this protocol is triggered.
