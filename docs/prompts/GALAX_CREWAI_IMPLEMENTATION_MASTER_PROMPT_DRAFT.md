# Galax AI — CrewAI Implementation Master Prompt

**Status:** `DRAFT_MUTABLE`  
**Purpose:** Paste this prompt into the coding assistant responsible for building the Galax CrewAI system.  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Important:** This prompt does not authorize merging, production deployment, secret creation, or enabling untested agents.

---

## MASTER PROMPT

You are the implementation assistant responsible for building the **Galax AI fact-checked, sequential CrewAI software-development assistant system** inside this repository:

```text
https://github.com/ariessocia04-rgb/galax-Ai-project
```

Your task is to turn the existing researched plans into a working, testable implementation without claiming any capability that CrewAI, the selected LLM, the assigned tool, Docker, Google Drive, Supabase, Notion, or GitHub cannot actually perform.

You are not authorized to redesign the approved agent roster, silently replace the selected provider, weaken security rules, merge a pull request, deploy production, or pretend an unimplemented capability works.

# 1. Mandatory repository-first procedure

Before writing code:

```text
1. Open the exact Galax repository.
2. Confirm the repository identity and default branch.
3. Read README.md completely.
4. Read every applicable file under docs/rules/.
5. Read every applicable file under docs/plan/.
6. Read docs/sources/SOURCE_INDEX.md.
7. Read the current CrewAI, LLM, Docker, memory, knowledge, GitHub, and agent research records.
8. Read the current agent source card before implementing that agent.
9. Detect exact duplicates before creating files.
10. Create or use a dedicated run branch. Never write directly to main.
```

Required branch format:

```text
galax/run/<run-id>-build-crewai-foundation
```

If README, active rules, source index, or required plans cannot be found:

```yaml
status: BLOCKED_REQUIRED_REPOSITORY_DOCUMENT_MISSING
can_continue: false
remedy:
  - list_the_missing_files
  - identify_the_expected_paths
  - create_only_the_missing_planning_record_if_authorized
  - do_not_implement_agents
```

# 2. Non-negotiable capability rule

Never assign an agent work unless all required layers are supported and live-tested:

```text
CrewAI framework
+ exact pinned CrewAI version
+ exact LiteLLM version when used
+ exact provider and model
+ exact agent prompt
+ exactly one role-specific tool interface
+ required permission profile
+ deterministic Flow
+ Docker or sandbox boundary when required
+ Google Drive learning context when required
+ memory context when required
+ structured output and guardrails
+ failure handling
+ live tests
+ human approval when required
```

When any layer is missing, deprecated, incompatible, unknown, or untested:

```yaml
status: BLOCKED_UNSUPPORTED_CAPABILITY
can_continue: false
must_not:
  - simulate_success
  - fabricate_tool_output
  - invent_test_results
  - invent_repository_changes
  - silently_skip_the_requirement
  - silently_use_another_provider_or_model
required_response:
  capability_requested:
  unsupported_or_missing_layer:
  factual_reason:
  official_source_or_repository_record:
  effect_on_flow:
  safe_remedy:
  required_tests_after_remedy:
```

# 3. Approved execution model

The running Crew must use:

```python
process=Process.sequential
```

Global execution restrictions:

```yaml
allow_delegation: false
async_execution: false
parallel_agents: false
parallel_tool_calls: false
concurrent_llm_calls: 1
active_agents_at_once: 1
automatic_provider_fallback: false
maximum_retries: 1
```

The deterministic Flow or trusted application must select the required agents and tasks before constructing the Crew.

The active CrewAI agent must never:

```text
- dynamically add agents
- dynamically reorder tasks
- delegate to another agent
- activate a Docker Compose profile
- create or change credentials
- merge a pull request
- deploy production
- approve its own work
```

# 4. One agent, one tool interface

Each agent receives exactly one role-specific tool interface.

```yaml
llm_profiles_per_agent: 1
tool_interfaces_per_agent: 1
```

A single tool interface may expose a small set of closely related operations required by that role. It must not expose unrelated GitHub, browser, shell, database, security, or deployment functions.

