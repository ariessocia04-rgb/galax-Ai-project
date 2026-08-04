# CrewAI 1.15.4 Capability and Limitation Matrix

**Status:** `RESEARCH_RECORD`  
**Verified:** 2026-07-20  
**Framework:** CrewAI `1.15.4`  
**Decision:** CrewAI is the orchestration and bounded-agent framework. External systems provide repository, research, knowledge, memory, browser, database, test, security, and sandbox capabilities.

## 1. Support classifications

```text
NATIVE_SUPPORTED
SUPPORTED_BY_CONFIGURATION
SUPPORTED_BY_FLOW
SUPPORTED_BY_CUSTOM_TOOL_OR_MCP
REQUIRES_EXTERNAL_SERVICE
MODEL_DEPENDENT
EARLY_RELEASE
DEPRECATED
UNSUPPORTED
UNKNOWN_UNTIL_LIVE_TEST
```

## 2. Core matrix

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
| Google Drive learning material | `SUPPORTED_BY_EXTERNAL_API_OR_TOOL` | Flow-managed read-only knowledge gateway | Drive search/export/LearningPacket tests |
| Notion as native CrewAI memory backend | `NOT_PROVEN` | Prohibited claim | No native provider approval exists in project evidence |
| Notion as external structured memory | `SUPPORTED_BY_EXTERNAL_API_OR_MCP` | Flow-managed dedicated memory gateway | Notion schema/read/write/security tests |
| Code execution through agent setting | `DEPRECATED` | Prohibited | Use external sandbox tool |
| External sandbox execution | `REQUIRES_EXTERNAL_SERVICE` | Planned local sandbox | Isolation and command tests |
| Database operations | `SUPPORTED_BY_TOOL_OR_MCP` | Local/test DB only initially | DB tool and permission tests |
| Browser automation | `SUPPORTED_BY_TOOL_OR_MCP` | Staging/local targets only | Browser tool tests |
| Production deployment | `REQUIRES_EXTERNAL_TOOL_AND_HUMAN_GATE` | Agent cannot authorize | CI/deploy tool plus owner approval |
| Pull-request merge | `REQUIRES_EXTERNAL_TOOL_AND_HUMAN_GATE` | Human only | No merge operation exposed to agents |
| CrewAI native memory | `NATIVE_SUPPORTED` | Disabled initially | Local privacy-safe design required |
| Knowledge sources | `NATIVE_SUPPORTED` | Not selected for raw Drive ingestion initially | Ingestion, retrieval, privacy, and version tests |
| Multimodal understanding | `MODEL_DEPENDENT` | Not available with current Cerebras model | Current model has no vision |
| Accurate current facts without tool | `UNSUPPORTED` | Prohibited | Current facts require research tool |
| Guaranteed correctness/security | `UNSUPPORTED` | Prohibited claim | Tests and human review only |
| Background execution without process | `UNSUPPORTED` | Prohibited claim | Runtime must be actively running |

## 3. Agent execution controls available in CrewAI

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

## 4. Code execution limitation

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

## 5. Sequential process limitation

`Process.sequential` executes tasks in the predefined list order and can pass previous task output as context. It does not itself decide that an agent is necessary, create safe permissions, retrieve Google Drive knowledge, query Notion memory, or validate business rules.

Galax consequence:

```text
Flow/application performs preflight, memory retrieval, knowledge retrieval,
agent selection, branch creation, and permission setup first.
CrewAI sequential process executes only the selected task list.
```

No dynamic delegation or manager allocation occurs inside the Crew.

## 6. Structured output limitation

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

## 7. Tool-use reliability limitation

CrewAI can register and invoke tools. Reliable execution still depends on:

```text
- exact model tool-calling behavior
- valid tool schema
- actual invocation evidence
- tool timeout and error behavior
- result validation
- prompt-injection resistance
```

A correct-looking answer is not proof that a tool executed. Galax requires trusted invocation IDs, actual tool results, and deterministic evidence comparison.

## 8. Google Drive knowledge limitation

CrewAI does not automatically understand the user's Google Drive. Drive access requires an authenticated API or tool.

The selected Galax design does not expose Drive directly to every agent. The Flow uses a read-only `DriveKnowledgeGateway` to search approved roots, retrieve content, and build a verified `LearningPacket`.

Drive file titles are not trusted. The gateway uses body text, metadata, folders, labels, properties, versions, and content hashes. Google Drive `fullText` search is lexical; semantic relevance is not guaranteed without an additional tested retrieval layer.

## 9. Notion memory limitation

Notion is not treated as CrewAI native memory.

The supported integration path is:

```text
CrewAI Flow/application
→ dedicated Notion memory gateway
→ official Notion API
→ scoped Galax memory data source/pages
```

Agents receive bounded verified memory context. They do not browse the entire workspace or write memory directly.

The hosted Notion MCP proves an MCP interoperability path, but broad user-level workspace access makes it unsuitable as the initial unattended memory-write default.

## 10. Memory and knowledge distinction

```text
Google Drive knowledge:
  owner-provided tutorials and reference material used before implementation

Notion memory:
  validated decisions, lessons, failures, checkpoints, and reusable evidence

GitHub repository:
  current source of truth
```

Neither Drive nor Notion can override active repository rules, current official documentation, or live test evidence.

## 11. Current framework decision

```yaml
CrewAI_version: 1.15.4
status: SELECTED_FOR_PINNED_VALIDATION
sequential_process: required
agent_delegation: disabled
async_tasks: disabled
built_in_code_execution: prohibited
CrewAI_native_memory: disabled_initially
Drive_knowledge_gateway: specified_not_implemented
Notion_external_memory_gateway: specified_not_implemented
production_ready: false
```
