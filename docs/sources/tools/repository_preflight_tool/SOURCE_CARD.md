# Tool Source Card — Repository Preflight Tool

**Source ID:** `TOOL-repository-preflight`  
**Status:** `CONDITIONALLY_APPROVED_FOR_IMPLEMENTATION_TEST`  
**Implementation:** `NOT_IMPLEMENTED`  
**Owner:** `GalaxFoundationFlow`  
**Invoked by Agent 01:** `false`  
**Verified:** 2026-07-21

## Identity

```yaml
name: RepositoryPreflightTool
type: local_custom_crewai_tool
maintainer: Galax AI project
license: project_license_pending
cost_status: fully_free_self_hosted
network_access: false
write_access: false
owner: GalaxFoundationFlow
invoked_before_agent: true
invocation_limit_per_run: 1
```

This is a planned Galax custom tool. It does not yet have an implementation commit, exact release, or live-test evidence.

## Active architecture

```text
GalaxFoundationFlow
→ invokes RepositoryPreflightTool exactly once
→ validates invocation evidence and typed RepositoryPreflightResult
→ checks LLM profile readiness
→ passes trusted result to engineering_manager
→ Agent 01 performs one bounded LLM evaluation
```

```yaml
engineering_manager.tools: []
Agent_01_direct_tool_calls: 0
result_as_answer_for_this_path: prohibited
```

Older records that attach this tool directly to Agent 01 or require `result_as_answer` are superseded only for this Foundation architecture by:

- [Foundation and Agent 01 Flow execution contract](../../../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md)

## CrewAI compatibility sources

- [CrewAI custom tools](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/create-custom-tools.mdx)
- [CrewAI Flows](https://github.com/crewAIInc/crewAI/tree/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/flows.mdx)
- [CrewAI tasks and structured outputs](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/tasks.mdx)

These sources support custom tools, deterministic Flow orchestration, and structured data boundaries. They do not prove the Galax implementation.

## Capability to implement

The Flow-owned tool must perform deterministic read-only repository preflight checks, return a strict typed result, and produce trusted invocation evidence outside the LLM.

It must enforce:

```text
- configured repository-root containment;
- no network access;
- no write or subprocess capability;
- path-traversal and symlink-escape rejection;
- secret-path exclusion;
- required document and manifest checks;
- exact active-plan and policy checks;
- repository identity and local Git-state checks;
- offline permission-profile declaration checks only;
- deterministic PASS/BLOCKED/FAIL results and remedies;
- one invocation per run;
- no fabricated invocation IDs, hashes, timestamps, or evidence.
```

The offline tool uses `REPO_PERMISSION_PROFILE_DECLARED`. It cannot claim `GITHUB_PERMISSIONS_LIVE_VALIDATED`; live permission evidence belongs to `GitHubRepositoryGateway`.

## Not proven by documentation

```text
- Repository identity verification works.
- Every required check is correctly implemented.
- Root and symlink boundaries are safe.
- Secret values cannot leak.
- Invocation evidence is append-only and valid.
- The tool is invoked exactly once.
- Blocked routes stop downstream execution.
- Agent 01 receives the exact trusted result.
```

These require implementation and deterministic tests.

## Approval blockers

```text
- Custom tool code does not exist.
- Flow-owned executor and invocation ledger do not exist.
- Tool tests have not run.
- Router and blocked-route tests have not run.
- Live GitHub permission evidence gateway is not implemented or tested.
- Agent 01 LLM profile is disabled and not approved.
```

## Revalidation triggers

Revalidate when CrewAI changes, the tool input/output schema changes, the Flow ownership or router contract changes, repository rules change, permission policy changes, or the implementation commit changes.

## Current status

```yaml
implementation_status: NOT_IMPLEMENTED
live_tests: NOT_RUN
external_tool_connected: false
Flow_owner_implemented: false
Agent_01_runtime_approved: false
production_ready: false
```