Google Drive knowledge retrieval, Supabase memory retrieval, Notion mirroring, branch creation, checkpointing, and agent selection are Flow/application infrastructure. They are not additional tools exposed directly to every agent.

If the active agent needs a capability outside its tool:

```yaml
status: DIFFERENT_SEQUENTIAL_STAGE_REQUIRED
can_continue_current_agent: false
remedy:
  - return_control_to_flow
  - select_the_correct_approved_agent_in_a_later_stage
  - preserve_the_checkpoint
```

# 5. Current candidate technology baseline

Treat all versions as candidates until compatibility tests pass and the lockfile is committed.

```yaml
python_candidate: "3.12"
crewai_candidate: "1.15.4"
process: sequential
llm_provider_candidate: Cerebras
llm_model_candidate: cerebras/gpt-oss-120b
crewai_native_memory: disabled
primary_machine_memory_candidate: Supabase_Postgres_or_Postgres_with_pgvector
human_memory_mirror_candidate: Notion_optional
knowledge_source: approved_Google_Drive_folders
container_runtime: Docker_Compose
built_in_crewai_code_execution: prohibited
```

Before pinning dependencies, verify the current official package metadata and compatibility. Record:

```yaml
python_version:
crewai_version:
litellm_version:
pydantic_version:
provider_adapter_version:
docker_version:
docker_compose_version:
postgres_version:
pgvector_version:
supabase_client_version:
google_drive_client_version:
notion_client_version:
verified_date:
```

If the exact candidate version is unavailable or incompatible, do not silently upgrade or downgrade. Return `REVALIDATION_REQUIRED` with the reason and proposed tested version.

# 6. Required project structure

Create a clean Python project using `src/` layout. Preserve existing valid repository files.

```text
.
├── README.md
├── pyproject.toml
├── uv.lock or another approved committed lockfile
├── .env.example
├── .gitignore
├── compose.yaml
├── compose.override.example.yaml
├── Dockerfile
├── docker/
│   ├── api.Dockerfile
│   ├── flow-runner.Dockerfile
│   ├── gateway.Dockerfile
│   ├── healthchecks/
│   └── security/
├── src/
│   └── galax_ai/
│       ├── __init__.py
│       ├── api/
│       ├── flow/
│       │   ├── state.py
│       │   ├── router.py
│       │   ├── checkpoints.py
│       │   ├── change_detector.py
│       │   └── execution.py
│       ├── crew/
│       │   ├── crew.py
│       │   ├── registry.py
│       │   ├── agents.yaml
│       │   ├── tasks.yaml
│       │   └── run_manifest.py
│       ├── llm/
│       │   ├── factory.py
│       │   ├── profiles.py
│       │   ├── budget.py
│       │   └── validation.py
│       ├── tools/
│       │   ├── base.py
│       │   ├── repository_preflight.py
│       │   └── profiles/
│       ├── gateways/
│       │   ├── repository/
│       │   ├── drive_knowledge/
│       │   ├── memory/
│       │   ├── notion_mirror/
│       │   ├── research/
│       │   └── sandbox/
│       ├── diagnostics/
│       ├── guardrails/
│       ├── schemas/
│       ├── security/
│       ├── observability/
│       └── settings.py
├── migrations/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── security/
│   ├── docker/
│   ├── llm/
│   ├── tools/
│   └── flow/
└── docs/
```

Do not create an exact duplicate of an existing file or record. When normalized content is 100% identical, keep one canonical file, update references, and remove the duplicate only when authorized and safely verified.

# 7. Installation procedure

## 7.1 Host prerequisites

Verify and report, do not assume:

```text
- Git
- Python 3.12 candidate
- uv or approved Python package manager
- Docker Engine or Docker Desktop
- Docker Compose v2
- sufficient disk and memory
```

Provide exact commands for the detected operating system. Do not claim that a command ran unless actual command evidence exists.

Candidate Python setup:

```bash
python --version
uv --version
uv sync
```

When the project has not yet been initialized, use the approved package manager to create the environment and install the pinned dependencies. Candidate dependency groups include:

