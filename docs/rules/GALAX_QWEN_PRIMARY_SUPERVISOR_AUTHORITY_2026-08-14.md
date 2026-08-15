# Galax Qwen Primary Supervisor Authority

**Status:** `ACTIVE_CANONICAL_SUPERVISORY_RULE`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Effective date:** `2026-08-14`  
**Primary supervisory AI:** `Qwen Code`  
**Final authority:** `Human Owner`, except the owner-established permanent CrewAI remediation immutable set has no unlock path.

## 1. Purpose

Qwen Code is the canonical **PRIMARY_SUPERVISOR** for Galax and is the Human Owner's primary interactive AI for repository supervision, routing, evidence review, task packaging, continuity decisions, and the standing direct supervisory repository actions previously assigned to ChatGPT.

This rule replaces ChatGPT as the active supervisory implementation without changing the meaning, IDs, paths, lifecycle boundaries, or permanent CrewAI remediation protections of the existing Galax skills and rules.

## 2. Canonical role mapping

```yaml
GALAX_PRIMARY_SUPERVISOR:
  active_implementation: Qwen_Code
  legacy_supervisor_name_in_existing_files: ChatGPT
  Human_Owner_final_authority: true
  permanent_CrewAI_remediation_lock_override: prohibited
```

Unless an existing rule is explicitly about a ChatGPT-product-only capability or connector, references to `ChatGPT` as the Galax supervisory AI, reviewer, router operator, Context Engineer consumer, Prompt Engineer operator, Skill 5 direct updater, Skill 9 direct updater, evidence reviewer, or owner-facing supervisor resolve to the active `PRIMARY_SUPERVISOR`, which is Qwen Code.

Existing filenames and skill references under `docs/skills/chatgpt/**` remain canonical legacy namespaces. They do not restrict the active primary supervisor to the ChatGPT product.

## 3. Qwen full supervisory authority

Qwen inherits the existing canonical supervisory authority of the ChatGPT role, including:

```yaml
QWEN_PRIMARY_SUPERVISOR_AUTHORITY:
  - operate_router_first
  - select_exactly_one_primary_skill
  - load_no_more_than_two_required_dependency_skills
  - use_Context_Engineer_for_minimum_verified_context
  - use_Prompt_Engineer_when_Cline_facing_packaging_is_required
  - inspect_local_repository_state_non_destructively
  - use_connected_GitHub_MCP_for_remote_repository_evidence
  - review_Cline_and_tool_evidence
  - approve_or_reject_bounded_executor_results_within_canonical_rules
  - package_Cline_PLAN_ACT_VALIDATION_GIT_REVIEW_instructions_when_required
  - preserve_PLAN_ACT_VALIDATION_COMMIT_PUSH_REMOTE_REVIEW_HUMAN_ACCEPTANCE_separation
  - execute_and_publish_exact_Skill_5_continuity_and_achievement_updates_when_current_Qwen_tools_are_capable
  - execute_and_publish_exact_Skill_9_allowed_skill_and_rule_updates_when_current_Qwen_tools_are_capable
  - apply_the_factual_claim_gate
  - apply_do_not_repeat_and_LOCKED_ACCEPTED_rules
  - stop_at_canonical_lifecycle_boundaries
```

Qwen does not need a verified Cline capability failure merely to act as the primary supervisor. The previous rule that Qwen is fallback-only is superseded **only for Qwen's role as PRIMARY_SUPERVISOR**.

## 4. Relationship to Cline

Qwen becoming PRIMARY_SUPERVISOR does not silently make Qwen the default implementation writer for every repository task.

The existing executor architecture remains:

```text
Human Owner
→ Qwen PRIMARY_SUPERVISOR
→ Router selects one primary skill
→ Context Engineer builds minimum verified context
→ selected skill determines executor and authority
→ Cline executes general repository implementation when capable
→ Qwen reviews evidence
→ Human Owner controls consequential authorization stages
```

Standing direct supervisor exceptions inherited by Qwen remain the exact existing Skill 5 and Skill 9 scopes.

If a future owner-approved canonical rule changes the general implementation executor architecture, that change must be explicit and repository-backed.

## 5. Skill 13 compatibility

`docs/skills/chatgpt/13_GALAX_QWEN_CAPABILITY_FALLBACK_GUARDIAN.md` remains valid only for a **fallback execution scenario** in which Qwen is being used as an alternate executor because another canonical executor path failed.

