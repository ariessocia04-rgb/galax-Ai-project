# External AI Platform Command and Instruction Survey — 2026-07-21

**Status:** `OFFICIAL_SOURCE_RESEARCH_COMPLETE_CONTROLLED_TRIAL_PENDING`  
**Purpose:** Define how Galax should give clear, professional, repository-aware assignments to the selected external AI coding contributors.  
**Approval effect:** None. Official documentation proves configuration paths and platform behavior; it does not prove Galax compatibility until controlled trials pass.

## 1. Survey conclusion

The most consistent professional pattern across current coding-agent platforms is:

```text
persistent repository instructions
+ one bounded task prompt
+ exact file/path scope
+ explicit build/test commands
+ explicit prohibited actions
+ safe execution mode
+ observable output/evidence
+ human review
```

Vague instructions such as `fix the project`, `continue the work`, or `make it production ready` are rejected for Galax. Every assignment must name the repository, branch, starting SHA, role, objective, allowed paths, prohibited paths, commands, tests, output artifacts, stop conditions, and human approval gates.

## 2. Cross-platform repository instruction finding

### `AGENTS.md`

GitHub documents `AGENTS.md` as an agent-instruction format discoverable by coding agents, and Cline explicitly supports `AGENTS.md` for cross-tool compatibility. OpenHands documentation also recommends repository-specific onboarding content that explains purpose, setup, structure, workflows, and development rules.

Galax decision:

```yaml
root_AGENTS_md: required
purpose:
  - mandatory_reading_order
  - repository_identity
  - branch_and_permission_rules
  - universal_status_and_evidence_contract
  - contributor_separation
platform_specific_prompts: still_required
```

`AGENTS.md` is persistent context, not a substitute for the exact task assignment.

Official sources:

- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- https://docs.github.com/en/copilot/concepts/prompting/response-customization
- https://docs.cline.bot/customization/cline-rules
- https://docs.openhands.dev/overview/skills/repo

## 3. Instruction-writing rules adopted by Galax

Official platform guidance repeatedly favors instructions that are specific, scannable, current, and tied to actual repository paths and commands.

Galax command standard:

1. State the contributor's exact role and bounded authority.
2. Explain the project objective and why the task exists.
3. Name the exact repository, branch, starting SHA, and workspace.
4. Require reading the repository records before any edit.
5. Name the exact files or directories allowed and prohibited.
6. Give expected inputs and machine-checkable outputs.
7. Give actual build, lint, type-check, and test commands.
8. Specify safe operating mode and approval settings.
9. Specify when to stop instead of improvising.
10. Require a final evidence report that separates passed, failed, skipped, blocked, and not run.

Do not write fictional professional biographies. Use:

```text
Operate using the documented practices expected from a senior practitioner in <domain>.
```

Do not write:

```text
You have ten years of real experience.
You are certified.
You guarantee secure and bug-free output.
```

## 4. Cline survey

### Officially documented mechanisms

- Workspace rules live in `.clinerules/`.
- Cline also recognizes `AGENTS.md`.
- Rule files should be focused, structured with headings and bullets, specific rather than vague, current, and linked to repository examples.
- Conditional rules can be scoped by file paths.
- Cline CLI supports plan mode, working-directory selection, timeout, model selection, structured output, and auto-approval configuration.
- Current CLI documentation states that auto-approval defaults to enabled in the CLI; therefore Galax must explicitly set it to `false`.
- YOLO mode auto-approves file, command, browser, MCP, and mode-transition actions and is unsafe for Galax.

Galax configuration decision:

```yaml
persistent_rules:
  - AGENTS.md
  - .clinerules/00-galax-governance.md
first_run: plan_only
act_run: human_approved
--auto-approve: false
YOLO: prohibited
MCP: explicit_allowlist_only
```

Official sources:

- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/features/auto-approve
- https://docs.cline.bot/usage/cli-overview
- https://docs.cline.bot/cli/cli-reference

## 5. OpenHands Core survey

### Officially documented mechanisms

- Repository customization uses a `.openhands` directory.
- Skills extend prompts with repository-specific behavior.
- `.openhands/setup.sh` may prepare a repository environment.
- `.openhands/hooks.json` can run hooks and stop completion when quality checks fail.
- Docker is the recommended sandbox and provides isolation and reproducibility.
- Process sandbox runs directly on the host without container isolation and is unsuitable for Galax.
- A read-write mounted workspace can be modified by the agent.

Galax configuration decision:

```yaml
variant: self_hosted_OpenHands_Core
sandbox: Docker
process_sandbox: prohibited
repository_mount: dedicated_isolated_worktree
network: deny_by_default
GitHub_token_inside_agent: prohibited
role: fallback_reproduction_only
```

Galax will not create an automated OpenHands setup script until the exact dependency lock and sandbox image are approved. Repository instructions and the bounded fallback prompt are prepared first.

