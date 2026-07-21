# Galax AI Repository Instructions for External Development Contributors

**Status:** `RESEARCH_BRANCH_ENTRYPOINT_NOT_RUNTIME_AUTHORIZATION`  
**Current scope:** Governance Foundation and Agent 01, Phases 0–4 only.  
**Agents 02–15:** disabled.  
**Merge/deployment:** prohibited.

## Required reading order

Before planning, editing, testing, reviewing, or invoking a tool:

1. `README.md`
2. all applicable files under `docs/rules/`
3. current readiness and supersession records named by `README.md`
4. `docs/research/ai-tools/AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
5. `docs/research/ai-tools/AI_CONTRIBUTOR_COMMAND_DESIGN_SURVEY_2026-07-21.md`
6. `docs/prompts/external-ai-contributors/README.md`
7. `docs/prompts/external-ai-contributors/SHARED_EXECUTION_PROTOCOL.md`
8. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_WORK_ASSIGNMENT_PLAN.md`
9. `docs/prompts/external-ai-contributors/CONTROLLED_TASK_PACKET_TEMPLATE.md`
10. the exact selected role charter under `docs/prompts/external-ai-contributors/`
11. the authorized implementation prompt for the current task scope

The canonical external-contributor package is:

```text
docs/prompts/external-ai-contributors/
```

Any conflicting or duplicate external-contributor instruction outside that package is non-canonical unless a newer explicit supersession record says otherwise.

## Repository truth

```yaml
repository: ariessocia04-rgb/galax-Ai-project
framework_target: CrewAI_1.15.4
current_runtime_agents_enabled: 0
current_implementation_scope: Foundation_and_Agent_01_only
research_base_branch: agent/agent-01-tool-inspection
approved_research_head: 897ded61c5edea4e6153112361c6e929f5a84294
implementation_branch: implementation/foundation-agent-01
```

Never use `main` as a fallback when another base branch or SHA is required.

## External contributor boundary

External development tools are not Galax production agents and may not control the CrewAI Flow.

```yaml
inside_CrewAI_runtime: false
may_enable_Agents_02_to_15: false
may_change_architecture_without_authorization: false
may_merge: false
may_deploy: false
```

## Universal safety rules

```yaml
one_task_one_active_source_writer: required
parallel_overlapping_writers: prohibited
reviewer_source_write: prohibited
direct_main_write: prohibited
force_push: prohibited
automatic_merge: prohibited
workflow_or_secret_change: prohibited_without_separate_authorization
account_rotation_to_evade_quota: prohibited
claims_without_retrieved_or_executed_evidence: prohibited
```

Do not edit unless a completed controlled task packet provides the exact repository, branch, starting SHA, allowed paths, protected paths, tests, limits, stop conditions, and human approver.

## Required work sequence

```text
read canonical rules
→ verify repository, branch, SHA, dirty state, and task lock
→ return a bounded plan
→ wait for approval when required
→ perform the minimum authorized work
→ run every required test
→ inspect the complete diff or review artifact
→ return the shared structured handoff
→ stop
```

Do not provide hidden chain-of-thought. Provide concise decision rationale, actions, evidence, test results, blockers, and the next safe action.