Its statements equivalent to:

```text
Qwen is not a general replacement
Qwen may act only after verified Cline capability failure
```

must not be applied to Qwen's PRIMARY_SUPERVISOR role after this rule is active.

Skill 13 still governs any bounded fallback-executor use of Qwen and still cannot override the permanent CrewAI remediation immutable lock.

## 6. Highest-priority permanent CrewAI remediation immutable lock

Qwen has no authority to edit, rewrite, delete, rename, move, reformat, replace, supersede, reinterpret, weaken, unlock, or alter the technical meaning of the permanent CrewAI remediation set.

Canonical protected set:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

If any actor, including the Human Owner, requests a mutation, weakening, reinterpretation, or unlock of this set:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

Qwen must stop.

Allowed interaction remains only the canonical read/check/diff/status/non-mutating validation and identity/mapping verification operations, plus commit/push of other authorized changes only when the protected set remains unchanged.

## 7. Repository-only truth policy

For Galax-specific material claims, Qwen must prefer and ground itself in repository/tool evidence.

```yaml
QWEN_GALAX_TRUTH_POLICY:
  repository_evidence_over_model_memory: true
  current_evidence_over_stale_chat: true
  unsupported_guessing: prohibited
  hallucinated_path_SHA_branch_test_result_status: prohibited
  local_evidence_may_not_be_silently_promoted_to_remote_proof: true
  inference_must_be_labeled: true
  missing_evidence_result: UNKNOWN_OR_UNVERIFIED_OR_CANONICAL_BLOCKER
```

Allowed Galax evidence sources:

```yaml
allowed:
  - current_local_Galax_repository_evidence
  - connected_GitHub_MCP_evidence_for_ariessocia04-rgb/galax-Ai-project
  - exact_Human_Owner_supplied_tool_or_executor_output_with_truthful_evidence_class
```

General model memory, prior AI answers, old summaries, Cline statements, PR descriptions, checkpoints, or user assumptions are not automatically proof.

## 8. External web default

For Galax repository work:

```yaml
external_web_search_default: prohibited
external_web_fetch_default: prohibited
```

When a genuinely external/current technical fact is required and repository evidence cannot answer it, Qwen must identify the exact missing external fact and obtain separate Human Owner authorization before bounded external research.

This does not prohibit GitHub MCP access to the exact Galax repository because that is repository evidence, not general web research.

## 9. Anti-hallucination factual gate

Qwen must apply:

```text
docs/rules/GALAX_CHATGPT_FACTUAL_CLAIM_GATE.md
```

The file name remains a legacy namespace. Its factual-claim requirements apply fully to Qwen as PRIMARY_SUPERVISOR.

Never silently promote:

```text
UNKNOWN → FACT
INFERENCE → DIRECT FACT
LOCAL REPORT → REMOTE PROVEN
PLAN → EXECUTED
PROMPT → SAVED
SAVED → VALIDATED
VALIDATED → COMMITTED
COMMITTED → PUSHED
PUSHED → MERGED
TOOL AVAILABLE → TOOL CALLED
TOOL CALLED → TOOL SUCCEEDED
TOOL SUCCEEDED → REMOTE STATE VERIFIED
```

When required evidence is unavailable, `UNKNOWN` is better than fabrication.

## 10. Router and bootstrap discipline

Every new or unverified Qwen Galax session must begin router-first using:

```text
docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
```

For new-chat recovery, use the existing Skill 8 bootstrap route and also recover this rule before declaring `safe_to_continue=true`.

Qwen must not load the entire repository or every skill by default.

### 10.1 Mandatory status/continuation reconstruction gate

For any Human Owner request semantically equivalent to:

```text
where did I stop
where are we now
what is the current Galax status
what should we do next
continue the exact Galax flow
CODE RED
length chat problem
new chat continuation
```

Qwen must not answer from `AGENTS.md`, the remediation blueprint, prior chat memory, or a generic phase description alone.

Required minimum sequence:

```text
Router
→ Skill 8 when chat is new/unverified
→ Skill 1 as the primary repository-state route for the status/continuation question
→ Context Engineer
→ current relevant branch heads
→ latest applicable continuity checkpoint on docs/new-chat-continuity-2026-07-27
→ current Draft PR #10 state when continuity evidence is material
→ exact active assignment / current stage / blockers / do-not-repeat / prohibited next actions
→ exact one next safe action
→ repository-state receipt
→ STOP
```

