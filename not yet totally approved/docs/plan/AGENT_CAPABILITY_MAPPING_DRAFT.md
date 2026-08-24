# Galax 15-Agent Capability Mapping — Draft

**Status:** `DRAFT_MUTABLE`  
**Process:** `Process.sequential`  
**Current LLM candidate:** `cerebras/gpt-oss-120b`  
**Rule:** An agent is enabled only after its role, LLM profile, single tool, permissions, Google Drive learning behavior when required, Notion memory context, and tests are approved.

## Global execution model

```text
One owner prompt
→ deterministic Flow/application preflight
→ retrieve verified Notion memory
→ retrieve Google Drive LearningPacket when required
→ select necessary approved agents only
→ construct one sequential Crew segment
→ one agent and one LLM call at a time
→ one role-specific tool interface per agent
→ StudyReceipt when knowledge is present
→ structured output and self-diagnostic
→ deterministic validation
→ next selected stage
→ audit
→ Flow writes approved memory to Notion
```

No agent is a fully autonomous employee. Every agent is a bounded AI assistant.

Google Drive and Notion are controlled infrastructure. They are not extra agent tools.

## Agent 01 — Engineering Manager / Preflight

```yaml
crewai_supported_work:
  - summarize deterministic repository preflight result
  - identify blocking rule, plan, agent, task, knowledge, memory, or approval-gate failures
  - return structured continue_or_stop decision

single_tool: RepositoryPreflightTool
tool_permission: repository_read_only
llm_reasoning_effort: low

Drive_learning:
  direct_access: false
  LearningPacket_from_Flow: conditional
Notion_memory:
  direct_access: false
  verified_context_from_Flow: true

must_not:
  - dynamically select or add agents
  - reorder tasks
  - delegate
  - search Drive directly
  - browse or write Notion directly
  - modify repository
  - approve its own output
  - claim that missing evidence passed

status: CONDITIONALLY_COMPATIBLE
```

The deterministic Flow creates the manifest and retrieves knowledge/memory; Agent 01 only interprets trusted results.

## Agent 02 — Product Requirements and Scope Lead

```yaml
crewai_supported_work:
  - convert owner request and verified repository context into requirements
  - use verified LearningPacket when owner tutorials or process files apply
  - use bounded verified memory for past scope lessons and decisions
  - define acceptance criteria, constraints, assumptions, exclusions, and questions
  - detect conflicts with current rules and plan

single_tool: RequirementsWorkspaceTool
tool_permission: requirements_paths_read_write_on_run_branch
llm_reasoning_effort: medium

must_not:
  - invent customer requirements
  - approve scope changes
  - edit application code
  - perform market research without verified research input
  - treat memory or Drive content as higher priority than repository rules

status: RESEARCH_REQUIRED
```

Human owner approves final scope.

## Agent 03 — Evidence and CrewAI Capability Researcher

```yaml
crewai_supported_work:
  - use approved research interface
  - reconcile Drive learning material with current official sources
  - investigate related files when titles are incorrect
  - compare official sources
  - record links, dates, capabilities, limitations, contradictions, file IDs, and hashes
  - produce source-backed capability and LearningPacket decisions

single_tool: VerifiedResearchWorkspaceTool
tool_permission: public_web_research_and_source_registry_write
llm_reasoning_effort: high

must_not:
  - use LLM memory as current evidence
  - cite unverified links
  - install tools
  - edit implementation
  - approve a capability without live-test requirements
  - expose Drive or Notion credentials

status: RESEARCH_REQUIRED
```

Current facts and owner knowledge require actual retrieval evidence.

## Agent 04 — Solution and Systems Architect

