# Tool Source Card — Notion Curated Memory Mirror Gateway

**Source ID:** `TOOL-notion-memory-gateway`  
**Status:** `OPTIONAL_SELECTED_FOR_VALIDATION`  
**Implementation:** `NOT_IMPLEMENTED`  
**Type:** trusted Flow/application infrastructure, not direct agent memory  
**Verified:** 2026-07-20

## Corrected identity

```yaml
name: GalaxNotionMirrorGateway
provider: Notion_API
purpose: mirror_approved_human_readable_memory_from_primary_Supabase_record
authentication: dedicated_Notion_connection_or_integration
workspace_scope: dedicated_Galax_memory_pages_and_data_source_only
agent_direct_access: false
primary_runtime_memory: false
```

Notion was previously selected as the primary external memory candidate. Current research supersedes that decision: Supabase/Postgres is the primary machine-memory candidate; Notion remains an optional curated mirror.

## Official sources

- [Notion API documentation](https://developers.notion.com/)
- [Notion MCP overview](https://developers.notion.com/guides/mcp/overview)
- [Connect to Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp)
- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Notion MCP security best practices](https://developers.notion.com/guides/mcp/mcp-security-best-practices)
- [Retrieve page as markdown](https://developers.notion.com/reference/retrieve-page-markdown)
- [Work with markdown content](https://developers.notion.com/guides/data-apis/working-with-markdown-content)
- [Query a data source](https://developers.notion.com/reference/query-a-data-source)
- [Search limitations](https://developers.notion.com/reference/search-optimizations-and-limitations)
- [Request limits](https://developers.notion.com/reference/request-limits)
- [Webhooks](https://developers.notion.com/reference/webhooks)
- [CrewAI MCP overview](https://docs.crewai.com/en/mcp/overview)

## Verified technical facts

```text
- Notion provides official API and hosted MCP read/write paths.
- Notion pages can be retrieved and updated as enhanced Markdown.
- Data sources support structured queries.
- Access depends on connection capabilities and shared content.
- Rate limits require HTTP 429/Retry-After handling.
- General search is not exhaustive and may have indexing delay.
- Notion is not proven as a native CrewAI memory backend.
```

## Selected use

```text
verified Supabase memory record
→ choose approved human-readable memory type
→ redact secrets and oversized evidence
→ create or targeted-update Notion page
→ write Notion page ID/status back to primary record
```

If Notion is unavailable, the primary Supabase record remains valid. No reverse sync is enabled initially.

## Security decision

```yaml
Notion_MCP_human_assisted_lookup: conditionally_allowed
Notion_MCP_unattended_broad_write: rejected_initially
agent_direct_memory_write: prohibited
raw_chain_of_thought_storage: prohibited
secrets_or_personal_data_storage: prohibited
workspace_search_as_primary_memory: prohibited
```

## Related records

- [Primary memory rule](../../../rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md)
- [Notion vs Supabase decision](../../../research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md)
- [Earlier Notion research](../../../research/notion/NOTION_CREWAI_10_VERIFIED_FACTS_2026-07-20.md)
- [15-agent runtime limits](../../../plan/15_AGENT_RUNTIME_LIMITS_DRAFT.md)

## Approval blockers

```text
- Dedicated mirror data source/pages do not exist.
- Connection scope is not configured.
- Primary Supabase memory gateway is not implemented.
- Targeted update, idempotency, redaction, rate-limit, and failure-isolation tests have not run.
- CrewAI Flow integration is not implemented or tested.
```
