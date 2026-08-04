# Galax Foundation and Agent 01 Implementation/Validation Prompt

**Status:** `AUTHORIZED_FOUNDATION_PROMPT_RECONCILED_2026-07-21`  
**Scope:** Governance Foundation and Agent 01 evaluator only  
**Full 15-agent build:** prohibited  
**Merge/deploy:** prohibited  
**Operational claim:** prohibited until exact implementation and tests pass

---

## Prompt to paste into Cline, Codex, VS Code, Claude Code, or another repository-aware coding assistant

You are acting as a senior Python, CrewAI, GitHub integration, application-security, and test-automation engineer.

Your assignment is to implement and prove only the minimum Galax Governance Foundation and Agent 01 evaluator architecture in this repository:

```yaml
repository: https://github.com/ariessocia04-rgb/galax-Ai-project
research_branch: agent/agent-01-tool-inspection
implementation_branch: implementation/foundation-agent-01
framework_target: CrewAI 1.15.4
python_target: '>=3.10,<3.14'
execution_process: Process.sequential
production_agents_enabled: 0_until_tests_and_approval_pass
```

Do not build or enable Agents 02–15. Do not merge, deploy, create paid resources, expose credentials, or claim production readiness.

## 1. Mandatory authority and reading order

Before modifying anything:

1. Verify repository identity, current branch, exact starting SHA, and Git status.
2. Read `README.md` completely.
3. Read `AGENTS.md` completely.
4. Read:
   - `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
   - the canonical target named by that alias
   - `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
   - `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
5. Read every applicable file under `docs/rules/` and `docs/plan/`.
6. Read:
   - `docs/sources/SOURCE_INDEX.md`
   - `docs/sources/agents/engineering_manager/SOURCE_CARD.md`
   - `docs/sources/tools/repository_preflight_tool/SOURCE_CARD.md`
   - `docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md`
7. Inspect the existing project structure, dependencies, tests, Docker files, and repository state.
8. Produce `REPOSITORY_READ_RECEIPT` before any edit.

Decision priority:

```text
README and AGENTS.md
→ canonical conflict audit
→ Foundation and Agent 01 Flow execution contract
→ remediation blueprint
→ active rules and plans
→ source cards
→ historical Agent 01 research
→ this assignment
```

The active Flow execution contract supersedes only older instructions that attach `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, or use `result_as_answer` for this path.

If repository, branch, SHA, required documents, or decision priority cannot be verified, stop:

```yaml
status: BLOCKED_REPOSITORY_STATE_MISMATCH
expected:
actual:
missing_or_conflicting_records: []
safe_remedy:
```

## 2. Truth and evidence rule

Never report a capability as working because documentation says it should work.

Every capability must progress through:

```text
DOCUMENTED
→ SOURCE_OR_ADAPTER_CONFIRMED
→ IMPLEMENTED_IN_GALAX
→ TESTED_WITH_DETERMINISTIC_FIXTURES
→ LIVE_TESTED_WHEN_CREDENTIALS_ARE_AVAILABLE
→ APPROVED_FOR_EXACT_PROFILE
```

When a required capability cannot be completed, return:

```yaml
status: BLOCKED_UNSUPPORTED_OR_UNVERIFIED
capability:
failed_layer:
observed_error:
evidence:
what_is_supported:
what_is_not_supported:
safe_remedy:
files_changed_before_block: []
commands_already_run: []
```

Do not fabricate tool calls, file writes, commits, tests, API responses, token usage, permissions, hashes, timestamps, human decisions, or successful integrations.

## 3. Non-negotiable Foundation architecture

Implement exactly:

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  invoked_before_agent: true
  calls_per_run: 1

