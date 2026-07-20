# Tool Source Card — Notion Memory Gateway

**Source ID:** `TOOL-notion-memory-gateway`  
**Status:** `SELECTED_FOR_VALIDATION`  
**Implementation:** `NOT_IMPLEMENTED`  
**Type:** trusted Flow/application infrastructure, not direct agent memory  
**Verified:** 2026-07-20

## Identity

```yaml
name: GalaxNotionMemoryGateway
provider: Notion API
purpose: query_and_write_validated_structured_project_memory
authentication: dedicated_Notion_connection_or_integration
api_version: 2026-03-11
workspace_scope: dedicated_Galax_memory_pages_and_data_source_only
agent_direct_access: false
```

## Official sources

- [Notion API documentation](https://developers.notion.com/)
- [Notion MCP overview](https://developers.notion.com/guides/mcp/overview)
- [Connect to Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp)
- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)
- [Notion MCP security best practices](https://developers.notion.com/guides/mcp/mcp-security-best-practices)
- [Retrieve page as markdown](https://developers.notion.com/reference/retrieve-page-markdown)
- [Work with markdown content](https://developers.notion.com/guides/data-apis/working-with-markdown-content)
- [Update page markdown](https://developers.notion.com/reference/update-page-markdown)
- [Query a data source](https://developers.notion.com/reference/query-a-data-source)
- [Search limitations](https://developers.notion.com/reference/search-optimizations-and-limitations)
- [Request limits](https://developers.notion.com/reference/request-limits)
- [Webhooks](https://developers.notion.com/reference/webhooks)
- [Webhook event delivery](https://developers.notion.com/reference/webhooks-events-delivery)
- [CrewAI MCP overview](https://docs.crewai.com/en/mcp/overview)
- [CrewAI annotations and MCP lifecycle](https://docs.crewai.com/learn/using-annotations)

## Verified technical facts

```text
- Notion provides official API and hosted MCP read/write paths.
- CrewAI can consume MCP tools, establishing a supported integration path.
- Notion pages can be retrieved as enhanced markdown.
- Notion pages can be created and updated using markdown APIs.
- Data sources support structured filtering, sorting, and pagination.
- API calls require configured connection capabilities and page access.
- Rate limits return HTTP 429 with Retry-After.
- Webhooks signal changes but require follow-up content retrieval.
```

## Important limitation

Notion is not claimed as a native CrewAI memory provider. The selected architecture treats Notion as an external structured memory store controlled by the deterministic Flow/application.

The hosted Notion MCP can have access equivalent to the connected user's workspace permissions. Therefore, broad unattended agent access is not selected as the initial default.

## Galax security decision

```yaml
preferred_runtime: dedicated_Notion_API_gateway
Notion_MCP_human_assisted_lookup: conditionally_allowed
Notion_MCP_unattended_broad_write: rejected_initially
agent_direct_memory_write: prohibited
raw_chain_of_thought_storage: prohibited
secrets_or_personal_data_storage: prohibited
structured_data_source_query: required
workspace_search_as_canonical_memory: prohibited
```

## Related records

- [Notion Memory Rule](../../../rules/NOTION_MEMORY_RULE_DRAFT.md)
- [Ten verified Notion and CrewAI facts](../../../research/notion/NOTION_CREWAI_10_VERIFIED_FACTS_2026-07-20.md)
- [Drive + Notion architecture](../../../architecture/GOOGLE_DRIVE_KNOWLEDGE_NOTION_MEMORY_DRAFT.md)
- [15-agent matrix](../../../plan/AGENT_LLM_TOOL_KNOWLEDGE_MEMORY_MATRIX_DRAFT.md)

## Current connected-workspace observation

The currently installed Notion connector successfully returned workspace search results on 2026-07-20. This confirms current human-session connectivity only; it does not approve production memory automation.

## Approval blockers

```text
- Dedicated Galax Memory data source does not yet exist.
- Connection scope and capabilities are not configured.
- Memory schema and duplicate/supersession logic are not implemented.
- API rate-limit, truncation, permission, secret-redaction, and audit-gate tests have not run.
- CrewAI Flow integration has not been implemented or tested.
```
