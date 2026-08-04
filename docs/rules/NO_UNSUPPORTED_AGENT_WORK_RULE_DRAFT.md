# No Unsupported Agent Work Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This rule may be revised after framework, provider, tool, and live integration tests.  
**Applies to:** ChatGPT planning, CrewAI Flows, Crews, agents, tasks, LLM profiles, tools, MCP servers, memory, knowledge, checkpoints, repository operations, and human approval gates.

## 1. Non-negotiable rule

```text
Never assign a CrewAI agent work that the complete verified runtime cannot perform.
```

A professional-sounding role, goal, backstory, or prompt does not create a technical capability.

A task is allowed only when every required layer is proven:

```text
CREWAI FRAMEWORK SUPPORT
AND EXACT PINNED VERSION SUPPORT
AND EXACT LLM/PROVIDER SUPPORT
AND ASSIGNED TOOL SUPPORT
AND REQUIRED PERMISSION SUPPORT
AND DETERMINISTIC FLOW SUPPORT
AND FAILURE HANDLING SUPPORT
AND LIVE TEST EVIDENCE
AND HUMAN GATE WHEN REQUIRED
```

If any layer is missing, unknown, deprecated, untested, or incompatible:

```yaml
status: BLOCKED_UNSUPPORTED_CAPABILITY
action:
  - do_not_start_agent
  - do_not_simulate_success
  - do_not_invent_tool_output
  - record_missing_capability
  - return_required_remedy
```

## 2. What a CrewAI agent actually is

A Galax CrewAI agent is an LLM-driven assistant assigned to one bounded task and one role-specific tool interface.

It is not:

```text
- a real employee
- a licensed professional
- a human engineering manager
- an independent operating system
- a background worker that continues without a running process
- a guaranteed source of facts
- a security certification authority
- a deployment authority
- a database administrator with inherent access
- a browser, shell, GitHub client, test runner, or code sandbox by itself
```

The role and backstory instruct behavior. They do not prove experience, identity, certification, access, or ability.

Agent descriptions must use wording such as:

```text
Operate using the documented practices expected from a senior practitioner.
```

They must not claim:

```text
I have ten years of real employment experience.
I am certified.
I personally tested this in production.
I guarantee this implementation is secure or bug-free.
```

## 3. Capability ownership

```yaml
crewAI_agent:
  owns:
    - bounded_reasoning
    - instruction_following
    - tool_selection_within_assigned_interface
    - structured_response_generation

crewAI_flow_or_trusted_application:
  owns:
    - run_creation
    - deterministic_agent_selection
    - execution_order
    - conditional_routing
    - branch_creation
    - checkpoint_policy
    - token_budget
    - retry_policy
    - permission_profiles
    - human_approval_gates
    - draft_pull_request_creation

tool_or_mcp_gateway:
  owns:
    - repository_read_write
    - public_web_access
    - test_execution
    - database_access
    - browser_operations
    - security_scanning
    - external_api_calls
    - sandbox_execution

human_owner:
  owns:
    - final_scope_decision
    - architecture_acceptance
    - risk_acceptance
    - production_credentials
    - production_deployment
    - destructive_migration_approval
    - pull_request_merge
```

## 4. Research before design

Before ChatGPT creates or edits an agent, task, LLM profile, tool, or Flow stage, it must:

```text
1. Read the current repository README.
2. Read all active rules and plans.
3. Read the current agent source card and research records.
4. Verify the currently pinned CrewAI version.
5. Read the matching versioned CrewAI documentation.
6. Inspect relevant CrewAI source code when documentation is insufficient.
7. Search current open and recently closed official CrewAI issues for the exact feature.
8. Verify the exact LLM provider and model documentation.
9. Verify the exact tool or MCP implementation and permissions.
10. Identify security, context, rate, token, reliability, and deprecation limits.
11. Define deterministic tests.
12. Record source links and evidence in the repository.
13. Leave the capability disabled until all mandatory tests pass.
```

Community examples may reveal risks but cannot by themselves approve a capability.

## 5. Triple-verification standard

A capability claim must be verified through three independent evidence layers where available:

```yaml
verification_layers:
  documentation:
    required: true
    source: official_versioned_documentation

  implementation:
    required: true
    source: official_source_code_or_exact_dependency_adapter

  execution:
    required: true
    source: live_test_in_pinned_environment
```

When source code is not available, provider API behavior and a live test replace the implementation layer.

The status values are:

```text
DOCUMENTED_ONLY
SOURCE_CONFIRMED_NOT_TESTED
LIVE_TESTED
APPROVED_FOR_AGENT
UNSUPPORTED
DEPRECATED
BLOCKED_UNKNOWN
REVALIDATION_REQUIRED
```

Only `APPROVED_FOR_AGENT` permits production agent configuration.

## 6. CrewAI process boundary

