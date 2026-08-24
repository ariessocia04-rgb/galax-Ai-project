# Automatic Revalidation Research Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This rule remains editable until its change detector, research gateway, and recovery tests pass.  
**Process:** deterministic Flow followed by `Process.sequential`  
**Research agent:** Agent 03 — Evidence and Capability Researcher

## 1. Core rule

```text
When a validated dependency, prompt, schema, permission, repository contract,
provider limit, or security rule changes, every affected capability becomes
REVALIDATION_REQUIRED before another affected agent may run.
```

The system must research the change, its reason, factual impact, and supported solution before implementation. It must not automatically assume that an older configuration is still compatible.

## 2. Mandatory change triggers

The deterministic Flow computes and compares fingerprints for:

```yaml
revalidation_triggers:
  crewai_version:
  litellm_version:
  cerebras_api_version:
  cerebras_model_id:
  cerebras_model_metadata:
  cerebras_model_behavior_contract:
  agent_prompt_hash:
  tool_schema_hash:
  tool_implementation_commit:
  permission_policy_hash:
  repository_structure_manifest_hash:
  provider_account_rate_limit_snapshot:
  security_rules_hash:
  memory_schema_hash:
  docker_compose_and_image_digest_hash:
```

A change to any field does not automatically invalidate every agent. The Flow maps the changed fingerprint to the affected agents, tools, tests, and stages.

## 3. Immediate behavior after change detection

```text
DETECT CHANGE
→ record old and new fingerprints
→ identify affected capability records
→ set affected status to REVALIDATION_REQUIRED
→ disable affected agent profiles
→ save canonical checkpoint
→ prevent affected implementation work
→ start a separate revalidation research stage
```

Required blocked status:

```yaml
status: BLOCKED_REVALIDATION_REQUIRED
changed_items: []
affected_agents: []
affected_tools: []
affected_tests: []
last_verified_configuration:
current_detected_configuration:
```

## 4. Temporary research tool rule

The active implementation agent must never receive a temporary second tool.

The Flow starts a separate Agent 03 task and assigns exactly one temporary-lifecycle composite interface:

```yaml
agent: evidence_capability_researcher
single_tool: EphemeralRevalidationResearchTool
tool_lifecycle: created_for_run_destroyed_after_run
maximum_distinct_tool_interfaces: 1
permissions:
  public_web_read: official_allowlist_only
  github_public_source_read: approved_repositories_only
  repository_write: research_and_source_records_on_run_branch_only
  software_installation: false
  shell_access: false
  production_access: false
  credential_access: false
```

“Temporary” describes the tool instance lifecycle. It does not permit an agent to hold two tool interfaces.

## 5. Official-source allowlist

The research tool starts with an allowlist appropriate to the changed capability. Examples:

```text
docs.crewai.com
github.com/crewAIInc/crewAI
pypi.org/project/crewai
github.com/BerriAI/litellm
inference-docs.cerebras.ai
console.groq.com
docs.docker.com
github.com/docker
supabase.com/docs
github.com/supabase
developers.notion.com
github.com/makenotion
cloud.google.com
developers.google.com
docs.github.com
github.com/github
```

A community repository or issue may reveal a risk or working example, but it cannot independently approve a capability.

## 6. Required revalidation research output

```yaml
RevalidationResearchResult:
  change_id:
  detected_at:
  changed_item:
  old_value:
  new_value:
  change_reason:
  official_sources: []
  official_source_dates: []
  source_code_or_adapter_evidence: []
  current_open_issue_risks: []
  affected_agents: []
  affected_tool_schemas: []
  affected_prompts: []
  affected_permissions: []
  backward_compatible: true_or_false_or_unknown
  required_migration:
  proposed_solution:
  unsupported_options: []
  security_impact:
  token_and_rate_impact:
  mandatory_live_tests: []
  implementation_allowed: false
```

Research alone never enables implementation.

## 7. Triple-verification sequence

```text
CURRENT OFFICIAL DOCUMENTATION
→ CURRENT OFFICIAL SOURCE OR EXACT ADAPTER
→ LIVE TEST IN PINNED ENVIRONMENT
```

If any layer is unavailable:

```text
STATUS: BLOCKED_INSUFFICIENT_REVALIDATION_EVIDENCE
```

