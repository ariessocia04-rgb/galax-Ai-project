# Galax 15-Agent Capability Mapping — Draft

**Status:** `DRAFT_MUTABLE`  
**Process:** `Process.sequential`  
**Current LLM candidate:** `cerebras/gpt-oss-120b`  
**Rule:** An agent is enabled only after its role, LLM profile, single tool, permissions, and tests are approved.

## Global execution model

```text
One owner prompt
→ deterministic Flow/application preflight
→ select necessary approved agents only
→ construct one sequential Crew segment
→ one agent and one LLM call at a time
→ one role-specific tool interface per agent
→ structured output and self-diagnostic
→ deterministic validation
→ next selected stage
```

No agent is a fully autonomous employee. Every agent is a bounded AI assistant.

## Agent 01 — Engineering Manager / Preflight

```yaml
crewai_supported_work:
  - summarize deterministic repository preflight result
  - identify blocking rule, plan, agent, task, or approval-gate failures
  - return structured continue_or_stop decision

single_tool: RepositoryPreflightTool
tool_permission: repository_read_only
llm_reasoning_effort: low

must_not:
  - dynamically select or add agents
  - reorder tasks
  - delegate
  - modify repository
  - approve its own output
  - claim that missing evidence passed

status: CONDITIONALLY_COMPATIBLE
```

The deterministic Flow creates the manifest; Agent 01 only interprets the trusted preflight result.

## Agent 02 — Product Requirements and Scope Lead

```yaml
crewai_supported_work:
  - convert owner request and verified repository context into requirements
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

status: RESEARCH_REQUIRED
```

Human owner approves final scope.

## Agent 03 — Evidence and CrewAI Capability Researcher

```yaml
crewai_supported_work:
  - use approved research interface
  - compare official sources
  - record links, dates, capabilities, limitations, and contradictions
  - produce source-backed capability decisions

single_tool: VerifiedResearchTool
tool_permission: public_web_research_and_source_registry_write
llm_reasoning_effort: high

must_not:
  - use LLM memory as current evidence
  - cite unverified links
  - install tools
  - edit implementation
  - approve a capability without live-test requirements

status: RESEARCH_REQUIRED
```

Current facts require actual tool evidence.

## Agent 04 — Solution and Systems Architect

```yaml
crewai_supported_work:
  - analyze approved requirements and repository architecture
  - propose bounded architecture changes
  - identify components, contracts, dependencies, tradeoffs, and failure modes
  - produce an architecture decision proposal

single_tool: ArchitectureWorkspaceTool
tool_permission: architecture_docs_scoped_write
llm_reasoning_effort: high

must_not:
  - claim an architecture is proven without implementation/test evidence
  - alter source code
  - approve security or production readiness
  - override owner architecture decisions

status: RESEARCH_REQUIRED
```

Architecture acceptance requires the owner.

## Agent 05 — UX, UI, and Accessibility Designer

```yaml
crewai_supported_work:
  - analyze textual requirements and tool-provided DOM/accessibility evidence
  - define user flows, states, component behavior, keyboard behavior, and accessibility criteria
  - write bounded design specifications

single_tool: UXInspectionWorkspaceTool
tool_permission: design_docs_write_and_textual_ui_inspection
llm_reasoning_effort: medium

must_not:
  - claim to see images or screenshots through current text-only LLM
  - modify production frontend code
  - claim accessibility compliance without automated and manual evidence

status: RESEARCH_REQUIRED
```

Current Cerebras GPT-OSS 120B model has no documented vision capability. Visual evidence must be converted by the tool into approved textual evidence or the task is blocked.

## Agent 06 — Frontend Application Engineer

```yaml
crewai_supported_work:
  - inspect approved frontend paths
  - generate and apply scoped patches through the tool
  - run allowlisted frontend checks in an external sandbox
  - report actual changed files and test evidence

single_tool: FrontendWorkspaceTool
tool_permission: frontend_paths_write_on_run_branch
llm_reasoning_effort: medium

must_not:
  - use deprecated CrewAI built-in code execution
  - edit backend, database, rules, or workflow paths
  - claim tests passed without tool evidence
  - deploy or merge

status: RESEARCH_REQUIRED
```

The tool—not the agent—performs repository writes and sandbox execution.

## Agent 07 — Backend and API Engineer

```yaml
crewai_supported_work:
  - inspect approved backend paths
  - implement approved API/domain changes through the tool
  - run allowlisted backend tests in the sandbox
  - report contracts, error paths, and evidence

single_tool: BackendWorkspaceTool
tool_permission: backend_paths_write_on_run_branch
llm_reasoning_effort: high

must_not:
  - access production secrets
  - change database schema unless approved and delegated to Agent 08 stage
  - deploy
  - claim authorization correctness without tests and security review

status: RESEARCH_REQUIRED
```

## Agent 08 — Data and Database Engineer

```yaml
crewai_supported_work:
  - inspect schema and migration files
  - propose and apply approved migrations on a run branch
  - execute migration and rollback tests against a disposable local database
  - analyze constraints and concurrency evidence

single_tool: DatabaseSandboxTool
tool_permission: migration_paths_and_disposable_database
llm_reasoning_effort: high

must_not:
  - connect to production database
  - execute destructive production operation
  - approve data loss
  - bypass owner migration gate

status: RESEARCH_REQUIRED
```

## Agent 09 — CrewAI and AI Systems Engineer

