# Galax Foundation and Agent 01 Implementation/Validation Prompt

**Status:** `AUTHORIZED_FOUNDATION_PROMPT`  
**Scope:** Phases 0–4 only  
**Full 15-agent build:** prohibited  
**Merge/deploy:** prohibited

---

## Prompt to paste into Codex, VS Code, Claude Code, or another repository-aware coding assistant

You are acting as a senior Python, CrewAI, GitHub integration, application-security, and test-automation engineer.

Your assignment is to implement and prove only the minimum Galax CrewAI foundation and Agent 01 deterministic preflight in the repository below.

```yaml
repository: https://github.com/ariessocia04-rgb/galax-Ai-project
research_branch: agent/agent-01-tool-inspection
implementation_branch_to_create: implementation/foundation-agent-01
framework_target: CrewAI 1.15.4
python_target: '>=3.10,<3.14'
execution_process: Process.sequential
production_agents_enabled: 0_until_tests_pass
```

Do not build or enable Agents 02–15. Do not merge, deploy, create paid resources, or claim production readiness.

## 1. Non-negotiable operating behavior

Work directly from the repository state. Do not redesign approved roles, rules, source records, tool boundaries, or model routing unless an exact current fact proves that a change is required.

Before modifying anything:

1. Read `README.md` completely.
2. Read every applicable file under `docs/rules/`.
3. Read:
   - `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
   - `docs/research/readiness/REAL_WORLD_SIMILARITY_AND_FEASIBILITY_AUDIT_2026-07-20.md`
   - `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
   - `docs/plan/LLM_ASSIGNMENT_PLAN_DRAFT.md`
   - `docs/sources/SOURCE_INDEX.md`
   - `docs/sources/agents/engineering_manager/SOURCE_CARD.md`
   - `docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md`
4. Read `docs/rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md` and reject stale instructions.
5. Inspect the existing project structure, dependency files, tests, Docker files, and Git status.
6. Create `implementation/foundation-agent-01` from the exact current research-branch head.
7. Never write directly to `main`.

If the repository or current branch differs from the values above, stop and report:

```text
STATUS: BLOCKED_REPOSITORY_STATE_MISMATCH
EXPECTED:
ACTUAL:
SAFE REMEDY:
```

## 2. Truth and capability rule

Never report a capability as working because documentation says it should work.

Every capability must progress through:

```text
DOCUMENTED
→ SOURCE_OR_ADAPTER_CONFIRMED
→ IMPLEMENTED_IN_GALAX
→ TESTED_WITH_DETERMINISTIC_FIXTURES
→ LIVE_TESTED_WHEN_CREDENTIALS_ARE_AVAILABLE
→ APPROVED_FOR_THE_EXACT_AGENT_PROFILE
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
files_changed_before_block:
commands_already_run:
```

Do not fabricate tool calls, file writes, commits, tests, API responses, token usage, or successful integrations.

## 3. Mandatory CrewAI configuration

Implement the foundation with these exact defaults:

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

Do not silently substitute another framework, model provider, process, memory system, planner, or code executor.

Use CrewAI `1.15.4` exactly for this validation branch. Pin all direct dependencies and record the resolved versions and hashes in the implementation report.

Use UV for dependency management when compatible with the existing repository.

Candidate setup commands, to be adjusted only after inspecting the current project:

```bash
uv venv --python 3.12
uv sync
uv add "crewai==1.15.4"
```

Do not add an MCP package or provider SDK until you have confirmed the exact official package name and compatible version for the pinned environment. Record the official source used for every added integration dependency.

## 4. Required architecture

Implement this minimum structure without creating duplicate responsibilities:

```text
src/galax_ai/
├── flow/
│   ├── foundation_flow.py
│   └── transitions.py
├── governance/
│   ├── model_hooks.py
│   ├── tool_hooks.py
│   ├── policies.py
│   ├── invocation_ledger.py
│   └── blockers.py
├── models/
│   ├── run_manifest.py
│   ├── profiles.py
│   ├── tool_results.py
│   ├── checkpoints.py
│   └── evidence.py
├── agents/
│   └── engineering_manager.py
├── tools/
│   └── repository_preflight_tool.py
├── gateways/
│   └── github_repository_gateway.py
├── llm/
│   └── profile_factory.py
└── settings.py

tests/
├── unit/
├── integration/
├── security/
├── contract/
└── live/
```

Adapt paths to the existing package name if necessary. Do not create a second parallel package tree.

## 5. Typed contracts to implement

Use Pydantic models with strict validation and forbidden extra fields for all machine-controlled boundaries.

At minimum implement:

### `RunManifest`