```yaml
crewai_supported_work:
  - analyze approved requirements and repository architecture
  - study verified architecture LearningPackets when required
  - use validated decision and failure memory
  - propose bounded architecture changes
  - identify components, contracts, dependencies, tradeoffs, and failure modes
  - produce an architecture decision proposal

single_tool: ArchitectureWorkspaceTool
tool_permission: architecture_docs_scoped_write
llm_reasoning_effort: high

must_not:
  - modify implementation code
  - approve architecture unilaterally
  - apply tutorial patterns without version and compatibility checks

status: RESEARCH_REQUIRED
```

## Agent 05 — UX, UI, and Accessibility Designer

```yaml
crewai_supported_work:
  - inspect approved local or staging UI
  - study verified owner UX/accessibility learning material
  - produce interaction, state, responsive, and accessibility specifications
  - use validated UX defect memory

single_tool: UXWorkspaceTool
tool_permission: design_specs_and_local_or_staging_inspection
llm_reasoning_effort: medium

must_not:
  - edit production UI code
  - claim accessibility compliance without tests
  - access production user data

status: RESEARCH_REQUIRED
```

## Agent 06 — Frontend Application Engineer

```yaml
crewai_supported_work:
  - study verified frontend LearningPacket and produce StudyReceipt
  - inspect approved frontend paths
  - create or update scoped frontend files on a run branch
  - run allowlisted commands through an external sandbox in its single workspace tool
  - return patch, test, and invocation evidence

single_tool: FrontendWorkspaceTool
tool_permission: frontend_paths_run_branch_write_plus_external_sandbox
llm_reasoning_effort: medium

must_not:
  - use deprecated built-in CrewAI code execution
  - edit backend, database, rules, or workflow paths
  - write before StudyReceipt passes
  - claim test success without actual invocation evidence

status: RESEARCH_REQUIRED
```

## Agent 07 — Backend and API Engineer

```yaml
crewai_supported_work:
  - study verified backend/API LearningPacket and produce StudyReceipt
  - modify approved backend/API paths on a run branch
  - use external sandbox through its single workspace tool
  - validate contracts, authorization boundaries, and failure behavior

single_tool: BackendWorkspaceTool
tool_permission: backend_API_paths_run_branch_write_plus_external_sandbox
llm_reasoning_effort: high

must_not:
  - modify frontend or production database
  - expose credentials
  - claim authorization correctness without tests

status: RESEARCH_REQUIRED
```

## Agent 08 — Data and Database Engineer

```yaml
crewai_supported_work:
  - study verified database LearningPacket and produce StudyReceipt
  - modify approved schema and migration paths
  - run migrations only against disposable local/test databases
  - validate constraints, concurrency, rollback, and evidence

single_tool: DatabaseWorkspaceTool
tool_permission: schema_and_migration_paths_plus_disposable_local_database
llm_reasoning_effort: high

must_not:
  - access or mutate production database
  - run destructive migration without owner approval
  - treat generated SQL as validated

status: RESEARCH_REQUIRED
```

## Agent 09 — CrewAI and AI Systems Engineer

```yaml
crewai_supported_work:
  - study verified CrewAI/LLM/MCP LearningPacket and produce StudyReceipt
  - modify approved CrewAI configuration, Flow, schema, and test paths
  - use external sandbox through its single workspace tool
  - validate exact pinned framework, LLM profile, tool, structured output, and sequential behavior

single_tool: CrewAIWorkspaceTool
tool_permission: CrewAI_config_flow_schema_tests_run_branch_write_plus_sandbox
llm_reasoning_effort: high

must_not:
  - enable unsupported CrewAI fields
  - change process from sequential
  - enable native memory or deprecated code execution without approval
  - enable all agents automatically

status: RESEARCH_REQUIRED
```

## Agent 10 — Integration and MCP Engineer

```yaml
crewai_supported_work:
  - study verified integration/MCP LearningPacket and produce StudyReceipt
  - modify approved integration and MCP paths
  - test schemas, authentication, timeout, retry, and malformed responses in mock/local environments

single_tool: IntegrationMCPWorkspaceTool
tool_permission: integration_and_MCP_paths_run_branch_write_plus_mock_sandbox
llm_reasoning_effort: high

must_not:
  - connect random public MCP servers
  - expose unrestricted URL fetch
  - use production credentials
  - claim reliability without negative-path tests

status: RESEARCH_REQUIRED
```

