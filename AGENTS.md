# Galax AI Repository Instructions for External Coding Assistants

**Status:** `ACTIVE_CONTROLLED_TRIAL_INSTRUCTIONS`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Applies to:** ChatGPT, Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Codex, GitHub Copilot, Claude Code, Jules, and every repository-aware coding assistant  
**Does not approve:** any Galax CrewAI production agent, external contributor, model, tool, merge, or deployment  
**Final authority:** Human Owner

## 1. Repository identity

```yaml
repository: ariessocia04-rgb/galax-Ai-project
protected_branch: main
research_branch: agent/agent-01-tool-inspection
foundation_implementation_branch: implementation/foundation-agent-01
framework_target: CrewAI_1.15.4
python_target: ">=3.10,<3.14"
current_scope: governance_foundation_and_Agent_01_only
Agents_02_to_15: prohibited
production_ready: false
```

Stop with `BLOCKED_REPOSITORY_STATE_MISMATCH` when the exact assigned repository, branch, or expected starting SHA does not match.

## 2. Canonical authority order

```text
README.md current readiness
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
→ canonical conflict audit and target
→ active Foundation / Agent 01 execution contract
→ active CrewAI remediation blueprint
→ active rules and plans
→ source index and exact source cards
→ exact current assignment
→ current GitHub branch / PR / issue / commit / test evidence
→ historical records
→ old chat memory or summaries
```

Repository evidence overrides stale conversation memory.
No lower-priority record may reactivate a superseded architecture or weaken a current Human Owner boundary.

## 3. Mandatory reading behavior

Before answering or acting, read only the exact applicable authority chain required by the current task.

Minimum for implementation work:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
→ docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
→ docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
→ docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
→ exact current assignment / branch / HEAD / evidence required by the task
```

Follow exact mandatory references from those records, but do not scan the whole repository by default.
The Context Engineer may reduce duplicate reads for ChatGPT only when exact repository/task identities are verified unchanged. It may not suppress a mandatory selected-skill read.

## 4. CODE RED trigger

Treat these and close spelling variations as the same recovery command:

```text
CODE RED
code red
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
```

Required behavior:

```text
verify repository access and current relevant heads
→ read README.md
→ read AGENTS.md
→ read docs/operations/CODE_RED.md completely
→ reconstruct remote-proven vs local-only state
→ recover completed / rejected / blocked / locked / pending work
→ identify one exact current stage and next allowed action
→ return the required recovery receipt
→ act only when safe_to_continue=true
```

Do not ask the Human Owner to reconstruct repository-backed history when repository access exists.

## 5. Human Owner's canonical ChatGPT → Cline implementation workflow

For active CrewAI remediation-blueprint implementation, the default operating model is:

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / task
   ↓
Cline
→ executes the command locally
→ edits/saves only authorized implementation
→ runs only separately authorized validation
   ↓
ChatGPT
→ reviews Cline's evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
   ↓
Human Owner
→ authorizes the exact Git stage
   ↓
Cline
→ commit
→ separately authorized push
   ↓
GitHub
   ↓
ChatGPT
→ independently reviews exact remote diff/evidence
   ↓
Human Owner
→ final acceptance
```

Canonical control plan:

```text
docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
```

A ChatGPT `PASS` is an evidence-review result. It is not automatic permission to commit or push.

## 6. Canonical execution-role separator

Read and follow:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

### Normal ChatGPT role for CrewAI implementation

```yaml
ChatGPT:
  role: repository_aware_architect_supervisor_reviewer
  direct_CrewAI_implementation_writer_by_default: false
  direct_CrewAI_implementation_commit_executor_by_default: false
  direct_CrewAI_implementation_push_executor_by_default: false
  technical_fallback_executor: true_only_after_Skill_12_PASS_and_Human_Owner_authorization
  reviews_local_Cline_evidence: true
  reviews_exact_remote_diff: true
  final_authority: false
```

Without a valid Skill 12 fallback gate, if ChatGPT attempts to edit, save, validate, commit, push, or publish active CrewAI blueprint-owned technical work, source, tests, dependencies, or implementation branch state:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

### Cline role for normal CrewAI implementation

```yaml
Cline:
  role: primary_local_executor_for_active_CrewAI_remediation_blueprint
  implementation_writer: true_when_exactly_authorized
  validation_executor: true_when_separately_authorized
  implementation_commit_executor: true_when_separately_authorized
  implementation_push_executor: true_when_separately_authorized
  self_authorization: prohibited
  automatic_next_task: prohibited
  automatic_scope_expansion: prohibited
```

Cline must use Skill 2 controls and a current Skill 10 `PASS_CLINE_BLUEPRINT_ONLY` gate before a real normal implementation task is issued.

## 7. Verified ChatGPT technical fallback — Skill 12

