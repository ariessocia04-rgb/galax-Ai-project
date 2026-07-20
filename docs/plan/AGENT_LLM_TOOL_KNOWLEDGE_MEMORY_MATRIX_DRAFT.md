# 15-Agent LLM, Tool, Knowledge, and Memory Matrix — Draft

**Status:** `DRAFT_MUTABLE`  
**Framework candidate:** CrewAI 1.15.4  
**LLM candidate:** `cerebras/gpt-oss-120b`  
**Process:** `Process.sequential`  
**Global rule:** One agent receives one role-specific tool interface. Google Drive knowledge and Notion memory are injected by trusted Flow/application infrastructure.

## Global LLM restrictions

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: SELECTED_FOR_VALIDATION_NOT_USED
temperature: 1.0
timeout_seconds: 120
max_retries: 1
max_rpm: 4
allow_delegation: false
allow_code_execution: false
async_execution: false
memory: false
respect_context_window: false
crewai_reasoning_loop: false
```

Every profile below remains disabled until its own prompt, tool schema, actual tool invocation, structured output, security, rate-limit, and sequential-context tests pass.

## Shared context order

```text
1. Immutable system and repository rules.
2. Current run manifest and task contract.
3. Verified Notion memory context.
4. Verified Google Drive LearningPacket when required.
5. Relevant repository excerpts.
6. One role-specific tool schema.
7. Prior structured sequential task output.
```

## Agent 01 — Engineering Manager / Preflight

```yaml
llm_profile:
  reasoning_effort: low
  max_completion_tokens: 800
  max_iter: 4
  status: DISABLED_PENDING_TESTS
single_tool:
  name: RepositoryPreflightTool
  permission: repository_read_only
  status: CONDITIONALLY_APPROVED_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - explicit owner preflight policies
    - task-specific governance tutorials
Notion_memory_read:
  - GLOBAL_BLOCKER
  - AGENT_VALIDATION
  - TOOL_VALIDATION
  - LLM_VALIDATION
must_not:
  - choose or add agents dynamically
  - reorder tasks
  - write repository
  - approve its own result
required_tests:
  - exact preflight tool invocation
  - continue_or_stop schema
  - blocking result stops sequential run
```

## Agent 02 — Product Requirements and Scope Lead

```yaml
llm_profile:
  reasoning_effort: medium
  max_completion_tokens: 1600
  max_iter: 6
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: RequirementsWorkspaceTool
  permission: requirements_and_acceptance_docs_run_branch_write
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - owner business-process tutorials
    - copied product workflow references
    - domain terminology files
Notion_memory_read:
  - DECISION
  - LESSON
  - SCOPE_CONFLICT
  - RUN_SUMMARY
must_not:
  - invent requirements
  - approve scope
  - edit application code
  - use outdated learning material without flagging it
required_tests:
  - requirement traceability to owner prompt and LearningPacket
  - acceptance criteria schema
  - no unsupported feature invention
```

## Agent 03 — Evidence and Capability Researcher

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: VerifiedResearchWorkspaceTool
  permission: public_web_research_plus_source_registry_run_branch_write
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  primary_role:
    - reconcile owner Drive learning files with current official sources
    - investigate related files when titles are wrong
Notion_memory_read:
  - SOURCE_WARNING
  - LESSON
  - PRIOR_RESEARCH_GAP
must_not:
  - treat model memory as current evidence
  - cite aggregator as final authority
  - install or enable providers
  - approve without live-test requirements
required_tests:
  - official-source priority
  - source date and version capture
  - contradiction detection
  - real Drive file ID and hash evidence
```

## Agent 04 — Solution and Systems Architect

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2400
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: ArchitectureWorkspaceTool
  permission: architecture_docs_run_branch_write
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - architecture tutorials
    - owner-approved system patterns
    - protocol and failure-mode references
Notion_memory_read:
  - DECISION
  - LESSON
  - MISTAKE
  - ARCHITECTURE_RISK
must_not:
  - modify implementation code
  - approve architecture unilaterally
  - treat tutorial pattern as compatible without version check
required_tests:
  - architecture proposal schema
  - dependency and failure-mode evidence
  - conflict with current architecture detection
