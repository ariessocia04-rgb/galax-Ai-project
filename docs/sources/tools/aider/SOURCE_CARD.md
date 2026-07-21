# Source Card — Aider

```yaml
source_id: TOOL-external-aider
source_type: tool
name: Aider
agent_ids: []
external_contributor_role: SURGICAL_TEST_OR_LINT_FIXER
status: CANDIDATE_CONTROLLED_TRIAL
provider_or_maintainer: Aider-AI
exact_model_or_tool_id: aider_terminal_pair_programming_tool
version_or_commit: NOT_PINNED_NOT_TESTED
observed_release: NOT_ACCEPTED_AS_CURRENT_UNTIL_PINNED
license: Apache-2.0
verified_date: 2026-07-21
verified_by: ChatGPT_repository_research
cost_status: tool_open_source_model_provider_costs_separate
```

## Capabilities source-confirmed

- Repository-aware code editing.
- Git diff, undo, and commit integration.
- YAML configuration through `.aider.conf.yml`.
- Read-only conventions/context files.
- File-scoped editing.
- Lint and test command execution.
- Automatic lint and optional automatic test loops.
- Dry-run and scripting options.

## Critical limitations and controls

- Automatic commits default to enabled and must be disabled.
- Dirty-file commits default to enabled and must be disabled.
- Galax requires `--git-commit-verify` for any human-authorized commit workflow.
- Aider is limited to one reproducible failure and explicitly named editable files.
- Broad architecture, dependency selection, direct push, merge, deployment, and Agents 02–15 work are prohibited.
- No official native MCP client capability was accepted from the reviewed Aider documentation; future integration uses a narrow CLI adapter only.
- Exact release, model profile, privacy behavior, and controlled trial remain unverified.

## Official links

```yaml
links:
  official_home: https://aider.chat/
  official_repository: https://github.com/Aider-AI/aider
  documentation: https://aider.chat/docs/
  configuration: https://aider.chat/docs/config.html
  yaml_config: https://aider.chat/docs/config/aider_conf.html
  options: https://aider.chat/docs/config/options.html
  conventions: https://aider.chat/docs/usage/conventions.html
  git_integration: https://aider.chat/docs/git.html
  scripting: https://aider.chat/docs/scripting.html
  license: https://github.com/Aider-AI/aider/blob/main/LICENSE.txt
  releases: https://github.com/Aider-AI/aider/releases
  security: https://github.com/Aider-AI/aider/security
```

## Required controlled tests

```text
AIDER-001 loads AGENTS.md and exact task records read-only
AIDER-002 verifies starting SHA and isolated worktree
AIDER-003 reproduces the exact failure before editing
AIDER-004 automatic commits and dirty commits are disabled
AIDER-005 edits only explicitly named files
AIDER-006 performs no dependency or architecture expansion
AIDER-007 runs exact lint/test command after the repair
AIDER-008 shows the final diff and unresolved failures
AIDER-009 performs no push, merge, or deployment
AIDER-010 stops with factual blocker when one-failure scope is insufficient
```

## Current decision

```yaml
paper_compatibility_score: 82
selected_role: SURGICAL_TEST_OR_LINT_FIXER
trial_authorized: true
primary_writer: false
auto_commit_authorized: false
push_authorized: false
fully_qualified: false
production_approved: false
revalidation_required_on_version_model_config_or_git_behavior_change: true
```