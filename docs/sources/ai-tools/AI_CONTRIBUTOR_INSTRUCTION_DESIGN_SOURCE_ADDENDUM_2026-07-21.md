# AI Contributor Instruction Design Source Addendum

**Record date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `CURRENT_INSTRUCTION_DESIGN_EVIDENCE`  
**Purpose:** Ground the Galax external-contributor role cards, task packets, and command templates in current official platform guidance.

## Evidence rules

1. Official documentation and canonical repositories are primary sources.
2. Platform examples are adapted to Galax; they do not override Galax governance.
3. Persistent instructions must remain concise and point to canonical files instead of duplicating entire plans.
4. One task must have one goal, explicit context, acceptance criteria, allowed paths, tests, and a stopping condition.
5. Tool-specific prompts must reflect the actual tool interface; unsupported capabilities must not be invented.
6. Agents must provide concise decision rationale and evidence, not hidden chain-of-thought.

## Cross-platform findings

### Repository-wide instruction files

- **GitHub Copilot repository instructions:** https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
  - Supports repository-wide, path-specific, and `AGENTS.md` agent instructions.
  - Repository instructions should explain how to understand, build, test, and validate changes.
- **GitHub Copilot prompt engineering:** https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
  - Recommends specific requests, examples, smaller tasks, unambiguous requirements, and relevant code context.
- **GitHub Copilot coding-agent task guidance:** https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks
  - A well-scoped task includes the problem, complete acceptance criteria, and affected files.
- **GitHub Copilot usage optimization:** https://docs.github.com/en/copilot/tutorials/optimize-ai-usage
  - Recommends clear task definition, relevant context, a stopping condition, lean context, deterministic guardrails, and only necessary tools.

### Cline

- **Rules:** https://docs.cline.bot/customization/cline-rules
  - Cline supports `.clinerules/` and cross-tool `AGENTS.md`.
  - Effective rules are scannable, specific, organized by headings and bullets, explain non-obvious reasons, and point to repository examples.
  - One concern per rule file and concise context are recommended.
- **Tasks:** https://docs.cline.bot/core-workflows/task-management
  - A task is a self-contained session; clear and specific initial prompts improve results.
  - One task should equal one goal.
  - Tasks preserve conversation, code changes, decisions, token usage, costs, execution time, and checkpoints.

### OpenHands

- **Repository skills:** https://docs.openhands.dev/overview/skills/repo
  - Recommends repository orientation and a succinct `AGENTS.md` covering purpose, setup, structure, CI, and development guidelines.
- **Skills overview:** https://docs.openhands.dev/overview/skills
  - Root `AGENTS.md` is recommended for permanent repository-wide context.
  - Project skills may be placed in `.agents/skills/` and loaded on demand.
- **Skill best practices:** https://docs.openhands.dev/overview/skills/public
  - Skills should have clear scope, explicit instructions, useful examples, safety constraints, and integration awareness.
- **Repository customization:** https://docs.openhands.dev/openhands/usage/customization/repository
  - Repository-specific setup and stop hooks can be configured, but Galax will not add executable setup hooks before a separate security review.

### Aider

- **Coding conventions:** https://aider.chat/docs/usage/conventions.html
  - A small Markdown conventions file can be loaded read-only with `/read` or `aider --read`.
  - Galax will load `AGENTS.md`, the selected role card, and the canonical task packet as read-only context.
- **Git integration:** https://aider.chat/docs/git.html
  - Automatic commits and dirty-file behavior require explicit Galax overrides.
- **Lint and test:** https://aider.chat/docs/usage/lint-test.html
  - Lint and test commands must be configured for the exact surgical task.

### mini-SWE-agent

- **Canonical repository:** https://github.com/SWE-agent/mini-swe-agent
  - Current minimal issue-solving agent with versioned YAML configuration and trajectory output.
- **Default agent configuration:** https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/agents/default.py
  - Supports separate `system_template` and `instance_template`, step limit, cost limit, and trajectory output path.
  - Uses strict template rendering, so required variables must be explicit.
- **Release controls:** https://github.com/SWE-agent/mini-swe-agent/releases
  - Current releases include cost-limit and wall-clock-limit controls.

### PR-Agent

- **Review tool:** https://github.com/The-PR-Agent/pr-agent/blob/main/docs/docs/tools/review.md
  - Supports project-specific `extra_instructions`.
  - Official guidance says extra instructions should be specific, clear, concise, identify the relevant review tool, and emphasize exact review aspects.
- **Usage and local output:** https://github.com/The-PR-Agent/pr-agent/blob/main/docs/docs/usage-guide/automations_and_usage.md
  - Configuration can keep `publish_output=false` for local review before comments are posted.
  - Automatic feedback can be disabled.

## Galax command-design standard derived from the sources

Every external contributor command must use this order:

```text
1. Identity and exact role
2. Repository and exact starting branch/SHA
3. Required reading order
4. Background and reason the role exists
5. One canonical goal
6. Allowed inputs, paths, and tools
7. Explicit prohibited actions
8. Plan-before-act requirement
9. Ordered execution procedure
10. Acceptance tests and security-negative tests
11. Resource/time/cost/step limits
12. Stop conditions
13. Exact output and handoff schema
14. Human approval boundary
```

## Persistent versus task-specific instructions

```yaml
persistent_repository_context:
  file: AGENTS.md
  contains:
    - canonical reading order
    - current project scope
    - universal safety rules
    - contributor routing
    - task-packet requirement
  must_not_contain:
    - temporary branch SHA
    - one-off task details
    - secrets
    - provider credentials

task_specific_context:
  files:
    - docs/ai-contributors/templates/CANONICAL_TASK_PACKET.yaml
    - selected role card
    - task-specific prompt
  contains:
    - exact branch and SHA
    - exact allowed paths
    - tests
    - limits
    - expected output
    - stop conditions
```

## Non-determinism warning

Platform documentation consistently treats custom instructions as guidance rather than a proof of compliance. Galax therefore requires deterministic checks, branch/path inspection, test evidence, handoff records, and human review in addition to prompts.
