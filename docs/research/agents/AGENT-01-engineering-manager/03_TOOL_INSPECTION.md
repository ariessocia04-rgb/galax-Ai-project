d:** 2026-07-20  
**Permanent rule:** No. This record may be revised when repository rules, CrewAI, the LLM, or the execution design changes.

> **SUPERSESSION NOTICE (2026-07-21):** The active Foundation and Agent 01 Flow execution contract at `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md` supersedes sections of this document where they assign `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, or use `result_as_answer` for this path.
>
> **Active architecture for current Foundation scope:**
> - `RepositoryPreflightTool` is owned and invoked exactly once by `GalaxFoundationFlow`, NOT by Agent 01.
> - Agent 01 (`engineering_manager`) has zero direct tools (`tools: []`; `direct_tool_calls: 0`).
> - `result_as_answer` is prohibited for this Foundation path.
> - Agent 01 executes exactly one LLM call and produces `AgentTaskResult`.
> - Sections 14 (agent usage rule), 15 (self-diagnostic requiring tool call), 16 (token controls exposing tool schema), and 18 (tests requiring Agent 01 to call a tool) are superseded. All non-conflicting security boundaries, check definitions, and input/output contracts remain active evidence.
>
> This notice preserves this record's historical research value. No historical content has been deleted.

## 1. Scope of this inspection

This document inspects only the single tool proposed for Agent 01. It does not approve the final agent prompt, LLM, task, or implementation.

The existing Agent 01 role, goal, backstory, responsibilities, and output contract remain unchanged while tool research is in progress.

## 2. Proposed single tool

```yaml
agent_id: engineering_manager
tool_id: repository_preflight_tool
tool_class: RepositoryPreflightTool
tool_type: local_custom_crewai_tool
cost: fully_free_self_hosted
network_access: false
filesystem_access: read_only_repository_scoped
write_access: false
production_access: false
status: CONDITIONALLY_APPROVED_FOR_IMPLEMENTATION_TEST
```

## 3. Decision

The proposed tool is a **local custom CrewAI tool**, not an MCP server and not a paid cloud service.

CrewAI officially supports agents with designated tools and supports custom tool initialization through the `@tool` annotation. CrewAI also supports sequential crews where tasks execute in the defined order. These facts make a single read-only preflight tool technically compatible with the planned Galax sequential crew.

Official CrewAI references:

- Agent capabilities and tools: https://docs.crewai.com/v1.15.4/en/concepts/agents.md
- Custom tools: https://docs.crewai.com/v1.15.4/en/learn/create-custom-tools.md
- Tool annotations: https://docs.crewai.com/v1.15.4/en/learn/using-annotations.md
- Sequential execution: https://docs.crewai.com/v1.15.4/en/learn/sequential-process.md
- Structured task outputs and guardrails: https://docs.crewai.com/v1.15.4/en/concepts/tasks.md

## 4. Why this tool fits Agent 01

Agent 01 must validate an already prepared execution plan before the sequential Crew starts specialist work. It must not dynamically delegate, add agents, reorder tasks, edit code, or modify the repository.

A deterministic read-only preflight tool is appropriate because it can inspect and validate exact repository records without giving Agent 01 broad GitHub, shell, browser, database, or filesystem-write access.

This tool keeps the boundaries clear:

```text
Flow or application code creates the run manifest.
Agent 01 validates the manifest and required repository evidence.
Agent 01 does not create or change the manifest.
Process.sequential controls the task order.
```

## 5. Why the previous `flow_state_mcp` idea is not selected

`flow_state_mcp` is not selected as Agent 01's tool because state mutation belongs to deterministic application or Flow code, not to the LLM-controlled agent.

Giving Agent 01 write access to execution state would allow it to change agent selection, task order, or status records. That conflicts with the strict sequential and least-privilege rules.

The Flow may maintain state internally, but Agent 01 receives only a read-only preflight interface.

## 6. Exact tool objective

```text
Validate that the current Galax run can safely enter sequential execution by checking the repository identity, required reading files, approved agent decisions, selected task order, allowed paths, prohibited paths, and required approval gates.
```

## 7. Tool input contract

The LLM must not provide arbitrary file paths. The tool accepts only a run identifier.

```python
class RepositoryPreflightInput(BaseModel):
    run_id: str