```text
runtime:
- crewai with LiteLLM support
- fastapi
- uvicorn
- pydantic
- pydantic-settings
- httpx
- structlog
- psycopg
- pgvector
- Google Drive API client and Google authentication libraries
- Notion client only for the optional mirror

development:
- pytest
- pytest-asyncio
- coverage
- ruff
- mypy
- bandit
- pip-audit or approved dependency scanner
```

Do not invent package versions. Research, test, pin, and commit the exact compatible versions.

## 7.2 Environment template

Create `.env.example` only. Never create or commit real secrets.

```env
GALAX_ENV=development
GALAX_REPOSITORY=ariessocia04-rgb/galax-Ai-project
GALAX_PROCESS=sequential
GALAX_MAX_CONCURRENT_LLM_CALLS=1
GALAX_MAX_ACTIVE_AGENTS=1
GALAX_INTERNAL_MAX_RPM=4
GALAX_RUN_SOFT_TOKEN_LIMIT=90000
GALAX_RUN_HARD_TOKEN_LIMIT=120000

CEREBRAS_API_KEY=
GALAX_LLM_MODEL=cerebras/gpt-oss-120b

GITHUB_APP_ID=
GITHUB_APP_INSTALLATION_ID=
GITHUB_APP_PRIVATE_KEY_FILE=/run/secrets/github_app_private_key

GOOGLE_DRIVE_CREDENTIALS_FILE=/run/secrets/google_drive_credentials
GOOGLE_DRIVE_ALLOWED_ROOT_ID=

MEMORY_DATABASE_URL=
SUPABASE_URL=
SUPABASE_SECRET_KEY_FILE=/run/secrets/supabase_secret_key

NOTION_TOKEN_FILE=/run/secrets/notion_token
NOTION_MEMORY_INDEX_PAGE_ID=

SANDBOX_CONTROLLER_URL=
SANDBOX_CONTROLLER_TOKEN_FILE=/run/secrets/sandbox_controller_token
```

Ensure `.env`, secret files, private keys, database dumps, and generated credentials are ignored.

# 8. Docker implementation

Create a Compose design with these core services:

```text
- galax-api
- galax-flow-runner
- repository-gateway
- drive-knowledge-gateway
- memory-gateway
```

Optional profiles:

```text
- research
- notion-mirror
- local-memory
- full-supabase
- sandbox-client
- observability
```

Do not let an LLM activate profiles. Only trusted operator/application configuration may do so.

Every Galax-owned container must use this baseline unless a documented exception is approved:

```yaml
user: non_root_numeric_uid
read_only: true
cap_drop:
  - ALL
security_opt:
  - no-new-privileges:true
init: true
pids_limit: explicit
mem_limit: explicit
cpus: explicit
tmpfs:
  - /tmp
```

Prohibited Docker configuration:

```text
- privileged: true
- host network mode
- host PID mode
- host root filesystem mount
- production SSH directory mount
- unrestricted Docker socket mount
- Docker-in-Docker as the default sandbox
- one shared secret mounted into all services
```

Use per-service Compose secrets. Add health checks and prevent the Flow runner from accepting work until mandatory gateways are healthy and their permission self-tests pass.

Use multi-stage images, pin validated base-image digests, run as non-root, generate an SBOM, and scan the final images.

# 9. External sandbox implementation boundary

CrewAI built-in code execution must remain disabled.

The coding and testing tools must use:

```text
workspace tool
→ authenticated sandbox-controller API
→ separate rootless Docker daemon or separate sandbox host
→ ephemeral non-root container
→ mounted run worktree only
→ no secrets
→ network disabled by default
→ allowlisted command
→ CPU, memory, PID, and time limits
→ output and artifact hashes
→ mandatory cleanup
```

Do not mount the Docker socket into the CrewAI or Flow container.

If a safe external sandbox is not available:

```yaml
status: BLOCKED_SANDBOX_NOT_AVAILABLE
blocked_agents:
  - frontend_engineer
  - backend_engineer
  - database_engineer_for_execution
  - crewai_engineer_for_runtime_tests
  - qa_engineer
  - devops_engineer_for_builds
remedy:
  - implement_and_test_the_separate_sandbox_controller
  - or_limit_the_stage_to_read_only_planning_without_claiming_execution
```

# 10. LLM implementation and validation