Official sources:

- https://docs.openhands.dev/openhands/usage/customization/repository
- https://docs.openhands.dev/openhands/usage/sandboxes/docker
- https://docs.openhands.dev/openhands/usage/sandboxes/overview

## 6. mini-SWE-agent survey

### Officially documented mechanisms

- The CLI accepts a task with `--task`, a YAML config with `--config`, and a model with `--model`.
- Confirm mode asks for human confirmation; YOLO mode executes without confirmation.
- `AgentConfig` supports separate system and instance templates plus step, cost, wall-time, and format-error limits.
- Output trajectory files contain the run history, configuration, model-call metadata, and cost information.

Galax configuration decision:

```yaml
role: isolated_patch_comparison
mode: confirm
-y_or_YOLO: prohibited
system_template: Galax_role_and_safety_contract
instance_template: one_exact_issue_assignment
step_limit: required
cost_limit: required
wall_time_limit_seconds: required
trajectory_output: required
direct_GitHub_write: prohibited
```

Official sources:

- https://mini-swe-agent.com/latest/usage/mini/
- https://mini-swe-agent.com/latest/usage/config/
- https://mini-swe-agent.com/latest/reference/agents/default/
- https://mini-swe-agent.com/latest/usage/output_files/

## 7. Aider survey

### Officially documented mechanisms

- Repository configuration may be stored in `.aider.conf.yml`.
- A small conventions file can be loaded read-only with `--read` or configured under `read:`.
- Automatic commits and dirty-file commits default to enabled and can be disabled with `--no-auto-commits` and `--no-dirty-commits`.
- Aider supports lint and test commands, automatic linting/testing, dry run, file-scoped editing, diffs, and undo.
- Official guidance recommends a minimal configuration containing only settings actually needed.

Galax configuration decision:

```yaml
role: surgical_single_failure_fixer
persistent_read_context:
  - AGENTS.md
  - exact_assignment
--no-auto-commits: required
--no-dirty-commits: required
--git-commit-verify: required
--auto-lint: required
--test-cmd: exact_task_command
--auto-test: required_for_assigned_repair
push: prohibited
```

Official sources:

- https://aider.chat/docs/config/aider_conf.html
- https://aider.chat/docs/config/options.html
- https://aider.chat/docs/usage/conventions.html
- https://aider.chat/docs/git.html
- https://aider.chat/docs/scripting.html

## 8. PR-Agent survey

### Officially documented mechanisms

- Repository configuration uses a minimal `.pr_agent.toml`.
- `pr_reviewer.extra_instructions` provides repository-specific review rules.
- `config.publish_output=false` prints results locally without publishing.
- CLI supports review, describe, improve, ask, and configuration overrides.
- A non-default configuration branch can be specified, but official documentation warns that the config branch is a privileged trust boundary and must never come from untrusted PR input.
- The project has moved to the community-owned `The-PR-Agent/pr-agent` repository; current release and image identity must be pinned before trial.

Galax configuration decision:

```yaml
role: read_only_stable_PR_reviewer
configuration: minimal
publish_output: false_initially
extra_instructions: Galax_scope_security_evidence_review
config_branch: fixed_maintainer_controlled_value_only
source_write: prohibited
labels: prohibited_initially
approval: prohibited
merge: prohibited
```

Official sources:

- https://docs.pr-agent.ai/usage-guide/configuration_options/
- https://docs.pr-agent.ai/usage-guide/additional_configurations/
- https://docs.pr-agent.ai/usage-guide/automations_and_usage/
- https://github.com/The-PR-Agent/pr-agent

## 9. Why no direct five-tool MCP mesh

MCP exposes tools and resources; it does not create a safe multi-writer repository coordination protocol. Directly connecting multiple coding contributors to broad repository operations would increase trust, permission, and conflict surfaces.

Galax decision:

```yaml
direct_agent_to_agent_MCP_mesh: prohibited
shared_raw_GitHub_credentials: prohibited
simultaneous_repository_writers: prohibited
future_narrow_contributor_gateway: research_only
```

A future trusted gateway may expose narrow operations such as task submission, status, cancellation, and artifact retrieval. Repository mutation remains governed by branch, expected-SHA, path, permission, evidence, and human gates.

## 10. Remaining factual gaps before approval

For each selected contributor, Galax still needs:

- Exact installed version or commit.
- Exact license verification.
- Exact model/provider profile used in the trial.
- Environment and sandbox fingerprint.
- Credential and network behavior verification.
- Repository-read compliance trial.
- Protected-path and unauthorized-command negative tests.
- Output and evidence-contract validation.
- Reproducibility test.
- Human acceptance.

Until then:

```yaml
paper_research: complete
platform_command_pack: specified
controlled_trial: not_run
fully_qualified: false
production_use: prohibited
```