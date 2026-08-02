# Custom GPT Storage and Achievement Separation Policy

```yaml
status: ACTIVE_CUSTOM_GPT_GOVERNANCE_POLICY
repository: ariessocia04-rgb/galax-Ai-project
branch_family: docs/chatgpt-*
policy_scope: Custom_GPT_configuration_instruction_skill_schema_package_and_validation_records
Galax_runtime_effect: none
CrewAI_Flow_routing_effect: none
Galax_source_or_tests_effect: none
final_authority: Human_Owner
```

## 1. Purpose

This policy keeps Custom GPT work physically stored in the Galax AI repository while keeping it logically and historically separate from Galax AI runtime, implementation, planning, validation, continuity, and achievement records.

The repository is the storage container. Storage in the same repository does not make a Custom GPT artifact a Galax AI runtime artifact or a Galax AI achievement.

## 2. Two independent achievement domains

```yaml
GALAX_AI_ACHIEVEMENT_DOMAIN:
  canonical_record: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
  includes:
    - Galax_architecture_and_governance_decisions
    - accepted_Galax_plans
    - verified_Galax_runtime_or_source_work
    - validated_Galax_tests
    - authorized_Galax_commits_pushes_merges_or_deployments
    - accepted_and_locked_Galax_artifacts
  excludes:
    - Custom_GPT_builder_configuration
    - Custom_GPT_knowledge_uploads
    - Custom_GPT_instruction_revisions
    - Custom_GPT_action_schemas
    - Custom_GPT_packaging
    - Custom_GPT_preview_tests

CUSTOM_GPT_ACHIEVEMENT_DOMAIN:
  canonical_record: docs/skills/chatgpt/achievements/CUSTOM_GPT_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-08-02.md
  includes:
    - Custom_GPT_creation_and_configuration
    - Custom_GPT_router_and_skill_knowledge_files
    - Custom_GPT_instruction_versions
    - Custom_GPT_storage_policy
    - Custom_GPT_action_schema_design
    - Custom_GPT_read_only_gateway_design
    - Custom_GPT_preview_and_routing_validation
    - Custom_GPT_packages_and_manifests
  excludes:
    - Galax_runtime_completion_claims
    - Galax_source_or_test_completion_claims
    - CrewAI_agent_or_Flow_completion_claims
    - Galax_merge_deployment_or_production_readiness_claims
```

## 3. Absolute separation rule

```text
Custom GPT achievement
→ record only in the Custom GPT achievement ledger
→ do not append it to the Galax AI achievement ledger

Galax AI achievement
→ record only in the Galax AI achievement ledger
→ do not append it to the Custom GPT achievement ledger
```

A shared event may appear in both domains only when it creates two independently proven results:

1. a completed Custom GPT result; and
2. a completed Galax AI result.

When that rare condition exists:

- create separate entries;
- use separate evidence;
- identify the exact effect in each domain;
- do not copy the same achievement text into both records;
- do not claim a Galax runtime effect from a Custom GPT configuration change;
- obtain the Human Owner authorization required by each domain.

Default rule:

```yaml
Custom_GPT_instruction_saved: CUSTOM_GPT_ACHIEVEMENT_ONLY
Custom_GPT_skill_file_saved: CUSTOM_GPT_ACHIEVEMENT_ONLY
Custom_GPT_knowledge_package_created: CUSTOM_GPT_ACHIEVEMENT_ONLY
Custom_GPT_preview_test_passed: CUSTOM_GPT_ACHIEVEMENT_ONLY
Galax_AI_achievement_created_automatically: false
```

## 4. Canonical Custom GPT storage root

All Custom GPT-specific files for Galax must be stored under:

```text
docs/skills/chatgpt/
```

This path is the Custom GPT governance and knowledge area inside the Galax AI repository.

Recommended structure:

```text
docs/skills/chatgpt/
├── 00_GALAX_SKILL_ROUTER_MANAGER.md
├── 01_GALAX_REPOSITORY_STATE_SCOPE_GUARDIAN.md
├── 02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md
├── 03_GALAX_EVIDENCE_VALIDATION_ACCEPTANCE_GUARDIAN.md
├── 04_GALAX_DRAFT_PR_EXACT_DIFF_REVIEWER.md
├── 05_GALAX_CONTINUITY_ACHIEVEMENT_GUARDIAN.md
├── 06_GALAX_LOCKED_ARTIFACT_GUARDIAN.md
├── 07_GALAX_REPOSITORY_CLEANUP_AUDITOR.md
├── CUSTOM_GPT_STORAGE_AND_ACHIEVEMENT_POLICY.md
├── instructions/
├── schemas/
├── packages/
├── validation/
└── achievements/
```

Folder responsibilities:

```yaml
instructions:
  purpose: versioned_Custom_GPT_builder_and_bootstrap_instructions

schemas:
  purpose: future_OpenAPI_Action_schemas_and_non_secret_contracts

packages:
  purpose: manifests_checksums_release_notes_and_upload_lists
  binary_or_secret_policy: do_not_commit_by_default

validation:
  purpose: Custom_GPT_preview_prompts_routing_receipts_and_behavior_checks

achievements:
  purpose: Custom_GPT_only_achievement_records
```