Create one LLM factory and separate per-agent profiles. The LLM is not a tool.

Current selected validation candidate:

```text
cerebras/gpt-oss-120b
```

Provider metadata and limits must be read from the current official provider source and, when available, the connected account. Published limits are planning information only.

Global internal restrictions:

```yaml
timeout_seconds: 120
maximum_retries: 1
internal_max_rpm: 4
respect_context_window: false
crewai_reasoning_loop: false
memory: false
allow_delegation: false
allow_code_execution: false
async_execution: false
```

Do not enable an agent profile until the exact model and profile pass:

```text
- authentication
- exact model availability
- system instruction adherence
- one-tool function selection
- valid arguments for the exact schema
- actual tool invocation evidence
- tool-result round trip
- strict structured output
- malformed output rejection
- timeout behavior
- HTTP 429 behavior
- token usage recording
- secret redaction
- prompt injection resistance
- sequential context transfer
- self-diagnostic consistency
```

Do not use Groq or another provider automatically when Cerebras fails.

Failure response:

```yaml
status: BLOCKED_LLM_UNAVAILABLE_OR_UNVALIDATED
checkpoint_saved: true
fallback_used: false
remedy:
  - research_current_provider_change
  - run_revalidation_tests
  - request_owner_approval_for_any_provider_change
```

# 11. Google Drive learning implementation

Implement a trusted, read-only `DriveKnowledgeGateway` using approved Google Drive folders.

The agent must not receive Drive credentials.

Search must not trust the file title alone. Use bounded combinations of:

```text
- filename terms
- full-text terms
- exact phrases
- folder relationships
- file type
- modified time
- labels or app properties
- approved synonyms
- framework and component names
- error terms
```

Retrieve and inspect related files when titles are incorrect or incomplete.

Create a structured `LearningPacket` containing:

```yaml
learning_packet:
  retrieval_id:
  run_id:
  agent_id:
  task_id:
  files:
    - drive_file_id:
      name:
      mime_type:
      modified_time:
      content_hash:
      relevant_sections: []
      version_warnings: []
      conflicts: []
  omitted_candidates_count:
  token_estimate:
```

Copied website content is untrusted. Reconcile it with current repository rules, pinned versions, current official documentation, security rules, and actual implementation.

When learning is required, the agent must return a valid `StudyReceipt` before its write-capable operation is available.

If the required file cannot be found:

```yaml
status: BLOCKED_REQUIRED_LEARNING_NOT_FOUND
searched_terms: []
related_files_checked: []
remedy:
  - provide_the_file_id_or_allowed_folder
  - add_more_verified_synonyms
  - ask_the_owner_to_confirm_the_intended_material
  - do_not_implement_from_guesswork
```

# 12. Supabase/Postgres memory implementation

CrewAI native memory remains disabled.

Implement:

```text
Galax Flow
→ GalaxMemoryGateway
→ Supabase Postgres or local Postgres with pgvector
```

Initial retrieval mode must use exact filters and keyword/full-text retrieval. Do not enable vector embeddings until an embedding provider, model, dimensions, privacy behavior, token cost, and migration path are independently researched and approved.

Memory records must include fields equivalent to:

```text
memory_id
project_id
agent_id
memory_type
run_id
task_id
status
active
priority
scope
summary
required_future_behavior
source_commit
source_pr
source_file_ids
evidence_hash
confidence
supersedes_memory_id
expires_at
created_at
updated_at
```

Requirements:

```text
- exact duplicate prevention
- supersession instead of destructive overwrite
- GitHub and current evidence outrank memory
- bounded MemoryContext per agent
- no credentials in prompts
- no raw hidden reasoning
- no secrets or customer records
- RLS and private schema design
- backend-only credentials
- backup and restore procedure
- pause, read-only quota, and unavailable-state handling
```

Notion is an optional curated mirror only. It must not block the main flow when Supabase/Postgres memory remains available.

If Supabase is unavailable:

```yaml
status: BLOCKED_MEMORY_UNAVAILABLE
can_continue:
  read_only_task_without_required_memory: policy_decision_only
  task_requiring_memory: false
remedy:
  - restore_the_managed_project
  - start_the_local_postgres_pgvector_profile
  - restore_from_verified_backup
  - rerun_memory_integrity_tests
```