Galax uses:

```yaml
process: Process.sequential
allow_delegation: false
async_execution: false
parallel_agents: false
concurrent_llm_calls: 1
```

The selected tasks run in the predetermined task-list order.

Agents must not:

```text
- dynamically add agents
- dynamically reorder tasks
- create hidden subtasks outside the manifest
- delegate to another agent
- switch to a hierarchical manager
- run in parallel
- continue after a blocking guardrail or tool failure
```

Conditional agent selection and stage routing belong to deterministic Flow/application code before the sequential Crew is constructed.

## 7. LLM is not a tool

```text
LLM != TOOL
```

The LLM provides language reasoning and tool-call arguments. It does not automatically provide:

```text
- internet access
- repository access
- file modification
- command execution
- test execution
- database access
- current factual knowledge
- secure authentication
```

Every external action requires the assigned tool interface and successful tool evidence.

## 8. One agent, one tool interface

Each agent may receive exactly one role-specific tool interface.

```yaml
agent:
  llm_profiles: 1
  tool_interfaces: 1
```

The interface may contain only closely related operations required by that role. The LLM must not receive every underlying GitHub, filesystem, browser, database, or security function.

A required capability outside the assigned interface results in:

```yaml
status: DELEGATION_TO_DIFFERENT_STAGE_REQUIRED
action: return_to_deterministic_flow
```

The Flow may select a different approved agent in a later sequential stage. The active agent cannot directly call another agent's tool.

## 9. Mandatory tool evidence

An agent may not claim an external action occurred based on its own narration.

A successful action requires:

```yaml
tool_evidence:
  actual_tool_invocation_id:
  tool_name:
  operation:
  input_hash:
  status:
  output_hash:
  affected_resources: []
  timestamp:
```

If a model writes text such as `Action`, `Observation`, `test passed`, `file saved`, or `commit created` without matching trusted tool evidence:

```text
STATUS: FAILED_FABRICATED_TOOL_RESULT
```

Tool calls must be tested with the exact provider/model because model behavior can differ even when the framework accepts the tool schema.

## 10. Code execution limitation

CrewAI 1.15.4 documents `allow_code_execution` and `code_execution_mode` as deprecated and states that `CodeInterpreterTool` was removed from `crewai-tools`.

Therefore:

```yaml
agent_settings:
  allow_code_execution: false
  code_execution_mode: not_used
```

No agent may be assigned code execution unless its single approved workspace tool calls a separately tested external sandbox.

The sandbox must enforce:

```text
- rootless or equivalent isolation
- no privileged mode
- no host shell
- no host network by default
- no secret mounts
- exact repository/worktree scope
- CPU, memory, process, and time limits
- command allowlist
- output capture
- forced cleanup
```

Without the sandbox:

```text
STATUS: BLOCKED_SANDBOX_NOT_AVAILABLE
```

## 11. Repository limitation

CrewAI does not inherently read or write the Galax GitHub repository.

Repository capability requires the approved role-scoped repository gateway, credentials, path policy, branch policy, and GitHub API tests.

An implementation agent may write only when all are true:

```text
- run branch exists
- expected branch SHA matches
- task manifest permits writing
- agent role permits writing
- path is allowlisted
- path is not protected
- content passed secret scanning
- repository gateway returned success
```

No agent may directly write to `main`, force push, merge, modify secrets, or alter production credentials.

## 12. Web and factual research limitation

An LLM's internal knowledge is not accepted as current research.

Current or niche facts require the approved research tool and source records.

The Evidence Researcher may claim a fact only when the output includes:

```yaml
claim:
source_url:
source_owner:
published_or_updated_date:
retrieved_date:
source_type:
relevant_excerpt_or_structured_fact:
limitations:
```

No research tool means:

```text
STATUS: BLOCKED_RESEARCH_TOOL_UNAVAILABLE
```

## 13. Structured output limitation

CrewAI supports `output_pydantic`, `output_json`, and task guardrails. This does not prove that every provider/model reliably supports strict structured output.

Approval requires separate live tests for:

```text
- ordinary completion
- strict JSON schema output
- Pydantic conversion
- tool call only
- tool-result round trip
- tool call plus final structured task output
- malformed output recovery
```

A Pydantic declaration is a validation requirement, not a guarantee that the LLM will comply on the first attempt.

## 14. Guardrail limitation

Guardrails validate task output. They do not automatically prove factual correctness, code correctness, tool authorization, security, or production safety.

Galax uses deterministic function guardrails for machine-checkable requirements. LLM-based guardrails may assist with subjective review but cannot be the only security or correctness gate.

```yaml
guardrail_max_retries: 1
```

On the second failure:

```text
STATUS: FAILED_GUARDRAIL
ACTION: checkpoint_and_stop
```

## 15. Context-window limitation

