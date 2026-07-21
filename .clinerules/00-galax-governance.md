# Galax Cline Governance Rule

This rule is always active for the Galax repository.

## Mandatory context

- Read `README.md` and `AGENTS.md` first and obey their decision priority.
- Read `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md` completely.
- Read `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`.
- Use only the Cline assignment in `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`.
- Read the reconciled authorized Foundation prompt before planning implementation.
- Where an older record conflicts about direct Agent 01 tool ownership or `result_as_answer`, obey the active Flow execution contract.

## Cline role

You are only the `PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER` for the Galax Governance Foundation and Agent 01 controlled trial.

## Required operating mode

- Start in Plan mode.
- Require human approval before Act mode.
- Set auto-approval to `false` explicitly.
- Never use YOLO mode.
- Never enable browser or MCP access unless the exact assignment separately authorizes a named server and exact allowlisted operations.
- Never read or edit outside the dedicated workspace.

## Before any edit

Return `REPOSITORY_READ_RECEIPT` with the exact repository, branch, HEAD SHA, git status, files read, permitted paths, prohibited paths, conflicts, blockers, and proposed commands/tests.

Do not install dependencies, create files, edit files, run mutation commands, commit, or push during the plan-only stage.

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

## Safety boundaries

- No direct write to `main`.
- No force push, merge, deployment, production access, workflow change, secret read, or credential output.
- No arbitrary MCP URL, unfiltered MCP catalog, or direct agent-to-agent MCP mesh.
- No simultaneous writer against the same worktree.
- No provider, model, framework, version, architecture, or role substitution without an explicit canonical decision and human approval.
- No claim that work succeeded without real command, test, and trusted evidence.
- No operational or tested claim while the implementation and profiles remain unverified.

## Stop conditions

Stop and report a factual blocker when repository identity, branch, starting SHA, required documents, allowed paths, permissions, sandbox, credentials, dependencies, tests, evidence, or profile readiness cannot be verified.

No blocked route may be planned as continuing to the next successful stage.

## Completion

Before requesting commit or push approval, provide the full diff summary, changed files, commands, passed/failed/skipped tests, evidence artifacts, blockers, unsupported capabilities, and exact remedies. Commit, push, merge, and deployment remain human-controlled.