engineering_manager:
  tools: []
  direct_tool_calls: 0
  receives:
    - trusted RepositoryPreflightResult
  produces:
    - AgentTaskResult

Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_router_for_every_branching_stage: required
```

Agent 01 must never call the preflight tool. The Flow calls it exactly once, validates trusted evidence and the typed result, checks LLM profile readiness, and passes the bounded trusted result to Agent 01.

## 4. Mandatory CrewAI and application settings

```yaml
process: Process.sequential
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution: false
async_execution: false
parallel_agents: false
parallel_tool_calls: false
concurrent_llm_calls: 1
respect_context_window: false
max_retry_limit: 1
guardrail_max_retries: 1
```

Do not silently substitute another framework, version, model provider, process, memory system, planner, code executor, tool ownership model, or routing design.

Pin CrewAI `1.15.4` and every direct dependency used by the Foundation. Record exact versions, sources, and lock evidence. Use UV when compatible with the existing repository.

Do not add an MCP package or provider SDK until the exact official package, compatible version, role, permissions, and test scope are confirmed.

## 5. Minimum package structure

Adapt to the existing package name and structure. Do not create a second parallel package tree.

Minimum expected responsibilities:

```text
src/galax_ai/
├── flow/
│   ├── foundation_flow.py
│   └── transitions.py
├── governance/
│   ├── model_hooks.py
│   ├── policies.py
│   ├── invocation_ledger.py
│   ├── blockers.py
│   └── permission_readiness.py
├── models/
│   ├── run_manifest.py
│   ├── profiles.py
│   ├── evidence.py
│   ├── tool_results.py
│   ├── human_review.py
│   └── checkpoints.py
├── agents/
│   └── engineering_manager.py
├── tools/
│   └── repository_preflight_tool.py
├── executors/
│   └── governed_tool_executor.py
├── gateways/
│   └── github_repository_gateway.py
├── llm/
│   └── profile_factory.py
└── settings.py

tests/
├── unit/
├── contract/
├── security/
├── integration/
└── live/
```

A different layout is allowed only when it reuses the current repository structure and preserves each responsibility exactly once.

## 6. Strict typed contracts

Use strict Pydantic models with `extra='forbid'` for machine-controlled boundaries.

### 6.1 RunManifest

At minimum:

```yaml
run_id: UUID
repository_id: exact_owner/name
repository_root: absolute_configured_path
expected_branch: exact_branch
expected_head_sha: full_40_character_SHA
approved_agent_ids: exactly_[engineering_manager]
approved_llm_profile_id: required
approved_tool_profile_id: required
allowed_paths: explicit_list
protected_paths: explicit_list
data_classification: public | private_scoped | sensitive_restricted
phase_authorization: PHASE_0 | PHASE_1
requires_live_github_access: boolean
github_permission_evidence_id: optional_required_when_live_access_true
created_at: trusted_application_timestamp
```

### 6.2 ToolInvocationRecord

```yaml
invocation_id: UUID
run_id: UUID
task_id: string
owner: GalaxFoundationFlow
tool_profile_id: string
operation: string
input_hash: SHA_256
started_at: trusted_timestamp
finished_at: optional_trusted_timestamp
status: STARTED | SUCCEEDED | BLOCKED | FAILED
raw_output_hash: optional_SHA_256
affected_resources: []
external_evidence_ids: []
error_code: optional
redacted_error_summary: optional
```

### 6.3 RepositoryPreflightResult

```yaml
run_id: UUID
overall_status: PASS | BLOCKED | FAIL
checks:
  - check_id:
    status: PASS | BLOCKED | FAIL
    evidence_id:
    redacted_summary:
    exact_remedy:
blocking_reasons: []
invocation_id: UUID
input_hash: SHA_256
result_hash: SHA_256
```

### 6.4 AgentTaskResult

```yaml
run_id:
agent_id: engineering_manager
task_id: evaluate_preflight_result
status: PASS | BLOCKED | FAIL
summary:
supported_claims:
  - statement:
    evidence_id:
unsupported_claims:
  - statement:
    reason: no_invocation_evidence | fabricated | out_of_scope
next_transition: STOP | HUMAN_REVIEW | CONTINUE_TO_TEST_ONLY_STAGE
exact_remedies: []
```

Agent 01 produces only this model. Invocation IDs, hashes, trusted timestamps, profile readiness, and human decisions are not generated by the agent.

### 6.5 HumanReviewRequest

```yaml
requested_action:
current_status:
confirmed_evidence: []
missing_evidence: []
risks: []
recommended_next_step:
prohibited_next_steps:
  - merge_to_main_or_master
  - deployment
  - activation_of_Agents_02_to_15
  - enabling_unvalidated_LLM_profiles
human_decision: PENDING
created_at: trusted_application_timestamp
```

Build this with pure Python/Pydantic from `RepositoryPreflightResult` and validated `AgentTaskResult`. No second LLM call.

## 7. Deterministic Flow and routers

Required sequence:

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
→ persist and pause for authenticated human decision
→ router after resume

complete_foundation_plan()
```