```yaml
run_id: UUID
repository: exact owner/name
base_branch: main
run_branch: required prefix galax-validation/
base_head_sha: required full SHA
run_branch_head_sha: optional full SHA
selected_agent_ids: exactly [engineering_manager] for production phase
approved_llm_profile_id: required
approved_tool_profile_id: required
allowed_paths: explicit list
protected_paths: explicit list
data_classification: public | private_scoped | sensitive_restricted
created_at: UTC timestamp
```

### `ToolInvocationRecord`

```yaml
invocation_id: UUID
run_id: UUID
task_id: string
agent_id: string
tool_profile_id: string
operation: string
input_hash: SHA-256
started_at: UTC timestamp
finished_at: UTC timestamp
status: STARTED | SUCCEEDED | BLOCKED | FAILED
raw_output_hash: optional SHA-256
affected_resources: list
external_evidence_ids: list
error_code: optional string
```

### `RepositoryPreflightResult`

Use the exact preflight checks already specified in the Agent 01 research and source card. Do not invent fewer checks.

Required general fields:

```yaml
run_id:
overall_status: PASS | BLOCKED | FAIL
checks:
  - check_id:
    status: PASS | BLOCKED | FAIL
    evidence:
    exact_remedy:
blocking_reasons: []
invocation_id:
input_hash:
result_hash:
```

### `AgentTaskResult`

```yaml
run_id:
agent_id:
task_id:
status: PASS | BLOCKED | FAIL
summary:
evidence_ids: []
invocation_ids: []
claims:
  - statement:
    evidence_id:
unsupported_claims: []
next_transition: STOP | HUMAN_REVIEW | CONTINUE_TO_TEST_ONLY_STAGE
```

## 6. Governance foundation

### 6.1 Model-call gate

Create crew-scoped `PRE_MODEL_CALL` and `POST_MODEL_CALL` hooks.

The pre-model hook must fail closed when any of these are missing or invalid:

```text
- run manifest;
- exact agent ID;
- exact task ID;
- approved LLM profile;
- model/provider match;
- token/call budget;
- data classification;
- secret-redaction result;
- exactly one agent prompt;
- exactly one assigned tool schema;
- prohibited planning/reasoning/native-memory configuration.
```

The post-model hook may redact sensitive output and record usage. It must never convert a blocked or unsupported result into PASS.

Raise `HookAborted` with an explicit reason and source. Do not rely on ordinary exceptions because the CrewAI hook documentation warns that non-abort exceptions may fail open.

### 6.2 Tool-call gate

Create crew-scoped `PRE_TOOL_CALL` and `POST_TOOL_CALL` hooks.

The pre-tool hook must:

```text
- match engineering_manager to RepositoryPreflightTool only;
- reject all other tools;
- verify run ID and task ID;
- verify operation name;
- enforce read-only/no-network behavior;
- reject absolute paths and traversal;
- enforce repository-root and configured allowlists;
- enforce one tool call for Agent 01;
- create the trusted invocation ledger STARTED record.
```

The post-tool hook must:

```text
- hash the raw typed result;
- finish the invocation record;
- reject a missing invocation ID;
- redact secrets from stored diagnostics;
- preserve the original raw result for deterministic validation.
```

A blocked hook result is not enough to stop the system. Implement a deterministic task guardrail and Flow transition that stop downstream work on `BLOCKED` or `FAIL`.

## 7. Agent 01 implementation

Implement only:

```yaml
agent_id: engineering_manager
role: AI Engineering Manager and CrewAI Execution Planning Lead
tool: RepositoryPreflightTool
maximum_tool_interfaces: 1
repository_write: false
network: false
result_as_answer: true
```

Agent 01 must not:

```text
- select agents dynamically;
- modify the run manifest;
- reorder tasks;
- delegate;
- browse the web;
- directly query Drive, Supabase, or Notion;
- edit files;
- create branches or commits;
- approve itself or the system;
- continue after a blocking preflight result.
```

Configure the Agent 01 task so the exact typed `RepositoryPreflightTool` result becomes the task result. The LLM may explain evidence only in a separately labeled advisory field if that does not alter the deterministic status.

## 8. RepositoryPreflightTool

Implement as a custom CrewAI `BaseTool` with strict input and result schemas.

Requirements:

```yaml
filesystem_access: read_only
network_access: none
repository_scope: configured_repository_root_only
symlink_escape: blocked
path_traversal: blocked
secret_values_in_output: prohibited
result_as_answer: true
automatic_retry: 0
```

Implement every check already defined in `03_TOOL_INSPECTION.md`. Include at least these classes of checks:

```text
- repository root and Git metadata;
- required canonical documents;
- supersession registry;
- no active stale Cerebras configuration;
- planning/reasoning/memory/delegation disabled;
- one-agent/one-tool contract;
- approved profile identifiers;
- protected path policy;
- current branch and base SHA consistency;
- dirty/untracked state policy;
- secrets and .env exclusion;
- duplicate-record policy availability;
- required run manifest fields;
- checkpoint and invocation-ledger availability;
- repository permission profile;
- required evidence/source records;
- known MCP security blocker status;
- test-fixture readiness;
- implementation phase authorization;
- exact blocker/remedy generation.
```

If the existing research defines exact IDs or more checks, use those exact definitions as the authority.

## 9. LLM profile factory

Implement profiles as disabled by default.

Agent 01 candidate:

```yaml
profile_id: engineering_manager_groq_gpt_oss_20b_v1
provider: groq
model: groq/openai/gpt-oss-20b
data_classification: private_scoped
reasoning_effort: low
max_completion_tokens: 800
timeout_seconds: 120
max_retries: 1
max_iter: 4
enabled: false
```

Hosted fallback candidate:

```yaml
profile_id: engineering_manager_cloudflare_gpt_oss_20b_v1
provider: custom_openai
model: '@cf/openai/gpt-oss-20b'
enabled: false
```

Rules:

```text
- No fallback is attached simultaneously to the agent.
- No automatic provider switch.
- No provider switch during any external mutation.
- The profile may be enabled only after its exact live test suite passes.
- Missing API credentials produce SKIPPED_LIVE_TEST_MISSING_SECRET, not PASS or FAIL.
- Never print or store API keys.
```

Create a deterministic fake/test LLM only for unit and plumbing tests. Clearly label it `TEST_DOUBLE_NOT_PROVIDER_PROOF`.

## 10. GitHub repository gateway validation

Do not expose the complete GitHub MCP catalog to an agent.

For this phase, implement a trusted application gateway using official GitHub REST/Git Database operations or a strictly filtered local MCP operation behind the gateway.

The gateway must support only these test operations:

```text
get_repository_metadata
read_file_at_ref
get_branch_head
create_validation_branch
commit_validation_fixture
read_commit_and_diff
```

The write operation must require:

```yaml
expected_branch_head_sha: required
allowed_branch_prefix: galax-validation/
force_update: false
allowed_paths:
  - tests/fixtures/github_gateway/**
  - docs/evidence/live-validation/**
maximum_files_per_commit: 5
maximum_total_bytes: bounded and configured
commit_message_prefix: 'test(galax-validation):'
automatic_write_retries: 0
```

Reject:

```text
main/master write;
force push;
branch outside the validation prefix;
protected or workflow paths;
secret files;
deletions;
expected-SHA mismatch;
repository mismatch;
more files or bytes than the configured limit.
```

After a write, re-read the commit and diff and compare path/content hashes. Record the external commit SHA in the invocation ledger.

Do not run the live write without an explicit environment switch such as:

```env
GALAX_ENABLE_LIVE_GITHUB_VALIDATION=true
```

Credentials must come from environment variables or a secret manager. Prefer a repository-scoped GitHub App token. A fine-grained PAT is allowed only for validation and only with the minimum repository permissions.

## 11. Docker foundation

Create a minimal Dockerfile and Compose validation profile only if the repository does not already have an approved equivalent.

Requirements:

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

Do not implement privileged Docker-in-Docker. Do not implement the full coding sandbox in this phase. Create only the interface and explicit blocker:

```text
STATUS: BLOCKED_SANDBOX_NOT_IMPLEMENTED
REMEDY: implement and validate a separate rootless external sandbox before enabling coding agents.
```

## 12. Tests that must be implemented

### 12.1 Unit tests

Test:

```text
- every Pydantic schema;
- strict extra-field rejection;
- profile disabled-by-default behavior;
- path traversal and symlink escape rejection;
- protected-path rejection;
- superseded configuration rejection;
- secret redaction;
- invocation ledger state transitions;
- result hashing;
- Agent 01 one-tool mapping;
- deterministic preflight PASS/BLOCKED/FAIL fixtures.
```

### 12.2 CrewAI contract tests

Prove in the pinned environment:

```text
- one Agent 01 instance;
- exactly one tool attached;
- Process.sequential;
- planning/reasoning/memory/delegation/code execution disabled;
- typed tool output round trip;
- result_as_answer preserves the tool result;
- PRE/POST model hooks execute;
- PRE/POST tool hooks execute;
- blocked tool status stops the Flow;
- a narrative claim without an invocation record is rejected.
```

### 12.3 GitHub gateway negative tests

