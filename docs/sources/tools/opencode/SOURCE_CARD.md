# External Contributor Source Card — OpenCode

**Source ID:** `EXTERNAL-opencode`  
**Source type:** `tool`  
**Status:** `DECLINED_CURRENT_GALAX_PHASE`  
**Paper compatibility score:** `74`  
**Verified:** `2026-07-21`  
**Repository permission:** `NONE`

## Identity

```yaml
name: OpenCode
maintainer: anomalyco
official_repository: https://github.com/anomalyco/opencode
license: MIT
version_or_commit_tested: NOT_TESTED
exact_release_pinned: false
native_MCP: documented
```

OpenCode is an external software-development tool. It is not a Galax CrewAI Agent 01–15 and is not approved for repository use.

## Documented capabilities considered

Official records reviewed for the paper screening document:

```text
- local coding-agent operation;
- shell, file, and web tools;
- granular allow, ask, and deny permission rules;
- read-only and write-capable agent profiles;
- subagent/task support;
- MCP server configuration.
```

## Security boundary finding

The project security policy states that OpenCode runs locally with shell execution, file operations, and web access. It also states that OpenCode does not sandbox the agent and that its permission system is a user-experience approval mechanism rather than security isolation. The project recommends Docker or a virtual machine when true isolation is required.

The repository security page also listed one critical and one high advisory published on 2026-01-12 for local/server execution surfaces at the time of verification.

Official permission documentation provides granular `allow`, `ask`, and `deny` behavior, but also supports an `--auto` mode that automatically approves requests not explicitly denied. This does not replace an independently tested sandbox boundary.

## Galax decision

```yaml
paper_score: 74
decision: DECLINED
blocker: SECURITY_BOUNDARY_NOT_PROVEN
current_role_assignment: none
controlled_trial_authorized: false
repository_write: prohibited
MCP_connection_authorized: false
production_use: prohibited
```

Reason:

OpenCode has useful configuration and MCP capabilities, but the current Galax phase requires a proven isolated execution boundary for any write-capable contributor. Its documented permission prompts alone are not accepted as isolation. The identified security advisories also require exact-release review and negative testing before reconsideration.

This is a role-and-phase decision, not a claim that OpenCode is universally unsafe or unusable.

## Reconsideration gate

OpenCode may be researched again only after:

```text
- an exact release or commit is pinned;
- its license and security advisories are rechecked;
- execution is placed inside an approved isolated container or VM;
- repository-read compliance passes;
- protected-path and unauthorized-command negative tests pass;
- network, credential, MCP, and subagent behavior is bounded;
- output and evidence contracts pass;
- a human accepts the controlled-trial result.
```

## Official sources

- Official repository: https://github.com/anomalyco/opencode
- License: https://github.com/anomalyco/opencode/blob/dev/LICENSE
- Security policy and advisories: https://github.com/anomalyco/opencode/security
- Permission documentation: https://opencode.ai/docs/permissions/

## Current factual status

```yaml
source_record_complete_for_decline: true
installed: false
connected: false
live_tests_run: false
fully_qualified: false
active_Galax_contributor: false
```