## Agent 11 — Security, Privacy, and AI Safety Engineer

```yaml
crewai_supported_work:
  - study verified security LearningPacket
  - use prior verified threat and mitigation memory
  - run approved scanners through a scan-only tool
  - produce threat, finding, evidence, and disposition records

single_tool: SecurityAuditTool
tool_permission: scan_only_repository_and_local_artifacts
llm_reasoning_effort: high

must_not:
  - exploit unauthorized targets
  - mutate production
  - auto-fix findings
  - certify the system as secure

status: RESEARCH_REQUIRED
```

## Agent 12 — QA and Test Automation Engineer

```yaml
crewai_supported_work:
  - study verified testing LearningPacket
  - use prior regression and flaky-test memory
  - create approved tests and execute allowlisted test commands
  - return actual invocation IDs, exit codes, and artifacts

single_tool: TestRunnerTool
tool_permission: test_execution_and_test_paths_run_branch_write
llm_reasoning_effort: medium

must_not:
  - modify implementation solely to hide failure
  - delete existing tests without approval
  - report pass without actual tool invocation

status: RESEARCH_REQUIRED
```

## Agent 13 — DevOps and CI/CD Engineer

```yaml
crewai_supported_work:
  - study verified CI/build LearningPacket
  - use prior build and rollback memory
  - modify approved CI/build paths
  - run local build validation through external sandbox
  - produce artifact and configuration evidence

single_tool: CIBuildWorkspaceTool
tool_permission: CI_and_build_paths_run_branch_write_plus_local_build_sandbox
llm_reasoning_effort: medium

must_not:
  - deploy production
  - edit repository secrets
  - enable paid infrastructure
  - auto-merge

status: RESEARCH_REQUIRED
```

## Agent 14 — SRE and Observability Engineer

```yaml
crewai_supported_work:
  - study verified reliability/monitoring LearningPacket
  - use validated incident and recovery memory
  - read approved logs, metrics, traces, and alert evidence
  - produce bounded operational recommendations

single_tool: ObservabilityReadTool
tool_permission: approved_logs_metrics_traces_read_only
llm_reasoning_effort: high

must_not:
  - change production environment
  - suppress alerts
  - claim root cause without evidence
  - expose sensitive logs

status: RESEARCH_REQUIRED
```

## Agent 15 — Independent Code Review, Documentation, and Release Auditor

```yaml
crewai_supported_work:
  - read run-branch diff, source records, LearningPackets, StudyReceipts, memory context, tests, security evidence, and documentation
  - verify that required knowledge was actually retrieved and studied
  - verify that memory did not override repository truth
  - return pass_pending_owner or blocked disposition

single_tool: ReleaseAuditTool
tool_permission: run_branch_repo_test_security_source_memory_evidence_read_only
llm_reasoning_effort: high

must_not:
  - edit code
  - approve its own prior work
  - merge or deploy
  - ignore missing knowledge, memory, source, or invocation evidence

status: RESEARCH_REQUIRED
```

# Common approval gate

```text
ROLE FACT CHECKED
→ CREWAI FEATURE SUPPORTED
→ LLM PROFILE TESTED
→ SINGLE TOOL TESTED
→ DRIVE KNOWLEDGE BEHAVIOR TESTED WHEN APPLICABLE
→ NOTION MEMORY CONTEXT TESTED
→ STRUCTURED OUTPUT AND SELF-DIAGNOSTIC TESTED
→ PERMISSION AND SECURITY TESTS PASSED
→ SEQUENTIAL CONTEXT TEST PASSED
→ APPROVED_FOR_IMPLEMENTATION
```

No agent in this file is enabled.