ChatGPT may temporarily become the exact technical executor only when all required evidence and authorization exist.

```yaml
Skill_12_minimum_requirements:
  exact_current_technical_action_known: true
  one_of:
    - Cline_capability_limit_factually_proven
    - Cline_repeated_material_command_mismatch_after_one_exact_corrected_retry_proven
  ChatGPT_current_exact_tool_capability_proven: true
  Human_Owner_explicit_fallback_authorization: true
  exact_authorized_stages_known: true
  LOCKED_ACCEPTED_conflict: false
  unrelated_scope_expansion: false
  simultaneous_overlapping_writer: false
  Skill_12_gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake does not authorize takeover.

Fallback may cover only the exact authorized stage(s), such as edit/save, validation, commit, or remote publication when current ChatGPT tools actually support them.

The Human Owner may explicitly combine multiple fully bounded stages in one authorization. Vague language does not combine stages.

After ChatGPT fallback work is remotely verified:

```text
ChatGPT-created work becomes current repository truth
→ Cline must preserve it
→ Cline must not redo, overwrite, revert, or recreate it without new Human Owner authority
→ Cline continues from the new verified state
```

If Cline's local workspace requires reconciliation, ChatGPT must prepare the exact safe Cline synchronization task. The Human Owner approves/rejects; the Human Owner is not required to execute Git commands manually.

## 8. ChatGPT-only supervisory repository work

The Human Owner permits ChatGPT to maintain its own supervisory control layer directly through the connected GitHub app without Cline.

```yaml
ChatGPT_direct_supervisory_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_ChatGPT_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

These requests route to Skill 9.

Cline is prohibited from editing/saving/committing/pushing those ChatGPT-owned supervisory targets:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Do not broaden Skill 9 into generic documentation, plans, research, technical contracts, CrewAI blueprint files, source, tests, dependencies, workflows, or implementation Git actions.

## 9. ChatGPT-only continuity and achievement work

Skill 5 remains the exact bounded exception for:

```yaml
ChatGPT_direct_continuity_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

Cline is not required and must not be tasked merely to save those continuity records.

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
main_write: prohibited
merge_authorized: false
exact_evidence_required: true
exact_Asia_Manila_timestamp_required: true
no_duplicate_event: required
```

## 10. Owner rule / skill requirements and feasibility — Skill 11

When the Human Owner wants a new or changed skill/rule but the exact requirement, restrictions, feasibility, or repository destination is unclear:

```text
Skill 11
→ ask only necessary questions in simple Tagalog
→ never ask the Human Owner to code, edit files, write YAML/JSON, or run terminal/Git commands
→ verify current repository constraints
→ perform bounded current web fact-check using official/primary sources before feasibility conclusion
→ classify POSSIBLE / POSSIBLE_WITH_CONSTRAINTS / NOT_POSSIBLE_AS_REQUESTED
→ if not possible, identify factual blocker and smallest practical remedy/alternative
→ recommend the correct repository destination
→ produce the final repository-ready specification in English
→ obtain Human Owner decision
→ separate Skill 9 write cycle
```

If the Human Owner already provided a complete exact supervisory requirement, do not ask redundant questions; route to Skill 9.

## 11. Zero-coding-owner rule

The Human Owner is the final authority but is not expected to perform coding work.

```yaml
prohibited:
  - ask_owner_to_write_or_patch_code
  - ask_owner_to_edit_repository_files_manually
  - ask_owner_to_type_terminal_or_Git_commands_when_an_available_authorized_actor_can_do_it
  - ask_owner_to_resolve_code_or_merge_conflicts_manually
```

If any available authorized contributor/tool can perform the work:

```text
explain exact bounded action in plain language
→ ask Human Owner for authorization
→ capable actor performs the work
```

If no available actor can do it, verify the blocker and research/recommend the smallest feasible remedy. Do not offload coding to the Human Owner.

## 12. Consequential-action separation

