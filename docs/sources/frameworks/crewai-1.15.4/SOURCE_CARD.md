# Framework Source Card — CrewAI 1.15.4

**Source ID:** `FRAMEWORK-crewai-1.15.4`  
**Status:** `SELECTED_FOR_PINNED_VALIDATION`  
**Approved for production:** No  
**Verified:** 2026-07-20

## Identity

```yaml
name: CrewAI
version: 1.15.4
package: crewai
python_requirement: ">=3.10,<3.14"
license: MIT
source_repository: crewAIInc/crewAI
candidate_source_commit: 69c0308f2cf4fa17214eab4db10071abc08602fd
```

## Exact official links

### Package and source

- [CrewAI 1.15.4 on PyPI](https://pypi.org/project/crewai/)
- [CrewAI source repository](https://github.com/crewAIInc/crewAI)
- [CrewAI license](https://github.com/crewAIInc/crewAI/blob/main/LICENSE)
- [CrewAI documentation](https://docs.crewai.com/)

### Versioned core documentation

- [Agents — versioned 1.15.4 source](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)
- [Tasks](https://docs.crewai.com/en/concepts/tasks)
- [Processes](https://docs.crewai.com/en/concepts/processes)
- [Flows](https://docs.crewai.com/en/concepts/flows)
- [Memory](https://docs.crewai.com/en/concepts/memory)
- [Checkpointing](https://docs.crewai.com/en/concepts/checkpointing)
- [LLM configuration](https://docs.crewai.com/en/concepts/llms)
- [MCP overview](https://docs.crewai.com/en/mcp/overview)
- [MCP security](https://docs.crewai.com/en/mcp/security)
- [Strategic LLM selection guide](https://docs.crewai.com/en/learn/llm-selection-guide)

## Confirmed supported framework functions

```text
- agent role, goal, and backstory
- agent LLM assignment
- agent tools and MCP tools
- custom tools
- sequential process
- hierarchical process
- Flow routing and state
- structured task output
- task guardrails
- callbacks and events
- memory and knowledge integrations
- checkpointing in early release
```

Each function still requires exact provider/tool and live compatibility tests.

## Confirmed limitations relevant to Galax

```text
- Built-in agent code execution settings are deprecated.
- CodeInterpreterTool was removed from crewai-tools.
- Consensual process is planned but not implemented.
- Sequential process follows task-list order; deterministic agent selection must be done outside the active Crew.
- Structured output support depends on the exact LLM/provider.
- Tool use reliability depends on the exact LLM/provider and tool implementation.
- Context-window handling may summarize content when enabled.
- Memory may call an analysis LLM and defaults to an OpenAI embedder when not configured.
- Checkpointing is early release and checkpoint write behavior may be best-effort.
- MCP metadata itself may contain prompt injection.
- CrewAI does not supply repository access, browser access, database access, or production permissions without tools.
```

## Official issue risk records

- [Issue #3154 — agent fabricated tool observation without invocation](https://github.com/crewAIInc/crewAI/issues/3154)
- [Issue #5888 — requested framework-level governance hook for tool authorization](https://github.com/crewAIInc/crewAI/issues/5888)
- [Issue #6504 — reported SSRF/DNS rebinding and MCP URL validation risks](https://github.com/crewAIInc/crewAI/issues/6504)
- [Issue #6545 — proposed MCP production reliability layer](https://github.com/crewAIInc/crewAI/issues/6545)

Open issue reports are risk evidence, not proof that every installation is vulnerable. Galax treats unresolved reports as mandatory test and mitigation inputs.

## Galax framework settings

```yaml
process: sequential
allow_delegation: false
async_tasks: false
parallel_agents: false
memory: false
allow_code_execution: false
respect_context_window: false
max_retry_limit: 1
guardrail_max_retries: 1
```

These are planning defaults and remain disabled until pinned-environment tests pass.

## Required framework validation

```text
CRW-001 install exact 1.15.4 package
CRW-002 verify package hashes and lockfile
CRW-003 load classic YAML or selected project format without mixing formats
CRW-004 construct one agent and one task
CRW-005 run Process.sequential in exact order
CRW-006 pass structured Pydantic output
CRW-007 enforce deterministic function guardrail
CRW-008 call one actual custom tool
CRW-009 preserve trusted tool invocation evidence
CRW-010 reject fabricated tool-success claim
CRW-011 enforce max iterations, retries, RPM, and execution time
CRW-012 stop on context overflow with summarization disabled
CRW-013 preserve task context only as configured
CRW-014 persist canonical Galax checkpoint
CRW-015 verify no hidden memory/embedder calls
CRW-016 verify no deprecated code execution path
CRW-017 validate MCP tool filtering in isolated test
CRW-018 validate malicious MCP metadata and URL protections
CRW-019 verify only selected agents are instantiated
CRW-020 verify blocked stage prevents all downstream tasks
```

Approval requires 20/20 tests.

## Current decision

```yaml
framework_identity_verified: true
version_documented: true
source_links_recorded: true
bounded_sequential_assistant_use_supported: true
unrestricted_autonomous_company_use_supported: false
live_validation_completed: false
approved: false
```
