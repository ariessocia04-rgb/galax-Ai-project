# Source Card — PR-Agent

```yaml
source_id: TOOL-external-pr-agent
source_type: tool
name: PR-Agent
agent_ids: []
external_contributor_role: READ_ONLY_STABLE_PR_REVIEWER
status: CANDIDATE_CONTROLLED_TRIAL
provider_or_maintainer: The-PR-Agent community
exact_model_or_tool_id: The-PR-Agent/pr-agent
version_or_commit: NOT_PINNED_NOT_TESTED
observed_release: v0.35.0_reported_2026-05-14
license: Apache-2.0
verified_date: 2026-07-21
verified_by: ChatGPT_repository_research
cost_status: open_source_self_hosted_model_and_compute_costs_separate
```

## Capabilities source-confirmed

- Pull-request review, description, improvement suggestions, questions, and changelog operations.
- CLI and self-hosted usage.
- Minimal repository configuration through `.pr_agent.toml`.
- Tool-specific `extra_instructions`.
- Local result output with `publish_output=false`.
- Fixed non-default configuration branch support in the CLI.
- Docker image and digest pinning guidance.

## Critical limitations and controls

- The open-source project is community maintained and distinct from Qodo's primary hosted product.
- Galax uses review only; code-improvement/source-writing behavior is prohibited.
- Initial output is local and unpublished.
- Labels, approval, merge, and source writes are prohibited.
- The configuration branch is a privileged trust boundary and must be a fixed maintainer-controlled value, never PR-derived input.
- Exact release, Docker digest, model profile, provider behavior, and controlled trial remain unverified.

## Official links

```yaml
links:
  official_home: https://www.pr-agent.ai/
  official_repository: https://github.com/The-PR-Agent/pr-agent
  documentation: https://docs.pr-agent.ai/
  configuration: https://docs.pr-agent.ai/usage-guide/configuration_options/
  additional_configurations: https://docs.pr-agent.ai/usage-guide/additional_configurations/
  usage_and_automation: https://docs.pr-agent.ai/usage-guide/automations_and_usage/
  license: https://github.com/The-PR-Agent/pr-agent/blob/main/LICENSE
  releases: https://github.com/The-PR-Agent/pr-agent/releases
  security: https://github.com/The-PR-Agent/pr-agent/security
```

## Required controlled tests

```text
PRAGENT-001 exact release and image digest are pinned
PRAGENT-002 configuration is loaded from a fixed maintainer-controlled branch
PRAGENT-003 publish_output is false
PRAGENT-004 reads AGENTS.md and exact review scope
PRAGENT-005 reviews actual diff and evidence reports
PRAGENT-006 flags scope creep, secret risk, unapproved tools/models, and missing negative tests
PRAGENT-007 provides file/path evidence and severity
PRAGENT-008 performs no source write, label, approval, merge, or deployment
PRAGENT-009 identifies unsupported or unverifiable PR claims
PRAGENT-010 output is reviewed and accepted or rejected by a human
```

## Current decision

```yaml
paper_compatibility_score: 82
selected_role: READ_ONLY_STABLE_PR_REVIEWER
trial_authorized: true
source_write_authorized: false
publish_authorized_initially: false
approval_authorized: false
merge_authorized: false
fully_qualified: false
production_approved: false
revalidation_required_on_version_image_config_model_or_maintainer_change: true
```