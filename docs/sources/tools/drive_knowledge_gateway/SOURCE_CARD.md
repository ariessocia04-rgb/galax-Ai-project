# Tool Source Card — Drive Knowledge Gateway

**Source ID:** `TOOL-drive-knowledge-gateway`  
**Status:** `SELECTED_FOR_VALIDATION`  
**Implementation:** `NOT_IMPLEMENTED`  
**Type:** trusted Flow/application infrastructure, not an agent-exposed second tool  
**Verified:** 2026-07-20

## Identity

```yaml
name: DriveKnowledgeGateway
provider: Google Drive API v3
purpose: read_owner_learning_material_and_build_verified_LearningPackets
authentication: OAuth_2_or_service_identity_as_approved
initial_scope: https://www.googleapis.com/auth/drive.readonly
write_access: false
allowed_roots: configured_Galax_knowledge_roots_only
```

## Official sources

- [Google Drive API v3](https://developers.google.com/workspace/drive/api/reference/rest/v3)
- [Search for files and folders](https://developers.google.com/workspace/drive/api/guides/search-files)
- [Search terms and operators](https://developers.google.com/workspace/drive/api/guides/ref-search-terms)
- [List files](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list)
- [Get file metadata/content](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/get)
- [Export Google Workspace documents](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/export)
- [Download and export files](https://developers.google.com/workspace/drive/api/guides/manage-downloads)
- [Drive labels overview](https://developers.google.com/workspace/drive/api/guides/about-labels)
- [Custom file properties](https://developers.google.com/workspace/drive/api/guides/properties)
- [Drive changes](https://developers.google.com/workspace/drive/api/guides/manage-changes)
- [Watch changes](https://developers.google.com/workspace/drive/api/reference/rest/v3/changes/watch)

## Verified capabilities

```text
- search by filename and metadata
- search using fullText lexical terms and exact phrases
- restrict by parent folder, MIME type, modified time, labels, and properties
- retrieve file metadata by stable file ID
- download supported blob files
- export Google Workspace documents
- identify changes through Drive change feeds and notifications
```

## Important limitations

```text
- Drive fullText search is lexical and is not a guaranteed semantic search engine.
- Search can return incomplete results across very large corpora; incompleteSearch must be checked.
- Google Workspace export content is limited by the provider's export-size limit.
- File title alone is not reliable evidence of content relevance.
- Change notifications are signals and do not contain the full updated content.
- Restricted OAuth scopes may require additional Google verification depending on deployment.
```

## Galax security decision

```yaml
agent_direct_credentials: prohibited
agent_direct_Drive_access: prohibited
Flow_managed_retrieval: selected
read_only: required_initially
search_outside_configured_roots: prohibited
Drive_write_delete_share: prohibited
prompt_injection_from_file_content: treat_as_untrusted_data
```

## Related records

- [Knowledge Before Implementation Rule](../../../rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md)
- [Drive + Notion architecture](../../../architecture/GOOGLE_DRIVE_KNOWLEDGE_NOTION_MEMORY_DRAFT.md)
- [15-agent matrix](../../../plan/AGENT_LLM_TOOL_KNOWLEDGE_MEMORY_MATRIX_DRAFT.md)

## Approval blockers

```text
- Google Cloud project and OAuth client not configured.
- Approved Drive root IDs are not configured.
- File parsers are not implemented.
- LearningPacket and StudyReceipt tests have not run.
- Secret scanning and prompt-injection tests have not run.
```