## 5. Files that must not receive Custom GPT records

Do not save Custom GPT-only instructions, achievements, schemas, packages, or preview tests under:

```text
src/
tests/
.github/workflows/
docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
docs/plan/ unless the file is a separately authorized Galax plan
docs/rules/ unless the file is a separately authorized Galax rule
```

Custom GPT files must not modify or reinterpret:

- `GalaxFoundationFlow`;
- CrewAI `@router` execution;
- Agent 01 or Agents 02–15;
- Galax source code or tests;
- active implementation assignments;
- `LOCKED_ACCEPTED` artifacts;
- GitHub workflows or secrets;
- merge or deployment authority.

## 6. Custom GPT instruction-save rule

Every completed, remotely verified save of a new or materially revised Custom GPT instruction may be evaluated as a Custom GPT achievement.

Required evidence:

```yaml
CUSTOM_GPT_INSTRUCTION_SAVE_RECEIPT_V1:
  repository:
  branch:
  commit_sha:
  file_path:
  instruction_type:
  previous_version_or_state:
  new_version_or_state:
  material_change_summary:
  Custom_GPT_effect:
  Galax_runtime_effect: none
  Galax_source_or_tests_effect: none
  secrets_added: false
  achievement_candidate: true | false
```

A save is not an achievement when it is:

- an empty file;
- an exact duplicate;
- an unreviewed draft with no completed purpose;
- a secret or credential upload;
- a misleading claim that the Custom GPT was installed, tested, synced, or connected when it was not;
- a change that merely reformats text without a material result.

## 7. Custom GPT achievement criteria

A Custom GPT achievement must be:

```yaml
completed: true
material: true
non_duplicate: true
evidence_classified: true
scope: Custom_GPT_only
unsupported_claims: none
Galax_runtime_claim: none_unless_independently_proven
```

Valid examples:

- private Custom GPT created by the Human Owner;
- router-first Custom GPT instructions completed;
- Skills 0–7 knowledge files saved and verified;
- knowledge upload package completed;
- exact storage and achievement policy completed;
- read-only OpenAPI schema completed and validated;
- secure gateway configured without exposing credentials;
- Custom GPT preview test proves correct primary-skill routing;
- stale Custom GPT knowledge files replaced with a verified version.

Invalid examples:

- planning to create a Custom GPT;
- requesting an API key;
- uploading an unverified or incomplete file;
- claiming live GitHub sync without an Action, App, or gateway;
- claiming a native plugin skill installation from a Markdown upload;
- claiming Galax runtime completion from Custom GPT configuration.

## 8. Evidence classes

```yaml
REMOTE_PROVEN:
  meaning: verified_in_the_current_GitHub_branch_file_or_commit

HUMAN_OWNER_REPORTED_CUSTOM_GPT_UI_STATE:
  meaning: Custom_GPT_builder_or_UI_state_reported_by_the_Human_Owner_but_not_visible_in_GitHub

LOCAL_ARTIFACT_PROVIDED:
  meaning: generated_package_or_file_provided_to_the_Human_Owner_but_not_committed_to_GitHub

NOT_PROVEN:
  meaning: no_sufficient_evidence
```

Do not convert a Human Owner UI report into GitHub proof. Do not convert a GitHub document into proof that the Custom GPT UI actually applied or uploaded it.

## 9. Separate commit and review rule

Custom GPT governance changes should use a docs-only branch and remain separate from Galax runtime implementation commits.

```yaml
preferred_branch_family: docs/chatgpt-*
runtime_files_in_same_commit: prohibited
source_or_tests_in_same_commit: prohibited
workflow_or_secret_changes_in_same_commit: prohibited
merge_to_main: separately_authorized
```

When a Custom GPT achievement ledger and an instruction file both change:

```text
save the instruction or policy first
→ verify its commit SHA
→ update the Custom GPT achievement ledger separately
→ reference the verified instruction commit SHA
→ stop
```

Do not update the Galax AI achievement ledger during this sequence.

## 10. Secret and API-key prohibition

Never save any of the following in the repository, Custom GPT Knowledge, builder instructions, schema files, packages, achievement records, or chat transcripts:

```text
OpenAI API keys
GitHub personal access tokens
GitHub App private keys
OAuth client secrets
backend API keys
webhook secrets
service-account credentials
private certificates
```

Only non-secret schemas, endpoint contracts, environment-variable names, and setup instructions may be stored.

## 11. Final storage contract

```text
All Galax-related Custom GPT artifacts
→ save under docs/skills/chatgpt/
→ classify as Custom GPT work
→ record completed Custom GPT achievements only in the Custom GPT achievement ledger
→ keep Galax AI achievements in their existing separate ledger
→ never mix the two domains by default
→ Human Owner remains final authority
```
