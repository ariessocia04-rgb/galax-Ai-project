# Notion Memory Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This rule may be revised after Notion API, database schema, permission, retrieval, and CrewAI integration tests.  
**Decision:** Notion is an external structured project-memory store. It is not treated as CrewAI's native memory backend.

## 1. Core rule

```text
Only validated, concise, source-linked project memory may be stored in the dedicated Galax Notion memory area.
```

Notion memory supports future runs. It never outranks the active GitHub repository, current official sources, or live test evidence.

## 2. Why Notion is external memory

CrewAI can use tools and MCP integrations, but the Galax system has no verified native CrewAI memory provider that automatically turns Notion into CrewAI memory.

The supported architecture is:

```text
CrewAI Flow/application
→ GalaxNotionMemoryGateway
→ official Notion API
→ dedicated Galax memory data source/pages
```

The official Notion MCP may be used for human-assisted workspace search and testing. It is not selected for unattended broad agent memory because the hosted MCP can operate with the connected user's workspace access.

## 3. Capability ownership

```yaml
Flow_or_trusted_application:
  owns:
    - memory query construction
    - memory relevance filtering
    - memory budget
    - memory write eligibility
    - idempotency checks
    - supersession rules
    - post-audit memory write

GalaxNotionMemoryGateway:
  owns:
    - Notion authentication
    - dedicated data source query
    - page retrieval as markdown
    - create and targeted update operations
    - rate-limit handling
    - response validation
    - Notion page and data source IDs

CrewAI_agent:
  receives:
    - selected validated memory excerpts
  may_not:
    - browse the whole Notion workspace
    - directly create, overwrite, move, or delete memory pages
    - treat memory as repository truth
    - store raw reasoning

Release_Auditor_and_owner:
  approve:
    - durable lessons
    - resolved decisions
    - confirmed mistakes
    - reusable validation evidence
```

## 4. Access design

Preferred production design:

```yaml
authentication: dedicated_Notion_integration_or_OAuth_connection
shared_content:
  - Galax Memory data source
  - Galax Memory Index page
workspace_wide_access: prohibited
read_content: true
insert_content: true
update_content: true
comment_access: false_initially
```

Secrets:

```env
NOTION_API_KEY=
NOTION_MEMORY_DATA_SOURCE_ID=
NOTION_MEMORY_INDEX_PAGE_ID=
NOTION_API_VERSION=2026-03-11
```

Secrets never appear in agent prompts, YAML, repository commits, diagnostic output, source cards, or Notion memory content.

## 5. Memory data model

Canonical data source: `Galax Memory`.

Required properties:

```yaml
Memory_ID: title
Project_ID: text
Memory_Type: select
Agent_ID: text
Run_ID: text
Task_ID: text
Status: select
Active: checkbox
Priority: select
Scope: multi_select
Source_Commit: text
Source_PR: url
Source_File_IDs: text
Evidence_Hash: text
Confidence: select
Created_At: created_time
Last_Edited_At: last_edited_time
Supersedes_Memory_ID: text
Expires_At: date
```

Allowed `Memory_Type` values:

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
```

## 6. Memory page body

```markdown
# Memory summary

## Confirmed fact

## Evidence

## Applicable scope

## What failed or changed

## Required future behavior

## Limitations

## Source links
```

Every memory entry must be concise and independently understandable.

## 7. Prohibited memory content

```text
- raw chain-of-thought or hidden reasoning
- complete prompts when not necessary
- API keys, tokens, passwords, cookies, or private keys
- full `.env` content
- customer personal information
- production database records
- unverified speculation written as fact
- duplicate copies of repository rules
- copied source material without provenance
- unsupported claims that an agent is fully autonomous or guaranteed correct
```

## 8. Retrieval rule

Do not use broad Notion workspace search as the canonical memory lookup.

The Flow queries the dedicated Galax Memory data source using structured filters:

```yaml
filters:
  Project_ID: galax
  Active: true
  Status: VERIFIED
  Memory_Type: task_relevant_types
  Agent_ID: selected_agent_or_GLOBAL
  Scope: current_task_tags
sorts:
  - Priority: descending
  - Last_Edited_At: descending