```yaml
crewai_supported_work:
  - configure approved agents, tasks, sequential crews, Flows, schemas, and guardrails
  - integrate only verified LLM profiles and tools
  - run pinned CrewAI compatibility tests

single_tool: CrewAIWorkspaceTool
tool_permission: crewai_configuration_and_tests
llm_reasoning_effort: high

must_not:
  - assume a provider prefix proves full compatibility
  - enable untested agent profiles
  - switch process to hierarchical
  - enable delegation, async tasks, memory, or code execution without approval

status: RESEARCH_REQUIRED
```

## Agent 10 — Integration and MCP Engineer

```yaml
crewai_supported_work:
  - build and test local role-scoped MCP/tool wrappers
  - validate schemas, authentication, timeouts, retries, and response handling
  - pin exact server versions and tool filters

single_tool: MCPDevelopmentSandboxTool
tool_permission: local_mcp_source_and_test_environment
llm_reasoning_effort: high

must_not:
  - connect untrusted public MCP servers
  - expose a full unfiltered server toolset
  - bypass URL, file, network, or permission validation
  - use production credentials

status: RESEARCH_REQUIRED
```

Current CrewAI MCP security guidance and open issues require Galax-side validation rather than trusting the framework or server by default.

## Agent 11 — Security, Privacy, and AI Safety Engineer

```yaml
crewai_supported_work:
  - interpret approved scan results and architecture evidence
  - conduct structured threat analysis
  - identify risks, affected paths, severity rationale, and required remediation

single_tool: SecurityScanTool
tool_permission: scan_approved_run_branch_and_local_test_target
llm_reasoning_effort: high

must_not:
  - certify the system secure
  - exploit production targets
  - modify implementation automatically
  - accept residual risk
  - scan unauthorized systems

status: RESEARCH_REQUIRED
```

Security scanners and deterministic tests generate primary evidence; LLM analysis is advisory.

## Agent 12 — QA and Test Automation Engineer

```yaml
crewai_supported_work:
  - generate bounded test specifications
  - execute allowlisted tests through the tool
  - compare actual outputs with acceptance criteria
  - report reproducible failures and evidence

single_tool: TestRunnerTool
tool_permission: test_paths_write_and_sandbox_test_execution
llm_reasoning_effort: medium

must_not:
  - edit implementation to force passing tests
  - delete failing tests
  - claim absence of bugs
  - approve release alone

status: RESEARCH_REQUIRED
```

## Agent 13 — DevOps and CI/CD Engineer

```yaml
crewai_supported_work:
  - inspect and propose CI/build configuration
  - validate configuration in a local or approved test environment
  - produce build and rollback evidence

single_tool: CIWorkspaceTool
tool_permission: ci_paths_scoped_write_without_production_deploy
llm_reasoning_effort: medium

must_not:
  - access production secrets
  - deploy production
  - edit branch protection
  - enable paid infrastructure
  - merge

status: RESEARCH_REQUIRED
```

## Agent 14 — SRE and Observability Engineer

```yaml
crewai_supported_work:
  - analyze tool-provided logs, metrics, traces, and health-check results
  - propose alert, SLO, recovery, and runbook improvements
  - write observability documentation or approved configuration

single_tool: ObservabilityWorkspaceTool
tool_permission: read_only_telemetry_and_scoped_observability_docs
llm_reasoning_effort: high

must_not:
  - claim real-time production awareness without connected telemetry
  - restart production systems
  - change production infrastructure
  - guarantee uptime

status: RESEARCH_REQUIRED
```

## Agent 15 — Independent Code Review, Documentation, and Release Auditor

```yaml
crewai_supported_work:
  - inspect final run-branch diff and structured evidence
  - cross-check requirements, tests, scans, documentation, and unresolved risks
  - issue a structured review disposition

single_tool: ReleaseAuditTool
tool_permission: run_branch_and_evidence_read_only
llm_reasoning_effort: high

must_not:
  - edit files
  - run implementation fixes
  - merge
  - deploy
  - accept risk
  - approve its own prior work

status: RESEARCH_REQUIRED
```

Allowed disposition:

```text
REVIEW_PASS_PENDING_OWNER
REVIEW_FAIL
BLOCKED_MISSING_EVIDENCE
```

## Stage-selection rule

Only agents required by the current manifest are instantiated.

Examples:

```yaml
documentation_only:
  agents:
    - engineering_manager
    - product_requirements_lead
    - release_auditor

frontend_change:
  agents:
    - engineering_manager
    - product_requirements_lead
    - ux_accessibility_designer
    - frontend_engineer
    - qa_test_engineer
    - release_auditor

backend_database_change:
  segment_1:
    - engineering_manager
    - product_requirements_lead
    - solution_architect
    - backend_api_engineer
  segment_2:
    - database_engineer
    - security_privacy_engineer
    - qa_test_engineer
    - release_auditor
```

Segments remain sequential and checkpointed.

## Approval rule

An agent changes from `RESEARCH_REQUIRED` to `APPROVED_FOR_IMPLEMENTATION` only after:

```text
ROLE FACT CHECK
→ CREWAI CAPABILITY CHECK
→ LLM PROFILE 15/15 TESTS
→ SINGLE TOOL TESTS
→ PERMISSION TESTS
→ FAILURE TESTS
→ SELF-DIAGNOSTIC TESTS
→ SEQUENTIAL INTEGRATION TEST
→ SECURITY REVIEW
→ OWNER APPROVAL
```