Every stage that may return multiple outcomes must use explicit `@router` logic and named route labels.

Required route classes include:

```text
manifest_valid | manifest_blocked
preflight_tool_available | preflight_tool_unavailable
preflight_requires_evaluation | preflight_failed | preflight_evidence_missing
llm_profile_approved | llm_profile_blocked
human_review_required | agent_recommends_stop | agent_evaluation_failed
human_decision_pending | human_decision_rejected | human_decision_approved_test_only
```

No blocked, failed, unavailable, evidence-missing, rejected, or pending route may trigger a successful downstream stage.

An unconditional branching `@listen` chain is prohibited.

## 8. Governed preflight invocation

Implement a deterministic executor owned by trusted application code.

It must:

```text
1. Verify exact tool identity and registered profile.
2. Validate strict RepositoryPreflightInput.
3. Enforce one invocation per run.
4. Enforce read-only, no-network, root-containment, no-traversal, and no-symlink-escape rules.
5. Canonicalize and hash the input.
6. Create a STARTED invocation record.
7. Invoke RepositoryPreflightTool exactly once.
8. Validate the raw result against the strict payload schema.
9. Validate evidence identifiers and cross-references.
10. Redact secrets from diagnostics.
11. Canonicalize and hash result material.
12. Construct the trusted RepositoryPreflightResult envelope.
13. Finish the ledger as SUCCEEDED, BLOCKED, or FAILED.
```

Do not assume direct Agent tool hooks govern a Flow-owned call. The executor and deterministic Flow are the security and evidence boundary for this invocation.

## 9. RepositoryPreflightTool

Implement as a local custom CrewAI-compatible tool class or equivalent bounded callable used only by the governed executor.

```yaml
filesystem_access: read_only
network_access: none
repository_scope: configured_repository_root_only
symlink_escape: blocked
path_traversal: blocked
secret_values_in_output: prohibited
automatic_retry: 0
```

It must implement the exact active preflight definitions after reconciling historical Agent 01 research with the Flow contract. At minimum verify:

```text
- repository root and Git metadata;
- required canonical documents;
- active supersession and execution contract;
- no active stale Cerebras configuration;
- planning/reasoning/memory/delegation disabled;
- Agent 01 has zero direct tools;
- Flow-owned one-preflight invocation contract;
- approved profile identifiers;
- protected and secret path policy;
- branch and expected SHA consistency;
- dirty/untracked state policy;
- duplicate-record rule availability;
- complete run manifest;
- checkpoint and invocation-ledger availability;
- REPO_PERMISSION_PROFILE_DECLARED only;
- required evidence/source records;
- MCP security blocker status;
- test-fixture readiness;
- exact phase authorization;
- exact blocker/remedy generation.
```

The offline tool cannot prove live GitHub permissions.

## 10. Permission evidence split

Offline check:

```text
REPO_PERMISSION_PROFILE_DECLARED
```

It verifies only local declarations: profile exists, repository matches, required permissions are declared, prohibited permissions are absent, and the local profile is not expired.

Live check:

```text
GITHUB_PERMISSIONS_LIVE_VALIDATED
```

Owner: `GitHubRepositoryGateway`.

Trusted evidence model:

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

If `requires_live_github_access=true` and valid trusted gateway evidence is absent, return `BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING`.

Do not perform a live write unless an explicit environment switch, minimum-scoped credential, exact branch policy, and human authorization exist.

Direct main/master writes, force push, workflow/secret changes, protected-path writes, deletions, ambiguous write retries, and automatic merge are prohibited.

## 11. Agent 01 evaluator

Implement only:

```yaml
agent_id: engineering_manager
role: AI Engineering Manager and CrewAI Execution Planning Lead
tools: []
allow_delegation: false
allow_code_execution: false
reasoning: false
memory: false
LLM_calls_per_run: 1
output: AgentTaskResult
```

Agent 01 receives one trusted `RepositoryPreflightResult` from the Flow and may only classify evidence and recommend an allowed next transition.

Agent 01 must not:

```text
- call any tool;
- generate or modify invocation IDs, hashes, timestamps, or evidence;
- create HumanReviewRequest;
- create or modify human_decision;
- control routing;
- select agents;
- delegate;
- access repository, network, Drive, Supabase, Notion, GitHub, or MCP directly;
- edit files or run commands;
- create branches, commits, PRs, merges, or deployments;
- execute a second LLM call;
- enable Agents 02–15.
```