```

Validation rules:

```yaml
run_id:
  required: true
  pattern: '^RUN-[0-9]{4}-[0-9]{4,}$'
  maximum_length: 32

arbitrary_paths_from_agent: prohibited
arbitrary_repository_url_from_agent: prohibited
arbitrary_branch_from_agent: prohibited
```

Repository root, manifest directory, and required document locations must be configured by trusted application code outside the prompt.

## 8. Files the tool may read

```text
README.md
docs/rules/**/*.md
docs/plan/**/*.md
runs/<run_id>/run_manifest.yaml
docs/research/agents/<selected-agent>/08_DECISION.md
src/galax_ai/config/agent_registry.yaml
src/galax_ai/config/task_registry.yaml
```

These files do not all exist yet. Their absence must produce an explicit blocked result rather than an assumption.

## 9. Files and paths the tool must never read

```text
.env
.env.*
*.pem
*.key
*.p12
*.pfx
.ssh/
.aws/
.git/credentials
credential files
secret stores
user home directories
paths outside the configured repository root
```

Symlinks resolving outside the repository root must be rejected.

## 10. Checks performed by the tool

The tool performs these checks in this exact order:

```text
PREFLIGHT-001 Confirm configured repository root exists.
PREFLIGHT-002 Confirm repository identifier matches the configured Galax repository.
PREFLIGHT-003 Confirm README.md exists and is readable.
PREFLIGHT-004 Confirm required rule files exist and are readable.
PREFLIGHT-005 Confirm the active plan exists and is readable.
PREFLIGHT-006 Load the exact run manifest for run_id.
PREFLIGHT-007 Validate the manifest against its local schema.
PREFLIGHT-008 Confirm process is sequential.
PREFLIGHT-009 Confirm parallel and asynchronous execution are disabled.
PREFLIGHT-010 Confirm every selected agent exists in the registry.
PREFLIGHT-011 Confirm every selected agent decision is APPROVED_FOR_IMPLEMENTATION or later.
PREFLIGHT-012 Confirm every selected task exists in the task registry.
PREFLIGHT-013 Confirm task order exactly matches the execution_order list.
PREFLIGHT-014 Confirm no duplicate task or agent identifiers.
PREFLIGHT-015 Confirm selected agents are necessary for at least one selected task.
PREFLIGHT-016 Confirm allowed and prohibited paths do not conflict.
PREFLIGHT-017 Confirm protected and secret paths are excluded.
PREFLIGHT-018 Confirm required human approval gates are present.
PREFLIGHT-019 Compute SHA-256 hashes for the validated planning records.
PREFLIGHT-020 Return a structured report without modifying any file.
```

## 11. Tool output contract

```python
class PreflightFinding(BaseModel):
    check_id: str
    status: Literal['PASS', 'FAIL', 'BLOCKED']
    message: str
    evidence_path: str | None = None
    evidence_sha256: str | None = None


class RepositoryPreflightResult(BaseModel):
    run_id: str
    status: Literal[
        'PASS',
        'BLOCKED_REPOSITORY',
        'BLOCKED_REQUIRED_DOCUMENT',
        'BLOCKED_MANIFEST',
        'BLOCKED_AGENT_APPROVAL',
        'BLOCKED_TASK_ORDER',
        'BLOCKED_PATH_POLICY',
        'BLOCKED_APPROVAL_GATE',
        'FAILED_TOOL_EXECUTION',
    ]
    repository_id: str
    process: str | None
    selected_agents: list[str]
    selected_tasks: list[str]
    findings: list[PreflightFinding]
    checked_files: list[str]
    checked_file_hashes: dict[str, str]
    errors: list[str]
    safe_to_continue: bool
```

## 12. Pass rule

The tool may return `PASS` only when:

```text
- All 20 checks ran.
- Every required check passed.
- No required file is missing.
- Process is exactly sequential.
- Selected agents and tasks are approved and registered.
- No path-policy conflict exists.
- Required approval gates exist.
- No file was modified.
```

`safe_to_continue` must be `true` only for `PASS`.

## 13. Failure behavior

```yaml
retry_policy:
  automatic_retries: 0
  reason: deterministic local validation should not consume another LLM call

on_missing_file:
  action: return_blocked

on_invalid_yaml:
  action: return_blocked

on_schema_failure:
  action: return_blocked

on_path_escape_or_symlink_escape:
  action: return_blocked_security

