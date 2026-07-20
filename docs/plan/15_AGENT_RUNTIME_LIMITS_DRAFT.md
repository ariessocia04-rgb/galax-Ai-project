# Galax 15-Agent Runtime Limits — Draft

**Status:** `DRAFT_MUTABLE`  
**Framework candidate:** CrewAI 1.15.4  
**LLM candidate:** `cerebras/gpt-oss-120b`  
**LLM status:** selected for validation, not enabled  
**Process:** `Process.sequential`

## 1. Provider facts vs Galax internal limits

### Current documented Cerebras model capacity

```yaml
model: gpt-oss-120b
context_window_tokens: 131072
maximum_completion_tokens: 40960
reasoning_effort:
  - low
  - medium
  - high
tool_calling: true
structured_outputs: true
vision: false
parallel_tool_calls: false
```

Official sources:

- [Cerebras supported models](https://inference-docs.cerebras.ai/models/overview)
- [Cerebras public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)

### Published general free-tier limits

```yaml
tokens_per_minute: 64000
tokens_per_hour: 1000000
tokens_per_day: 1000000
requests_per_minute: 30
requests_per_hour: 900
requests_per_day: 14400
```

Cerebras states that specific account limits can vary, and its model page notes temporary free-tier reductions for high-demand models. Therefore, these values are not hardcoded as guaranteed runtime capacity.

Source:

- [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits)

### Global Galax ceilings

```yaml
execution:
  active_agents: 1
  concurrent_llm_calls: 1
  async_tasks: false
  allow_delegation: false
  parallel_tool_calls: false

provider_control:
  internal_max_rpm: 4
  effective_rpm: minimum_of_internal_ceiling_and_current_account_limit_with_headroom
  maximum_retries: 1
  timeout_seconds: 120

context:
  low_or_medium_reasoning_input_soft_limit: 12000
  high_reasoning_input_soft_limit: 16000
  per_call_input_hard_limit: 20000
  respect_context_window: false

run_budget:
  soft_limit_total_tokens: 90000
  hard_limit_total_tokens: 120000
```

The internal `max_rpm: 4` is a conservative Galax policy, not a claim about the provider's permanent limit.

## 2. Agent table

| ID | Agent | One tool interface | Reasoning | Max output tokens | Max iterations | Max tool calls/task | Current status |
|---:|---|---|---|---:|---:|---:|---|
| 01 | Engineering Manager / Preflight | `RepositoryPreflightTool` | Low | 800 | 4 | 1 | Disabled; tool not implemented |
| 02 | Product Requirements and Scope Lead | `RequirementsWorkspaceTool` | Medium | 1,600 | 6 | 3 | Disabled; research required |
| 03 | Evidence and Capability Researcher | `VerifiedResearchWorkspaceTool` | High | 2,200 | 8 | 5 | Disabled; research gateway not implemented |
| 04 | Solution and Systems Architect | `ArchitectureWorkspaceTool` | High | 2,400 | 8 | 3 | Disabled; research required |
| 05 | UX, UI, and Accessibility Designer | `UXWorkspaceTool` | Medium | 1,600 | 6 | 3 | Disabled; research required |
| 06 | Frontend Application Engineer | `FrontendWorkspaceTool` | Medium | 2,000 | 8 | 3 | Disabled; sandbox required |
| 07 | Backend and API Engineer | `BackendWorkspaceTool` | High | 2,200 | 8 | 3 | Disabled; sandbox required |
| 08 | Data and Database Engineer | `DatabaseWorkspaceTool` | High | 2,200 | 8 | 3 | Disabled; disposable DB required |
| 09 | CrewAI and AI Systems Engineer | `CrewAIWorkspaceTool` | High | 2,400 | 8 | 3 | Disabled; pinned integration required |
| 10 | Integration and MCP Engineer | `IntegrationMCPWorkspaceTool` | High | 2,200 | 8 | 3 | Disabled; MCP security tests required |
| 11 | Security, Privacy, and AI Safety Engineer | `SecurityAuditTool` | High | 2,400 | 8 | 2 | Disabled; scanners not implemented |
| 12 | QA and Test Automation Engineer | `TestRunnerTool` | Medium | 1,800 | 8 | 3 | Disabled; test sandbox required |
| 13 | DevOps and CI/CD Engineer | `CIBuildWorkspaceTool` | Medium | 1,800 | 8 | 3 | Disabled; build sandbox required |
| 14 | SRE and Observability Engineer | `ObservabilityReadTool` | High | 2,200 | 8 | 2 | Disabled; approved telemetry source required |
| 15 | Independent Code Review, Documentation, and Release Auditor | `ReleaseAuditTool` | High | 2,200 | 8 | 2 | Disabled; evidence gateway required |

Tool-call ceilings are internal design values and must be verified against the exact task implementation. One tool interface may perform several closely related operations; it is still one assigned tool.

## 3. Agent-specific restrictions

### Agent 01 — Engineering Manager / Preflight

```text
May: interpret actual structured preflight evidence.
Must not: add agents, reorder tasks, delegate, write repository, self-approve.
```

### Agent 02 — Product Requirements and Scope Lead

```text
May: write requirements and acceptance criteria on a run branch.
Must not: invent requirements, approve scope, edit application code.
```

### Agent 03 — Evidence and Capability Researcher

```text
May: research official sources and update research/source records.
Must not: treat LLM memory or an aggregator as authority, install software,
approve implementation, or change production configuration.
```

During automatic revalidation, Agent 03 receives one ephemeral instance of the same approved research interface profile. It does not receive a second tool.

### Agent 04 — Solution and Systems Architect

```text
May: write architecture proposals and trade-off records.
Must not: edit implementation or unilaterally approve architecture.
```

### Agent 05 — UX, UI, and Accessibility Designer

```text
May: write design specifications and inspect approved local/staging UI.
Must not: edit production code, access production user data, or certify compliance.
```

### Agent 06 — Frontend Application Engineer

```text
May: edit frontend allowlisted paths and run approved commands in external sandbox.
Must not: use deprecated CrewAI code execution, edit backend/database/rules,
or write before a required StudyReceipt passes.
```

### Agent 07 — Backend and API Engineer

```text
May: edit backend/API allowlisted paths and run sandbox tests.
Must not: edit frontend, mutate production database, expose credentials,
or claim authorization correctness without tests.
```

### Agent 08 — Data and Database Engineer

```text
May: edit schema/migration paths and use disposable local/test database.
Must not: access production data, run destructive production migrations,
or treat generated SQL as validated.
```

### Agent 09 — CrewAI and AI Systems Engineer

```text
May: edit CrewAI Flow, task, schema, guardrail, and tested LLM configuration paths.
Must not: enable unsupported fields, change from sequential process,
enable native memory/deprecated code execution, or enable every agent automatically.
```

### Agent 10 — Integration and MCP Engineer

```text
May: implement scoped adapters and MCP servers using mocks/test credentials.
Must not: connect random public MCP servers, expose unrestricted URL fetch,
use production credentials, or claim reliability without failure tests.
```

### Agent 11 — Security, Privacy, and AI Safety Engineer

```text
May: perform approved read-only scans and threat analysis.
Must not: exploit unauthorized targets, mutate production, auto-fix findings,
or certify the system as secure.
```

### Agent 12 — QA and Test Automation Engineer

```text
May: write test paths and run approved tests in sandbox.
Must not: hide failures, delete tests without approval, or report pass without invocation evidence.
```

### Agent 13 — DevOps and CI/CD Engineer

```text
May: edit CI/build files and validate builds locally.
Must not: deploy production, edit repository secrets, enable paid infrastructure,
or merge automatically.
```

### Agent 14 — SRE and Observability Engineer

```text
May: read approved logs, metrics, and traces.
Must not: modify production, suppress alerts, expose sensitive logs,
or claim root cause without correlated evidence.
```

### Agent 15 — Independent Release Auditor

```text
May: reconcile run-branch, source, learning, memory, tool, test, and security evidence.
Must not: edit implementation, approve its own prior work, merge, or deploy.
```

## 4. Tool-call pattern

For ordinary writer agents, the intended maximum three calls are:

```text
1. inspect authorized workspace
2. apply one approved change set
3. verify committed change set and sandbox evidence
```

Agent 03 may need up to five calls because it must search, fetch, compare, record, and verify. Read-only auditors use fewer calls.

A tool call count increase changes the agent profile and triggers revalidation.

## 5. Token accounting

Count whenever available:

```text
input tokens
+ provider reasoning tokens
+ tool-result context tokens
+ output tokens
+ retry tokens
```

At the run soft limit:

```text
- do not start optional agents
- reuse verified evidence by ID/hash
- stop nonessential narrative expansion
- preserve required QA/security/audit work
```

At the hard limit:

```text
STATUS: BLOCKED_LLM_BUDGET
ACTION: save canonical checkpoint and stop new LLM calls
```

## 6. Context restrictions

```text
- Never send the entire repository.
- Never send all 15 prompts or tool schemas in one call.
- Never send `.env`, credentials, private keys, or production records.
- Send only current rules, task contract, bounded memory, LearningPacket,
  relevant repository excerpts, one tool schema, and required prior output.
```

When required exact context exceeds the hard limit:

```text
STATUS: BLOCKED_CONTEXT_LIMIT
ACTION: split into checkpointed sequential segments
```

## 7. Enablement gate

```text
ROLE FACT CHECKED
→ CREWAI FEATURE SUPPORTED
→ LLM PROFILE LIVE TESTED
→ ONE TOOL IMPLEMENTED AND LIVE TESTED
→ DOCKER/SANDBOX TESTS WHEN REQUIRED
→ DRIVE STUDY TEST WHEN REQUIRED
→ SUPABASE MEMORY CONTEXT TESTED
→ STRUCTURED OUTPUT AND SELF-DIAGNOSTIC TESTED
→ SECURITY/PERMISSION TESTS PASSED
→ SEQUENTIAL CONTEXT TEST PASSED
→ AUDITOR EVIDENCE PASSED
→ OWNER DECISION
```

No agent is currently enabled.
