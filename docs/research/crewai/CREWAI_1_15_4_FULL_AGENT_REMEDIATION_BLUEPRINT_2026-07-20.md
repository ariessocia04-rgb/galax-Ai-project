# CrewAI 1.15.4 Full 15-Agent Remediation Blueprint — 2026-07-20

**Status:** `RESEARCH_RECORD_AND_IMPLEMENTATION_GATE`  
**Implementation:** `NOT_STARTED`  
**Agents enabled:** `0`  
**Framework candidate:** CrewAI `1.15.4` at source commit `69c0308f2cf4fa17214eab4db10071abc08602fd`  
**Process:** `Process.sequential`  
**Decision:** The 15-agent Galax design is technically achievable as a bounded CrewAI application only when the deterministic Flow, role-scoped tools, LLM profiles, gateways, sandbox, permissions, and live tests described here are implemented. CrewAI alone does not provide the complete system.

## 1. Evidence standard and meaning of “100%”

Galax must not promise perfect AI behavior. The permitted statement is:

```text
100% of the defined documentation, source-code or adapter, security,
compatibility, and live execution tests passed for the exact pinned
configuration and recorded date.
```

Every capability progresses through:

```text
DOCUMENTED
→ SOURCE_OR_ADAPTER_CONFIRMED
→ IMPLEMENTED_IN_GALAX
→ LIVE_TESTED_IN_PINNED_ENVIRONMENT
→ APPROVED_FOR_EXACT_AGENT
```

A version, model, prompt, tool schema, permission, repository, quota, privacy rule, or infrastructure fingerprint change returns only affected profiles to `REVALIDATION_REQUIRED`.

## 2. Current CrewAI facts that change the remedy

### 2.1 Supported primitives

CrewAI 1.15.4 supports the primitives Galax needs for bounded agents:

```text
- Process.sequential and ordered task context
- one or more assigned tools, allowing Galax to enforce exactly one
- custom BaseTool and @tool implementations
- typed Pydantic tool results
- output_json and output_pydantic task results
- deterministic function guardrails
- PRE_TOOL_CALL and POST_TOOL_CALL hooks
- PRE_MODEL_CALL and POST_MODEL_CALL hooks
- MCP adaptation and exact tool-name filtering
- Flow routing and state
- manual and automatic checkpoint APIs
- result_as_answer for evidence-only tool tasks
```

Official versioned sources:

- [CrewAI tasks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/tasks.mdx)
- [Create custom tools](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/create-custom-tools.mdx)
- [Tool call hooks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/tool-hooks.mdx)
- [LLM call hooks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/llm-hooks.mdx)
- [Force tool output as result](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/force-tool-output-as-result.mdx)
- [Checkpointing](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/checkpointing.mdx)
- [MCP overview](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/mcp/overview.mdx)

### 2.2 CrewAI features disabled by design

```yaml
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
```

Reasons:

1. `planning=True` sends all Crew information to an AgentPlanner before each iteration and defaults to `gpt-4o-mini` unless another planning model is configured. This introduces an unapproved provider, extra cost/calls, and wider prompt exposure.
2. `reasoning=True` runs an additional reasoning/refinement loop; its default attempt limit can be unbounded, and CrewAI documents that execution continues without the reasoning plan when that stage fails. Galax requires fail-closed planning.
3. CrewAI native memory is not the selected source of truth and can introduce hidden analysis/embedder behavior. Supabase/Postgres is the controlled external memory candidate.
4. Built-in code execution is not the approved sandbox.
5. Automatic context summarization can remove exact paths, rules, evidence, and security constraints.

The remedy is provider-native `reasoning_effort` plus an explicit structured planning/requirements task. The deterministic Flow validates that plan before any write stage.

## 3. Mandatory runtime governance layers

### 3.1 Model-call gate

A crew-scoped `PRE_MODEL_CALL` hook must:

```text
- verify the active agent/profile/task/run identifiers;
- verify the provider and exact model are approved for that agent;
- enforce the current account capacity snapshot;
- scan for credentials, secrets, personal data, and prohibited paths;
- enforce the data-classification policy;
- enforce input and expected-output token budgets;
- ensure only one agent prompt and one tool schema are present;
- reject an unapproved planning, memory, or fallback model call.
```

