# External Contributor Source Card — goose

**Source ID:** `EXTERNAL-goose`  
**Source type:** `tool`  
**Status:** `DECLINED_CURRENT_PHASE_RESEARCH_LATER`  
**Paper compatibility score:** `77`  
**Verified:** `2026-07-21`  
**Repository permission:** `NONE`

## Identity

```yaml
name: goose
maintainer: Agentic AI Foundation project
canonical_repository: https://github.com/aaif-goose/goose
license: Apache-2.0
version_or_commit_tested: NOT_TESTED
exact_release_pinned: false
native_MCP: true
```

goose is an external general-purpose AI agent. It is not a Galax CrewAI Agent 01–15 and is not approved for repository use in the current phase.

## Documented capabilities considered

The canonical project describes goose as a local general-purpose AI agent with a desktop application, CLI, and API. It supports multiple model providers and more than 70 extensions through MCP. Its repository also documents custom distributions for preconfigured providers and extensions.

Security-related configuration includes an extension allowlist, keyring controls, optional prompt-injection detection, and telemetry controls. These controls require exact configuration and testing; their existence alone does not approve a Galax runtime profile.

## Galax decision

```yaml
paper_score: 77
decision: DECLINED_NOW_RESEARCH_LATER
blocker: SCOPE_TOO_BROAD_AND_ROLE_DUPLICATION
current_role_assignment: none
controlled_trial_authorized: false
repository_write: prohibited
MCP_connection_authorized: false
production_use: prohibited
```

Reason:

goose is active, open source, MCP-native, and broadly capable. However, its general-purpose agent, provider, extension, workflow, and integration surface is materially wider than the bounded current need. Adding it now would overlap the selected contributor coordination and future gateway responsibilities without proving a narrower security and permission profile.

This is a current-phase scope and duplication decision, not a claim that goose is technically incapable.

## Future reconsideration gate

Research may resume only after Agent 01 and the Governance Foundation are operationally validated and a narrow goose distribution is designed.

Required future profile:

```yaml
custom_distribution: required
extension_allowlist: minimal_exact_set
unneeded_extensions: disabled
repository_workspace: isolated
raw_GitHub_token: prohibited
main_write: prohibited
merge: prohibited
force_push: prohibited
workflow_and_secret_write: prohibited
arbitrary_shell: prohibited
arbitrary_filesystem: prohibited
arbitrary_MCP_URL: prohibited
network: deny_by_default
exact_release_and_digest: required
```

It must also pass repository-read compliance, protected-path and unauthorized-command negative tests, credential and network tests, MCP metadata/prompt-injection tests, reproducibility tests, evidence-contract validation, and human acceptance.

## Official sources

- Canonical repository: https://github.com/aaif-goose/goose
- Documentation: https://goose-docs.ai/
- License: https://github.com/aaif-goose/goose/blob/main/LICENSE
- Security policy: https://github.com/aaif-goose/goose/blob/main/SECURITY.md
- Environment and security configuration: https://github.com/aaif-goose/goose/blob/main/documentation/docs/guides/environment-variables.md
- Custom distributions: https://github.com/aaif-goose/goose/blob/main/CUSTOM_DISTROS.md

## Current factual status

```yaml
source_record_complete_for_current_decision: true
installed: false
connected: false
live_tests_run: false
fully_qualified: false
active_Galax_contributor: false
future_narrow_profile: research_only
```