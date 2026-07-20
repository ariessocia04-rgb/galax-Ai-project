# External AI Contributor Command Design Survey

**Date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `RESEARCH_COMPLETE_ROLE_PACKS_NOT_ACTIVATED`

## Purpose

Define a professional, understandable, repository-first command standard for the five paper-qualified external development contributors:

- Cline;
- OpenHands Core;
- Aider;
- mini-SWE-agent;
- PR-Agent.

These are external development tools. They are not Galax CrewAI production agents and may not control the Galax Flow.

## Official-platform survey

### Cline

Official guidance supports:

- one focused goal per task;
- Plan Mode before Act Mode for medium or complex work;
- `/deep-planning` for multi-file or architectural work;
- repository rules through `.clinerules/` or `AGENTS.md`;
- checkpoints for task/file recovery;
- relevant context instead of loading unnecessary files;
- isolated worktrees for task separation.

Sources:

- https://docs.cline.bot/core-workflows/task-management
- https://docs.cline.bot/core-workflows/plan-and-act
- https://docs.cline.bot/core-workflows/using-commands
- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/core-workflows/working-with-files
- https://docs.cline.bot/core-workflows/checkpoints

### OpenHands Core

Official guidance supports:

- repository customization through `.openhands/`;
- repository-specific skills and stop hooks;
- beginning from repository documentation, setup, structure, and CI workflows;
- task input through a prompt or task file;
- pause/resume and headless structured execution;
- bounded iteration configuration;
- Docker isolation for safer execution.

Sources:

- https://docs.openhands.dev/openhands/usage/customization/repository
- https://docs.openhands.dev/overview/skills/repo
- https://docs.openhands.dev/openhands/usage/cli/quick-start
- https://docs.openhands.dev/openhands/usage/cli/command-reference
- https://docs.openhands.dev/openhands/usage/agents

### Aider

Official guidance supports:

- loading coding conventions as a read-only Markdown file;
- adding only the files that need to change;
- avoiding excessive unrelated context;
- splitting large work into bite-sized steps;
- discussing the plan before complex edits;
- configuring lint and test commands;
- controlling automatic Git commits.

Sources:

- https://aider.chat/docs/usage/conventions.html
- https://aider.chat/docs/usage/tips.html
- https://aider.chat/docs/usage/lint-test.html
- https://aider.chat/docs/git.html
- https://aider.chat/docs/config/aider_conf.html

### mini-SWE-agent

Official guidance supports:

- exact YAML configuration;
- explicit model and environment selection;
- isolated Docker, Singularity, bubblewrap, or related execution backends;
- saving trajectories and cost information;
- confirmation mode instead of unrestricted execution;
- explicit resource limits.

Sources:

- https://mini-swe-agent.com/latest/advanced/environments/
- https://mini-swe-agent.com/latest/advanced/global_configuration/
- https://mini-swe-agent.com/latest/usage/config/
- https://github.com/SWE-agent/mini-swe-agent

### PR-Agent

Official guidance supports:

- a narrow PR-review role;
- CLI, Docker, or GitHub Action execution;
- repository configuration;
- review, describe, improve, and question operations;
- local/non-published review output;
- exact image/release pinning for reproducibility.

Sources:

- https://github.com/The-PR-Agent/pr-agent
- https://github.com/The-PR-Agent/pr-agent/security
- https://www.pr-agent.ai/

### Cross-platform repository instruction patterns

GitHub documents repository-wide instructions, path-specific instructions, `AGENTS.md`, and reusable prompt files. It warns that instructions are non-deterministic and therefore still require verification. The common professional pattern is to keep global rules short, separate path-specific rules, and give each task a clear objective and validation method.

Sources:

- https://docs.github.com/en/copilot/concepts/prompting/response-customization
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents

## Galax command-design conclusion

Every contributor command must contain these sections in this order:

```text
1. Identity and exact role
2. Professional background relevant to the task
3. Single mission and measurable goal
4. Repository, required base branch, and exact starting SHA
5. Mandatory reading order
6. Current project truth and architecture boundary
7. Authorized files and operations
8. Prohibited files and operations
9. Required plan before modification
10. Step-by-step execution procedure
11. Tests and negative tests
12. Stop conditions
13. Required evidence and handoff schema
14. Acceptance criteria
```

## Command quality rules

```yaml
one_task_one_goal: required
role_specific_context: required
repository_first: required
exact_branch_and_SHA: required
plan_before_complex_edit: required
allowed_paths: required
prohibited_actions: required
test_commands: required
negative_tests: required
stop_conditions: required
structured_handoff: required
claims_without_evidence: prohibited
parallel_overlapping_writers: prohibited
```

## Why this standard is selected

A generic prompt such as “build Agent 01” is insufficient. It does not establish the repository state, ownership boundary, exact output, tests, or stop behavior. The selected structure reduces ambiguity by making the contributor answer five questions before acting:

```text
Where am I working?
What exact role do I have?
What exact result is required?
What am I forbidden to touch?
What evidence proves completion?
```

## Repository integration decision

The role packs are stored as documentation only. They do not create active `.clinerules`, `.openhands`, `.aider.conf.yml`, mini-SWE configuration, GitHub Actions, or MCP servers.

```yaml
role_documents_added: true
tool_specific_runtime_configuration_added: false
credentials_added: false
MCP_servers_added: false
GitHub_workflows_added: false
candidate_repository_write_authorized: false
```
