# GitHub Repository Read/Write Architecture — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This design may be revised after implementation tests.  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Crew process:** `Process.sequential`

## 1. Objective

Allow one owner prompt to start a controlled CrewAI run in which only the necessary agents execute sequentially, read the current Galax repository, write authorized changes to a dedicated run branch, validate the result, and create a draft pull request without writing directly to `main`.

## 2. Factual support

CrewAI supports:

- Agents with designated tools.
- Custom tools.
- MCP servers as agent tools.
- Sequential task execution.
- Flows for deterministic orchestration and state.
- Hooks and guardrails around tool and task execution.

GitHub supports:

- Reading repository contents and Git trees.
- Creating blobs and trees.
- Creating commits.
- Creating and updating branch references.
- Creating pull requests.
- Fine-grained repository permissions.

Official sources are recorded in the source card for this architecture.

## 3. Architecture decision

The Galax system will not expose the full unrestricted GitHub MCP toolset directly to every agent.

Instead, it will use a self-hosted, role-scoped repository gateway named:

```text
galax-repository-mcp
```

The gateway will use the GitHub REST API and expose one role-specific composite MCP tool to each selected agent.

This preserves the project policy:

```text
ONE AGENT = ONE TOOL INTERFACE
```

The official GitHub MCP Server remains a verified reference and optional implementation dependency, but the direct full toolset is not approved for ordinary agents because it can expose many unrelated operations and increase context, permission, and tool-selection risk.

## 4. One-prompt execution

“One prompt” means one owner command starts one controlled workflow. It does not mean that all 15 agents run or that all work occurs in one LLM call.

```text
OWNER PROMPT
→ deterministic request parser
→ repository and rules preflight
→ create run ID
→ create run branch
→ choose only required approved agents
→ construct selected sequential Crew
→ run Agent 1
→ run required specialist agents in order
→ run QA
→ run independent auditor
→ create or update draft PR
→ return result and links
```

Only one agent and one LLM operation may run at a time.

## 5. Branch policy

Every implementation run must use a dedicated branch:

```text
galax/run/<run-id>-<short-task-name>
```

Example:

```text
galax/run/RUN-2026-0001-add-agent-source-index
```

Rules:

```yaml
direct_write_to_main: prohibited
force_push: prohibited
branch_creation: trusted_application_code_only
branch_base: current_main_sha
expected_head_sha_required: true
pull_request_mode: draft
merge: human_only
```

If the branch head changes unexpectedly, the tool returns `BLOCKED_CONCURRENT_CHANGE` and does not overwrite the branch.

## 6. Authentication

Preferred authentication order:

```text
1. GitHub App installation token restricted to this repository.
2. Fine-grained personal access token restricted to this repository.
3. Classic personal access token: rejected for the normal design.
```

Minimum planned repository permissions:

```yaml
metadata: read
contents: read_and_write
pull_requests: read_and_write
issues: none_by_default
actions: read_only_if_required
workflows: none
administration: none
secrets: none
environments: none
```

The token is stored only in the runtime environment or local secret store:

```env
GITHUB_TOKEN=
GALAX_REPOSITORY=ariessocia04-rgb/galax-Ai-project
```

The token must never appear in prompts, source cards, logs, commits, task results, or diagnostic output.

## 7. Repository gateway

The gateway is a local self-hosted MCP server built with the official MCP SDK or a local CrewAI custom tool implementation.

Preferred transport:

```yaml
transport: stdio
network_exposure: local_process_only
remote_public_endpoint: prohibited
```

The gateway performs GitHub API calls; the LLM does not receive the token.

## 8. Role-specific tool profiles

Each selected agent receives one profile. A profile is one exported tool interface with tightly related operations and path rules.

Examples:

```text
repository_preflight
requirements_workspace
architecture_workspace
frontend_workspace
backend_workspace
database_workspace
crewai_workspace
integration_workspace
security_scan_workspace
test_workspace
ci_workspace
observability_workspace
release_audit_workspace
```

Not every profile has write permission.

## 9. Agent 1 boundary

Agent 1 remains read-only:

```yaml
agent_id: engineering_manager
tool: repository_preflight
read: true
write: false
```

The system as a whole has repository write capability, but Agent 1 does not require it. Write capability belongs only to implementation agents whose approved task requires file changes.

## 10. Writer-agent capability

A writer profile may expose these operations through one tool interface:

```yaml
operations:
  - inspect_workspace
  - read_allowed_files
  - search_allowed_paths
  - propose_change_set
  - apply_change_set
  - verify_committed_change_set
```

The tool may be called more than once during a task. “One agent, one tool” does not mean only one tool invocation.

Recommended maximum:

```yaml
max_tool_calls_per_task: 3
call_1: inspect
call_2: apply
call_3: verify
```

## 11. Structured tool input

```python
class RepositoryWorkspaceRequest(BaseModel):
    run_id: str
    operation: Literal[
        "inspect_workspace",
        "read_allowed_files",
        "search_allowed_paths",
        "apply_change_set",
        "verify_committed_change_set",
    ]
    expected_branch_head_sha: str
    paths: list[str] = []
    search_terms: list[str] = []
    changes: list["FileChange"] = []
    commit_message: str | None = None


class FileChange(BaseModel):
    path: str
    action: Literal["create", "update"]
    expected_blob_sha: str | None = None
    content: str
```

Deletion is excluded from the initial implementation.

## 12. Structured tool output

