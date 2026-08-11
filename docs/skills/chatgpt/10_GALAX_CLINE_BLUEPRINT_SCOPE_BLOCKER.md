```yaml
skill_reference: $galax-cline-blueprint-scope-blocker
skill_id: GALAX-SKILL-10
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 10: Galax Cline Blueprint Scope Blocker

## 1. Purpose

Skill 10 is a mandatory scope gate only for real active CrewAI remediation-blueprint implementation tasks.

It prevents Cline from executing CrewAI implementation that cannot be traced to the exact active blueprint/assignment/branch/HEAD and authorized scope.

It is NOT a generic blocker against Cline executing governance, documentation, router, ChatGPT skill, Context Engineer, Prompt Engineer, continuity, or achievement changes.

## 2. PASS condition

Return:

```text
PASS_CLINE_BLUEPRINT_ONLY
```

only when all are proven for the proposed CrewAI implementation task:

```yaml
repository_matches: true
active_blueprint_verified: true
active_assignment_verified: true
branch_verified: true
HEAD_verified: true
proposed_action_traces_to_active_blueprint: true
LOCKED_ACCEPTED_preserved: true
completed_work_not_repeated: true
scope_is_bounded: true
```

Otherwise return the exact factual blocker.

## 3. Non-blueprint Cline work

When the task is governance, ChatGPT skills/router, Context Engineer, Prompt Engineer, supervisory rules, continuity/achievement, or ordinary documentation:

```text
NOT_A_SKILL_10_BLUEPRINT_TASK
```

Do not block Cline merely because that work is not part of the CrewAI remediation blueprint.

The Router/selected skill/Skill 2/Prompt Engineer still must provide exact authority, scope, mode, prohibitions, and stop condition.

## 4. Executor rule

Cline is the default repository executor whenever capable.

If ChatGPT attempts repository execution while Cline is capable:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Skill 12 remains the only verified owner-authorized fallback exception.

## 5. Final contract

```text
CrewAI blueprint implementation → Skill 10 gate required.
Non-blueprint authorized Cline work → Skill 10 does not block it.
```