```

## Agent 05 — UX, UI, and Accessibility Designer

```yaml
llm_profile:
  reasoning_effort: medium
  max_completion_tokens: 1600
  max_iter: 6
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: UXWorkspaceTool
  permission: design_specs_and_local_or_staging_inspection
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - copied UI tutorials
    - design patterns
    - accessibility learning files
Notion_memory_read:
  - DECISION
  - UX_LESSON
  - ACCESSIBILITY_DEFECT
must_not:
  - edit production UI code
  - claim accessibility compliance without test evidence
  - access production user data
required_tests:
  - interaction-state specification
  - keyboard and accessibility evidence
  - design-to-requirement traceability
```

## Agent 06 — Frontend Application Engineer

```yaml
llm_profile:
  reasoning_effort: medium
  max_completion_tokens: 2000
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: FrontendWorkspaceTool
  permission: frontend_paths_run_branch_write_plus_external_sandbox
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - framework tutorials
    - component patterns
    - owner UI implementation references
Notion_memory_read:
  - FRONTEND_LESSON
  - REGRESSION
  - BUILD_FAILURE
must_not:
  - use deprecated CrewAI built-in code execution
  - edit backend, database, rules, or workflow paths
  - write before StudyReceipt passes
required_tests:
  - allowed-path enforcement
  - patch and sandbox execution evidence
  - lint/unit/UI test evidence
  - stale framework tutorial rejection
```

## Agent 07 — Backend and API Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: BackendWorkspaceTool
  permission: backend_API_paths_run_branch_write_plus_external_sandbox
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - API tutorials
    - domain logic references
    - authentication and error-handling materials
Notion_memory_read:
  - BACKEND_LESSON
  - API_CONTRACT_FAILURE
  - SECURITY_WARNING
must_not:
  - modify frontend or production database
  - expose credentials
  - claim authorization correctness without tests
required_tests:
  - API contract validation
  - auth boundary tests
  - failure and retry behavior
  - allowed-path and sandbox evidence
```

## Agent 08 — Data and Database Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: DatabaseWorkspaceTool
  permission: schema_and_migration_paths_plus_disposable_local_database
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - schema tutorials
    - migration references
    - concurrency and rollback learning files
Notion_memory_read:
  - DATABASE_LESSON
  - MIGRATION_FAILURE
  - DATA_RISK
must_not:
  - access or mutate production database
  - run destructive migration without owner approval
  - treat generated SQL as validated
required_tests:
  - local disposable migration
  - rollback test
  - constraint and concurrency validation
  - no production credentials
```

## Agent 09 — CrewAI and AI Systems Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2400
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: CrewAIWorkspaceTool
  permission: CrewAI_config_flow_schema_tests_run_branch_write_plus_sandbox
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - owner CrewAI tutorials
    - agent prompt patterns
    - LLM and MCP setup references
Notion_memory_read:
  - AGENT_VALIDATION
  - LLM_VALIDATION
  - TOOL_VALIDATION
  - CREWAI_FAILURE
must_not:
  - enable unsupported CrewAI fields
  - change process from sequential
  - enable native memory or deprecated code execution without approval
  - enable all agents automatically
required_tests:
  - pinned CrewAI load test
  - exact agent/tool/LLM profile test
  - sequential-order test
  - structured self-diagnostic test
```

## Agent 10 — Integration and MCP Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: IntegrationMCPWorkspaceTool
  permission: integration_and_MCP_paths_run_branch_write_plus_mock_sandbox
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - API integration tutorials
    - MCP protocol references
    - authentication setup files
Notion_memory_read:
  - INTEGRATION_LESSON
  - AUTH_FAILURE
  - MCP_VALIDATION
must_not:
  - connect random public MCP server
  - expose unrestricted URL fetch
  - use production credentials
  - claim reliability without malformed-response tests
required_tests:
  - schema and auth tests
  - timeout/retry/429 tests
  - SSRF and path validation
  - MCP response validation