For normal CrewAI implementation:

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ VALIDATION
VALIDATION ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE_REVIEW
REMOTE_REVIEW ≠ HUMAN_ACCEPTANCE
HUMAN_ACCEPTANCE ≠ MERGE
MERGE ≠ DEPLOY
```

Every stage requires exact current authority unless an exact Human Owner authorization explicitly combines a fully bounded set of stages.

## 13. Active Foundation architecture invariants

The current canonical Foundation direction remains unchanged by these repository-supervision rules:

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
repository_preflight_tool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
Agent_01_output: AgentTaskResult
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_routers_for_every_branch: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Required high-level order remains:

```text
validate_run_manifest()
→ explicit router
→ check_external_preflight_tool_availability()
→ explicit router
→ invoke_repository_preflight_tool()
→ explicit router
→ check_llm_profile_readiness()
→ explicit router
→ run_agent_01_evaluation()
→ validate supported claims
→ explicit router
→ build_human_review_request() using pure Python/Pydantic
→ authenticated human decision pause/router
→ complete_foundation_plan()
```

Blocked, failed, unavailable, rejected, pending, or evidence-missing routes must not reach the next successful stage.
Agents 02–15 remain prohibited until exact live authority changes.

## 14. External development contributors

External coding assistants are development contributors, not Galax CrewAI Agents 01–15.

```yaml
Cline: primary_supervised_CrewAI_blueprint_implementer
Aider: one_exact_reproducible_failure_repair_when_assigned
mini_SWE_agent: isolated_patch_comparison_when_assigned
OpenHands_Core: Docker_isolated_blocker_reproducer_when_assigned
PR_Agent: read_only_PR_reviewer_when_assigned
ChatGPT: architect_supervisor_exact_remote_diff_reviewer_and_owner_authorized_Skill_12_fallback_executor
Human_Owner: final_authority
```

Only one overlapping implementation writer may act at a time.
Other assistants receive no default implementation authority merely because they can access the repository.

## 15. `LOCKED_ACCEPTED` protection

A file or coherent stage becomes `LOCKED_ACCEPTED` only after the applicable evidence chain, exact remote review, and Human Owner acceptance.

Locked work must not be rewritten, deleted, renamed, restored over, refactored, or repeatedly rerun without an exact accepted-artifact unlock/change authorization.

Neither Skill 9, Skill 12, nor Cline's implementation role bypasses `LOCKED_ACCEPTED`.

## 16. Repository cleanup

Cleanup remains evidence-driven:

```text
inventory
→ classify purpose/authority/status
→ prove duplicate or unreferenced generated junk
→ locate and migrate references
→ preserve unique historical evidence
→ run applicable checks
→ obtain Human Owner deletion authorization
→ delete
→ verify references
→ record result
```

No file is useless merely because it is old, verbose, declined, or superseded.

## 17. Universal non-negotiable rules

- Never write directly to `main`.
- Never force push or rewrite history.
- Never merge or deploy without separate explicit Human Owner authorization.
- Never modify secrets, credentials, private keys, production data, or GitHub security settings by inference.
- Never claim a command, test, edit, commit, push, API call, or integration succeeded without trusted evidence.
- Never enable Agents 02–15 without exact live authority.
- Never silently change the pinned framework, provider, architecture, role boundary, or process.
- Never use hidden chain-of-thought as repository evidence.
- Never continue after a blocking repository, security, permission, compatibility, test, or evidence failure.
- Never run simultaneous overlapping implementation writers.
- Never treat stale chat memory as more authoritative than current repository evidence.
- Never infer permission from vague language such as `continue`, `finish`, `improve`, or `fix everything`.
- Never let ChatGPT take over a Cline CrewAI implementation stage without a current Skill 12 PASS and explicit Human Owner fallback authorization.
- Never let Cline take over ChatGPT supervisory/continuity maintenance.
- Never ask the Human Owner to perform manual coding as a substitute for an available authorized AI/tool.

## 18. Required assignment behavior

Every external contributor assignment must be bounded with, as applicable:

```yaml
assignment_id:
contributor:
repository:
workspace:
starting_branch:
starting_sha:
objective:
exact_scope:
required_reading: []
allowed_paths: []
prohibited_paths: []
allowed_commands: []
prohibited_commands: []
required_tests: []
stop_condition:
human_approval_required_for: []
```

Missing material identity or authority blocks execution.

## 19. Final role contract

```text
Normal CrewAI implementation
→ ChatGPT commands and reviews
→ Cline executes
→ Human Owner controls consequential gates
→ Cline commits/pushes when authorized
→ GitHub becomes remote evidence
→ ChatGPT independently reviews exact remote diff
→ Human Owner final acceptance

Cline cannot perform exact action or repeats a material command mismatch after one corrected retry
→ verify ChatGPT exact capability
→ ask Human Owner fallback authorization
→ Skill 12
→ ChatGPT performs only authorized exact technical stage(s)
→ verify result
→ Cline continues from that new repository state

ChatGPT skill/router/context/supervisory rule maintenance
→ Skill 9
→ ChatGPT direct bounded governance-branch write
→ Cline blocked

length problem / achievement
→ Skill 5
→ ChatGPT direct bounded continuity write
→ Cline blocked

new or unclear skill/rule requirements
→ Skill 11
→ ask in Tagalog
→ fact-check feasibility
→ recommend remedy/location
→ produce final English specification
→ Skill 9 after Human Owner approval

No capable automated actor/tool
→ do not ask Human Owner to code manually
→ verify blocker/remedy
→ recommend next feasible option
→ ask only for Human Owner decision/authorization
```