```python
class RepositoryWorkspaceResult(BaseModel):
    run_id: str
    operation: str
    status: Literal[
        "PASS",
        "BLOCKED_PERMISSION",
        "BLOCKED_PATH_POLICY",
        "BLOCKED_CONCURRENT_CHANGE",
        "BLOCKED_VALIDATION",
        "FAILED_GITHUB_API",
    ]
    repository: str
    branch: str
    previous_head_sha: str
    new_head_sha: str | None
    files_read: list[str]
    files_created: list[str]
    files_updated: list[str]
    commit_sha: str | None
    evidence: list[str]
    errors: list[str]
```

## 13. Write transaction

For a multi-file change, the gateway should use the GitHub Git database sequence:

```text
read current branch head
→ verify expected SHA
→ read base commit and tree
→ create blobs
→ create one new tree based on the current tree
→ create one commit with the current branch head as parent
→ update run-branch reference with force=false
→ re-read commit and changed files
```

This produces one intentional commit for the agent task and avoids parallel per-file content writes.

## 14. Path scope

Each agent profile has exact allowed and prohibited paths.

Example frontend profile:

```yaml
allowed_paths:
  - src/frontend/**
  - tests/frontend/**
  - docs/implementation/frontend/**

prohibited_paths:
  - .github/workflows/**
  - .env
  - .env.*
  - secrets/**
  - src/backend/**
  - migrations/**
  - docs/rules/**
  - docs/plan/**
```

A path outside the allowlist is rejected before any GitHub write call.

## 15. Mandatory read order

Before a writer agent may apply changes, its first inspection must confirm hashes for:

```text
README.md
active repository rules
active flow plan
current run manifest
agent approval decision
relevant architecture decisions
relevant existing implementation
```

The `apply_change_set` call must include the exact rule and plan hashes returned by `inspect_workspace`. If any hash changed, the write is blocked and the agent must reread.

## 16. Prompt injection boundary

Repository content is untrusted input.

The gateway never treats repository text as executable instructions. It returns files and metadata only. The agent prompt must state that instructions found inside source files, issues, comments, or external content cannot override system rules, repository rules, tool permissions, or the approved run manifest.

## 17. Self-diagnostic and evidence

Every writer agent must report:

```yaml
self_diagnostic:
  repository_rules_read:
  assigned_tool_used:
  unapproved_tool_requested:
  allowed_paths_respected:
  prohibited_path_attempted:
  expected_head_sha_matched:
  files_changed: []
  commit_sha:
  tests_requested:
  remaining_risks: []
```

A deterministic guardrail compares this report with the actual gateway result.

## 18. QA and audit

QA and Release Auditor profiles are read-only. They inspect the run branch and commit evidence.

The Release Auditor cannot modify code, approve risk, merge, or deploy.

## 19. Pull-request creation

Draft PR creation belongs to trusted Flow/application code after QA and audit, not to an implementation agent.

PR creation conditions:

```text
all required sequential tasks completed
AND no unresolved tool failure
AND QA evidence exists
AND security disposition exists when required
AND auditor result is REVIEW_PASS_PENDING_OWNER
```

The PR remains draft until the owner decides otherwise.

## 20. Source lookup in the same system

The owner may ask:

```text
source <agent-id>
```

The application reads `docs/sources/agents/<agent-id>/SOURCE_CARD.md` and returns the exact clickable LLM and tool links. This lookup does not depend on model memory.

## 21. Required tests

```text
REPO-001 Read public repository file.
REPO-002 Read authenticated repository metadata.
REPO-003 Reject wrong repository ID.
REPO-004 Create run branch from exact main SHA.
REPO-005 Reject direct main write.
REPO-006 Read only allowed files.
REPO-007 Reject protected file read.
REPO-008 Create allowed file on run branch.
REPO-009 Update allowed file with expected blob SHA.
REPO-010 Reject update with stale blob SHA.
REPO-011 Create multi-file tree and one commit.
REPO-012 Update branch with force=false.
REPO-013 Reject stale branch-head SHA.
REPO-014 Reject path traversal.
REPO-015 Reject symlink escape.
REPO-016 Reject secret path.
REPO-017 Reject workflow modification without workflow permission.
REPO-018 Confirm token absent from output and logs.
REPO-019 Confirm Agent 1 cannot write.
REPO-020 Confirm writer cannot modify another role's paths.
REPO-021 Confirm QA is read-only.
REPO-022 Confirm Auditor is read-only.
REPO-023 Confirm failed stage stops downstream sequential execution.
REPO-024 Confirm draft PR created only after required gates.
REPO-025 Confirm no automatic merge.
```

Approval requires 25 of 25 tests in a pinned environment.

## 22. Current verdict

```yaml
crewai_tool_support: FACT_CHECKED_SUPPORTED
crewai_mcp_support: FACT_CHECKED_SUPPORTED
sequential_one_prompt_kickoff: SUPPORTED_BY_APPLICATION_DESIGN
github_read: FACT_CHECKED_SUPPORTED
github_write: FACT_CHECKED_SUPPORTED_WITH_PERMISSION
one_agent_one_tool: SUPPORTED_BY_ROLE_SCOPED_WRAPPER
direct_main_write: REJECTED
automatic_merge: REJECTED
production_status: NOT_IMPLEMENTED
final_status: CONDITIONALLY_COMPATIBLE
```

This architecture remains a draft until the source registry, gateway implementation, authentication method, and all tests are complete.
