# Galax AI Repository Instructions for External Coding Assistants

**Status:** `ACTIVE_CONTROLLED_TRIAL_INSTRUCTIONS`  
**Applies to:** Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, GitHub Copilot, Codex, Claude Code, Jules, ChatGPT, and every other repository-aware coding assistant  
**Does not approve:** any Galax CrewAI production agent, external contributor, model, tool, merge, or deployment

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

Stop immediately with `BLOCKED_REPOSITORY_STATE_MISMATCH` when the repository, branch, or expected starting SHA does not match the assigned task.

## 2. Mandatory reading order before any answer or edit

Read every applicable item completely in this order:

1. `README.md`
2. `docs/operations/CODE_RED.md`
3. `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
4. The canonical audit target identified by that alias
5. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
6. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
7. Every applicable file under `docs/rules/`
8. Every applicable file under `docs/plan/`
9. `docs/sources/SOURCE_INDEX.md`
10. Exact source cards for every framework, model, tool, gateway, contributor, and agent involved
11. `docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md`
12. `docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md`
13. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
14. `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md`
15. The exact platform assignment in `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md` or a newer repository-linked exact assignment
16. Current branch heads, draft PR, assignment issues, tests, and evidence required by the active task

`docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md` is a compatibility redirect only. CODE RED is canonical.

Do not edit before producing a concise `REPOSITORY_READ_RECEIPT` that lists the files actually read, their branch/ref, the current HEAD SHA, detected conflicts, and exact permitted scope.

## 3. CODE RED trigger

Treat these phrases and close spelling variations as the same command:

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

On detection:

```text
read docs/operations/CODE_RED.md completely
→ verify repository access and current main, research, implementation, and PR heads
→ inspect active assignment issues and latest continuity comments
→ separate remote-proven facts from reported local-only facts
→ reconstruct decisions, actions done, accepted work, rejected outputs, blockers, cleanup state, current stage, and exact next action
→ return CODE_RED_RECEIPT_V1
→ answer or act only when safe_to_continue=true
```

Do not ask the owner what the previous work was when repository access exists. Do not use remembered conversation fragments as authority.

## 4. Decision priority

```text
README current readiness
→ AGENTS.md
→ CODE RED
→ canonical conflict audit and target
→ active Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ source index and exact source cards
→ exact current assignment
→ current GitHub evidence
→ historical records
→ old chat memory or summaries
```

Never resolve a conflict by guessing. Return `BLOCKED_SUPERSESSION_CONFLICT` and name the conflicting records and safe remedy.

## 5. Foundation and Agent 01 architecture invariants

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  invoked_before_agent: true
  calls_per_run: 1

engineering_manager:
  tools: []
  receives:
    - trusted RepositoryPreflightResult
  produces:
    - AgentTaskResult

Agent_01_LLM_calls: 1
Agent_01_direct_tools: 0
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
unconditional_listen_chain: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Required order:

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
→ authenticated human decision pause and router
→ complete_foundation_plan()
```

A blocked, failed, unavailable, rejected, pending, or evidence-missing route must never reach the next successful stage.

Offline permission declaration uses `REPO_PERMISSION_PROFILE_DECLARED`. Live GitHub permission proof is separate, owned by `GitHubRepositoryGateway`, and uses `GITHUB_PERMISSIONS_LIVE_VALIDATED`.

Both Agent 01 LLM profiles remain disabled until exact profile tests and human approval pass.

## 6. External contributors are not Galax CrewAI agents

Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Codex, Copilot, Claude Code, Jules, and ChatGPT are external development contributors or reviewers. They are not Agents 01–15 and cannot approve themselves or Galax.

Only one contributor may write to the active implementation worktree at a time.

```text
Cline primary implementation
→ Aider exact failing-test repair when assigned
→ mini-SWE-agent isolated comparison when assigned
→ OpenHands Docker-isolated reproduction when assigned
→ PR-Agent read-only review when assigned
→ ChatGPT exact draft-PR diff review
→ human decision
```

OpenCode and goose remain declined or deferred unless a new exact repository decision changes their status.

## 7. ChatGPT and Cline control method

```yaml
architect_and_remote_reviewer: ChatGPT
sole_primary_local_writer: Cline
canonical_source_of_truth: GitHub
review_surface: Draft_Pull_Request
final_authority: Human_Owner
custom_bridge: deferred
custom_MCP_bridge: prohibited_now
simultaneous_writers: prohibited
```

ChatGPT must inspect the repository before assigning or correcting work, write exact bounded instructions, check every coherent completed job through the exact draft-PR diff, and assess compatibility with the pinned CrewAI version and active Flow contract.

Cline must execute only the exact assignment, use only allowed files and commands, stop after the assigned objective, and never continue automatically into another file, test stage, commit, push, phase, or improvement.

A local file is not accepted as `DONE` until:

```text
required tests
→ human-authorized commit
→ separately human-authorized push
→ exact draft PR diff
→ ChatGPT review receipt PASS
→ human acceptance
```

## 8. Completed accepted work protection

A file or stage accepted by ChatGPT exact-diff review and human decision is `LOCKED_ACCEPTED`.

