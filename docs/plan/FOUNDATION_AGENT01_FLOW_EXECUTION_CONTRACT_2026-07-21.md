# Foundation and Agent 01 Flow Execution Contract — 2026-07-21

**Status:** `ACTIVE_CANONICAL_FOUNDATION_EXECUTION_CONTRACT`  
**Scope:** Galax Governance Foundation and Agent 01 only  
**Runtime status:** `NOT_OPERATIONAL`  
**Repository implementation:** `NOT_PERFORMED`  
**Merge/deployment:** `PROHIBITED`

## 1. Purpose and authority

This file records the final execution architecture for the Foundation and Agent 01 implementation handoff. It resolves the remaining conflict between two incompatible patterns:

1. Agent 01 directly owning and calling `RepositoryPreflightTool` with `result_as_answer`; and
2. `GalaxFoundationFlow` invoking the external tool before the Agent 01 LLM evaluation.

The second pattern is the active decision.

This is one materially distinct execution contract, not a duplicate copy of the full CrewAI remediation blueprint, the Foundation implementation prompt, the Agent 01 research record, or the external contributor plan. Those records retain their non-conflicting research, requirements, tests, and historical evidence.

## 2. Narrow supersession boundary

The following older instructions are inactive only where they assign `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, attach `result_as_answer`, or test that direct-agent pattern:

```text
docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md
docs/sources/agents/engineering_manager/SOURCE_CARD.md
docs/plan/15_AGENT_RUNTIME_LIMITS_DRAFT.md
docs/plan/AGENT_CAPABILITY_MAPPING_DRAFT.md
docs/plan/AGENT_LLM_TOOL_KNOWLEDGE_MEMORY_MATRIX_DRAFT.md
docs/rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md
```

All materially different non-conflicting requirements in those files remain active according to the repository decision priority.

Do not delete those records. They are historical and research evidence. Exact duplicate removal remains governed by `docs/rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md` and requires normalized-hash equality, reference reconciliation, logging, and verification.

## 3. Final ownership model

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  invoked_before_agent: true
  invocation_limit_per_run: 1

engineering_manager:
  agent_id: engineering_manager
  tools: []
  direct_tool_calls: 0
  receives:
    - trusted RepositoryPreflightResult
  produces:
    - AgentTaskResult
```

Rules:

- Remove `RepositoryPreflightTool` from the Agent 01 tools list.
- Do not use `result_as_answer` for this architecture.
- The Flow invokes the external preflight tool exactly once.
- The Flow validates the invocation evidence and typed result before Agent 01 runs.
- Agent 01 must never call the preflight tool a second time.
- Agent 01 receives only the bounded trusted result required for evaluation.

## 4. Explicit router requirement

Every stage that may return `PASS`, `BLOCKED`, `FAIL`, `UNAVAILABLE`, `PENDING`, `REJECTED`, or an equivalent branch outcome must use an explicit CrewAI Flow router and a named route label.

An unconditional linear `@listen` chain is prohibited for branching stages.

Required pattern:

```python
class GalaxFoundationFlow(Flow[GalaxFoundationFlowState]):

    @start()
    def validate_run_manifest(self):
        ...

    @router(validate_run_manifest)
    def route_manifest_validation(self):
        if self.state.manifest_validation_result.status == "PASS":
            return "manifest_valid"
        return "manifest_blocked"

    @listen("manifest_blocked")
    def stop_manifest_blocked(self):
        ...

    @listen("manifest_valid")
    def check_external_preflight_tool_availability(self):
        ...

    @router(check_external_preflight_tool_availability)
    def route_tool_availability(self):
        if self.state.tool_availability == "AVAILABLE":
            return "preflight_tool_available"
        return "preflight_tool_unavailable"

    @listen("preflight_tool_unavailable")
    def stop_tool_unavailable(self):
        ...

    @listen("preflight_tool_available")
    def invoke_repository_preflight_tool(self):
        ...

    @router(invoke_repository_preflight_tool)
    def route_preflight_result(self):
        result = self.state.preflight_result

        if result is None or not result.invocation_id:
            return "preflight_evidence_missing"

        if result.overall_status == "FAIL":
            return "preflight_failed"

        return "preflight_requires_evaluation"
```

Continue the same explicit router-label pattern through LLM profile readiness, Agent 01 evaluation, human-review construction, authenticated human decision, and final completion.

No blocked, failed, unavailable, rejected, pending, or evidence-missing route may trigger the next successful stage.

## 5. Exactly one Agent 01 LLM execution

```text
trusted RepositoryPreflightResult
→ one Agent 01 evaluation
→ validated AgentTaskResult
→ deterministic Flow method builds HumanReviewRequest
```

```yaml
Agent_01_LLM_calls: 1
Agent_01_outputs:
  - AgentTaskResult
hidden_second_agent_call: prohibited
```

Agent 01 may recommend an allowed `next_transition`. It does not own routing and must not create, approve, reject, or modify the human decision.

The Flow must validate every supported claim against real evidence identifiers. A fabricated, missing, or mismatched evidence identifier cannot be upgraded to `PASS`.

## 6. Deterministic HumanReviewRequest

```python
@listen("human_review_required")
def build_human_review_request(self):
    # Pure Python/Pydantic.
    # No LLM call.
    # Uses RepositoryPreflightResult + AgentTaskResult.
    ...
```

The Flow creates:

```text
confirmed_evidence
missing_evidence
risks derived from blocker categories
prohibited_next_steps
human_decision=PENDING
created_at
```

`HumanReviewRequest` construction must be pure Python/Pydantic. It must not trigger a second Agent 01 execution.

