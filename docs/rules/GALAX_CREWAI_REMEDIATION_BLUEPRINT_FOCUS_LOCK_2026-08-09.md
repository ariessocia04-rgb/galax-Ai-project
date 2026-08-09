# Galax CrewAI Remediation Blueprint Focus Lock — 2026-08-09

**Status:** `ACTIVE_CANONICAL_DEVELOPMENT_FOCUS_LOCK`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Applies to:** ChatGPT, Cline, Codex, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, GitHub Copilot, Claude Code, Jules, and every repository-aware AI or human-supervised development workflow  
**Technical center:** `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`  
**Existing narrow supersession preserved:** `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`  
**Runtime effect:** none  
**Source/test change authorized by this rule:** false  
**Final authority for governance-rule enhancements:** Human Owner

## 1. Purpose

Galax development is locked to the CrewAI 1.15.4 remediation blueprint as the center of technical development.

Every technical development, implementation, validation, compatibility, security, test, model, tool, gateway, sandbox, permission, memory, knowledge, Flow, agent, or infrastructure task must map directly to an exact requirement, remedy, gate, compatibility item, or agent boundary in:

```text
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
```

No unrelated technical work may be introduced merely because a tool, runtime, contributor, package, executable, library, platform, or possible improvement exists.

## 2. Existing Foundation narrow supersession must remain intact

This focus lock does not reactivate the older Agent 01 pattern that the active Foundation execution contract already superseded.

The following existing narrow correction remains controlling for Foundation / Agent 01:

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
RepositoryPreflightTool_invoked_by_Agent_01: false
Agent_01_direct_tool_calls: 0
engineering_manager_tools: []
result_as_answer_for_this_Foundation_path: prohibited
Flow_invokes_preflight_before_Agent_01: true
```

This narrow supersession comes only from:

```text
docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

No assistant may invent another supersession or use this focus lock to widen that exception.

## 3. Mandatory blueprint mapping gate

Before any new technical action is proposed, assigned, executed, validated, or saved, the responsible assistant must establish:

```yaml
GALAX_CREWAI_BLUEPRINT_MAPPING_GATE_V1:
  blueprint_path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  exact_blueprint_section_or_requirement:
  exact_current_remedy_or_gate:
  current_task_directly_required_by_blueprint: true | false
  Foundation_Agent01_narrow_supersession_applicable: true | false
  governance_only_enhancement: true | false
  changes_blueprint_technical_meaning: false
  adds_unrelated_technical_scope: false
  status: PASS | BLOCKED
```

A technical task may proceed only when:

```text
current_task_directly_required_by_blueprint = true
```

or when it is a governance-only enhancement allowed by Section 5.

If neither condition is satisfied, return exactly:

```text
BLOCKED_OUTSIDE_CREWAI_REMEDIATION_BLUEPRINT
```

and stop.

## 4. Technical plan freeze

The CrewAI remediation blueprint is the frozen technical development center for the current Galax build.

Repository-aware assistants must not:

- rewrite, replace, broaden, narrow, reinterpret, or silently supersede the blueprint;
- add a new technical roadmap that competes with the blueprint;
- insert unrelated frameworks, runtimes, tools, contributors, services, packages, or architectural goals;
- conduct open-ended executable or PATH capability hunts that are not directly required by an exact blueprint remedy or gate;
- turn a Cline/editor limitation into a new Galax technical objective;
- use repository cleanup, convenience, experimentation, or tooling availability to redirect the development center;
- change CrewAI version, process, runtime architecture, role boundaries, tools, models, gateways, memory, knowledge, security, sandbox, or test strategy outside an exact blueprint requirement and the existing narrow Foundation supersession;
- treat an external development contributor as a Galax CrewAI Agent 01–15;
- continue to a new technical stage merely because the previous stage was blocked.

When a proposed action would change the technical meaning of the blueprint, return:

```text
BLOCKED_BLUEPRINT_MUTATION_PROHIBITED
```

and stop.

## 5. Only governance/control enhancements may be added outside the blueprint

The Human Owner may enhance only supervisory and repository-control rules that help ChatGPT, Cline, and the repository follow the frozen technical plan more accurately.

Allowed governance-only enhancement areas:

```yaml
allowed_governance_enhancements:
  - ChatGPT routing and repository-supervision rules
  - ChatGPT context-selection and evidence-preservation rules
  - Cline prompting, permission, scope, and stop-condition rules
  - repository governance, continuity, evidence, lock, and recovery rules
  - stricter auto-block rules for work outside the blueprint
  - stronger protection against duplicate, stale, unrelated, or unauthorized work
```

