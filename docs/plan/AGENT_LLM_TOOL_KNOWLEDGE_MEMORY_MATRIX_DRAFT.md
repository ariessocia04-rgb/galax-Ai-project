# 15-Agent LLM, Tool, Knowledge, and Memory Matrix — Draft

**Status:** `DRAFT_MUTABLE`  
**Framework candidate:** CrewAI 1.15.4  
**Process:** `Process.sequential`  
**Agents enabled:** `0`

## 1. Global architecture

```yaml
private_repository_primary_candidate: groq/openai/gpt-oss-120b
private_hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
public_redacted_long_context_candidate: gemini/gemini-2.5-flash
optional_local_fallback_candidate: ollama/gpt-oss:20b
rejected_trial_only_candidate: cerebras/gpt-oss-120b

allow_delegation: false
allow_code_execution: false
async_execution: false
native_CrewAI_memory: false
parallel_tool_calls: false
maximum_active_agents: 1
maximum_active_LLM_calls: 1
```

Every provider profile remains disabled until it passes its own agent-specific prompt, tool, structured-output, privacy, rate/allocation, failure, and sequential-context tests.

## 2. Shared context order

```text
1. Immutable repository rules.
2. Current run manifest and exact task contract.
3. Verified bounded Supabase MemoryContext.
4. Verified Google Drive LearningPacket when required.
5. Relevant repository excerpts.
6. One role-specific tool schema.
7. Prior approved structured sequential output.
```

Notion is an optional curated human-readable mirror. It is not the primary machine-memory context.

## 3. Provider selection boundary

### Private or confidential task context

```yaml
primary: groq/openai/gpt-oss-120b
hosted_fallback: cloudflare/@cf/openai/gpt-oss-120b
local_fallback: ollama/gpt-oss:20b
```

### Public or fully redacted long-context material

```yaml
candidate: gemini/gemini-2.5-flash
```

The free Gemini profile cannot receive confidential repository code, secrets, customer data, or private owner documents because free-tier data may be used to improve Google products.

Only one LLM profile is attached to an agent for one task. Alternate profiles are selected by deterministic Flow only from a safe checkpoint.

## 4. Agent matrix

| ID | Agent | Default data class | LLM profile candidate | One tool interface | Drive learning | Supabase memory types | Current status |
|---:|---|---|---|---|---|---|---|
| 01 | Engineering Manager / Preflight | Private scoped metadata | Groq primary; Cloudflare fallback | `RepositoryPreflightTool` | Governance/tutorial references when required | `GLOBAL_BLOCKER`, `AGENT_VALIDATION`, `TOOL_VALIDATION`, `LLM_VALIDATION` | Disabled |
| 02 | Product Requirements and Scope Lead | Private owner requirements | Groq primary; Cloudflare fallback | `RequirementsWorkspaceTool` | Business-process, workflow, terminology files | `DECISION`, `LESSON`, `SCOPE_CONFLICT`, `RUN_SUMMARY` | Disabled |
| 03 | Evidence and Capability Researcher | Public/redacted or private scoped | Gemini for public/redacted large packets; Groq for private scoped work | `VerifiedResearchWorkspaceTool` | Primary Drive reconciliation and related-file discovery | `SOURCE_WARNING`, `LESSON`, `PRIOR_RESEARCH_GAP` | Disabled |
| 04 | Solution and Systems Architect | Private scoped architecture | Groq primary; Cloudflare fallback | `ArchitectureWorkspaceTool` | Architecture patterns, protocols, failure modes | `DECISION`, `LESSON`, `MISTAKE`, `ARCHITECTURE_RISK` | Disabled |
| 05 | UX, UI, and Accessibility Designer | Private scoped design | Groq primary; Cloudflare fallback | `UXWorkspaceTool` | UI, interaction, accessibility learning files | `DECISION`, `UX_LESSON`, `ACCESSIBILITY_DEFECT` | Disabled |
| 06 | Frontend Application Engineer | Private scoped code | Groq primary; Cloudflare/Ollama validated fallback | `FrontendWorkspaceTool` | Framework tutorials, components, owner UI references | `FRONTEND_LESSON`, `REGRESSION`, `BUILD_FAILURE` | Disabled |
| 07 | Backend and API Engineer | Private scoped code | Groq primary; Cloudflare/Ollama validated fallback | `BackendWorkspaceTool` | API, domain, authentication, failure references | `BACKEND_LESSON`, `API_CONTRACT_FAILURE`, `SECURITY_WARNING` | Disabled |
| 08 | Data and Database Engineer | Private schema/disposable data | Groq primary; Cloudflare/Ollama validated fallback | `DatabaseWorkspaceTool` | Schema, migration, rollback, concurrency material | `DATABASE_LESSON`, `MIGRATION_FAILURE`, `DATA_RISK` | Disabled |
| 09 | CrewAI and AI Systems Engineer | Private CrewAI/config source | Groq primary; Cloudflare/Ollama validated fallback | `CrewAIWorkspaceTool` | CrewAI, LLM, MCP, prompt-pattern references | `AGENT_VALIDATION`, `LLM_VALIDATION`, `TOOL_VALIDATION`, `CREWAI_FAILURE` | Disabled |
| 10 | Integration and MCP Engineer | Private adapters + public protocol docs | Groq primary; Gemini public-doc research only | `IntegrationMCPWorkspaceTool` | API/MCP/authentication references | `INTEGRATION_LESSON`, `AUTH_FAILURE`, `MCP_VALIDATION` | Disabled |
| 11 | Security, Privacy, and AI Safety Engineer | Sensitive scoped evidence | Groq primary; local Ollama only after quality tests | `SecurityAuditTool` | Owner security policies, threat-model references | `SECURITY_WARNING`, `THREAT`, `MITIGATION`, `PRIOR_FINDING` | Disabled |
| 12 | QA and Test Automation Engineer | Private tests/results | Groq primary; Cloudflare/Ollama validated fallback | `TestRunnerTool` | Test patterns and acceptance examples | `REGRESSION`, `FLAKY_TEST`, `QA_LESSON` | Disabled |
| 13 | DevOps and CI/CD Engineer | Private CI/build configuration | Groq primary; Cloudflare/Ollama validated fallback | `CIBuildWorkspaceTool` | CI, packaging, deployment procedures | `BUILD_FAILURE`, `RELEASE_LESSON`, `ROLLBACK_LESSON` | Disabled |
| 14 | SRE and Observability Engineer | Redacted telemetry | Groq primary; Gemini only for fully redacted large telemetry summaries | `ObservabilityReadTool` | SLO, incident, monitoring, recovery references | `INCIDENT`, `RECOVERY_CHECKPOINT`, `SRE_LESSON` | Disabled |
| 15 | Independent Release Auditor | Private bounded evidence | Groq primary; Cloudflare/Ollama validated fallback | `ReleaseAuditTool` | Release criteria, audit standards | `PRIOR_RELEASE_RISK`, `UNRESOLVED_BLOCKER`, `AGENT_VALIDATION`, `TOOL_VALIDATION`, `LLM_VALIDATION` | Disabled |