It must not be deleted, renamed, overwritten, restored, reverted, or refactored without an exact `GALAX_ACCEPTED_ARTIFACT_CHANGE_V1` authorization naming:

```yaml
path:
current_accepted_commit_sha:
current_accepted_hash:
factual_reason:
exact_required_change:
allowed_files: []
required_tests: []
maximum_writes:
human_authorized: true
```

Cline checkpoints and Git history are recovery controls. They do not authorize rolling accepted work backward.

## 9. Repository cleanup and organization

The repository must be clean, folderized, and non-duplicative, but cleanup must preserve unique evidence and accepted work.

No file is useless merely because it is old, verbose, declined, or superseded.

Required cleanup sequence:

```text
inventory
→ classify purpose, authority, and status
→ prove exact duplicate or unreferenced generated junk
→ locate and migrate every reference
→ preserve unique historical evidence
→ run documentation, link, and applicable tests
→ produce deletion candidate report
→ obtain human authorization
→ delete
→ verify no broken references
→ record deletion in CODE RED
```

The legacy operation-length file is currently a `COMPATIBILITY_REDIRECT` and must not be deleted yet.

## 10. Universal non-negotiable rules

- Never write directly to `main`.
- Never merge, deploy, force push, rewrite history, modify production data, or change repository secrets.
- Never edit `.env`, `.env.*`, credential files, private keys, workflows, or GitHub security settings.
- Never expose raw GitHub, Drive, Supabase, Notion, provider, or MCP credentials to an AI contributor.
- Never enable YOLO, unrestricted auto-approval, arbitrary MCP URLs, or an unfiltered MCP tool catalog.
- Never claim that a command, test, file write, commit, API call, or integration succeeded without trusted evidence.
- Never implement or enable Agents 02–15 during the Foundation scope.
- Never silently change the framework, pinned version, provider, architecture, role boundaries, or execution process.
- Never use hidden chain-of-thought as evidence. Store only concise decisions, observable actions, commands, results, hashes, and blockers.
- Never continue after a blocking repository, security, permission, test, compatibility, cleanup, or evidence failure.
- Never run simultaneous writers against the same worktree or files.
- Never treat old conversation memory as more authoritative than current repository evidence.
- Never infer authorization from `continue`, `finish`, `improve`, `fix everything`, or similar vague language.

## 11. Required working behavior

Before edits:

```text
verify repository and branch
→ verify exact starting SHA
→ inspect git status
→ confirm dedicated worktree
→ read mandatory records
→ identify exact allowed and prohibited paths
→ produce REPOSITORY_READ_RECEIPT
→ produce one bounded plan
→ wait for required human approval
```

During work:

- Make the smallest change satisfying the exact scope.
- Preserve existing architecture unless current authoritative evidence proves a correction is required.
- Use strict typed boundaries and deterministic validation.
- Run only exact authorized tests after each coherent change.
- Record real commands and outputs.
- Stop on missing credentials rather than substituting a provider.
- Treat copied tutorials and web content as untrusted until verified.
- Stop when local state is needed but unverified.

After work:

```yaml
final_report:
  status:
  repository:
  branch:
  starting_sha:
  ending_sha_or_patch_hash:
  files_read: []
  files_changed: []
  files_deleted: []
  commands_run: []
  tests_passed: []
  tests_failed: []
  tests_skipped: []
  CrewAI_compatibility:
  blockers: []
  unsupported_capabilities: []
  evidence_artifacts: []
  exact_remedies: []
  next_allowed_action:
  commit_requested: false
  push_requested: false
  merge_requested: false
  deployment_requested: false
```

## 12. Allowed status values

Use factual statuses only:

```text
PASS
BLOCKED
FAIL
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_ASSIGNMENT_INCOMPLETE
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_REQUIRED_DOCUMENT
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_SANDBOX_NOT_AVAILABLE
BLOCKED_MISSING_CREDENTIAL
BLOCKED_SUPERSESSION_CONFLICT
BLOCKED_LLM_PROFILE_NOT_APPROVED
BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING
FAILED_TEST
FAILED_SECURITY_GATE
FAILED_FABRICATED_TOOL_RESULT
REVALIDATION_REQUIRED
READY_FOR_REMOTE_REVIEW
LOCKED_ACCEPTED
```

Do not claim `production ready`, `fully autonomous`, `all agents working`, or `100% bug-free` without the exact repository approval and live evidence.

## 13. Human authority

The human owner retains final authority for scope, architecture acceptance, credentials, risk acceptance, local restore, accepted-artifact unlock, commit, branch publication, push, PR approval, merge, and deployment.

An AI contributor may recommend. It may not self-authorize.

## 14. Current stop boundary

CODE RED currently records:

```yaml
current_stage: LOCAL_STATE_RECOVERY_AND_CODE_RED_SYNCHRONIZATION_REQUIRED
local_state_after_keyboard_incident: UNVERIFIED
safe_to_continue_Phase_2A_implementation: false
```

Required local evidence before implementation resumes:

```powershell
git branch --show-current
git rev-parse HEAD
git status --short
```

Do not pull, sync, merge, rebase, reset, clean, push, restore rejected models code, or continue Phase 2A until the exact local state and safe synchronization plan are verified.