Every governance-only enhancement must satisfy all of:

```yaml
must_not:
  - modify the CrewAI remediation blueprint content
  - modify the blueprint technical meaning
  - create a competing development plan
  - modify Galax runtime behavior by documentation alone
  - authorize source or test edits by itself
  - add unrelated technical objectives
  - unlock LOCKED_ACCEPTED work
  - authorize implementation commit, push, merge, or deployment
```

A governance enhancement that violates any of these conditions returns:

```text
BLOCKED_GOVERNANCE_ENHANCEMENT_CHANGES_TECHNICAL_PLAN
```

## 6. Human Owner boundary

The Human Owner remains the final authority for governance-rule enhancements and action approvals, but ordinary development instructions do not authorize mutation of the frozen CrewAI remediation blueprint.

Under this active focus lock:

```yaml
Human_Owner_may_enhance_ChatGPT_rules: true
Human_Owner_may_enhance_Cline_rules: true
Human_Owner_may_enhance_repository_governance_rules: true
Human_Owner_may_directly_mutate_blueprint_through_ordinary_development_instruction: false
assistant_may_mutate_blueprint: false
Cline_may_mutate_blueprint: false
other_contributor_may_mutate_blueprint: false
```

This focus lock itself may be strengthened to improve enforcement, but must not be weakened to authorize unrelated technical development or silent blueprint mutation.

## 7. Scope test for every next action

Before recommending a next technical action, ask only:

```text
Which exact CrewAI remediation blueprint requirement does this action implement, prove, validate, secure, or unblock?
```

If no exact answer exists, the action is outside scope.

Examples of actions that must be blocked unless an exact blueprint requirement specifically requires them:

```text
random runtime or executable discovery
open-ended PATH checks
unrelated package installation
new contributor qualification
new framework experiments
unrelated infrastructure setup
feature development outside the current blueprint gate
cleanup that is not required to preserve or execute the blueprint
```

Repository/editor mechanics may be solved only as the minimum means required to complete an already-authorized blueprint task. The mechanic itself must not become a new development track.

## 8. Required behavior for ChatGPT and Cline

ChatGPT must:

```text
fresh-read repository authority
→ identify the exact blueprint mapping
→ preserve the active Foundation narrow supersession when applicable
→ block unrelated work
→ issue only the smallest blueprint-aligned Cline task
→ stop at the task boundary
```

Cline must:

```text
accept only the exact blueprint-aligned assignment
→ perform only allowlisted reads/actions
→ reject or report unrelated discoveries without acting on them
→ never create a new remediation track
→ stop when the bounded objective is complete or blocked
```

Neither ChatGPT nor Cline may use a tool limitation as authority to expand Galax technical scope.

## 9. Compatibility and safety rule

CrewAI compatibility claims must be based on the exact blueprint requirements plus the active Foundation narrow supersession where applicable.

A task is not CrewAI-compatible merely because it is useful for coding or repository manipulation.

External development tooling is supporting infrastructure only. It is not part of the Galax CrewAI runtime unless the blueprint explicitly defines the corresponding runtime requirement.

## 10. Stop conditions

Stop immediately when any of the following is true:

```yaml
no_exact_blueprint_mapping: BLOCKED_OUTSIDE_CREWAI_REMEDIATION_BLUEPRINT
proposed_blueprint_mutation: BLOCKED_BLUEPRINT_MUTATION_PROHIBITED
governance_change_alters_technical_plan: BLOCKED_GOVERNANCE_ENHANCEMENT_CHANGES_TECHNICAL_PLAN
new_unrelated_technical_track_detected: BLOCKED_OUTSIDE_CREWAI_REMEDIATION_BLUEPRINT
existing_Foundation_narrow_supersession_would_be_broken: BLOCKED_SUPERSESSION_CONFLICT
```

No automatic fallback to another technical task is allowed after one of these blockers.

## 11. Final focus contract

```text
CrewAI 1.15.4 remediation blueprint
+ existing narrow Foundation/Agent 01 supersession only where already canonical
→ exact current blueprint gate
→ one bounded implementation or validation action
→ evidence
→ Human Owner decision
→ next exact blueprint gate
```

```yaml
technical_development_center: CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20
unrelated_technical_work: AUTO_BLOCK
blueprint_mutation: PROHIBITED
new_competing_plan: PROHIBITED
governance_only_enhancements: ALLOWED_WITHOUT_TECHNICAL_PLAN_CHANGE
source_changed_by_this_rule: false
tests_changed_by_this_rule: false
runtime_changed_by_this_rule: false
CrewAI_version_changed_by_this_rule: false
Foundation_narrow_supersession_preserved: true
```