```

## Agent 11 — Security, Privacy, and AI Safety Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2400
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: SecurityAuditTool
  permission: scan_only_repository_and_local_artifacts
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - owner security policies
    - threat-model tutorials
    - approved standards references
Notion_memory_read:
  - SECURITY_WARNING
  - THREAT
  - MITIGATION
  - PRIOR_FINDING
must_not:
  - exploit unauthorized targets
  - mutate production
  - auto-fix findings
  - certify system as secure
required_tests:
  - tool-generated scan evidence
  - false-positive disposition schema
  - secret and PII redaction
  - human gate for high-risk actions
```

## Agent 12 — QA and Test Automation Engineer

```yaml
llm_profile:
  reasoning_effort: medium
  max_completion_tokens: 1800
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: TestRunnerTool
  permission: test_execution_and_test_paths_run_branch_write
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - testing tutorials
    - owner acceptance examples
    - framework-specific test patterns
Notion_memory_read:
  - REGRESSION
  - FLAKY_TEST
  - QA_LESSON
must_not:
  - modify implementation solely to hide failure
  - delete existing tests without approval
  - report pass without actual test invocation
required_tests:
  - invocation ID and exit-code evidence
  - unit/integration/browser result parsing
  - failed test stops downstream release
```

## Agent 13 — DevOps and CI/CD Engineer

```yaml
llm_profile:
  reasoning_effort: medium
  max_completion_tokens: 1800
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: CIBuildWorkspaceTool
  permission: CI_and_build_paths_run_branch_write_plus_local_build_sandbox
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - CI tutorials
    - build and packaging references
    - owner deployment procedures
Notion_memory_read:
  - BUILD_FAILURE
  - RELEASE_LESSON
  - ROLLBACK_LESSON
must_not:
  - deploy production
  - edit repository secrets
  - enable paid infrastructure
  - auto-merge
required_tests:
  - local build evidence
  - workflow syntax validation
  - artifact hash
  - production deployment gate
```

## Agent 14 — SRE and Observability Engineer

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: ObservabilityReadTool
  permission: approved_logs_metrics_traces_read_only
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - monitoring tutorials
    - SLO and incident references
    - owner recovery procedures
Notion_memory_read:
  - INCIDENT
  - RECOVERY_CHECKPOINT
  - SRE_LESSON
must_not:
  - change production environment
  - suppress alerts
  - claim root cause without evidence
  - expose sensitive logs
required_tests:
  - read-only enforcement
  - trace/metric/log correlation evidence
  - redaction
  - recovery recommendation schema
```

## Agent 15 — Independent Code Review, Documentation, and Release Auditor

```yaml
llm_profile:
  reasoning_effort: high
  max_completion_tokens: 2200
  max_iter: 8
  status: DISABLED_PENDING_RESEARCH
single_tool:
  name: ReleaseAuditTool
  permission: run_branch_repo_test_security_source_memory_evidence_read_only
  status: CANDIDATE_NOT_IMPLEMENTED
Drive_knowledge:
  required_for:
    - owner release criteria
    - audit tutorials
    - final reference standards
Notion_memory_read:
  - PRIOR_RELEASE_RISK
  - UNRESOLVED_BLOCKER
  - AGENT_VALIDATION
  - TOOL_VALIDATION
  - LLM_VALIDATION
must_not:
  - edit code
  - approve its own prior work
  - merge or deploy
  - ignore missing learning or memory evidence
required_tests:
  - independent evidence reconciliation
  - source and StudyReceipt verification
  - final blocked/pass-pending-owner schema
```

# Common enablement gate

Every agent requires:

```text
ROLE FACT CHECKED
→ CREWAI FEATURE SUPPORTED
→ LLM PROFILE TESTED
→ SINGLE TOOL IMPLEMENTED AND TESTED
→ DRIVE LEARNING BEHAVIOR TESTED WHEN APPLICABLE
→ NOTION MEMORY CONTEXT TESTED
→ STRUCTURED OUTPUT AND SELF-DIAGNOSTIC TESTED
→ SECURITY AND PERMISSION TESTS PASSED
→ SEQUENTIAL CONTEXT TEST PASSED
→ STATUS = APPROVED_FOR_IMPLEMENTATION
```

No agent in this matrix is currently enabled.