After Agent 01 returns, deterministic application code validates every supported claim against the trusted evidence set. A fabricated or unknown evidence ID blocks progression.

## 12. LLM profile readiness

Both profiles remain disabled by default:

```yaml
primary:
  profile_id: engineering_manager_groq_gpt_oss_20b_v1
  provider: groq
  model: groq/openai/gpt-oss-20b
  profile_enabled: false
  provider_live_tested: false
  agent_profile_approved: false

hosted_fallback:
  profile_id: engineering_manager_cloudflare_gpt_oss_20b_v1
  provider: custom_openai_compatible
  model: '@cf/openai/gpt-oss-20b'
  profile_enabled: false
  provider_live_tested: false
  agent_profile_approved: false
```

Before Agent 01, `check_llm_profile_readiness()` verifies:

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

Any failure stops before the LLM call:

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

Do not activate either profile in CrewAI Studio. Missing credentials produce `SKIPPED_LIVE_TEST_MISSING_SECRET`, not PASS.

## 13. Human review pause and resume

`build_human_review_request()` is pure Python/Pydantic and uses the trusted preflight result plus validated AgentTaskResult.

Persist the Flow state before returning control to the application.

A future continuation service must:

```text
- load the exact persisted flow_state_id;
- verify AWAITING_HUMAN_REVIEW;
- verify reviewer identity and authorization;
- validate decision enum only;
- verify trusted review evidence;
- reject duplicate or replayed decisions;
- persist the signed/hashed decision atomically;
- resume through a tested application entrypoint;
- never use a model to create or authorize the decision.
```

Allowed decisions:

```text
PENDING
REJECTED
APPROVED_TEST_ONLY
```

Merge, deployment, and Agents 02–15 approval are not valid decisions at this gate.

## 14. Docker and sandbox boundary

Create only the minimal validation container configuration required for deterministic tests when the repository has no approved equivalent.

```yaml
user: non_root
read_only_root_filesystem: true_where_possible
cap_drop: [ALL]
no_new_privileges: true
host_docker_socket: prohibited
privileged: false
secrets_in_image_or_compose: prohibited
network: disabled_for_preflight_tests
resource_limits: required
timeout_and_cleanup: required
```

Do not implement privileged Docker-in-Docker or claim a secure coding sandbox exists. If absent, report:

```text
STATUS: BLOCKED_SANDBOX_NOT_IMPLEMENTED
REMEDY: implement and validate a separate rootless external sandbox before enabling coding agents
```

## 15. Required deterministic tests

### Unit tests

Prove:

```text
- strict Pydantic schemas and extra-field rejection;
- profile disabled-by-default behavior;
- canonical hashing and ledger transitions;
- path traversal and symlink escape rejection;
- protected and secret path rejection;
- secret redaction;
- deterministic preflight PASS/BLOCKED/FAIL fixtures;
- Flow-owned tool identity and one-invocation limit;
- engineering_manager.tools is empty;
- Agent 01 direct tool calls are zero;
- HumanReviewRequest deterministic construction;
- offline/live permission evidence separation.
```

### CrewAI and Flow contract tests

Prove:

```text
- one Agent 01 instance;
- Agent 01 tools list is empty;
- Process.sequential;
- planning/reasoning/memory/delegation/code execution disabled;
- every conditional stage uses an explicit router and named labels;
- blocked routes never reach successful stages;
- RepositoryPreflightTool is invoked exactly once by Flow-owned code;
- no result_as_answer is configured for this path;
- check_llm_profile_readiness runs before Agent 01;
- disabled profile prevents LLM invocation;
- exactly one Agent 01 LLM evaluation;
- Agent 01 returns strict AgentTaskResult;
- supported claims require trusted evidence IDs;
- HumanReviewRequest uses no LLM call;
- no hidden second agent call exists;
- narrative success without invocation evidence is rejected.
```

### Security tests

Prove rejection of:

```text
- direct main/master write;
- wrong repository or branch;
- stale expected SHA;
- protected, workflow, secret, or traversal paths;
- symlink escape;
- deletion and force update;
- oversized payload;
- ambiguous automatic write retry;
- arbitrary MCP URL or unfiltered tool exposure;
- missing live GitHub permission evidence;
- fabricated invocation/evidence identifiers;
- unauthorized human decision or replay;
- activation of disabled profiles;
- Agents 02–15 activation.
```