limit: 10
```

Notion workspace search is name-oriented, can be incomplete, and can have indexing delay. Structured data-source queries are required for deterministic memory retrieval.

## 9. Memory priority

```text
Active GitHub repository rules and source files
> current official documentation
> current live test evidence
> approved architecture decisions
> verified Notion memory
> unverified historical notes
```

When memory conflicts with a higher-priority source:

```yaml
status: MEMORY_STALE_OR_CONFLICTING
use_memory: false
required_action:
  - cite conflict
  - mark entry for review
  - continue only with higher-priority source
```

## 10. Memory write gate

An agent result does not directly become memory.

```text
agent output
→ deterministic validation
→ tool and test evidence
→ QA or security result when required
→ Release Auditor review
→ owner-approved or policy-approved disposition
→ Flow writes memory through Notion gateway
```

Allowed automatic write:

```text
validated recovery checkpoint with no secrets
```

All durable decisions, lessons, or mistakes require audit evidence.

## 11. Idempotency and duplicates

Before creating a memory entry, the gateway queries by:

```text
Memory_ID
or Evidence_Hash + Memory_Type + Project_ID
```

If an exact duplicate exists:

```yaml
action: do_not_create_duplicate
result: EXISTING_MEMORY_RETURNED
```

If a newer entry replaces an older one:

```yaml
new_entry:
  Active: true
  Supersedes_Memory_ID: old_id
old_entry:
  Active: false
  Status: SUPERSEDED
```

## 12. Page retrieval and truncation

Memory pages are retrieved through the Notion markdown endpoint.

If the response says `truncated: true`, the gateway must retrieve the returned `unknown_block_ids` before claiming the page was fully read.

A partial page may not be represented as complete memory.

## 13. Rate-limit rule

Notion's general API limit is an average of three requests per second per connection.

Galax internal limit:

```yaml
maximum_requests_per_second: 1
parallel_notion_requests: false
on_429:
  - read Retry-After
  - save checkpoint
  - wait at least the required interval
  - retry at most once
```

## 14. Change detection

Notion webhooks may signal that a memory page or data source changed. The event does not contain the full changed content.

```text
webhook signal
→ verify event authenticity
→ fetch current page/data source
→ compare content hash
→ update local cache
→ revalidate affected memory
```

Webhook-triggered automatic execution is not enabled until webhook authentication and replay protection are tested.

## 15. Connected-source search boundary

Notion MCP can search connected sources such as Google Drive only when the workspace has the required Notion AI access. Without that plan, search is limited to the Notion workspace.

Therefore, Notion connected search is optional and cannot replace the direct DriveKnowledgeGateway.

## 16. Memory context schema

```yaml
memory_context:
  retrieval_id:
  run_id:
  agent_id:
  entries:
    - memory_id:
      memory_type:
      summary:
      required_future_behavior:
      source_commit:
      evidence_hash:
      last_edited_time:
      confidence:
  conflicts: []
  omitted_entries_count:
  token_estimate:
```

The Flow supplies only task-relevant entries within a fixed token budget.

## 17. Failure states

```text
BLOCKED_NOTION_AUTH
BLOCKED_NOTION_PERMISSION
BLOCKED_NOTION_RATE_LIMIT
BLOCKED_MEMORY_SCHEMA_MISMATCH
BLOCKED_MEMORY_TRUNCATED
BLOCKED_MEMORY_CONFLICT
BLOCKED_MEMORY_WRITE_NOT_APPROVED
BLOCKED_MEMORY_DUPLICATE_AMBIGUITY
```

## 18. Approval tests

```text
MEM-001 Connect only to the configured Notion workspace.
MEM-002 Access only the dedicated Galax memory pages/data source.
MEM-003 Query memory by structured data-source filters.
MEM-004 Retrieve full page markdown.
MEM-005 Follow truncated unknown block IDs.
MEM-006 Create a validated memory entry.
MEM-007 Perform a targeted update without replacing unrelated content.
MEM-008 Reject a write without audit approval.
MEM-009 Prevent exact duplicate memory.
MEM-010 Supersede stale memory safely.
MEM-011 Enforce repository-over-memory priority.
MEM-012 Redact secrets and prohibited personal data.
MEM-013 Handle HTTP 429 and Retry-After.
MEM-014 Confirm raw reasoning is never stored.
MEM-015 Invalidate cached memory after a verified change.
MEM-016 Confirm Notion token is absent from prompts and logs.
MEM-017 Confirm agents cannot directly call Notion.
MEM-018 Confirm memory context remains within token budget.
```

Approval requires 18 of 18 tests in the pinned environment.
