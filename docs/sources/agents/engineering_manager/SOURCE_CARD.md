# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING`  
**Verified:** 2026-07-20

## Assigned source records

### LLM

- [Candidate LLM source card: Groq OpenAI GPT-OSS 120B](../../llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md)
- [Exact official model page](https://console.groq.com/docs/model/openai/gpt-oss-120b)

Current LLM status: `CANDIDATE_NOT_USED`

### Tool

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)
- [CrewAI official custom-tools documentation](https://docs.crewai.com/v1.15.4/en/learn/create-custom-tools.md)

Current tool status: `CONDITIONALLY_APPROVED`

## Agent research records

- [Agent 01 Tool Inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [GitHub Repository Read/Write Architecture](../../../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [Source Traceability Rule](../../../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)

## CrewAI sources

- [CrewAI Agents](https://docs.crewai.com/v1.15.4/en/concepts/agents.md)
- [CrewAI Tools](https://docs.crewai.com/v1.15.4/en/concepts/tools.md)
- [CrewAI Sequential Process](https://docs.crewai.com/v1.15.4/en/learn/sequential-process.md)
- [CrewAI Annotations](https://docs.crewai.com/v1.15.4/en/learn/using-annotations.md)
- [CrewAI MCP Overview](https://docs.crewai.com/v1.15.4/en/mcp/overview.md)
- [CrewAI MCP Security](https://docs.crewai.com/v1.15.4/en/mcp/security.md)

## Current capability decision

```yaml
role_concept: supported
strict_sequential_execution: supported
dynamic_delegation: rejected
assigned_tool_count: 1
repository_preflight_read: conditionally_supported
repository_write_for_agent_01: rejected_not_required
system_repository_write: planned_for_role_scoped_writer_agents
llm: not_approved
agent_implementation: not_started
```

## Source query result

A future deterministic query:

```text
source engineering_manager
```

must return this card and the exact LLM and tool links above. It must not reconstruct sources from model memory.

## Revalidation required when

- Agent role, goal, or boundaries change.
- The selected LLM changes.
- The tool schema or implementation changes.
- CrewAI version changes.
- GitHub repository integration changes.
- Any source link becomes outdated or unavailable.