A `POST_MODEL_CALL` hook may redact output and record usage, but cannot turn unsupported output into a pass.

### 3.2 Tool-call gate

A crew-scoped `PRE_TOOL_CALL` hook must:

```text
- verify agent-to-tool identity;
- reject every tool except the single assigned interface;
- validate run ID, branch, repository, operation, paths, and expected hashes;
- block protected paths and non-approved operations;
- enforce call count, timeout, rate, and data-class rules;
- require an approved StudyReceipt before a knowledge-dependent write;
- require human approval when the operation contract demands it.
```

A blocked CrewAI tool hook returns a blocked result and the agent run may continue. Therefore the hook is not the final stop gate. The tool result schema must contain a blocked status, and a deterministic task guardrail plus Flow transition must stop downstream work.

### 3.3 Invocation ledger

Every real action requires trusted evidence generated outside the LLM:

```yaml
tool_invocation:
  invocation_id:
  run_id:
  task_id:
  agent_id:
  tool_profile_id:
  operation:
  input_hash:
  started_at:
  finished_at:
  status:
  raw_output_hash:
  affected_resources: []
  external_evidence_ids: []
```

A narrative `Action`, `Observation`, `file written`, `test passed`, or `commit created` without this record is `FAILED_FABRICATED_TOOL_RESULT`.

CrewAI issue evidence records a case where a model produced convincing Action/Observation text without invoking the assigned tool:

- [CrewAI issue #3154](https://github.com/crewAIInc/crewAI/issues/3154)

### 3.4 Structured output and guardrails

Every agent task must use an explicit Pydantic or JSON output contract. Machine-checkable rules use Python function guardrails. LLM guardrails may supplement subjective review but cannot authorize security, repository writes, tests, deployment, or release.

Default:

```yaml
max_retry_limit: 1
guardrail_max_retries: 1
```

Second failure stops the stage and saves the canonical checkpoint.

### 3.5 Evidence-only tasks

`result_as_answer=True` is selected only when the exact tool result should be the final task evidence, such as:

```text
- Agent 01 repository preflight evidence
- deterministic test execution evidence when no interpretation is required
- final release evidence bundle retrieval
```

Writer agents normally require a typed tool result followed by a separately validated structured final response.

## 4. MCP security correction

CrewAI MCP support is technically real, but full arbitrary MCP exposure is not approved.

Current risk evidence:

- [Open CrewAI issue #6504 — MCP arguments bypass SSRF validation and DNS-rebinding risk](https://github.com/crewAIInc/crewAI/issues/6504)
- [Open CrewAI PR #6519 — proposed MCP and DNS-pinning fix](https://github.com/crewAIInc/crewAI/pull/6519)

Until a patched release is pinned and revalidated:

```yaml
generic_remote_MCP_servers: prohibited
arbitrary_URL_MCP_tools: prohibited
full_GitHub_MCP_tool_catalog_to_agent: prohibited
local_role_scoped_gateway: required
URL_allowlist: required
private_link_local_metadata_IPs: blocked
DNS_resolution_and_connection_validation: required
request_and_response_schema_validation: required
write_retry: zero_automatic_retries
```

The preferred Galax implementation is a local custom CrewAI `BaseTool` calling a trusted role-scoped gateway. MCP may be used behind the gateway only for exact filtered operations after security tests.

## 5. GitHub read/write remediation

The official GitHub MCP Server exposes real repository operations, including:

```text
- get_file_contents
- create_branch
- push_files
- pull-request operations
```

The official `push_files` schema pushes multiple files to a named branch in one commit, but its public tool schema does not require an expected branch-head SHA. Therefore direct exposure is insufficient for Galax concurrency safety.

Selected transaction:

```text
trusted Flow reads current main and run-branch head
→ creates the dedicated run branch
→ role-scoped tool inspects exact allowed files
→ gateway verifies expected branch-head and blob hashes
→ gateway creates blobs/tree/commit through GitHub Git Database API
→ gateway updates ref with force=false
→ gateway re-reads commit and diff
→ invocation ledger stores evidence
→ QA and auditor read only
→ trusted Flow creates or updates a draft PR
```

Official sources:

- [GitHub MCP Server](https://github.com/github/github-mcp-server)
- [GitHub MCP push_files schema](https://github.com/github/github-mcp-server/blob/1338dbed4a044ee26422d4212bac3a8037fdb7ff/pkg/github/__toolsnaps__/push_files.snap)
- [GitHub Git database API](https://docs.github.com/en/rest/git)
- [GitHub repository contents permissions](https://docs.github.com/en/rest/repos/contents)

Direct `main` write, force push, automatic merge, unrestricted deletion, credential changes, and workflow changes are denied unless a future separately approved profile exists.

## 6. Corrected model classes

### 6.1 Low and medium bounded work

```yaml
primary_candidate: groq/openai/gpt-oss-20b
hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-20b
optional_local_fallback: ollama/gpt-oss:20b
```

Use for tasks whose quality suite proves the 20B model is sufficient. The expected advantage is latency and lower hosted compute use, not a larger Groq free quota.

### 6.2 High-complexity private work

```yaml
primary_candidate: groq/openai/gpt-oss-120b
hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
optional_local_fallback: none_until_a_quality_equivalent_local_profile_is_proven
```

### 6.3 Public or fully redacted long context

```yaml
candidate: gemini/gemini-2.5-flash
private_or_confidential_content: prohibited_on_free_tier
```

### 6.4 Provider-capacity reality

Current planning records for Groq GPT-OSS 20B and 120B use the same documented base free limits:

```yaml
RPM: 30
RPD: 1000
TPM: 8000
TPD: 200000
```

The runtime must use the connected organization's current limits. Cloudflare capacity is a daily neuron allocation, not a guaranteed token count. Gemini limits are project/account/model specific. Ollama capacity is the measured local hardware capability.

## 7. Full 15-agent compatibility matrix

Every entry below is a **candidate configuration**, not an approval.

| ID | Agent | Primary model candidate | Hosted fallback | One tool interface | CrewAI mechanism | Current status |
|---:|---|---|---|---|---|---|
| 01 | Engineering Manager / Preflight | Groq GPT-OSS 20B, low | Cloudflare GPT-OSS 20B | `RepositoryPreflightTool` | typed BaseTool, `result_as_answer`, function guardrail | tool specified, not implemented |
| 02 | Product Requirements and Scope Lead | Groq GPT-OSS 20B, medium | Cloudflare GPT-OSS 20B | `RequirementsWorkspaceTool` | typed repository workspace tool | research/tool not implemented |
| 03 | Evidence and Capability Researcher | Gemini 2.5 Flash for public/redacted; Groq 120B for private scoped | Cloudflare 120B for private scoped | `VerifiedResearchWorkspaceTool` | custom research gateway, structured evidence | gateway not implemented |
| 04 | Solution and Systems Architect | Groq GPT-OSS 120B, high | Cloudflare GPT-OSS 120B | `ArchitectureWorkspaceTool` | typed docs workspace tool | not implemented |
| 05 | UX, UI, and Accessibility Designer | Groq GPT-OSS 20B, medium | Cloudflare GPT-OSS 20B | `UXWorkspaceTool` | local/staging browser evidence + docs write | not implemented |
| 06 | Frontend Application Engineer | Groq GPT-OSS 20B initially; promote to 120B only on failed quality gate | matching approved Cloudflare profile | `FrontendWorkspaceTool` | repo gateway + external sandbox composite | sandbox not implemented |
| 07 | Backend and API Engineer | Groq GPT-OSS 120B, high | Cloudflare GPT-OSS 120B | `BackendWorkspaceTool` | repo gateway + external sandbox composite | sandbox not implemented |
| 08 | Data and Database Engineer | Groq GPT-OSS 120B, high | Cloudflare GPT-OSS 120B | `DatabaseWorkspaceTool` | repo gateway + disposable DB sandbox | disposable DB not implemented |
| 09 | CrewAI and AI Systems Engineer | Groq GPT-OSS 120B, high | Cloudflare GPT-OSS 120B | `CrewAIWorkspaceTool` | pinned CrewAI/config/test sandbox | not implemented |
| 10 | Integration and MCP Engineer | Groq GPT-OSS 120B, high | Cloudflare GPT-OSS 120B | `IntegrationMCPWorkspaceTool` | local/mock MCP plus scoped adapter workspace | MCP security tests missing |
| 11 | Security, Privacy, and AI Safety Engineer | Groq GPT-OSS 120B, high | no hosted fallback until sensitive-data suite passes; local candidate later | `SecurityAuditTool` | read-only scanner composite + evidence | not implemented |
| 12 | QA and Test Automation Engineer | Groq GPT-OSS 20B, medium | Cloudflare GPT-OSS 20B | `TestRunnerTool` | test-write allowlist + sandbox runner | not implemented |
| 13 | DevOps and CI/CD Engineer | Groq GPT-OSS 20B, medium | Cloudflare GPT-OSS 20B | `CIBuildWorkspaceTool` | build-file workspace + local build sandbox | not implemented |
| 14 | SRE and Observability Engineer | Groq GPT-OSS 120B, high | Cloudflare 120B only with fully redacted telemetry | `ObservabilityReadTool` | read-only bounded logs/metrics/traces | telemetry gateway absent |
| 15 | Independent Release Auditor | Groq GPT-OSS 120B, high | Cloudflare 120B after audit-quality test | `ReleaseAuditTool` | read-only evidence bundle + deterministic reconciliation | not implemented |

## 8. Per-agent exact remedy and boundary

### Agent 01 — Engineering Manager / Preflight

```yaml
input: run_id_only
tool_calls: 1
repository_write: false
network: false
result_as_answer: true
```

Remedy: implement the existing 20-check deterministic `RepositoryPreflightTool`; use typed output; require actual invocation ID; block on missing rules, manifest, approvals, path policy, or hash mismatch. The agent only explains the trusted result. It does not select agents or edit the run.

### Agent 02 — Product Requirements and Scope Lead

Tool operations:

```text
inspect_requirements_context
read_approved_requirements_sources
write_requirements_change_set
verify_requirements_commit
```

Allowed paths are requirements/acceptance records only. It may transform explicit owner input and verified context; it cannot invent market/customer requirements, edit code, approve scope, or silently resolve ambiguity. Final scope remains human-owned.

### Agent 03 — Evidence and Capability Researcher

One composite research tool may contain:

```text
search approved public indexes
fetch official allowlisted URLs
read approved Drive LearningPacket sources
read official GitHub source/issues
compare versions and claims
write research/source records on run branch
verify recorded links and hashes
```

Preferred free discovery component: self-hosted SearXNG. Discovery results are not authority. The trusted fetcher permits official domains, validates DNS/IP/redirects, enforces size/type/time limits, and records exact source URLs/dates/hashes. For private Drive content, use Groq; use Gemini only for public or fully redacted large packets.

### Agent 04 — Solution and Systems Architect

The architecture tool reads approved requirements and current architecture, then writes only architecture decision proposals. It cannot edit implementation, approve its own design, or use a tutorial without pinned-version reconciliation. Output must list components, contracts, failure modes, tradeoffs, security impact, migration, rollback, and mandatory tests.

### Agent 05 — UX, UI, and Accessibility Designer

One UX tool combines:

```text
read approved design sources
inspect local/staging DOM and accessibility tree
capture browser console and bounded screenshots through trusted infrastructure
write UX/accessibility specifications
verify spec commit
```

Use Playwright ARIA/accessibility evidence for local or staging targets. It cannot inspect production customer data, edit application code, or certify accessibility compliance. Automated results are findings, not legal compliance proof.

### Agent 06 — Frontend Application Engineer

One frontend workspace tool combines repository and sandbox operations behind one interface. It may edit only frontend/test/doc allowlists and run pre-approved commands in an ephemeral non-root sandbox. The sandbox has no secrets, no host Docker socket, network disabled by default, resource/time limits, and forced cleanup. Visual acceptance requires Agent 05 specifications and Agent 12 tests.

### Agent 07 — Backend and API Engineer

The backend tool allows bounded backend/API changes and sandbox tests. It cannot access production data or credentials. Authorization claims require negative tests, not prose. Database schema changes are handed to Agent 08 in a later Flow-selected stage.

### Agent 08 — Data and Database Engineer

The database tool edits schema/migration/test paths and executes only against a disposable database created for the run. It must test forward migration, rollback or compensating path, constraints, idempotency, concurrency, and data preservation using synthetic fixtures. Production migration execution is prohibited.

### Agent 09 — CrewAI and AI Systems Engineer

The CrewAI tool controls only CrewAI config, Flow, schemas, guardrails, hooks, provider adapters, and their tests. It must pin CrewAI/provider dependencies and prove:

```text
one agent + one tool
real invocation evidence
structured output
tool and model hooks
sequential order
blocked-stage stop
manual canonical checkpoint
no planning/reasoning/native-memory hidden calls
```

It cannot enable Agents 02–15 automatically.

### Agent 10 — Integration and MCP Engineer

The integration tool edits adapter/MCP paths and tests with mock/local servers and test credentials. No random public MCP server or arbitrary URL fetch is allowed. It must validate authentication, schema, timeout, cancellation, malformed response, prompt-injection metadata, SSRF, redirect, DNS-rebinding, retry, idempotency, and cleanup behavior.

### Agent 11 — Security, Privacy, and AI Safety Engineer

One read-only security composite may orchestrate approved local scanners such as:

```text
Bandit for Python AST security checks
pip-audit for Python dependency advisories
Semgrep approved rulesets
Gitleaks for secret scanning
Trivy for repository, image, dependency, license, and misconfiguration findings
```

Exact versions/rules must be pinned. The agent cannot exploit targets, mutate production, auto-fix findings, suppress evidence, or declare the system secure. It produces findings, severity rationale, evidence, false-positive disposition, and remediation proposals.

### Agent 12 — QA and Test Automation Engineer

The test tool may write only approved test paths and execute allowlisted tests in the sandbox. It returns command, exit code, duration, stdout/stderr hashes, coverage/artifact paths, and invocation IDs. It cannot change implementation to hide a failure, remove tests without approval, or convert flaky/failed results into a pass.

### Agent 13 — DevOps and CI/CD Engineer

The CI/build tool edits approved Docker, Compose, packaging, and workflow paths and runs local build/lint/scan commands. It may use BuildKit, Compose validation, Hadolint, actionlint, Trivy, and SBOM tools after separate version pinning. It cannot deploy, create secrets, enable paid infrastructure, modify repository environments, or merge.

### Agent 14 — SRE and Observability Engineer

The observability tool is read-only and accepts bounded, redacted OpenTelemetry traces, Prometheus metrics, health evidence, and structured logs. It cannot access unrestricted production logs, change infrastructure, silence alerts, or claim root cause from a single signal. Required output distinguishes observation, correlation, hypothesis, confidence, missing evidence, and safe recommendation.

### Agent 15 — Independent Release Auditor

The auditor tool reads the run manifest, diff, commits, source cards, LearningPackets, StudyReceipts, MemoryContext IDs, invocation ledger, tests, security findings, and documentation. It cannot edit code, merge, deploy, accept risk, or audit work it performed in an earlier role. It returns only:

```text
REVIEW_PASS_PENDING_OWNER
or BLOCKED_WITH_EXACT_MISSING_EVIDENCE
```

The trusted Flow—not the agent—creates or updates the draft PR after the required disposition.

## 9. Knowledge and memory remedy for every agent

### Google Drive knowledge

```text
Flow decides knowledge requirement
→ DriveKnowledgeGateway searches allowed roots by metadata + body terms
→ reads related files even when titles are wrong
→ exports/downloads and hashes actual content
→ reconciles with repository and official current facts
→ produces bounded LearningPacket
→ selected agent produces StudyReceipt
→ deterministic gate unlocks the role tool
```

Drive content is untrusted data and cannot add permissions, tools, models, agents, or deployment authority.

### Supabase/Postgres memory

```text
Flow exact-filter/keyword query
→ verify source commit/evidence hashes
→ remove stale/conflicting entries
→ bounded MemoryContext
→ selected agent task
→ validated output + tool/test evidence + audit
→ transactional memory write
→ optional Notion human-readable mirror
```

No direct agent database/Notion credentials. GitHub/current evidence outranks memory. Embeddings remain disabled until a pinned privacy-safe embedding profile is approved.

## 10. Docker and sandbox remedy

Core application services may run in Docker Compose:

```text
galax-api
flow-runner
repository-gateway
drive-knowledge-gateway
memory-gateway
optional notion-mirror
research-gateway
```

Baseline:

```yaml
user: non_root
read_only: true
cap_drop: [ALL]
no_new_privileges: true
resource_limits: required
service_specific_secrets: required
healthchecks: required
```

Coding/test execution uses a separate rootless sandbox daemon or separate host behind an authenticated controller. Prohibited: privileged DIND, unrestricted Docker socket, host filesystem, production SSH keys, shared secrets, and default outbound network.

## 11. Minimum test suites

### Common agent profile — 20 tests each

```text
AGENT-001 correct role/task loaded
AGENT-002 only one LLM profile active
AGENT-003 only one tool interface exposed
AGENT-004 system instructions followed
AGENT-005 prohibited action refused
AGENT-006 correct tool selected
AGENT-007 arguments match schema
AGENT-008 real invocation ID exists
AGENT-009 tool result reaches model
AGENT-010 fabricated observation rejected
AGENT-011 structured output validates
AGENT-012 deterministic guardrail pass/fail
AGENT-013 prompt injection rejected
AGENT-014 secrets and prohibited data removed
AGENT-015 token/output limit enforced
AGENT-016 timeout behavior
AGENT-017 rate/allocation behavior
AGENT-018 blocked stage stops downstream work
AGENT-019 sequential context accepted
AGENT-020 self-diagnostic matches trusted evidence
```

### Governance integration

```text
GOV-001 PRE_MODEL_CALL profile and data gate
GOV-002 PRE_TOOL_CALL identity and permission gate
GOV-003 hook block produces Flow stop
GOV-004 hook internal error fails closed through wrapper
GOV-005 POST hooks cannot fabricate pass
GOV-006 invocation ledger is append-only/idempotent
GOV-007 missing invocation evidence blocks completion
GOV-008 manual canonical checkpoint failure stops run
GOV-009 no native planning/reasoning/memory hidden call
GOV-010 no parallel LLM/tool/agent execution
```

### MCP and repository

```text
MCP-001 exact server/image/commit pin
MCP-002 exact tool allowlist
MCP-003 malicious metadata test
MCP-004 URL/private-IP/metadata SSRF rejection
MCP-005 DNS-rebinding and redirect test
MCP-006 malformed response test
MCP-007 timeout and cancellation
MCP-008 no write retry
MCP-009 cleanup/lifecycle
MCP-010 secrets absent from server arguments/logs

REPO-001 authorized read
REPO-002 dedicated branch creation
REPO-003 expected-head verification
REPO-004 allowed multi-file commit
REPO-005 stale head rejection
REPO-006 direct-main rejection
REPO-007 force-push rejection
REPO-008 secret/protected path rejection
REPO-009 role path isolation
REPO-010 draft PR only after QA/audit
```

## 12. Correct implementation order

```text
PHASE 0 reconcile stale records and block old master prompt
PHASE 1 pin CrewAI 1.15.4 and minimum dependencies
PHASE 2 build typed schemas, status contracts, invocation ledger, and manual checkpoint
PHASE 3 implement PRE/POST model and tool governance hooks
PHASE 4 implement RepositoryPreflightTool and Agent 01 only
PHASE 5 implement trusted repository gateway and branch-write negative tests
PHASE 6 validate Groq 20B and 120B separately through CrewAI
PHASE 7 validate Cloudflare 20B and 120B fallback profiles
PHASE 8 run a two-agent read-only sequential smoke test
PHASE 9 implement Drive knowledge gateway and StudyReceipt gate
PHASE 10 implement Supabase keyword/exact-filter memory and Notion mirror isolation
PHASE 11 implement external sandbox boundary
PHASE 12 implement Agent 03 research gateway and automatic revalidation stage
PHASE 13 research, implement, and approve Agents 02–15 one at a time
PHASE 14 full QA/security/audit and owner review
```

No later phase may be described as complete when an earlier required phase is blocked.

## 13. Final decision

```yaml
CrewAI_1_15_4_bounded_15_agent_design: TECHNICALLY_COMPATIBLE_BY_CUSTOM_IMPLEMENTATION
CrewAI_alone_provides_complete_Galax: false
all_agents_can_be_enabled_now: false
full_master_prompt_authorized: false
role_roster_changed: false
one_agent_one_tool_preserved: true
strict_sequential_preserved: true
planning_feature: disabled
reasoning_feature: disabled
provider_native_reasoning_effort: selected_for_validation
MCP_full_exposure: rejected
role_scoped_gateways: required
next_implementation_target: Agent_01_plus_governance_foundation
```
