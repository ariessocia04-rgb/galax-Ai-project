# Google Drive Knowledge + Notion Memory Architecture — Draft

**Status:** `DRAFT_MUTABLE`  
**Process:** `Process.sequential`  
**Agent tool policy:** one role-specific tool interface per agent  
**Knowledge source:** approved Google Drive folders  
**Project memory:** dedicated Notion data source/pages

## 1. Architecture decision

```text
Google Drive stores owner-provided learning material.
Notion stores validated project memory.
GitHub remains the implementation source of truth.
CrewAI coordinates bounded agent tasks.
The deterministic Flow controls retrieval, permissions, order, and writes.
```

The three stores have different purposes:

| Store | Purpose | Authority |
|---|---|---|
| GitHub | Current rules, code, schemas, tests, plans, source records | Highest project authority |
| Google Drive | Tutorials, copied website material, reference files, owner learning resources | Supporting knowledge |
| Notion | Validated lessons, decisions, mistakes, summaries, checkpoints, agent/tool/LLM evidence | Historical and operational memory |

## 2. One-prompt execution

```text
OWNER PROMPT
→ deterministic task classification
→ repository preflight
→ query verified Notion memory
→ determine whether owner knowledge is required
→ search approved Google Drive root
→ retrieve and validate relevant files
→ build LearningPacket
→ select only required approved agents
→ selected agent reads rules + memory + LearningPacket
→ agent produces StudyReceipt
→ deterministic guardrail validates StudyReceipt
→ agent uses its one role-specific tool
→ tests and evidence
→ sequential next stage
→ audit
→ Flow writes approved memory to Notion
→ draft PR/result
```

One owner prompt launches the process. It does not mean one LLM request or all agents at once.

## 3. System components

### 3.1 `DriveKnowledgeGateway`

A trusted, read-only application component using Google Drive API v3.

Operations:

```yaml
operations:
  - search_metadata_and_full_text
  - list_related_folder_files
  - get_file_metadata
  - export_google_workspace_document
  - download_supported_blob
  - parse_supported_file
  - hash_content
  - build_learning_packet_evidence
```

No agent directly receives Drive OAuth credentials.

### 3.2 `GalaxNotionMemoryGateway`

A trusted application component using the official Notion API.

Operations:

```yaml
operations:
  - query_memory_data_source
  - retrieve_memory_markdown
  - create_validated_memory
  - update_memory_status
  - supersede_memory
  - verify_memory_hash
```

No agent directly writes to Notion.

### 3.3 `GalaxRepositoryGateway`

Role-scoped GitHub read/write interface already planned for implementation agents.

### 3.4 `GalaxFlow`

Owns deterministic sequencing, budgets, selection, learning/memory injection, checkpoints, and approval gates.

## 4. Knowledge retrieval algorithm

### Stage K0 — Decide whether knowledge is required

Knowledge retrieval is required when:

```text
- owner explicitly says a Drive file/tutorial must be followed
- task manifest lists required learning topics
- agent decision record names required Drive sources
- implementation uses a technology or process governed by owner learning material
```

If not required, the Flow does not query Drive.

### Stage K1 — Build a task knowledge query

Inputs:

```yaml
run_id:
task_id:
agent_id:
objective:
repository_components: []
frameworks: []
feature_terms: []
error_terms: []
expected_outputs: []
known_synonyms: []
allowed_drive_root_id:
```

### Stage K2 — Search without trusting the title

The gateway performs multiple bounded queries using:

```text
name contains
fullText contains
exact phrase fullText contains
folder parent
mime type
modified time
labels
appProperties
```

The Drive API `fullText` query is lexical, not guaranteed semantic retrieval. The gateway expands queries with approved synonyms and component terms. Optional Notion AI connected-source semantic search may be tested separately but cannot be required.

### Stage K3 — Rank candidate files

Proposed deterministic score:

```yaml
content_term_matches: 35
exact_phrase_matches: 20
approved_folder_match: 15
Drive_label_or_app_property_match: 10
technology_version_match: 10
recently_modified_when_relevant: 5
filename_match: 5
```

Filename is intentionally only 5% of the score.

Negative adjustments:

```yaml
outdated_version: -30
conflicts_with_active_repository_rule: -50
outside_allowed_folder: reject
trashed: reject
cannot_download: reject
unsupported_mime_type: reject_or_block
```

### Stage K4 — Retrieve content

Google Docs, Sheets, and Slides use supported export formats. Blob files use download content endpoints. Exported Google Workspace content is subject to the provider's documented export limit.

### Stage K5 — Parse and inspect

The local parser:

```text
extracts text
→ identifies headings and sections
→ detects version/date statements
→ detects code blocks and commands
→ detects prompt-injection patterns
→ chunks content
→ hashes complete normalized content
```

### Stage K6 — Reconcile with current facts

Learning material is checked against:

```text
active repository rules
current official documentation
pinned dependency versions
security policy
current implementation
```

Outdated content is marked, not silently applied.

### Stage K7 — Produce LearningPacket

Only relevant excerpts and source evidence are passed to the selected agent.

## 5. Agent study gate

