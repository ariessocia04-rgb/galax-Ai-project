# Notion vs Supabase for Galax Memory — 2026-07-20

**Status:** `RESEARCH_RECORD`  
**Corrected decision:** Supabase Postgres with stable `pgvector` is selected for validation as the primary machine/runtime memory. Notion is retained as an optional curated human-readable mirror. Neither is claimed as a native CrewAI memory backend.

## 1. Decision summary

```yaml
primary_runtime_memory:
  platform: Supabase_Postgres_or_self_hosted_Postgres
  vector_extension: pgvector
  access: GalaxMemoryGateway_managed_by_Flow
  status: SELECTED_FOR_VALIDATION_NOT_LIVE_TESTED

human_readable_memory_mirror:
  platform: Notion
  access: GalaxNotionMirrorGateway_managed_by_Flow
  status: OPTIONAL_SELECTED_FOR_VALIDATION

crewai_native_memory:
  enabled: false
  reason: no_verified_native_Notion_or_Supabase_backend_for_current_design
```

## 2. Ten factual signs that the Supabase memory path is technically workable

These facts prove that the required storage and retrieval primitives exist. They do not replace the required CrewAI integration tests.

### Fact 1 — Supabase provides a Postgres database

A stable relational database can store structured memory records, source hashes, status, supersession relationships, agent scope, run IDs, and audit metadata.

Source:

- [Supabase database overview](https://supabase.com/docs/guides/database/overview)

### Fact 2 — Supabase supports `pgvector`

Supabase documents the Postgres `vector` extension for storing embeddings and vector similarity search, including retrieval-augmented generation use cases.

Sources:

- [pgvector extension](https://supabase.com/docs/guides/database/extensions/pgvector)
- [Vector columns](https://supabase.com/docs/guides/ai/vector-columns)

### Fact 3 — Supabase supports semantic search

Supabase documents semantic retrieval using embeddings and Postgres functions. This permits retrieval of related lessons even when exact words differ.

Source:

- [Semantic search](https://supabase.com/docs/guides/ai/semantic-search)

### Fact 4 — Supabase supports hybrid search

Hybrid search combines full-text keyword search with semantic search, which is useful for exact identifiers plus concept matching.

Source:

- [Hybrid search](https://supabase.com/docs/guides/ai/hybrid-search)

### Fact 5 — Python clients exist

Supabase provides Python-access paths, including `vecs` for pgvector collections and normal Postgres/Python tooling. This is compatible with a Python CrewAI Flow application at the application layer.

Sources:

- [Supabase Python vector client](https://supabase.com/docs/guides/ai/vecs-python-client)
- [Choosing a Python client](https://supabase.com/docs/guides/ai/python-clients)

### Fact 6 — Structured metadata filters are supported

Postgres columns and vector metadata can represent `Project_ID`, `Agent_ID`, `Memory_Type`, `Status`, `Active`, `Scope`, `Source_Commit`, `Evidence_Hash`, and expiry fields. Queries can combine exact filters with vector retrieval.

Sources:

- [Supabase vector columns](https://supabase.com/docs/guides/ai/vector-columns)
- [Vecs Python client](https://supabase.com/docs/guides/ai/vecs-python-client)

### Fact 7 — Row Level Security is supported

Supabase requires RLS on exposed-schema tables and documents policy-based row authorization. Galax can restrict memory by project, actor, gateway role, and operation.

Source:

- [Supabase Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)

### Fact 8 — Backend-only secret access is supported

Supabase documents that secret/service-role keys bypass RLS and must never be exposed to browsers or customers. Galax can keep the gateway credential in a backend-only Docker secret and never send it to an agent prompt.

Sources:

- [Securing Supabase data](https://supabase.com/docs/guides/database/secure-data)
- [Migrating to secret API keys](https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys)

### Fact 9 — Supabase can be self-hosted with Docker Compose

Supabase publishes an official Compose stack and documents tested releases. A smaller Galax deployment may instead run only Postgres with pgvector when the full Supabase product stack is unnecessary.

Sources:

- [Self-hosting with Docker](https://supabase.com/docs/guides/self-hosting/docker)
- [Self-hosting responsibilities](https://supabase.com/docs/guides/self-hosting)

### Fact 10 — Database changes can emit asynchronous webhooks

Supabase Database Webhooks fire after INSERT, UPDATE, and DELETE and use asynchronous `pg_net`. Galax may use this for cache invalidation after exact security tests.

Sources:

- [Database Webhooks](https://supabase.com/docs/guides/database/webhooks)
- [pg_net async networking](https://supabase.com/docs/guides/database/extensions/pg_net)

### Fact 11 — Vector indexes are supported

Supabase documents HNSW and IVFFlat indexing for pgvector, with HNSW generally recommended for performance and robustness. Index design must be benchmarked using Galax memory volume and embedding dimensions.

Source:

- [Vector indexes](https://supabase.com/docs/guides/ai/vector-indexes)

### Fact 12 — Backup behavior is explicitly documented

Hosted free projects do not include automatic backups; Supabase recommends regular CLI database dumps and off-site backups. Pro and higher plans receive daily backups. Self-hosted operators own backup and restore.

Sources:

- [Supabase database backups](https://supabase.com/docs/guides/platform/backups)
- [Supabase self-hosting responsibilities](https://supabase.com/docs/guides/self-hosting)

## 3. Current managed-free Supabase limits relevant to memory

```yaml
free_plan:
  database_size: 500_MB
  compute: shared_CPU_up_to_500_MB_RAM
  active_projects: 2
  pause_after_inactivity: 1_week
  automatic_backups: false
```

The database enters read-only mode when database size exceeds 500 MB. These limits can change and must be re-read before implementation.

Sources:

- [Supabase pricing](https://supabase.com/pricing)
- [Understanding database size](https://supabase.com/docs/guides/platform/database-size)
- [Supabase backups](https://supabase.com/docs/guides/platform/backups)

## 4. Ten factual signs for Notion as an external curated mirror

### Fact N1 — Notion provides an official hosted MCP server

Source: [Notion MCP overview](https://developers.notion.com/guides/mcp/overview)

### Fact N2 — Notion MCP supports OAuth-based workspace access

Source: [Connect to Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp)

### Fact N3 — Notion MCP exposes search, fetch, create, and update tools

Source: [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

### Fact N4 — Notion pages can be retrieved as enhanced Markdown

Source: [Retrieve page Markdown](https://developers.notion.com/reference/retrieve-page-markdown)

### Fact N5 — Notion supports targeted Markdown updates

Source: [Working with Markdown content](https://developers.notion.com/guides/data-apis/working-with-markdown-content)

### Fact N6 — Notion data sources support structured queries

Source: [Query a data source](https://developers.notion.com/reference/query-a-data-source)

### Fact N7 — Notion access is constrained by connection capabilities and shared pages

Source: [Notion authorization](https://developers.notion.com/docs/authorization)

### Fact N8 — Notion documents request limits and HTTP 429 handling

Source: [Notion request limits](https://developers.notion.com/reference/request-limits)

### Fact N9 — Notion webhooks signal content changes

Source: [Notion webhooks](https://developers.notion.com/reference/webhooks)

### Fact N10 — General Notion search is not exhaustive or immediate

Notion states that search is not guaranteed to return everything, is not optimized for querying within a database, and can have indexing delay. Dedicated data-source queries are required for deterministic retrieval.

Source: [Notion search limitations](https://developers.notion.com/reference/search-optimizations-and-limitations)

## 5. Why Notion is not selected as primary machine memory

```text
- General workspace search is not exhaustive.
- Search indexing is not immediate.
- Page-oriented updates are less suitable than transactions for concurrent machine memory.
- Relational constraints, exact idempotency, vector indexing, and hybrid search are stronger in Postgres.
- An OAuth-connected hosted MCP can have broad user-visible workspace access if not carefully scoped.
- Notion remains excellent for human-readable decisions, lessons, and dashboards.
```

## 6. Why Supabase is not native CrewAI memory

CrewAI can call Python application code and tools, but the current Galax research has not found an official native CrewAI storage adapter that directly makes Supabase or Notion the built-in CrewAI memory backend.

Therefore:

```text
CrewAI Flow
→ GalaxMemoryGateway
→ Supabase/Postgres
```

The gateway returns a bounded `MemoryContext` to the Flow. The agent does not directly receive database credentials or a second memory tool.

## 7. Proposed database schema

```sql
create extension if not exists vector with schema extensions;

create table galax_memory (
  memory_id uuid primary key,
  project_id text not null,
  agent_id text,
  memory_type text not null,
  run_id text,
  task_id text,
  status text not null,
  active boolean not null default true,
  priority smallint not null default 0,
  scope text[] not null default '{}',
  summary text not null,
  required_future_behavior text,
  source_commit text,
  source_pr text,
  source_file_ids text[] not null default '{}',
  evidence_hash text not null,
  confidence text not null,
  supersedes_memory_id uuid references galax_memory(memory_id),
  expires_at timestamptz,
  embedding extensions.vector(<PINNED_DIMENSION>),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (project_id, memory_type, evidence_hash)
);
```

The embedding dimension remains a placeholder until a free, privacy-safe, pinned embedding model is researched and tested. The system must not default silently to OpenAI embeddings.

## 8. Retrieval flow

```text
exact filters by project/status/agent/scope
→ keyword candidate query
→ semantic or hybrid retrieval when embedding service is approved
→ conflict check against GitHub and current official evidence
→ rank and trim to memory token budget
→ return MemoryContext with IDs and evidence hashes
```

The runtime can operate in structured keyword-only mode before embeddings are approved.

## 9. Write flow

```text
agent structured output
→ actual tool/test evidence
→ deterministic validation
→ duplicate and supersession check
→ QA/security/auditor disposition
→ owner or approved policy decision
→ Flow writes through GalaxMemoryGateway
→ optional Notion mirror entry
```

An agent cannot directly create durable memory.

## 10. Notion mirror flow

```text
verified Supabase memory record
→ select human-readable memory types
→ redact technical secrets and oversized evidence
→ create or targeted-update Notion page
→ save Notion page ID back to memory record
```

Notion mirror failures do not corrupt or delete the canonical Supabase memory record.

## 11. Security design

```text
- Put memory tables in a dedicated schema when practical.
- Enable RLS on exposed tables.
- Prefer a dedicated backend role with least privileges.
- Keep secret/service keys only in memory-gateway Docker secrets.
- Never expose the secret/service role to agents or client UI.
- Use exact parameterized queries or validated RPCs.
- Never store raw hidden reasoning, credentials, customer PII, or unrestricted repository content.
- Record evidence hashes and source commits.
- Maintain off-site backups.
```

## 12. Free-plan operational restrictions

```text
- Treat project pause as BLOCKED_MEMORY_UNAVAILABLE, not as empty memory.
- Restore project before writing.
- Keep memory compact to stay below 500 MB.
- Create scheduled logical dumps outside Supabase.
- Test restore before production approval.
- Do not depend on hosted free Supabase for high-availability production work.
```

## 13. Required CrewAI integration tests

```text
MEM-SB-001 Flow connects through backend-only gateway.
MEM-SB-002 Agent never receives database credential.
MEM-SB-003 Structured exact-filter retrieval works.
MEM-SB-004 Keyword retrieval works.
MEM-SB-005 pgvector retrieval works after embedding approval.
MEM-SB-006 Hybrid retrieval produces deterministic bounded results.
MEM-SB-007 Repository truth overrides conflicting memory.
MEM-SB-008 Exact duplicate is rejected.
MEM-SB-009 Supersession deactivates the older record safely.
MEM-SB-010 RLS and dedicated-role restrictions are enforced.
MEM-SB-011 Secret/service key is absent from logs and prompts.
MEM-SB-012 Paused/unavailable project blocks safely.
MEM-SB-013 500 MB/read-only behavior is detected.
MEM-SB-014 Backup is created and restore is verified.
MEM-SB-015 Notion mirror failure leaves primary memory intact.
MEM-SB-016 Notion mirror contains only approved memory types.
MEM-SB-017 Concurrent writes preserve uniqueness and evidence links.
MEM-SB-018 Memory context remains within token budget.
MEM-SB-019 Memory write requires audit/approval.
MEM-SB-020 CrewAI sequential flow receives only approved MemoryContext.
```

Approval requires 20 of 20 tests in the pinned environment.

## 14. Final status

```yaml
supabase_postgres_memory_primitives: FACT_CHECKED_SUPPORTED
supabase_pgvector: FACT_CHECKED_SUPPORTED
supabase_hybrid_search: FACT_CHECKED_SUPPORTED
supabase_python_access: FACT_CHECKED_SUPPORTED
supabase_self_host_docker: FACT_CHECKED_SUPPORTED
notion_curated_mirror: FACT_CHECKED_TECHNICALLY_SUPPORTED
native_crewai_supabase_memory: NOT_PROVEN
native_crewai_notion_memory: NOT_PROVEN
GalaxMemoryGateway: NOT_IMPLEMENTED
live_crewai_integration: NOT_TESTED
production_ready: false
```