The Flow pauses for a real authenticated human decision. Studio must not simulate the decision.

## 7. LLM profile readiness gate

Before kicking off the Agent 01 Crew, execute:

```text
check_llm_profile_readiness()
```

It verifies:

```text
profile exists
profile_enabled is true
provider_live_tested is true
agent_profile_approved is true
profile matches engineering_manager
data classification is allowed
required credential is available
current capacity snapshot is valid
```

Any failed condition stops the run before the LLM call:

```yaml
status: BLOCKED_LLM_PROFILE_NOT_APPROVED
profile_id:
profile_defined:
profile_enabled:
provider_live_tested:
agent_profile_approved:
credential_available:
failed_conditions: []
safe_remedy:
```

Both current Agent 01 profiles remain disabled. Do not activate either profile in CrewAI Studio. The Studio plan remains non-operational while they are disabled.

## 8. Declared permissions versus live GitHub validation

The offline `RepositoryPreflightTool` has no network access and cannot prove live GitHub App or token permissions.

Use this offline check name:

```text
REPO_PERMISSION_PROFILE_DECLARED
```

It may verify only:

```text
a permission-profile record exists
the repository owner/name matches
required permissions are declared
prohibited permissions are absent
the profile has not expired locally
```

Live permission evidence is separate:

```text
GITHUB_PERMISSIONS_LIVE_VALIDATED
```

Owner:

```text
GitHubRepositoryGateway
```

Required trusted evidence:

```yaml
authenticated_identity:
target_repository:
repository_access_confirmed:
contents_permission:
pull_requests_permission:
workflows_permission:
administration_permission:
checked_at:
evidence_id:
```

When a run requires real GitHub access but no trusted gateway evidence exists, return:

```text
BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING
```

An offline permission declaration must never be represented as live permission proof.

## 9. Final execution sequence

```text
validate_run_manifest()
→ router

check_external_preflight_tool_availability()
→ router

invoke_repository_preflight_tool()
→ router

check_llm_profile_readiness()
→ router

run_agent_01_evaluation()
→ validate supported claims
→ router

build_human_review_request()
→ pause for authenticated human decision
→ router

complete_foundation_plan()
```

Required invariants:

```yaml
repository_preflight_tool_calls: 1
Agent_01_LLM_calls: 1
Agent_01_direct_tools: 0
hidden_second_agent_call: prohibited
unconditional_listen_chain: prohibited
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```

## 10. Controlled implementation and test corrections

The repository-aware coding contributor must update the implementation and contract tests so that they prove:

```text
- engineering_manager.tools is empty;
- RepositoryPreflightTool is Flow-owned and invoked once;
- no result_as_answer is configured for this path;
- every conditional stage has an explicit router and named labels;
- check_llm_profile_readiness() runs before Agent 01;
- Agent 01 executes exactly once and returns AgentTaskResult;
- supported claims are validated against trusted evidence;
- HumanReviewRequest is built by pure Python/Pydantic;
- no hidden second agent call exists;
- offline permission declaration and live GitHub permission proof are separate;
- blocked routes never reach successful stages;
- disabled profiles prevent token use;
- no operational, tested, approved, merge, deployment, or Agents 02–15 claim is made without evidence.
```

Tests in older records that require one Agent 01 direct tool, `result_as_answer`, or an Agent 01 tool-call round trip are superseded for this Foundation architecture and must be replaced by Flow-owned invocation tests.

This exception does not generally authorize zero-tool agents. It applies only to Agent 01 in this exact evaluator architecture because trusted application code performs the deterministic external action first and supplies a validated typed result.

## 11. External contributor boundary

Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, and Codex remain external controlled-trial development contributors. They are not Galax Agents 01–15.

```yaml
simultaneous_repository_writers: prohibited
direct_agent_to_agent_MCP_mesh: prohibited
future_GalaxDevelopmentContributorGateway: research_only
gateway_implemented: false
MCP_connection_authorized_now: false
```

The deterministic contributor order remains conditional and sequential:

```text
Cline primary implementation
→ Aider one exact repair when separately assigned
→ mini-SWE-agent isolated comparison when separately assigned
→ OpenHands isolated fallback reproduction when separately assigned
→ optional external review layer according to the exact Stage 1 policy:
    - NEITHER
    - PR_AGENT_ONLY
    - CODEX_ONLY
    - PR_AGENT_AND_CODEX
→ when both are selected: PR-Agent REVIEW_ONLY, verify unchanged head,
  then Codex REVIEW_ONLY
→ ChatGPT canonical exact-diff review
→ Human Owner decision
```

```yaml
external_review_alignment:
  scope:
    - Governance_Foundation
    - Agent_01
  PR_Agent_optional: true
  Codex_optional: true
  both_reviewers_execution: SEQUENTIAL_READ_ONLY
  parallel_external_reviews: prohibited
  same_current_PR_head_required: true
  ChatGPT_canonical_review_required: true
  Human_Owner_final_authority: true
  runtime_architecture_changed: false
```

Stages may be skipped when their entry condition is absent. No two writers may edit the same worktree or overlapping files concurrently.

## 12. Final design status

```yaml
status: CREWAI_STUDIO_AUTOMATION_PLAN_FINALIZED
repository_implementation: NOT_PERFORMED
external_preflight_tool_connected: false
GitHub_permissions_live_validated: false
LLM_profiles_enabled: false
live_tests_performed: false
Agent_01_runtime_approved: false
Agents_02_to_15_enabled: false
next_required_environment: repository_aware_coding_agent
```

The plan is finalized for a bounded coding handoff. It is not operational, implemented, live-tested, runtime-approved, merged, deployed, or production-ready.