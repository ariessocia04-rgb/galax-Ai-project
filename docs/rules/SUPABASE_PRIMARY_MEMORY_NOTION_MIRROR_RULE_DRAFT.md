# Supabase Primary Memory + Notion Mirror Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Priority:** This rule supersedes `NOTION_MEMORY_RULE_DRAFT.md` wherever that file treats Notion as the primary runtime memory. The older file remains applicable to the optional Notion mirror behavior until consolidated.  
**CrewAI native memory:** disabled.

## 1. Core rule

```text
Supabase Postgres/pgvector is the candidate primary machine memory.
Notion is the candidate curated human-readable mirror.
GitHub remains the highest project source of truth.
CrewAI agents never directly own memory credentials or memory writes.
```

## 2. Capability ownership

```yaml
GalaxFlow:
  owns:
    - decide_if_memory_is_required
    - build_exact_filter_query
    - request_keyword_or_hybrid_retrieval
    - enforce_memory_token_budget
    - compare_memory_with_GitHub_and_current_evidence
    - decide_write_eligibility
    - queue_optional_Notion_mirror

GalaxMemoryGateway:
  owns:
    - Supabase_or_Postgres_authentication
    - exact_filter_queries
    - parameterized_keyword_queries
    - pgvector_or_hybrid_queries_after_embedding_approval
    - RLS_or_dedicated_role_enforcement
    - duplicate_and_supersession_transactions
    - backup_and_restore_operations

GalaxNotionMirrorGateway:
  owns:
    - create_human_readable_approved_memory
    - targeted_update
    - save_Notion_page_ID
    - retry_and_rate_limit_behavior

CrewAI_agent:
  receives:
    - bounded_MemoryContext
  may_not:
    - hold_database_credentials
    - directly_query_or_write_Supabase
    - directly_write_Notion
    - mark_its_own_output_as_durable_memory
    - treat_memory_as_higher_than_GitHub_or_current_evidence
```

## 3. CrewAI configuration

```python
crew = Crew(
    agents=selected_agents,
    tasks=selected_tasks,
    process=Process.sequential,
    memory=False,
)
```

The Flow retrieves memory before constructing or starting the affected task and inserts a validated `MemoryContext` into task inputs/context. CrewAI's built-in memory system is not used for this design.

## 4. MemoryContext schema

```python
class MemoryEntry(BaseModel):
    memory_id: UUID
    memory_type: str
    summary: str
    required_future_behavior: str | None
    source_commit: str | None
    evidence_hash: str
    confidence: Literal["HIGH", "MEDIUM", "LOW"]
    updated_at: datetime


class MemoryContext(BaseModel):
    retrieval_id: UUID
    project_id: str
    agent_id: str
    task_id: str
    entries: list[MemoryEntry]
    conflicts: list[str]
    omitted_entries: int
    token_estimate: int
```

## 5. Retrieval sequence

```text
Flow receives task
→ query active exact-filter memory candidates
→ query keyword candidates
→ run semantic/hybrid retrieval only when embedding system is approved
→ verify each evidence hash/source commit
→ remove stale or conflicting records
→ rank by relevance, priority, confidence, and recency
→ trim to maximum 10 records / 4,000 tokens
→ inject MemoryContext
```

## 6. Memory priority

```text
active GitHub rules/code
> current official documentation
> current live tests and tool evidence
> approved architecture decisions
> verified Supabase memory
> Notion mirror
> historical or unverified notes
```

## 7. Write gate

```text
agent result
→ deterministic schema validation
→ actual tool and test evidence
→ QA/security result when required
→ Release Auditor reconciliation
→ owner or approved policy disposition
→ transactional Supabase memory write
→ optional Notion mirror
```

Agent prose alone never becomes durable memory.

## 8. Memory types

```text
DECISION
LESSON
MISTAKE
BLOCKER
AGENT_VALIDATION
LLM_VALIDATION
TOOL_VALIDATION
RUN_SUMMARY
SOURCE_WARNING
RECOVERY_CHECKPOINT
REGRESSION
INCIDENT
```

## 9. Duplicate and supersession rule

Use a unique constraint on:

```text
Project_ID + Memory_Type + Evidence_Hash
```

Exact duplicate:

```text
return existing memory ID; do not insert
```

Supersession:

```text
insert verified replacement
→ set old Active=false and Status=SUPERSEDED
→ link both records in one transaction
```

## 10. Embedding rule

No embedding provider is approved yet.

Until approved:

```text
use exact filters + Postgres full-text/keyword retrieval
```

After approval:

```text
use pinned embedding model and dimension
→ pgvector index
→ benchmark threshold and recall
→ add hybrid retrieval
```

The gateway must not silently default to OpenAI embeddings or any paid provider.

## 11. RLS and credentials

```text
- Keep the memory gateway server-side only.
- Enable RLS on exposed tables.
- Prefer a dedicated backend database role or narrowly scoped secret key.
- Never put secret/service keys in browsers, agent prompts, tool arguments, or logs.
- Never give an agent direct database access.
- Validate every SQL/RPC argument.
```

## 12. Managed-free limits

For a hosted Supabase free pilot:

```yaml
database_size: 500_MB
project_pause_after_inactivity: 1_week
automatic_backups: false
active_free_projects: 2
```

Required behavior:

```text
paused/unavailable project → BLOCKED_MEMORY_UNAVAILABLE
read-only quota state → BLOCKED_MEMORY_READ_ONLY
backup missing → BLOCKED_MEMORY_BACKUP_REQUIRED before production approval
```

## 13. Docker modes

```yaml
managed_supabase:
  Galax_services_containerized: true
  database_external: true

minimal_local:
  postgres_pgvector_container: true
  full_supabase_stack: false

full_self_hosted_supabase:
  official_supabase_compose_release: required
  separate_profile_or_stack: required
  operator_owns_security_updates_backups_monitoring: true
```

## 14. Notion mirror rule

Only approved, concise records are mirrored. The Notion page must include the canonical Supabase `Memory_ID`, evidence hash, source commit, status, and last verification date.

If Notion is unavailable:

```text
primary Supabase write remains valid
→ mark mirror status PENDING or SKIPPED
→ do not retry more than once in the active run
```

Notion cannot change the primary memory record through an unattended reverse-sync until webhook, conflict, identity, and authorization tests are approved.

## 15. Revalidation triggers

```text
Supabase API/client version
Postgres version
pgvector version
schema or migration
RLS policy
secret/role permission
embedding model or dimension
retrieval threshold or ranking
Notion API version
Notion mirror schema
memory token budget
CrewAI task context schema
```

Any change sets affected memory capabilities to `REVALIDATION_REQUIRED`.

## 16. Current status

```yaml
Supabase_primary_memory: SELECTED_FOR_VALIDATION
Notion_primary_memory: SUPERSEDED_BY_THIS_DRAFT
Notion_curated_mirror: SELECTED_FOR_VALIDATION
CrewAI_native_memory: DISABLED
embedding_provider: NOT_SELECTED
GalaxMemoryGateway: NOT_IMPLEMENTED
GalaxNotionMirrorGateway: NOT_IMPLEMENTED
production_ready: false
```