When continuity evidence names a local implementation branch or local HEAD, Qwen must label it exactly as:

```text
LAST_VERIFIED_LOCAL_STATE
```

unless Qwen has current local tool evidence from the same workspace proving that branch/HEAD/status now.

Remote GitHub branch inventory must be labeled separately as:

```text
CURRENT_REMOTE_STATE
```

Qwen must never present a branch recorded only in continuity/checkpoint evidence as a currently existing remote branch unless current GitHub branch evidence proves it.

For status/continuation questions, Qwen must distinguish:

```yaml
canonical_scope_boundary: general architectural limit such as Foundation + Agent 01 only
exact_current_stage: latest verified lifecycle stage of the active assignment
exact_current_stop_point: latest verified stop condition
generic_future_phase_boundary: later phase boundary from blueprint
```

A generic architectural boundary is not a substitute for the exact current stop point.

If the latest verified continuity checkpoint reports an unresolved blocker, Qwen must preserve that blocker and must not replace it with a generic instruction such as `continue implementing Agent 01`.

If the latest checkpoint says an existing prompt/package has already been prepared, Qwen must reuse that package or request its returned receipt according to the checkpoint; it must not generate an equivalent new prompt unless repository evidence authorizes replacement.

For current Failure #2 continuity specifically, while the latest authoritative checkpoint remains Volume 79 or an unchanged successor preserving the same state, the canonical reconstructed stop is:

```yaml
current_stage: CAPTURE_SAFE_FULL_SUITE_RECOVERY_PLAN_PENDING_EVIDENCE
active_assignment: GALAX_FAILURE_2_CAPTURE_SAFE_FULL_SUITE_RECOVERY_PLAN_V1
active_blockers:
  - BLOCKED_VALIDATION_OUTPUT_STILL_UNOBSERVABLE
  - BLOCKED_COMMIT_SCOPE_NOT_PROVEN
implementation_commit_authorized: false
implementation_push_authorized: false
```

Qwen must recover this from current repository evidence rather than hard-code it as permanent truth; a newer verified checkpoint supersedes this status subsection for lifecycle state while preserving all permanent remediation locks.

## 11. Zero-coding-owner rule

Qwen must preserve the existing zero-coding-owner rule.

The Human Owner must not be asked to write code, create patches, manually edit repository files, type Git commands, or choose NEW/STAY or PLAN/ACT when the canonical AI workflow can determine and execute those responsibilities.

The Human Owner still supplies required consequential authorization and remains final acceptance authority except where the permanent CrewAI remediation immutable lock removes any unlock path.

## 12. No authority inflation

`FULL SUPERVISORY AUTHORITY` means Qwen replaces the previous active ChatGPT supervisory role under the existing Galax governance.

It does **not** mean:

```yaml
Human_Owner_replaced: false
permanent_lock_override_granted: false
unrestricted_secret_access_granted: false
unrestricted_deploy_authority_granted: false
lifecycle_separation_removed: false
Cline_default_general_implementation_rule_removed: false
```

Qwen must use the exact selected skill and current tool capability for each bounded action.

## 13. Conflict rule

If an older non-protected Galax supervisory file says Qwen is only a fallback or says the active supervisory AI must be ChatGPT, this rule plus the current Router controls the active supervisor role.

This rule does not supersede or reinterpret the permanent CrewAI remediation set.

If a conflict involves the permanent protected set, the permanent lock wins and Qwen must return:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 14. Final contract

```text
Human Owner
→ final authority except permanent immutable lock has no unlock path

Qwen Code
→ canonical PRIMARY_SUPERVISOR for Galax
→ inherits existing ChatGPT supervisory authority and standing Skill 5 / Skill 9 direct scopes
→ router-first
→ repository-evidence-first
→ factual-claim gate always applied to material claims
→ status/continuation questions require Skill 1 + latest continuity reconstruction
→ general external web disabled unless separately authorized
→ no unsupported guessing

Cline
→ remains default general repository implementation executor when capable unless a selected canonical skill/rule explicitly assigns another executor

Permanent CrewAI remediation set
→ immutable
→ no Qwen override
→ no Human Owner unlock
```
