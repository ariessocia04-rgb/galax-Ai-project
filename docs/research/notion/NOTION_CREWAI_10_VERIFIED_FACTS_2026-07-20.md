# Notion + CrewAI — 10 Verified Facts

**Verified:** 2026-07-20  
**Status:** `RESEARCH_RECORD`  
**Decision:** Notion can function as external structured memory for a CrewAI application through an official Notion API gateway or MCP integration, but it is not a verified native CrewAI memory backend.

## Fact 1 — Notion provides an official hosted MCP server

Notion's official MCP server is available through Streamable HTTP at:

```text
https://mcp.notion.com/mcp
```

Notion documents SSE as a legacy fallback. The hosted MCP uses OAuth and can read or write workspace content according to the connected user's access.

Sources:

- [Notion MCP overview](https://developers.notion.com/guides/mcp/overview)
- [Connect to Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp)
- [Build an MCP client for Notion](https://developers.notion.com/guides/mcp/build-mcp-client)

## Fact 2 — CrewAI can load MCP servers as agent tools

CrewAI supports MCP integration and can hydrate MCP tools into a CrewAI project. CrewAI project annotations can initialize LLMs and tools separately, and `@CrewBase` can manage an MCP adapter lifecycle.

This proves a technical connection path between CrewAI and Notion MCP. It does not prove that Notion becomes CrewAI's native memory automatically.

Sources:

- [CrewAI MCP overview](https://docs.crewai.com/en/mcp/overview)
- [CrewAI MCP security](https://docs.crewai.com/en/mcp/security)
- [CrewAI annotations](https://docs.crewai.com/learn/using-annotations)

## Fact 3 — Notion MCP supports searching, fetching, creating, and updating content

Official Notion MCP tools include workspace search, page/data-source fetch, page creation, page update, database creation, data-source update, comments, and other workspace operations.

This is sufficient to implement external memory read/write operations when permissions and schemas are constrained.

Source:

- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

## Fact 4 — Notion pages can be retrieved as enhanced markdown

The Notion API can retrieve a page as enhanced markdown through:

```text
GET /v1/pages/{page_id}/markdown
```

Notion describes this endpoint as especially useful for agentic systems and developer tools. The response includes a `truncated` flag and `unknown_block_ids`; a client must fetch missing subtrees before claiming it read the complete page.

Source:

- [Retrieve a page as markdown](https://developers.notion.com/reference/retrieve-page-markdown)

## Fact 5 — Notion supports creating and targeted updating of markdown content

The Notion API supports creating pages with markdown, retrieving markdown, and updating page content with targeted search-and-replace operations. Targeted updates are safer than full-page replacement because unrelated content can be preserved.

Sources:

- [Working with markdown content](https://developers.notion.com/guides/data-apis/working-with-markdown-content)
- [Update page markdown](https://developers.notion.com/reference/update-page-markdown)

## Fact 6 — Structured data-source queries are better than workspace search for deterministic memory

Notion data sources can be queried with filters, sorts, pagination, and selected properties. This supports memory retrieval by `Project_ID`, `Agent_ID`, `Memory_Type`, status, and scope.

Notion's general search endpoint is not guaranteed to enumerate everything, is primarily optimized for finding pages or databases by name, and can have indexing delays. Therefore, Galax must query a dedicated memory data source instead of relying on broad workspace search.

Sources:

- [Query a data source](https://developers.notion.com/reference/query-a-data-source)
- [Search optimizations and limitations](https://developers.notion.com/reference/search-optimizations-and-limitations)

## Fact 7 — Notion enforces content capabilities and page access

Read endpoints require read-content capability; update endpoints require update-content capability. Missing access can return HTTP 403 or appear as HTTP 404 for inaccessible pages.

This permits a dedicated Notion integration to be shared only to the Galax memory pages or data source instead of granting broad workspace access.

Sources:

- [Retrieve a page](https://developers.notion.com/reference/retrieve-a-page)
- [Retrieve a page as markdown](https://developers.notion.com/reference/retrieve-page-markdown)
- [Update a page](https://developers.notion.com/reference/patch-page)

## Fact 8 — Notion rate limits require explicit retry handling

Notion documents an average request limit of three requests per second per connection. Rate-limited requests return HTTP 429 and include a `Retry-After` header that clients must respect.

Notion MCP documents an overall average of 180 requests per minute and a search-specific limit of 30 searches per minute. These limits can change.

Sources:

- [Notion API request limits](https://developers.notion.com/reference/request-limits)
- [Notion MCP supported tools and rate limits](https://developers.notion.com/guides/mcp/mcp-supported-tools)

## Fact 9 — Notion webhooks can signal memory changes but do not include full content

Notion webhooks can notify a connection when pages or databases change. Webhook events act as signals and do not include the complete changed content. The application must fetch the latest page after receiving and verifying an event.

This supports cache invalidation, but it is not a replacement for reading current memory from Notion.

Sources:

- [Notion webhooks](https://developers.notion.com/reference/webhooks)
- [Webhook events and delivery](https://developers.notion.com/reference/webhooks-events-delivery)

## Fact 10 — Notion search can include connected Google Drive only under specific plan conditions

Notion MCP's `notion-search` can search connected sources such as Google Drive, Slack, and Jira. Notion states that connected-source search requires Notion AI access; without it, search is limited to the Notion workspace.

Therefore, Notion search cannot be the mandatory Google Drive knowledge path for Galax. Direct Google Drive API retrieval remains the provider-independent required path.

Source:

- [Notion MCP supported tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

# Verified connected-workspace observation

The currently connected Notion workspace successfully returned search results through the installed Notion connector on 2026-07-20. Existing project-memory-style pages were discoverable, confirming that the current user connection supports workspace search.

This observation proves current connector access only. It does not approve unattended CrewAI memory writes or broad workspace access.

# Final technical decision

```yaml
notion_as_native_crewai_memory: NOT_PROVEN_AND_NOT_CLAIMED
notion_as_external_structured_memory: FACT_CHECKED_TECHNICALLY_SUPPORTED
preferred_connection: dedicated_Notion_API_gateway
notion_mcp_for_human_assisted_search: ALLOWED_CONDITIONALLY
notion_mcp_for_unattended_broad_agent_write: REJECTED_INITIAL_DEFAULT
agent_direct_notion_access: PROHIBITED
flow_managed_memory_read_write: SELECTED_FOR_VALIDATION
production_status: NOT_IMPLEMENTED
```
