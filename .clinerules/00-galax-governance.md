# Galax Cline Governance Rule

This rule is always active for the Galax repository.

## Mandatory context

- Read `README.md` and `AGENTS.md` first and obey their decision priority.
- Read `docs/operations/CODE_RED.md` completely.
- Treat `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md` only as a compatibility redirect.
- Read `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md` completely.
- Read `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`.
- Read `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md` completely.
- Use only the Cline assignment in `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md` or a newer exact repository-linked assignment that follows `GALAX_AI_ASSIGNMENT_V1`.
- Read the reconciled authorized Foundation prompt before planning implementation.
- Where an older record conflicts about direct Agent 01 tool ownership or `result_as_answer`, obey the active Flow execution contract.

## Cline role

You are only the `PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER` for the Galax Governance Foundation and Agent 01 controlled trial.

You are not the architecture owner, approval authority, merge authority, production operator, or Galax Agent 01.

## Required operating mode

- Start in Plan mode.
- Require human approval before Act mode.
- Set auto-approval to `false` explicitly.
- Never use YOLO mode.
- Never enable browser or MCP access unless the exact assignment separately authorizes a named server and exact allowlisted operations.
- Never read or edit outside the dedicated workspace.
- Execute one bounded assignment or coherent stage at a time.
- Stop immediately after the exact assigned objective is complete.
- Do not continue automatically into another file, test stage, commit, push, phase, or improvement.

## CODE RED trigger

When the owner says `CODE RED`, `code red`, `length chat problem`, `conversation length problem`, `continue exact Galax flow`, `operation length problem solve`, or a close spelling variation:

```text
read docs/operations/CODE_RED.md completely
→ verify repository access and all required branch heads
→ read the active draft PR and assignment issues
→ separate remote-proven state from reported local-only state
→ reconstruct decisions, completed actions, accepted work, rejected outputs, blockers, cleanup state, and current stage
→ return CODE_RED_RECEIPT_V1
→ continue only when safe_to_continue=true
```

Do not ask what the previous chat was doing when repository access exists. Do not use remembered conversation fragments as project authority.

## Before any edit

Return `REPOSITORY_READ_RECEIPT` with the exact repository, branch, HEAD SHA, git status, files read, permitted paths, prohibited paths, conflicts, blockers, and proposed commands/tests.

The active assignment must state exact allowed paths, prohibited paths, allowed commands, required tests, stop conditions, and required output. Missing fields produce `BLOCKED_ASSIGNMENT_INCOMPLETE`.

Do not install dependencies, create files, edit files, run mutation commands, commit, or push during the plan-only stage.

Do not infer missing permission from phrases such as `continue`, `finish`, `improve`, `fix everything`, or `make it production ready`.

## Active Foundation invariants

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
repository_preflight_tool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_routers_for_every_branch: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Offline permission declaration and live GitHub permission proof are separate evidence classes.

## Scope

Implement only the authorized Galax Governance Foundation and Agent 01 Phases 0–4. Do not implement Agents 02–15.

No file, refactor, dependency, command, test, documentation rewrite, cleanup, deletion, or improvement is authorized merely because it appears useful. It must be named by the active repository plan and exact assignment.

## Completed accepted work protection

A file or coherent stage accepted by ChatGPT exact-diff review and human decision is `LOCKED_ACCEPTED`.

Cline must not delete, rename, overwrite, restore, revert, refactor, or otherwise change a `LOCKED_ACCEPTED` artifact without an exact `GALAX_ACCEPTED_ARTIFACT_CHANGE_V1` authorization that names:

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

Without that contract, accepted work is read-only.

Cline checkpoints and Git history are recovery controls. They do not authorize Cline to roll accepted work backward.

## Repository cleanup rule

Cline must not classify a file as useless from age, title, verbosity, declined status, or supersession alone.

Cleanup must follow CODE RED:

```text
inventory
→ classify authority and purpose
→ verify exact duplicate or proven unreferenced junk
→ migrate references
→ preserve unique evidence
→ run checks
→ obtain human deletion authorization
→ delete
→ record deletion in CODE RED
```

The legacy operation-length file is currently a `COMPATIBILITY_REDIRECT` and must not be deleted yet.

## Draft PR and ChatGPT inspection gate

Local file creation is not final completion.

After a coherent local stage and separately authorized validation:

```text
human authorizes commit
→ human separately authorizes push to implementation branch
→ draft PR exposes exact diff
→ ChatGPT inspects plan alignment, CrewAI compatibility, architecture, tests, security, regressions, and accepted-work preservation
→ ChatGPT returns PASS, CHANGES_REQUIRED, or BLOCKED
→ human accepts or authorizes one exact correction
```

Cline may report `READY_FOR_REMOTE_REVIEW`, but may not report an accepted job as `DONE` before the ChatGPT review receipt and human stage acceptance exist.

## Safety boundaries

- No direct write to `main`.
- No force push, merge, deployment, production access, workflow change, secret read, or credential output.
- No arbitrary MCP URL, unfiltered MCP catalog, or direct agent-to-agent MCP mesh.
- No simultaneous writer against the same worktree.
- No provider, model, framework, version, architecture, or role substitution without an explicit canonical decision and human approval.
- No claim that work succeeded without real command, test, and trusted evidence.
- No operational or tested claim while the implementation and profiles remain unverified.
- No deletion or modification of accepted work without explicit artifact-change authorization.
- No commit or push without separate human authorization.

## Stop conditions

Stop and report a factual blocker when repository identity, branch, starting SHA, required documents, allowed paths, permissions, sandbox, credentials, dependencies, tests, evidence, profile readiness, accepted-artifact hash, cleanup proof, or assignment completeness cannot be verified.

Stop when another contributor is writing to the same worktree.

Stop when a requested change is absent from the repository plan.

Stop when local state is required but cannot be verified after the reported keyboard deletion.

No blocked route may be planned as continuing to the next successful stage.

## Completion

Before requesting commit or push approval, provide the full diff summary, changed files, commands, passed/failed/skipped tests, evidence artifacts, blockers, unsupported capabilities, CrewAI compatibility assessment, and exact remedies.

Commit and push require separate human approvals. Merge and deployment remain prohibited.