## 5. Per-agent restrictions

### Agent 01

```text
No dynamic agent selection, task reordering, delegation, repository writing, or self-approval.
```

### Agent 02

```text
No invented requirements, unilateral scope approval, or application-code edits.
```

### Agent 03

```text
No model-memory-as-fact, aggregator-only approval, provider installation, or implementation approval.
```

### Agent 04

```text
No implementation edits, unilateral architecture approval, or tutorial compatibility assumptions.
```

### Agent 05

```text
No production UI edits, production user data, or unsupported accessibility certification.
```

### Agents 06–08, 09, 12, and 13

```text
No deprecated CrewAI built-in code execution. All commands run through the separately tested external sandbox in the assigned workspace tool.
```

### Agent 10

```text
No random public MCP servers, unrestricted URL fetch, production credentials, or untested authentication/retry behavior.
```

### Agent 11

```text
No unauthorized exploitation, production mutation, automatic remediation, or claim that the system is secure.
```

### Agent 14

```text
Read-only approved telemetry, with redaction. No production changes or unsupported root-cause claims.
```

### Agent 15

```text
No code edits, self-review of its own prior work, merge, deployment, or ignoring missing evidence.
```

## 6. Drive learning gate

When the run manifest requires owner learning material:

```text
Drive search by metadata + body text + related terms
→ fetch relevant candidates
→ inspect actual sections
→ version/conflict check
→ LearningPacket
→ selected agent StudyReceipt
→ deterministic validation
→ tool access enabled for the task
```

File title alone is not sufficient evidence of relevance.

## 7. Memory gate

```text
Supabase exact filters/keyword retrieval
→ bounded verified MemoryContext
→ repository conflict check
→ agent receives selected entries only
```

No agent receives Supabase credentials or directly writes durable memory. Validated results pass QA/audit before trusted Flow writes memory.

## 8. Common live-test gate

Every agent requires:

```text
ROLE FACT CHECKED
→ CREWAI FEATURE SUPPORTED
→ ACTIVE LLM PROFILE TESTED FOR THE AGENT AND DATA CLASS
→ REQUIRED FALLBACK PROFILE TESTED
→ SINGLE TOOL IMPLEMENTED AND TESTED
→ DRIVE LEARNING TESTED WHEN APPLICABLE
→ SUPABASE MEMORY CONTEXT TESTED
→ STRUCTURED OUTPUT AND SELF-DIAGNOSTIC TESTED
→ SECURITY/PERMISSION TESTS PASSED
→ PROCESS.SEQUENTIAL HANDOFF TESTED
→ STATUS = APPROVED_FOR_IMPLEMENTATION
```

No agent in this matrix is enabled.
