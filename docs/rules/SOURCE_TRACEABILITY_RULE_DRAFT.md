# Source Traceability Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This file may be revised when agents, tools, LLMs, providers, versions, or project rules change.  
**Applies to:** Every Galax AI agent, LLM, tool, MCP server, framework dependency, and factual capability claim.

## 1. Core rule

Every LLM and tool considered for a Galax AI agent must have an exact source record in the repository before it can be approved or used.

A source record must answer:

- What exact LLM or tool is this?
- Which agent uses it?
- What exact official page or repository proves its identity?
- What exact documentation proves the required capability?
- What license applies?
- What rate, token, quota, or cost limits apply?
- What privacy and data-retention policy applies?
- What version or release was tested?
- When was it verified?
- Is it active, candidate, rejected, deprecated, or awaiting revalidation?

## 2. Canonical source locations

```text
docs/sources/
├── SOURCE_INDEX.md
├── llms/
│   └── <llm-id>/SOURCE_CARD.md
├── tools/
│   └── <tool-id>/SOURCE_CARD.md
└── agents/
    └── <agent-id>/SOURCE_CARD.md
```

Each agent source card links to exactly one approved LLM source card and one approved tool source card.

## 3. Required LLM links

Every LLM source card must contain clickable links to:

1. Official provider page.
2. Exact official model page.
3. Official API documentation.
4. Official CrewAI connection documentation.
5. Official context-window and output-limit documentation.
6. Official tool/function-calling documentation when required.
7. Official structured-output documentation when required.
8. Official rate-limit documentation.
9. Official pricing or free-tier documentation.
10. Official privacy and data-retention policy.
11. Official model license or model-card license.
12. Official status or deprecation notice location when available.

A directory or aggregator such as FreeLLM may be recorded as a discovery source, but it cannot replace the actual provider and model sources.

## 4. Required tool links

Every tool source card must contain clickable links to:

1. Official project repository or official product page.
2. Official documentation.
3. Exact license file.
4. Exact release or commit tested.
5. Security documentation or advisories when available.
6. CrewAI compatibility documentation.
7. Required authentication and permissions documentation.
8. Cost or self-hosting documentation.

## 5. Required source-card fields

```yaml
source_id:
source_type: llm | tool | mcp | framework | standard
name:
agent_ids: []
status: CANDIDATE | CONDITIONALLY_APPROVED | APPROVED | REJECTED | DEPRECATED | REVALIDATION_REQUIRED
provider_or_maintainer:
exact_model_or_tool_id:
version_or_commit:
license:
verified_date:
verified_by:
capabilities_verified: []
limitations: []
security_notes: []
cost_status:
links:
  official_home:
  exact_model_or_tool_page:
  api_or_usage_docs:
  crewai_compatibility:
  rate_limits:
  pricing_or_free_tier:
  privacy_or_data_policy:
  license:
  release_or_commit:
  security:
test_evidence:
```

Missing fields must remain explicit as `null` or `NOT_FOUND`. They must never be guessed.

## 6. Agent source-card rule

Each agent must have:

```text
docs/sources/agents/<agent-id>/SOURCE_CARD.md
```

The card must show:

- Agent ID and role.
- LLM source-card link.
- Tool source-card link.
- Professional-role evidence links.
- CrewAI feature evidence links.
- Current approval status.
- Latest tested commit and date.

## 7. One-question source lookup

Galax must support a deterministic source lookup command:

```text
source <agent-id>
```

Examples:

```text
source engineering_manager
source frontend_engineer
source AGENT-01
```

The lookup must read the repository source index and return clickable links only from the recorded source cards. It must not use LLM memory to invent or reconstruct a link.

Expected output:

```yaml
agent_id:
agent_role:
llm:
  name:
  status:
  source_card:
  official_model_link:
tool:
  name:
  status:
  source_card:
  official_tool_link:
last_verified:
revalidation_required:
```

## 8. Source lookup implementation boundary

Source lookup must be deterministic application code or a read-only repository function. It is not a second agent tool and it must not consume an additional research LLM call.

The source lookup may be exposed before a normal run starts, or as a separate CLI/API route.

## 9. Approval rule

An LLM or tool cannot be referenced in production `agents.yaml` until:

```text
SOURCE CARD COMPLETE
→ OFFICIAL LINKS VERIFIED
→ LICENSE VERIFIED
→ COST VERIFIED
→ PERMISSIONS VERIFIED
→ COMPATIBILITY TESTED
→ SECURITY TESTED
→ STATUS = APPROVED
```

## 10. Change and revalidation rule

Any of these changes automatically set the source to `REVALIDATION_REQUIRED`:

- Provider change.
- Model ID change.
- Model revision change when behavior or limits may change.
- CrewAI version change.
- Tool or MCP release change.
- Authentication method change.
- Permission scope change.
- Pricing or quota change.
- Privacy or retention change.
- Tool schema change.

## 11. Link integrity test

Before approval, automated tests must verify that:

- Required links are present.
- Links use HTTPS.
- Links point to the official provider, maintainer, specification owner, or source repository.
- The exact model or tool identifier appears in the source page.
- No URL shortener is used.
- No affiliate or referral link is used.
- No secret, token, or signed temporary URL is stored.

## 12. Current status

This rule is saved as a draft. It is not yet merged into `main` and may be edited as agent-by-agent research continues.