Every selected implementation or review agent that receives a LearningPacket must pass:

```text
STUDY PACKET
→ identify applicable sections
→ identify obsolete/conflicting instructions
→ produce implementation and validation plan
→ emit StudyReceipt
→ deterministic validation
```

The assigned write/test tool remains unavailable until `ready_to_implement: true` and the receipt passes.

## 6. Notion memory lifecycle

### Stage M0 — Retrieve memory

Before an agent task, the Flow queries only the dedicated Galax Memory data source.

```text
Project_ID = galax
Active = true
Status = VERIFIED
Agent_ID = selected agent or GLOBAL
Scope overlaps current task
```

### Stage M1 — Apply priority

Memory that conflicts with GitHub or current official evidence is omitted and flagged stale.

### Stage M2 — Inject bounded context

The Flow passes concise entries only, with source commit and evidence hash.

### Stage M3 — Candidate memory generation

After task completion, the Flow builds a candidate memory record from structured evidence. Agent prose alone cannot create durable memory.

### Stage M4 — Validation and audit

```text
candidate memory
→ schema validation
→ source evidence verification
→ duplicate check
→ auditor disposition
→ owner/policy approval
```

### Stage M5 — Notion write

The gateway creates or updates memory using the dedicated connection and API version.

## 7. Per-agent knowledge and memory behavior

| Agent | Drive knowledge requirement | Memory read | Memory write |
|---|---|---|---|
| 01 Engineering Manager | Preflight policies only when manifest requires | Global blockers and agent validation | No direct write |
| 02 Product Requirements | Owner product tutorials and workflow references | Decisions, scope lessons, prior ambiguities | No direct write |
| 03 Evidence Researcher | Primary Drive discovery/reconciliation role | Source warnings and past research gaps | No direct write |
| 04 Architect | Architecture tutorials and approved patterns | Decisions, failures, tradeoffs | No direct write |
| 05 UX/Accessibility | UX patterns, copied tutorials, accessibility references | UX decisions and validated defects | No direct write |
| 06 Frontend | Framework/UI implementation tutorials | Frontend lessons and recurring failures | No direct write |
| 07 Backend/API | API/security/domain tutorials | Backend lessons and contract failures | No direct write |
| 08 Database | Schema/migration tutorials | Migration lessons and data risks | No direct write |
| 09 CrewAI Engineer | CrewAI/MCP/LLM setup tutorials | Agent/tool/LLM validation history | No direct write |
| 10 Integration/MCP | Integration setup and protocol files | Authentication and schema lessons | No direct write |
| 11 Security/Privacy | Security standards and owner policies | Confirmed threats and mitigations | No direct write |
| 12 QA/Test | Testing tutorials and acceptance references | Regression history and flaky-test lessons | No direct write |
| 13 DevOps | CI/build/deployment tutorials | Build failures and rollback lessons | No direct write |
| 14 SRE/Observability | Reliability and monitoring references | Incident and recovery lessons | No direct write |
| 15 Release Auditor | Audit criteria and release references | Prior release risks and unresolved blockers | No direct write |

All durable Notion writes are performed by the Flow after validation and audit.

## 8. Tool policy impact

Agents keep their one assigned tool. Drive and Notion are shared infrastructure layers, not extra exposed tools.

```yaml
agent_tool_count: 1
Drive_access_from_agent: false
Notion_write_from_agent: false
knowledge_context_from_flow: true
memory_context_from_flow: true
```

## 9. Security boundaries

```text
- Read-only Google Drive scope initially.
- Search only configured Drive roots.
- Dedicated Notion memory pages/data source only.
- No full-workspace Notion MCP for unattended agent writes.
- No raw chain-of-thought in Notion.
- No secrets in Drive-derived prompt context.
- Copied web content is untrusted.
- File names and page titles are not trusted as classifications.
- Every retrieved item carries stable IDs, timestamps, and hashes.
```

## 10. Token controls

```yaml
Drive_candidate_metadata_limit: 25
Drive_full_content_candidates_limit: 5
LearningPacket_excerpt_limit_per_file: 5
LearningPacket_total_token_soft_limit: 12000
Notion_memory_entries_limit: 10
Notion_memory_token_soft_limit: 4000
```

If required knowledge cannot fit safely:

```text
split into sequential study segments
→ checkpoint
→ continue with next packet
```

Never silently summarize away exact commands, warnings, or validation steps.

## 11. Current status

```yaml
Google_Drive_API_path: FACT_CHECKED_SUPPORTED
Drive_title_independent_lexical_search: FACT_CHECKED_SUPPORTED
Drive_semantic_search: NOT_GUARANTEED_BY_DRIVE_API
Notion_external_memory: FACT_CHECKED_TECHNICALLY_SUPPORTED
Notion_native_CrewAI_memory: NOT_PROVEN
Notion_current_workspace_search: VERIFIED_CONNECTED
Drive_gateway: NOT_IMPLEMENTED
Notion_memory_gateway: NOT_IMPLEMENTED
LearningPacket: SPECIFIED_NOT_TESTED
StudyReceipt: SPECIFIED_NOT_TESTED
all_agents_enabled: false
production_ready: false
```
