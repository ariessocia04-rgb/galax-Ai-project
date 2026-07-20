# Tool Source Card — Repository Preflight Tool

**Source ID:** `TOOL-repository-preflight`  
**Status:** `CONDITIONALLY_APPROVED`  
**Implementation:** `NOT_IMPLEMENTED`  
**Agent:** `engineering_manager`  
**Verified:** 2026-07-20

## Identity

```yaml
name: RepositoryPreflightTool
type: local_custom_crewai_tool
maintainer: Galax AI project
license: project_license_pending
cost_status: fully_free_self_hosted
network_access: false
write_access: false
```

This tool is a planned Galax custom tool. It does not yet have a release or implementation commit.

## CrewAI compatibility sources

- [CrewAI Agents](https://docs.crewai.com/v1.15.4/en/concepts/agents.md)
- [CrewAI Tools](https://docs.crewai.com/v1.15.4/en/concepts/tools.md)
- [Create Custom Tools](https://docs.crewai.com/v1.15.4/en/learn/create-custom-tools.md)
- [Using Annotations in crew.py](https://docs.crewai.com/v1.15.4/en/learn/using-annotations.md)
- [Sequential Processes](https://docs.crewai.com/v1.15.4/en/learn/sequential-process.md)
- [CrewAI Tasks and Guardrails](https://docs.crewai.com/v1.15.4/en/concepts/tasks.md)
- [CrewAI Documentation Index](https://docs.crewai.com/llms.txt)

## Capability evidence

The sources above support:

- Assigning designated tools to an agent.
- Creating local custom tools.
- Loading tools through CrewAI project configuration.
- Running tasks sequentially.
- Returning structured task output.
- Validating output with guardrails.

## Not proven by CrewAI documentation

The following behavior is Galax-specific and must be implemented and tested locally:

- Repository identity verification.
- Rule and plan hash verification.
- Secret-path exclusion.
- Symlink and path traversal rejection.
- Run-manifest validation.
- Agent and task approval validation.

## Exact design document

- [Agent 01 Tool Inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)

## Approval blockers

```text
- Custom tool code does not exist.
- Tool tests have not run.
- LLM tool-calling compatibility is not verified.
- Repository rule and plan files are incomplete.
```

## Revalidation triggers

Revalidate when CrewAI changes, the tool schema changes, the repository rules change, or the implementation commit changes.