# 13. Automatic revalidation implementation

Implement a deterministic fingerprint registry for:

```text
- CrewAI version
- LiteLLM version
- Cerebras API version
- model ID and metadata
- model behavior contract
- each agent prompt hash
- each tool schema hash
- tool implementation commit
- permission-policy hash
- repository-structure manifest hash
- current account rate-limit snapshot
- security-rules hash
- memory-schema hash
- Docker Compose and image-digest hash
```

On change:

```text
record old/new fingerprint
→ identify affected agents and stages
→ set only affected capabilities to REVALIDATION_REQUIRED
→ disable affected profiles
→ save checkpoint
→ block affected implementation
→ start separate Agent 03 revalidation research stage
```

Agent 03 receives exactly one `EphemeralRevalidationResearchTool` instance. It may read only official allowlisted sources and may write only research/source records on the run branch.

Research must return:

```yaml
change_reason:
official_sources: []
source_code_or_adapter_evidence: []
affected_agents: []
affected_tools: []
affected_prompts: []
backward_compatible:
required_migration:
proposed_solution:
unsupported_options: []
security_impact:
token_and_rate_impact:
mandatory_live_tests: []
implementation_allowed: false
```

Research never automatically enables implementation.

# 14. Agent scaffold and enablement order

Create configuration records for all 15 agents, but set every profile to disabled.

```text
01 Engineering Manager / Preflight
02 Product Requirements and Scope Lead
03 Evidence and Capability Researcher
04 Solution and Systems Architect
05 UX, UI, and Accessibility Designer
06 Frontend Application Engineer
07 Backend and API Engineer
08 Data and Database Engineer
09 CrewAI and AI Systems Engineer
10 Integration and MCP Engineer
11 Security, Privacy, and AI Safety Engineer
12 QA and Test Automation Engineer
13 DevOps and CI/CD Engineer
14 SRE and Observability Engineer
15 Independent Code Review, Documentation, and Release Auditor
```

Implement and validate agents one at a time.

First implementation target:

```text
Agent 01 + RepositoryPreflightTool
```

Do not enable Agent 02 until Agent 01, Flow selection, checkpoints, LLM profile, tool evidence, and sequential stop behavior pass.

Each agent requires:

```text
ROLE FACT CHECKED
→ CREWAI FEATURE SUPPORTED
→ LLM PROFILE LIVE TESTED
→ ONE TOOL IMPLEMENTED AND LIVE TESTED
→ KNOWLEDGE STUDY TEST WHEN REQUIRED
→ MEMORY CONTEXT TESTED WHEN REQUIRED
→ STRUCTURED OUTPUT AND SELF-DIAGNOSTIC TESTED
→ SECURITY AND PERMISSION TESTS PASSED
→ SEQUENTIAL CONTEXT TEST PASSED
→ INDEPENDENT AUDIT
→ OWNER DECISION
```

# 15. Self-diagnostic contract

Every task output must include a structured self-diagnostic, but the agent's own `PASS` is not final evidence.

```yaml
self_diagnostic:
  status: PASS | PARTIAL | BLOCKED_INPUT | BLOCKED_TOOL | BLOCKED_LLM | BLOCKED_MEMORY | BLOCKED_KNOWLEDGE | BLOCKED_SANDBOX | FAILED_VALIDATION | FAILED_EXECUTION
  objective_understood:
  repository_rules_read:
  required_inputs_present:
  learning_packet_read_when_required:
  memory_context_used_when_required:
  assigned_tool_used:
  actual_tool_invocation_ids: []
  unsupported_action_attempted:
  assumptions_made: []
  files_changed: []
  tests_run: []
  errors: []
  remaining_risks: []
  recommended_next_action:
```

A deterministic guardrail must compare the self-diagnostic against actual tool, repository, sandbox, test, and checkpoint evidence.

# 16. Minimum implementation phases

Execute in this order and stop when a phase is blocked:

```text
PHASE 0 — Repository preflight and duplicate scan
PHASE 1 — Current-version research and dependency lock proposal
PHASE 2 — Python project scaffold and schemas
PHASE 3 — Docker images, Compose, networks, secrets, healthchecks
PHASE 4 — Deterministic Flow, run ledger, manifests, checkpoints
PHASE 5 — LLM factory, budgets, and validation harness
PHASE 6 — Repository gateway and RepositoryPreflightTool
PHASE 7 — Agent 01 implementation and tests
PHASE 8 — Google Drive knowledge gateway and StudyReceipt tests
PHASE 9 — Supabase/Postgres memory gateway and integrity tests
PHASE 10 — Optional Notion mirror
PHASE 11 — External sandbox controller integration
PHASE 12 — Agent 03 revalidation research flow
PHASE 13 — Remaining agent scaffolds and one-by-one implementation
PHASE 14 — QA, security, observability, and release audit
```

Do not skip forward and then claim earlier dependencies are complete.

# 17. Required test categories

At minimum create tests for:

```text
- repository identity and protected branch rules
- no exact duplicate creation
- Process.sequential task order
- one active agent and one active LLM call
- exactly one tool interface per agent
- real tool invocation evidence
- malformed tool arguments
- failed tool stops downstream stages
- prompt and tool fingerprint revalidation
- HTTP 429 and timeout handling
- token soft and hard limits
- checkpoint save and resume
- Docker non-root/read-only/capability-drop rules
- secret isolation and log redaction
- no Docker socket access
- sandbox resource, network, command, and cleanup controls
- Drive related-file discovery when title is wrong
- LearningPacket and StudyReceipt validation
- Supabase exact-filter memory retrieval
- duplicate and supersession behavior
- RLS/private access boundaries
- memory backup/restore
- Notion mirror failure does not destroy runtime memory
- unsupported capability returns factual reason and remedy
```

A phase is complete only when 100% of its defined mandatory tests pass in the pinned environment and evidence is recorded.

# 18. Required response format during implementation

After every phase, return:

```yaml
phase:
status: COMPLETED | PARTIAL | BLOCKED
repository_branch:
commit_sha:
files_created: []
files_updated: []
commands_actually_run: []
tests_actually_run: []
tests_passed:
tests_failed:
tool_invocation_ids: []
facts_verified: []
assumptions: []
unsupported_items:
  - requested_capability:
    reason_not_supported:
    evidence:
    impact:
    safe_remedy:
    tests_required_after_remedy:
security_findings: []
remaining_blockers: []
next_permitted_phase:
```

Never report a command, test, Docker service, database migration, API connection, branch, commit, or file as successful without actual evidence.

# 19. Initial execution requested now

For the first run, do only the following:

```text
1. Inspect the repository and all current draft rules/plans.
2. Produce a conflicts-and-missing-prerequisites report.
3. Verify the current CrewAI, LiteLLM, Cerebras, Docker, Supabase, Google Drive, Notion, and GitHub integration assumptions using official sources.
4. Propose exact pinned dependency versions but do not silently finalize them without tests.
5. Create the implementation branch.
6. Create the clean src-based scaffold, schemas, test directories, Docker skeleton, and environment template.
7. Implement deterministic configuration loading, run manifest schema, status enums, and failure contracts.
8. Implement no production credentials and no direct-main-write protections.
9. Scaffold all 15 agents as disabled records only.
10. Implement Agent 01 and RepositoryPreflightTool only when its prerequisites are satisfied.
11. Run the Phase 0–7 mandatory tests that are possible in the current environment.
12. Clearly list everything that cannot yet be completed and give a factual remedy for each item.
13. Stop before enabling Agent 02 or any additional agent.
14. Create or update a draft pull request. Do not merge it.
```

Final first-run status must be one of:

```text
FOUNDATION_VALIDATED_AGENT_01_READY
FOUNDATION_PARTIAL_BLOCKERS_RECORDED
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_MISSING_CREDENTIALS_FOR_LIVE_TESTS
BLOCKED_SANDBOX_NOT_AVAILABLE
BLOCKED_REVALIDATION_REQUIRED
```

Do not use the words “fully working,” “production ready,” “secure,” or “complete” unless every defined mandatory test for that exact claim has passed and the evidence is recorded.
