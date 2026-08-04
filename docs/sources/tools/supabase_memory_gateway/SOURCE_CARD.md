# Tool Source Card — Galax Supabase Memory Gateway

**Source ID:** `TOOL-supabase-memory-gateway`  
**Status:** `SELECTED_FOR_VALIDATION`  
**Implementation:** `NOT_IMPLEMENTED`  
**Exposed directly to agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
name: GalaxMemoryGateway
type: trusted_Flow_application_component
primary_store: Supabase_Postgres_or_self_hosted_Postgres
vector_extension: pgvector
Notion_role: optional_curated_mirror
CrewAI_native_memory: false
```

## Official Supabase sources

- [Supabase database](https://supabase.com/docs/guides/database/overview)
- [AI and vectors](https://supabase.com/docs/guides/ai)
- [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector)
- [Vector columns](https://supabase.com/docs/guides/ai/vector-columns)
- [Semantic search](https://supabase.com/docs/guides/ai/semantic-search)
- [Hybrid search](https://supabase.com/docs/guides/ai/hybrid-search)
- [Vector indexes](https://supabase.com/docs/guides/ai/vector-indexes)
- [Python vector client](https://supabase.com/docs/guides/ai/vecs-python-client)
- [Python client selection](https://supabase.com/docs/guides/ai/python-clients)
- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Securing data and keys](https://supabase.com/docs/guides/database/secure-data)
- [Database Webhooks](https://supabase.com/docs/guides/database/webhooks)
- [Self-hosting with Docker](https://supabase.com/docs/guides/self-hosting/docker)
- [Self-hosting responsibilities](https://supabase.com/docs/guides/self-hosting)
- [Database backups](https://supabase.com/docs/guides/platform/backups)
- [Pricing and free limits](https://supabase.com/pricing)

## CrewAI connection decision

CrewAI agents do not call Supabase directly. The deterministic Flow requests memory through this gateway and injects a bounded validated `MemoryContext` into the selected task.

```python
crew = Crew(
    agents=selected_agents,
    tasks=selected_tasks,
    process=Process.sequential,
    memory=False,
)
```

Official CrewAI sources:

- [CrewAI documentation](https://docs.crewai.com/)
- [CrewAI Flows](https://docs.crewai.com/en/concepts/flows)
- [CrewAI sequential process](https://docs.crewai.com/en/concepts/processes)

## Supported candidate operations

```yaml
operations:
  - retrieve_exact_filtered_memory
  - retrieve_keyword_candidates
  - retrieve_pgvector_candidates_after_embedding_approval
  - retrieve_hybrid_candidates_after_embedding_approval
  - validate_evidence_hashes
  - create_validated_memory_transaction
  - reject_exact_duplicate
  - supersede_memory_transaction
  - write_backup
  - verify_restore
```

## Prohibited operations

```text
- credentials in prompts
- agent-direct SQL
- unrestricted query generation
- storing raw hidden reasoning
- storing secrets or production customer data
- silent embedding-provider fallback
- durable memory from unvalidated agent prose
```

## Current managed-free constraints

```yaml
database_size: 500_MB
project_pause_after_inactivity: 1_week
automatic_backups: false
active_free_projects: 2
```

These values must be checked again before implementation.

## Approval blockers

```text
- Database schema and migrations do not exist.
- Dedicated role/RLS policies are not implemented.
- Embedding model is not selected.
- Gateway code does not exist.
- CrewAI Flow integration is not tested.
- Backup and restore are not tested.
- Notion mirror gateway is not converted from primary-memory design.
```

## Revalidation triggers

- Supabase client/API change.
- Postgres or pgvector version change.
- Schema, RLS, or role permission change.
- Embedding model/dimension change.
- Retrieval threshold/ranking change.
- Free-plan quota or pause behavior change.
- CrewAI task-context schema change.