on_unexpected_exception:
  action: return_failed_tool_execution
```

The tool must never invent missing content, repair a manifest, create directories, or silently continue.

## 14. Agent usage rule

Agent 01 may call the tool exactly once per preflight task.

```yaml
agent_tool_policy:
  assigned_tools:
    - repository_preflight_tool
  maximum_tool_calls_per_task: 1
  second_tool: prohibited
  delegation: false
  tool_result_must_be_preserved: true
```

When the tool returns a blocked or failed status, Agent 01 must report that status and stop. It must not attempt a workaround.

## 15. Self-diagnostic requirement

Agent 01's task result must include:

```yaml
self_diagnostic:
  assigned_tool_used: true
  tool_called_once: true
  tool_status:
  unsupported_action_attempted: false
  repository_modified: false
  assumptions_made: []
  remaining_blockers: []
```

A deterministic guardrail must reject a claimed `PASS` when the tool result was not `PASS`.

## 16. Token controls

```yaml
token_controls:
  load_only_agent_01_prompt: true
  expose_only_repository_preflight_tool_schema: true
  maximum_tool_calls: 1
  tool_returns_structured_summary_not_full_file_contents: true
  include_full_repository_in_prompt: false
  agent_reasoning: false
  allow_delegation: false
```

The tool performs file checks in Python and returns only structured findings. Repository files are not copied in full into the LLM prompt.

## 17. Security boundaries

```yaml
security:
  default_permission: deny
  repository_scope: configured_galax_root_only
  mode: read_only
  network: disabled
  subprocess: disabled
  shell: disabled
  git_write: disabled
  github_write: disabled
  environment_variable_reading: disabled
  secret_path_reading: disabled
```

## 18. Required tests before approval

```text
TOOL-A01-001 Valid approved manifest returns PASS.
TOOL-A01-002 Missing README returns BLOCKED_REQUIRED_DOCUMENT.
TOOL-A01-003 Missing rule file returns BLOCKED_REQUIRED_DOCUMENT.
TOOL-A01-004 Invalid YAML returns BLOCKED_MANIFEST.
TOOL-A01-005 Invalid schema returns BLOCKED_MANIFEST.
TOOL-A01-006 Non-sequential process returns BLOCKED_MANIFEST.
TOOL-A01-007 Duplicate agent returns BLOCKED_MANIFEST.
TOOL-A01-008 Unapproved agent returns BLOCKED_AGENT_APPROVAL.
TOOL-A01-009 Incorrect task order returns BLOCKED_TASK_ORDER.
TOOL-A01-010 Path-policy conflict returns BLOCKED_PATH_POLICY.
TOOL-A01-011 Missing human gate returns BLOCKED_APPROVAL_GATE.
TOOL-A01-012 Attempted path traversal is rejected.
TOOL-A01-013 Symlink escape is rejected.
TOOL-A01-014 Secret path is rejected.
TOOL-A01-015 Repository remains byte-for-byte unchanged.
TOOL-A01-016 Tool makes no network request.
TOOL-A01-017 Tool starts no subprocess.
TOOL-A01-018 Output validates against RepositoryPreflightResult.
TOOL-A01-019 Agent calls no second tool.
TOOL-A01-020 Blocked result stops the sequential run.
```

Approval requires 20 of 20 tests to pass in the pinned environment.

## 19. Current verdict

```yaml
crewai_custom_tool_support: FACT_CHECKED_SUPPORTED
sequential_process_compatibility: FACT_CHECKED_SUPPORTED
one_agent_one_tool_compatibility: SUPPORTED_BY_CONFIGURATION
fully_free_local_operation: SUPPORTED
read_only_preflight_design: SUPPORTED_AS_CUSTOM_IMPLEMENTATION
production_readiness: NOT_YET_TESTED
llm_compatibility: NOT_YET_TESTED
final_status: CONDITIONALLY_COMPATIBLE
implementation_status: NOT_IMPLEMENTED
```

## 20. Approval blockers

```text
1. Repository rules and master plan are not complete.
2. Run-manifest schema does not exist.
3. Agent and task registries do not exist.
4. The custom tool has not been implemented.
5. The 20 required tool tests have not run.
6. The selected LLM has not passed CrewAI tool-calling tests.
7. Agent 01's final prompt has not been approved.
```

Until all blockers are resolved, this tool must not be placed in the production agent configuration.