CrewAI can summarize conversation history when `respect_context_window=True`. Summarization may remove exact paths, code details, requirements, constraints, or evidence.

For repository rules, architecture, code, security, database, migration, and audit tasks:

```yaml
respect_context_window: false
```

Galax must instead use scoped retrieval, chunking, hashes, and checkpointed structured outputs. When required context cannot fit:

```text
STATUS: BLOCKED_CONTEXT_LIMIT
```

No agent may silently continue using automatically summarized evidence for a precision-critical task.

## 16. Memory limitation

CrewAI memory is supporting context, not repository truth.

The current CrewAI memory documentation states that memory content may be sent to its configured analysis LLM and that a missing embedder configuration defaults to OpenAI. Memory analysis can also degrade gracefully without raising when its LLM fails.

Initial Galax rule:

```yaml
crewai_memory:
  enabled: false
  reason:
    - avoid unapproved OpenAI default embedder
    - avoid hidden external LLM calls
    - avoid stale memory overriding repository files
```

Until a local memory design is independently approved, use:

```text
repository records
+ Flow state
+ run manifest
+ task outputs
+ tool evidence
+ Git commit history
```

## 17. Checkpoint limitation

CrewAI checkpointing is documented as early release and its APIs may change. Checkpoint writes are also described as best-effort, where a write failure may be logged while execution continues.

Therefore, native checkpointing may be used only as a secondary convenience.

The canonical recovery record is:

```text
run ledger
+ committed run branch
+ task evidence files
+ exact last completed stage
+ provider usage record
```

A failed canonical checkpoint write must stop the run even if CrewAI native checkpointing would continue.

## 18. MCP limitation and security

CrewAI can expose MCP server tools to agents. Connecting to an MCP server does not prove that the server is safe, reliable, authorized, or resistant to prompt injection.

CrewAI's MCP security guidance warns that malicious tool metadata can influence an agent merely when tools are listed. Current official issue reports also identify unresolved risks around MCP URL handling and SSRF validation.

Rules:

```text
- no unknown public MCP server
- no full unfiltered server toolset
- prefer local stdio
- exact tool allowlist
- exact version or commit pin
- strong authentication for remote servers
- least-privilege credentials
- validate all URL and file arguments in the gateway
- deny private/internal network destinations unless explicitly required
- verify response schema
- timeout every call
- no automatic retry for non-idempotent writes
```

## 19. Human approval limitation

CrewAI can request or pause for human input, but an LLM cannot replace the owner for high-risk decisions.

Mandatory human approval before:

```text
- changing project scope
- accepting architecture risk
- modifying repository rules
- enabling a new LLM/provider/tool
- writing production credentials
- running destructive database operations
- deploying to production
- merging a pull request
- accepting unresolved security findings
```

## 20. Self-diagnostic limitation

CrewAI does not provide a magical guarantee that an agent accurately diagnoses itself.

A Galax self-diagnostic is implemented as:

```text
structured task output
→ deterministic function guardrail
→ actual tool evidence comparison
→ downstream QA
→ independent release audit
```

The agent's own `PASS` value never constitutes final approval.

## 21. Free-provider limitation

A free trial or free tier is not permanent infrastructure.

For Cerebras:

```text
- limits can vary by account
- limits and pricing can change
- free credits can be exhausted
- service is provided as-is and as-available
- no automatic provider fallback is permitted
- production approval requires live tests after provider/API changes
```

When quota, credits, service, or exact model access is unavailable:

```text
STATUS: BLOCKED_LLM_UNAVAILABLE
ACTION: save_canonical_checkpoint_and_stop
```

Never create additional accounts or keys to bypass limits.

## 22. Per-stage capability gate

Before each stage, trusted Flow/application code checks:

```yaml
stage_gate:
  agent_status: APPROVED_FOR_IMPLEMENTATION
  llm_profile_status: APPROVED
  tool_status: APPROVED
  tool_permission_profile_matches: true
  input_schema_valid: true
  required_repository_hashes_match: true
  provider_available: true
  provider_budget_available: true
  required_human_gate_present: true
```

Any `false` result stops the stage.

## 23. Completion standard

An agent task is complete only when:

```text
- exact expected output schema validates
- required tool actually executed
- tool evidence matches the claimed result
- required tests or scans ran
- no prohibited operation occurred
- self-diagnostic validates
- downstream acceptance gate passes
- all remaining assumptions and risks are explicit
```

Generated prose alone is never completion evidence.

## 24. Meaning of 100% fact-checked

Galax must not promise that an AI framework, model, or agent will work perfectly forever.

The allowed statement is:

```text
100% of the defined documentation, source-code, compatibility, security,
and execution tests passed for the exact pinned environment and recorded date.
```

Any version, provider, model, schema, tool, permission, or infrastructure change triggers:

```text
REVALIDATION_REQUIRED
```
