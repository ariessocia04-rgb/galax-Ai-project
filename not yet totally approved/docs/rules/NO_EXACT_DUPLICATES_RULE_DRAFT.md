# No Exact Duplicates Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This rule may be revised before merge.  
**Applies to:** agents, roles, goals, backstories, tasks, tools, LLM source cards, rules, plans, prompts, schemas, and documentation.

## 1. Core rule

```text
When two repository records are 100% identical after deterministic normalization,
keep one canonical record and remove the duplicate.

When the records have materially different roles, responsibilities, boundaries,
inputs, outputs, permissions, or workflow positions, both may remain.
```

## 2. Exact duplicate definition

A record is an exact duplicate only when all applicable normalized fields are identical.

For agents, compare:

```yaml
identity_fields:
  - role
  - goal
  - backstory
  - responsibilities
  - allowed_actions
  - prohibited_actions
  - input_contract
  - output_contract
  - assigned_llm
  - assigned_tool
  - tool_permissions
  - workflow_stage
  - self_diagnostic_schema
  - guardrails
```

For tools, compare:

```yaml
identity_fields:
  - tool_id
  - purpose
  - input_schema
  - output_schema
  - operations
  - permissions
  - allowed_paths
  - prohibited_paths
  - network_policy
  - authentication_method
  - failure_behavior
```

For LLM records, compare:

```yaml
identity_fields:
  - provider
  - exact_model_id
  - endpoint_type
  - model_revision
  - capabilities
  - limits
  - privacy_policy
  - license
  - tested_configuration
```

## 3. Deterministic normalization

The duplicate check may normalize only:

```text
- line-ending differences
- trailing whitespace
- repeated blank lines
- YAML key ordering
- JSON key ordering
- Markdown heading spacing
```

It must not remove, rewrite, summarize, paraphrase, or semantically reinterpret content before comparing it.

## 4. Hash rule

Every candidate record must receive a normalized SHA-256 content hash.

```yaml
exact_duplicate:
  same_normalized_hash: true
  same_record_type: true
  action: keep_canonical_remove_duplicate
```

A matching title or role name alone is not enough to declare a duplicate.

## 5. Materially different records

Two agents with similar names may remain when at least one material field differs.

Allowed example:

```text
Backend API Engineer
Database Engineer
```

They both work with server-side systems, but their responsibilities, permissions, tools, and outputs differ.

Another allowed example:

```text
QA Test Engineer
Release Auditor
```

Both verify work, but QA executes tests while the Auditor independently reviews final evidence and cannot edit implementation.

## 6. Near-duplicate rule

When records appear similar but are not 100% identical:

```yaml
status: POSSIBLE_OVERLAP_REVIEW_REQUIRED
automatic_deletion: false
required_action:
  - identify overlapping fields
  - identify distinct fields
  - document why both are needed or propose consolidation
  - obtain owner approval before removal
```

No LLM may automatically delete a near duplicate based only on semantic similarity.

## 7. Canonical-record selection

When an exact duplicate exists, keep the record that:

```text
1. Is referenced by the current README or active plan.
2. Has the current approved status.
3. Has the newest verified source links and test evidence.
4. Uses the canonical repository path.
5. Has the greatest number of valid inbound references.
```

If these rules do not resolve the choice, stop with:

```text
BLOCKED_CANONICAL_DUPLICATE_DECISION
```

## 8. Safe duplicate removal procedure

```text
DETECT EXACT DUPLICATE
→ verify normalized hashes match
→ choose canonical record
→ find all inbound references
→ update references to canonical path
→ record removal in duplicate log
→ delete duplicate on a run branch
→ validate no broken links or registry entries
→ QA verification
→ auditor verification
→ draft PR
```

## 9. Duplicate log

Every removed exact duplicate must be recorded in:

```text
docs/evidence/DUPLICATE_REMOVAL_LOG.md
```

Required fields:

```yaml
removed_path:
canonical_path:
normalized_sha256:
record_type:
reason: EXACT_DUPLICATE
references_updated: []
removed_by_run_id:
verified_by:
date:
```

## 10. Protected records

The following cannot be automatically deleted even when duplicated:

```text
- legal or license files
- security evidence
- historical release records
- signed audit evidence
- migration records
- incident records
- files required by an external standard
```

They must instead be flagged for owner review.

## 11. Agent duplicate enforcement

Before a new agent can be approved:

```text
compare against all existing agent normalized hashes
→ compare material responsibility fields
→ exact match: reject new duplicate and use canonical agent
→ partial overlap: produce overlap report
→ materially distinct: allow both
```

## 12. Current repository result

At the time this rule was created, no exact duplicate agent or LLM source card had been established in the draft branch. The existing Groq and Cerebras candidates are different provider records and are not duplicates.