### Integration tests

Use deterministic test doubles clearly labeled `TEST_DOUBLE_NOT_PROVIDER_PROOF`.

Prove the full bounded sequence, including stop routes, trusted evidence transfer, one Agent 01 call, deterministic human-review creation, persistence pause, and no later agent activation.

Do not label any test-only second fixture as Agent 02 approval.

### Opt-in live tests

Live tests require explicit enable flags and authorized credentials. They must skip safely when absent.

```text
- current account/profile readiness snapshot;
- exact provider completion and structured AgentTaskResult;
- timeout and 429 handling;
- no secret echo;
- live GitHub identity and permission evidence;
- optional disposable validation branch operation only when separately approved;
- no merge.
```

## 16. Verification commands

After adapting to the repository, provide exact Windows PowerShell and Linux/macOS commands.

Expected classes:

```bash
uv sync --frozen
uv run python -m pytest tests/unit -q
uv run python -m pytest tests/contract -q
uv run python -m pytest tests/security -q
uv run python -m pytest tests/integration -q
uv run ruff check .
uv run pyright

docker compose config
docker compose build --no-cache
docker compose run --rm galax-validation-tests
```

Live examples:

```bash
uv run pytest tests/live -m live_github
uv run pytest tests/live -m live_groq
```

Do not claim a command passed unless it ran and its exit result was recorded.

## 17. Required evidence reports

Create or update only the canonical evidence records:

```text
docs/evidence/foundation/DEPENDENCY_LOCK_REPORT.md
docs/evidence/foundation/GOVERNANCE_TEST_REPORT.md
docs/evidence/foundation/AGENT_01_TEST_REPORT.md
docs/evidence/foundation/GITHUB_GATEWAY_TEST_REPORT.md
docs/evidence/foundation/LLM_PROFILE_TEST_REPORT.md
docs/evidence/foundation/FLOW_ROUTER_TEST_REPORT.md
docs/evidence/foundation/HUMAN_REVIEW_CONTRACT_TEST_REPORT.md
docs/evidence/foundation/FOUNDATION_SELF_DIAGNOSTIC.md
```

Every report separates:

```yaml
confirmed_passed: []
confirmed_failed: []
blocked_missing_credentials: []
blocked_unsupported: []
not_run: []
assumptions: []
exact_remedies: []
commands: []
artifacts: []
commit_shas: []
dependency_versions: []
```

Do not create duplicate evidence files for the same capability/run. Update the canonical record or supersede it according to repository rules.

## 18. Completion gate

You may report `FOUNDATION_AND_AGENT01_VALIDATED_FOR_EXACT_PROFILE` only when all required deterministic, contract, security, integration, and enabled live tests pass for the exact pinned configuration and the human accepts the evidence.

While both profiles are disabled, the expected safe runtime status is:

```text
BLOCKED_LLM_PROFILE_NOT_APPROVED
```

Allowed factual implementation outcomes:

```text
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_LLM_PROFILE_NOT_APPROVED
BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING
FAILED_WITH_REPRODUCIBLE_EVIDENCE
FOUNDATION_TEST_ONLY_APPROVED_PENDING_RUNTIME_AUDIT
FOUNDATION_AND_AGENT01_VALIDATED_FOR_EXACT_PROFILE
```

Never use:

```text
100% production ready
all 15 agents working
fully autonomous software company complete
safe because it uses Docker
safe because it uses MCP
operational without implementation and test evidence
```

## 19. Required final response format

Return the final implementation report in this order:

```text
1. Final factual status
2. Repository branch, starting SHA, and ending SHA or patch hash
3. Files created or changed
4. Dependency versions and official sources
5. Architecture implemented
6. Flow/router and call-count evidence
7. Deterministic tests and results
8. Security negative tests
9. Live tests and results
10. Unsupported or unverified capabilities
11. Exact remedies
12. Whether Agent 01 may be enabled
13. Whether the full 15-agent prompt remains blocked
14. Human approvals still required
```

Do not merge. Do not deploy. Open or update a draft PR only when repository permissions and the owner's separate authorization allow it.

## 20. Current pre-implementation status

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
