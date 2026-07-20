# CrewAI 1.15.4 Capability and Limitation Matrix

**Status:** `DRAFT_RESEARCH_RECORD`  
**Framework version:** `crewai==1.15.4`  
**Python:** `>=3.10,<3.14`  
**Reviewed:** 2026-07-20  
**Purpose:** Define what Galax may and may not assign to CrewAI agents.

## 1. Version evidence

- [CrewAI 1.15.4 on PyPI](https://pypi.org/project/crewai/)
- [CrewAI source repository](https://github.com/crewAIInc/crewAI)
- [Versioned CrewAI 1.15.4 agent documentation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)
- [CrewAI tasks documentation](https://docs.crewai.com/en/concepts/tasks)
- [CrewAI processes documentation](https://docs.crewai.com/en/concepts/processes)
- [CrewAI Flows documentation](https://docs.crewai.com/en/concepts/flows)
- [CrewAI memory documentation](https://docs.crewai.com/en/concepts/memory)
- [CrewAI checkpointing documentation](https://docs.crewai.com/en/concepts/checkpointing)
- [CrewAI MCP overview](https://docs.crewai.com/en/mcp/overview)
- [CrewAI MCP security](https://docs.crewai.com/en/mcp/security)

## 2. Capability classifications

```text
NATIVE_SUPPORTED
SUPPORTED_BY_CONFIGURATION
SUPPORTED_BY_CUSTOM_TOOL
SUPPORTED_BY_MCP
SUPPORTED_BY_FLOW
REQUIRES_EXTERNAL_SERVICE
REQUIRES_HUMAN_GATE
DEPRECATED
EARLY_RELEASE
UNSUPPORTED
UNKNOWN_UNTIL_LIVE_TEST
```

## 3. Core matrix

| Capability | CrewAI status | Galax decision | Required proof |
|---|---|---|---|
| Define agent role, goal, backstory | `NATIVE_SUPPORTED` | Allowed | Configuration load test |
| Assign an LLM to an agent | `NATIVE_SUPPORTED` | Allowed conditionally | Exact provider/model live test |
| Assign tools to an agent | `NATIVE_SUPPORTED` | Allowed conditionally | Exact tool invocation evidence |
| Use one role-specific tool interface | `SUPPORTED_BY_CONFIGURATION` | Required | Agent tool list contains exactly one interface |
| Sequential task order | `NATIVE_SUPPORTED` | Required | `Process.sequential` order test |
| Hierarchical manager/delegation | `NATIVE_SUPPORTED` | Rejected for Galax | Not applicable |
| Consensual process | `UNSUPPORTED` | Prohibited | Docs say planned, not implemented |
| Dynamic deterministic routing | `SUPPORTED_BY_FLOW` | Allowed outside active agent | Flow router tests |
| Flow state persistence | `SUPPORTED_BY_FLOW` | Secondary mechanism | Persistence/resume test |
| Native checkpointing | `EARLY_RELEASE` | Secondary only | Recovery and failure-path tests |
| Structured task output | `NATIVE_SUPPORTED` | Required where schema exists | Exact model Pydantic/JSON test |
| Function guardrails | `NATIVE_SUPPORTED` | Required | Guardrail pass/fail test |
| LLM guardrails | `NATIVE_SUPPORTED` | Advisory only | Never sole security gate |
| Agent self-diagnosis | `UNSUPPORTED_AS_GUARANTEE` | Custom pattern only | Schema + deterministic validator + auditor |
| Repository read/write | `SUPPORTED_BY_CUSTOM_TOOL_OR_MCP` | Role-scoped only | GitHub gateway tests |
| Internet research | `SUPPORTED_BY_TOOL_OR_MCP` | Evidence Researcher only | Search/fetch tool tests |
| Code execution through agent setting | `DEPRECATED` | Prohibited | Use external sandbox tool |
| External sandbox execution | `REQUIRES_EXTERNAL_SERVICE` | Planned local sandbox | Isolation and command tests |
| Database operations | `SUPPORTED_BY_TOOL_OR_MCP` | Local/test DB only initially | DB tool and permission tests |
| Browser automation | `SUPPORTED_BY_TOOL_OR_MCP` | Staging/local targets only | Browser tool tests |
| Production deployment | `REQUIRES_EXTERNAL_TOOL_AND_HUMAN_GATE` | Agent cannot authorize | CI/deploy tool plus owner approval |
| Pull-request merge | `REQUIRES_EXTERNAL_TOOL_AND_HUMAN_GATE` | Human only | No merge operation exposed to agents |
| Memory | `NATIVE_SUPPORTED` | Disabled initially | Local privacy-safe design required |
| Knowledge sources | `NATIVE_SUPPORTED` | Candidate only | Ingestion, retrieval, privacy tests |
| Multimodal understanding | `MODEL_DEPENDENT` | Not available with current Cerebras model | Current model has no vision |
| Accurate current facts without tool | `UNSUPPORTED` | Prohibited | Current facts require research tool |
| Guaranteed correctness/security | `UNSUPPORTED` | Prohibited claim | Tests and human review only |
| Background execution without process | `UNSUPPORTED` | Prohibited claim | Runtime must be actively running |

## 4. Agent execution controls available in CrewAI

CrewAI 1.15.4 exposes configuration fields including:

```text
llm
function_calling_llm
tools
max_iter
max_rpm
max_execution_time
allow_delegation
step_callback
cache
max_retry_limit
respect_context_window
multimodal
reasoning
max_reasoning_attempts
knowledge_sources
embedder
```

Galax must test every field used with the pinned model and cannot infer support from the field's existence alone.

## 5. Code execution limitation

The versioned CrewAI 1.15.4 agent documentation states:

```text
allow_code_execution and code_execution_mode are deprecated.
CodeInterpreterTool has been removed from crewai-tools.
Use a dedicated sandbox service for secure code execution.
```

Galax consequence:

```yaml
all_agents:
  allow_code_execution: false

coding_agents:
  execution_path: assigned_workspace_tool_to_external_sandbox
```

The LLM may propose a patch. Only the workspace tool may write it and run approved commands inside the sandbox.

## 6. Sequential process limitation

`Process.sequential` executes tasks in the predefined list order and can pass previous task output as context. It does not itself decide that an agent is necessary, create safe permissions, or validate business rules.

Galax consequence:

```text
Flow/application selects approved agents and tasks first.
CrewAI sequential process executes only that selected list.
```

No dynamic delegation or manager allocation occurs inside the Crew.

## 7. Structured output limitation

CrewAI tasks can declare `output_pydantic` or `output_json`, and can apply one or more guardrails. Guardrail failures can cause an LLM retry.

Limitations:

```text
- Provider/model support may be incorrectly detected or absent.
- LLM output may fail schema validation.
- A guardrail validates output; it does not prove external facts.
- Retries consume provider quota.
```

Galax settings:

```yaml
guardrail_max_retries: 1
max_retry_limit: 1
```

Tool use and strict output must be live-tested both separately and in the same task flow.

## 8. Tool-use reliability limitation

CrewAI can register and invoke tools. However, reliable execution depends on:

```text
- provider/model function-calling behavior
- exact schema compatibility
- agent loop behavior
- tool implementation
- network/service reliability
```

An official CrewAI issue documented a case where an agent generated a plausible tool observation without an actual tool call. The issue is closed as not planned, but it demonstrates why Galax requires trusted tool invocation IDs and output hashes rather than accepting agent narration.

Source:

- [CrewAI issue #3154: fabricated tool observation](https://github.com/crewAIInc/crewAI/issues/3154)

## 9. Context limitation

CrewAI can automatically summarize when context exceeds the model window if `respect_context_window=True`.

This is useful for broad research but unsafe for exact code, security, rules, migrations, or audit evidence because summarization may omit critical details.

Galax defaults:

```yaml
precision_agents:
  respect_context_window: false

context_strategy:
  - scoped_repository_search
  - relevant_file_chunks
  - structured_task_output
  - file_hashes
  - stage_checkpoints
```

When exact context cannot fit, stop with `BLOCKED_CONTEXT_LIMIT`.

## 10. Memory limitation

Current CrewAI memory documentation states:

```text
- default storage is LanceDB
- default embedder is OpenAI when no embedder is configured
- memory content is sent to the configured LLM for analysis
- some memory-analysis failures degrade gracefully without raising an exception
```

Galax decision:

```yaml
memory_enabled_initially: false
canonical_truth:
  - repository
  - Flow state
  - run ledger
  - tool evidence
  - Git history
```

Memory cannot approve a task, override repository rules, or serve as evidence that a fact is current.

## 11. Checkpoint limitation

CrewAI documents checkpointing as early release and says APIs may change. It also describes manual checkpoint writes as best-effort, with execution continuing if a write fails.

Galax decision:

```text
CrewAI checkpoint = optional secondary recovery aid
Galax run ledger + run branch commits = canonical recovery evidence
```

A failure to write the canonical Galax checkpoint stops the run.

## 12. MCP limitation

CrewAI supports MCP tools through local stdio and remote HTTP/SSE transports and supports tool filtering.

Security limitations:

```text
- server metadata can contain prompt injection
- remote servers require authentication
- credentials require least privilege
- the MCP server controls the actual external operation
- malformed responses and network failures remain possible
```

CrewAI's own security documentation states that malicious server metadata can affect the agent simply when tools are listed.

Current official open issues also report:

- an SSRF/DNS-rebinding concern affecting URL validation and MCP tool argument handling
- a request for a production MCP reliability layer
- a request for a framework-level governance hook for tool authorization

Sources:

- [CrewAI MCP security guidance](https://docs.crewai.com/en/mcp/security)
- [CrewAI issue #6504: SSRF and MCP URL validation](https://github.com/crewAIInc/crewAI/issues/6504)
- [CrewAI issue #6545: MCP reliability layer proposal](https://github.com/crewAIInc/crewAI/issues/6545)
- [CrewAI issue #5888: governance tool-authorization hook request](https://github.com/crewAIInc/crewAI/issues/5888)

Galax must enforce permission and validation inside every role-scoped tool wrapper; it cannot rely on a future CrewAI-wide governance feature.

## 13. LLM provider integration limitation

CrewAI has native SDK paths for some providers and uses LiteLLM for other providers. A provider prefix or adapter existing in source code proves a connection path, not complete feature compatibility.

For Cerebras, Galax must separately test:

```text
- model discovery
- system messages
- reasoning effort
- function call arguments
- tool-result round trip
- strict JSON schema
- Pydantic task output
- usage reporting
- timeout
- HTTP 429
- API version patch behavior
```

## 14. Free Cerebras limitation

Current official Cerebras documentation and terms establish:

```text
- Free access is a trial with free credits, not permanent unlimited service.
- General free-trial rate limits are account/provider controlled.
- The current gpt-oss-120b table documents 5 RPM, 30,000 TPM,
  1,000,000 TPH, and 1,000,000 TPD.
- The service and outputs are provided as-is and as-available.
- Cerebras may change fees or discontinue offerings.
- The free trial does not provide the enterprise uptime guarantees.
```

Sources:

- [Cerebras pricing](https://www.cerebras.ai/pricing)
- [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits)
- [Cerebras terms](https://www.cerebras.ai/terms-of-service)

Galax cannot promise monthly continuity based on this free provider.

## 15. Current exact model limitation

Candidate model:

```yaml
provider: Cerebras
model: gpt-oss-120b
crewai_model_id: cerebras/gpt-oss-120b
context_window_tokens: 131072
maximum_completion_tokens: 40960
reasoning: true
function_calling: true
structured_output: true
parallel_tool_calls: false
vision: false
```

Implications:

```text
- No agent may be assigned image or screenshot understanding through this LLM.
- Browser/UI agents need textual DOM/accessibility output from their tool.
- Only one tool call should be active at a time.
- Exact tool and structured-output behavior remains disabled until live tests pass.
```

## 16. Per-agent proof requirement

Each agent must have a capability contract containing:

```yaml
agent_id:
role:
required_crewai_features: []
required_llm_capabilities: []
required_tool_operations: []
required_permissions: []
unsupported_actions: []
human_gates: []
source_links: []
mandatory_tests: []
status:
```

No shared generic claim such as `CrewAI supports agents` is sufficient to approve an individual agent's actual task.

## 17. Final framework decision

```yaml
framework: crewai
version_candidate: 1.15.4
version_pinned_for_tests: false
framework_supported_for_bounded_assistant_tasks: true
framework_supported_as_unrestricted_autonomous_software_company: false
sequential_process_supported: true
tool_and_llm_compatibility_universally_guaranteed: false
production_ready: false
next_gate: PIN_INSTALL_AND_LIVE_COMPATIBILITY_SUITE
```
