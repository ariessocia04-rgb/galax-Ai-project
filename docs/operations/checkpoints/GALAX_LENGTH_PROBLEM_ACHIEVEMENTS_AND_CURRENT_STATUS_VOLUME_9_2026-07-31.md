# Galax Length-Problem Achievements and Current Status — Volume 9

```yaml
document_id: GALAX_LENGTH_PROBLEM_ACHIEVEMENTS_AND_CURRENT_STATUS_VOLUME_9_2026_07_31
record_type: CLINE_PROMPT_CREATION_GOVERNANCE_MIGRATION_CHECKPOINT
recorded_date: 2026-07-31
recorded_local_time: 2026-07-31T06:47:00+08:00
repository: ariessocia04-rgb/galax-Ai-project
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
previous_volume_8: docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_ACHIEVEMENTS_AND_CURRENT_STATUS_VOLUME_8_2026-07-30.md
canonical_continuity_protocol: docs/operations/CODE_RED.md
canonical_Cline_prompt_creation_rule: docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
old_command_pack_path: docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
old_command_pack_current_status: SUPERSEDED_COMPATIBILITY_REDIRECT
runtime_or_source_change: false
implementation_authority_changed: false
```

## Human Owner decision

The Human Owner rejected the old generic Cline prompt-writing pattern as the active method for creating new Cline assignments.

The Human Owner requires the flat, strict, sectioned pattern demonstrated by the accepted assignments and conversations.

```yaml
owner_decision:
  old_generic_Cline_prompt_pattern_active: false
  new_canonical_prompt_guide_required: true
  new_chat_must_read_prompt_guide: true
  generic_nested_template_as_primary_prompt: prohibited
  automatic_Plan_to_Act_continuation: prohibited
  manual_approval_per_command: required_when_commands_exist
```

## New canonical path

Every ChatGPT session, new chat, and repository-aware assignment author must read:

```text
docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
```

before creating, correcting, reviewing, or approving any prompt for Cline.

The guide is titled:

```text
HOW TO PROPER CREATE PROMPT FOR CLINE
```

and is classified as:

```yaml
status: ACTIVE_CANONICAL_CLINE_PROMPT_CREATION_RULE
```

## Old prompt authority removed

The previous active contents of:

```text
docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
```

were removed from active prompt-construction authority.

That path now exists only as a compatibility redirect to the canonical guide. Its former contents remain preserved in Git history as historical evidence.

```yaml
old_generic_Cline_Stage_A_prompt: RETIRED
old_generic_Cline_Stage_B_prompt: RETIRED
old_universal_header_as_complete_prompt_method: RETIRED
generic_one_line_Cline_prompt: PROHIBITED
historical_evidence_deleted: false
```

## Required Cline prompt pattern

The canonical structure is:

```text
GALAX_AI_ASSIGNMENT_V1

assignment_id
parent_assignment_id when applicable
parent_plan_id when applicable
contributor
role
mode
repository
branch

OBJECTIVE

CHATGPT-VERIFIED CURRENT FACTS

WHAT HAS ALREADY BEEN COMPLETED

DO NOT REPEAT

MANDATORY CORRECTIONS
or
AUTHORIZED OBJECTIVE

CANONICAL STAGE MAPPING when applicable

THIS ASSIGNMENT AUTHORIZES ONLY

REPOSITORY-PLAN BOUNDARY

MINIMUM-SYSTEM-MUTATION RULE when applicable

COMMAND EXECUTION CONTROL when applicable

NUMBERED STEPS

AUTHORIZED EFFECTS

REQUIRED RESULT

STOP IMMEDIATELY IF

STRICT REPOSITORY PROHIBITIONS

REQUIRED OUTPUT

FINAL_STATUS

STOP after the output.
```

## Command-control rule

When a Cline assignment contains commands:

```text
run exactly one numbered command at a time
→ show the exact visible command popup
→ wait for Human Owner approval
→ keep auto-approval disabled
→ do not combine separately governed steps
→ do not silently continue
```

When a command fails:

```text
stop immediately
→ preserve the exact command
→ preserve the exit code
→ preserve raw output
→ do not improvise a replacement method
→ do not repeat automatically
→ return the exact blocker
```

## New-chat path updated

The legacy continuity redirect:

```text
docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
```

now routes every new chat through:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ this Volume 9 checkpoint
→ docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
→ the exact active plan and assignment
→ docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
→ live repository and owner-supplied evidence
```

The old command-pack path also redirects to the new canonical prompt guide. Therefore older README, AGENTS, issue, PR, plan, and conversation references still lead to the correct prompt-writing rule.

## Required new-chat prompt receipt

Before drafting a Cline prompt, a new chat must be able to return:

```yaml
CLINE_PROMPT_CREATION_PATH_RECEIPT_V1:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:
  prompt_guide_read: true
  live_state_verified:
  completed_actions_identified: []
  actions_that_must_not_be_repeated: []
  assignment_mode:
  single_objective:
  commands_batched: false
  automatic_continuation_allowed: false
  exact_receipt_defined:
  safe_to_draft_prompt: false
```

`safe_to_draft_prompt` becomes true only when repository facts, current evidence, exact scope, and Human Owner authority agree.

## Current technical state preserved

This governance migration does not change the technical result recorded in Volume 8.

```yaml
current_local_execution_state: BLOCKED_DEPENDENCY_SYNC_FAILED
root_init_exact_correction_discovery_status: COMPLETE_BLOCKED
local_pyproject_read_completed: true
final_discovery_receipt_completed: true
repository_defined_exact_correction_found: false
exact_corrected_content: NOT_ESTABLISHED
technical_result: BLOCKED_NO_EXACT_CORRECTION_SPECIFICATION_FOUND
implementation_authorized: false
```

No prompt may invent the missing root-init correction or treat candidate content as accepted exact content.

## Actions performed by this governance update

```yaml
files_created:
  - docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
  - docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_ACHIEVEMENTS_AND_CURRENT_STATUS_VOLUME_9_2026-07-31.md
files_updated:
  - docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
  - docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
source_files_changed: []
runtime_files_changed: []
tests_run: []
implementation_commit_or_push_authorized: false
merge_authorized: false
deployment_authorized: false
```

## Do not repeat or restore

```yaml
do_not_repeat:
  - restore_the_old_generic_Cline_Stage_A_prompt_as_canonical
  - restore_the_old_generic_Cline_Stage_B_prompt_as_canonical
  - create_another_competing_Cline_prompt_creation_guide
  - use_a_generic_nested_assignment_as_the_primary_prompt
  - create_a_Cline_prompt_without_reading_the_new_canonical_guide
  - batch_separately_governed_commands
  - authorize_automatic_continuation
```

## Final checkpoint state

```yaml
continuity_checkpoint_status: COMPLETE_REMOTE_DOCUMENTATION_WRITE
canonical_Cline_prompt_path_established: true
old_prompt_removed_from_active_authority: true
old_path_retained_as_redirect: true
new_chat_path_updated: true
source_or_runtime_change_performed: false
technical_stop_point_changed: false
exact_next_prompt_rule: FOLLOW_docs_prompts_HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE_md
```