Prove rejection of:

```text
- direct main write;
- wrong repository;
- wrong branch prefix;
- protected path;
- workflow path;
- secret-like file;
- path traversal;
- deletion;
- stale expected branch SHA;
- force update;
- oversized payload;
- automatic retry after ambiguous write failure.
```

### 12.4 Live GitHub validation

When explicitly enabled and credentials exist:

```text
1. Read repository metadata.
2. Read a known file from the expected base SHA.
3. Create one disposable galax-validation/<run-id> branch.
4. Commit one harmless fixture under an allowed validation path.
5. Verify commit SHA, changed path, content hash, and branch head.
6. Do not merge.
7. Report manual cleanup instructions; do not delete automatically unless a separate cleanup permission is approved.
```

### 12.5 LLM tests

For Groq GPT-OSS 20B, when `GROQ_API_KEY` exists:

```text
- direct completion;
- system-instruction adherence;
- exact single-tool selection;
- valid tool arguments;
- actual invocation-ledger evidence;
- typed result interpretation;
- structured AgentTaskResult output;
- 429/rate-limit handling;
- timeout handling;
- no retry beyond one safe LLM-only retry;
- private-scoped fixture handling;
- no secret echo;
- token usage recording;
- blocked preflight causes STOP.
```

Do not enable the profile unless every required test passes.

### 12.6 Two-agent sequential smoke test

Do not enable Agent 02.

Create test-only fixture agents that are not registered in the production roster:

```text
Fixture Agent A: uses a deterministic fixture preflight tool.
Fixture Agent B: consumes the exact structured result and returns a typed verification result.
```

Requirements:

```text
- Process.sequential ordering is proven from trusted timestamps/events;
- only one LLM call is active at a time;
- Agent B cannot run when Agent A is BLOCKED or FAIL;
- outputs are passed through explicit task context;
- both tool invocations have ledger records;
- fixture agents cannot access GitHub, network, or production paths.
```

Label the result clearly:

```text
TWO_AGENT_FRAMEWORK_SMOKE_TEST_ONLY
NOT_AGENT_02_APPROVAL
```

## 13. Installation and verification commands

After inspecting and adapting to the repository, provide exact runnable commands for Windows PowerShell and Linux/macOS.

At minimum document equivalents of:

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

Live tests must use explicit markers, for example:

```bash
uv run pytest tests/live -m live_github
uv run pytest tests/live -m live_groq
```

They must skip safely when the enabling environment variable or required secret is absent.

## 14. Required outputs

Create or update these records:

```text
docs/evidence/foundation/DEPENDENCY_LOCK_REPORT.md
docs/evidence/foundation/GOVERNANCE_TEST_REPORT.md
docs/evidence/foundation/AGENT_01_TEST_REPORT.md
docs/evidence/foundation/GITHUB_GATEWAY_TEST_REPORT.md
docs/evidence/foundation/LLM_PROFILE_TEST_REPORT.md
docs/evidence/foundation/TWO_AGENT_SMOKE_TEST_REPORT.md
docs/evidence/foundation/FOUNDATION_SELF_DIAGNOSTIC.md
```

Every report must separate:

```yaml
confirmed_passed:
confirmed_failed:
blocked_missing_credentials:
blocked_unsupported:
not_run:
assumptions:
exact_remedies:
commands:
artifacts:
commit_shas:
dependency_versions:
```

## 15. Completion gate

You may report `FOUNDATION_VALIDATED` only if all deterministic, contract, security, and enabled live tests pass.

Even when that happens, do not report the full Galax system as ready.

Allowed final states:

```text
FOUNDATION_VALIDATED_AGENT01_PROFILE_STILL_DISABLED
FOUNDATION_AND_AGENT01_VALIDATED_FOR_EXACT_PROFILE
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_UNSUPPORTED_CAPABILITY
FAILED_WITH_REPRODUCIBLE_EVIDENCE
```

Never use:

```text
100% production ready
all 15 agents working
fully autonomous software company complete
safe because it uses Docker
safe because it uses MCP
successful without test evidence
```

## 16. Final response format

Return your final report in this exact order:

```text
1. Final status
2. Repository branch and commit SHAs
3. Files created/changed
4. Dependency versions and official sources
5. Architecture implemented
6. Deterministic tests and results
7. Live tests and results
8. Security negative tests
9. Unsupported or unverified capabilities
10. Exact remedies
11. Whether Agent 01 may be enabled
12. Whether the full 15-agent prompt remains blocked
```

Do not merge the branch. Open or update a draft pull request only if repository permissions permit and the owner has already authorized draft-PR creation. Otherwise print the exact command or steps needed.