## 8. Sequential remediation flow

After Agent 03 produces a valid research result:

```text
Agent 03 research
→ deterministic research validation
→ owner reviews material change when required
→ Agent 09 updates CrewAI/LLM/tool configuration on run branch
→ relevant implementation specialist updates scoped code when required
→ Agent 12 runs exact tests
→ Agent 11 reviews security impact when applicable
→ Agent 15 independently audits evidence
→ owner approves or rejects
```

No stage may run when its required predecessor is blocked.

## 9. Provider and model rules

The revalidation process must never:

```text
- silently change provider
- silently change model
- silently change API version
- silently lower validation requirements
- automatically use Groq when Cerebras is unavailable
- automatically increase rate or token budgets
```

When Cerebras is unavailable or changed without completed research:

```text
STATUS: BLOCKED_LLM_REVALIDATION
ACTION: checkpoint_and_stop
```

## 10. Prompt and tool schema changes

An agent prompt change invalidates that agent's prompt-adherence and tool-selection evidence.

A tool schema change invalidates:

```text
- exact argument generation test
- actual tool invocation test
- malformed argument rejection
- tool-result round trip
- structured final-output test
- permission boundary test
```

The system must rerun these tests before re-enabling the affected profile.

## 11. Permission and repository structure changes

A permission-policy or repository-structure change requires:

```text
- path allowlist regeneration
- protected-path verification
- branch-policy verification
- current README/rules/plan discovery
- symlink and path-traversal tests
- stale SHA/concurrent-write tests
```

The tool must not infer permissions from the previous repository layout.

## 12. Rate-limit changes

Published provider limits are planning information only. Before each run group, the runtime records the connected account's current limit snapshot when the provider exposes it.

```yaml
effective_rpm: minimum_of(
  internal_agent_ceiling,
  current_account_rpm_minus_headroom
)
```

If the exact account limit cannot be read, the internal conservative ceiling remains in force and the run must not increase throughput.

## 13. Security-rule changes

A changed security rule stops all affected write-capable and network-capable tools until the permission profiles and negative tests are regenerated.

No agent may weaken a security rule to restore compatibility.

## 14. Tool failure

If the temporary research tool is unavailable:

```text
STATUS: BLOCKED_REVALIDATION_RESEARCH_UNAVAILABLE
ACTION: keep_affected_agents_disabled
```

Only one safe retry is permitted. The system must not continue using stale assumptions.

## 15. Evidence retention and cleanup

Retain:

```text
- research result
- official links
- source dates
- old/new fingerprints
- migration decision
- test plan
- final verification commit and date
```

Destroy after the run:

```text
- temporary tool credentials
- temporary provider sessions
- temporary downloaded untrusted files
- temporary containers and networks
```

## 16. Approval tests

```text
REVAL-001 Detect each declared trigger independently.
REVAL-002 Map a change only to affected agents and stages.
REVAL-003 Disable affected profiles before research begins.
REVAL-004 Confirm Agent 03 receives exactly one tool interface.
REVAL-005 Reject non-allowlisted research destinations.
REVAL-006 Produce old/new value and change reason.
REVAL-007 Record official source links and dates.
REVAL-008 Reject community-only approval evidence.
REVAL-009 Prevent automatic implementation after research.
REVAL-010 Prevent silent provider/model fallback.
REVAL-011 Rerun prompt tests after prompt hash change.
REVAL-012 Rerun tool-call tests after schema change.
REVAL-013 Regenerate path tests after repository change.
REVAL-014 Apply current account rate-limit headroom.
REVAL-015 Stop safely when research tool is unavailable.
REVAL-016 Destroy temporary credentials and containers.
REVAL-017 Preserve canonical checkpoint and evidence.
REVAL-018 Require QA, security when applicable, audit, and owner decision.
```

Approval requires 18 of 18 tests in the exact pinned environment.

## 17. Current status

```yaml
change_detector: SPECIFIED_NOT_IMPLEMENTED
fingerprint_registry: SPECIFIED_NOT_IMPLEMENTED
EphemeralRevalidationResearchTool: CANDIDATE_NOT_IMPLEMENTED
Agent_03_revalidation_profile: DISABLED
live_tests: NOT_RUN
production_ready: false
```
