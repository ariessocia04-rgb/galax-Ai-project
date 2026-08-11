```yaml
skill_reference: $galax-owner-direct-repository-update-guardian
skill_id: GALAX-SKILL-09
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 9: Galax ChatGPT Skill and Rule Update Guardian

## 1. Purpose

Skill 9 is the standing ChatGPT direct-update authority for **ChatGPT skills and repository rules only**, subject to the permanent CrewAI remediation immutable lock.

It does not grant ChatGPT broad repository-writing authority.

## 2. Exact standing ChatGPT scope

ChatGPT may directly edit/update rule content only in these path classes:

```yaml
SKILL_9_CHATGPT_DIRECT_SCOPE:
  allowed_path_prefixes:
    - docs/skills/chatgpt/
    - docs/rules/
  allowed_actions:
    - edit_existing_skill_rule_content
    - update_existing_skill_rule_content
    - correct_conflicting_skill_rule_content
    - keep_router_and_skill_rules_consistent_when_router_is_under_docs/skills/chatgpt/
  executor: ChatGPT
  publisher: ChatGPT_connected_GitHub_app_when_available
  Cline_required: false
```

This includes the ChatGPT skill Router because its canonical file is under `docs/skills/chatgpt/`.

## 3. Permanent CrewAI remediation exclusion

Path-prefix permission NEVER overrides the permanent CrewAI remediation lock.

Canonical permanent lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Skill 9 must not edit, update, correct, weaken, supersede, unlock, or replace:

```yaml
PERMANENT_SKILL_9_EXCLUSIONS:
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
  - any_new_or_existing_rule_whose_change_would_alter_the_locked_CrewAI_remediation_technical_meaning
```

This prohibition applies even when the Human Owner asks Skill 9 to edit/unlock the protected remediation set.

Required result:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

No Skill 9 direct-write exception exists for those protected artifacts or their technical meaning.

## 4. Other exact exclusions

Skill 9 does **not** authorize ChatGPT direct writes to:

```yaml
prohibited_direct_targets:
  - README.md
  - AGENTS.md
  - docs/operations/**
  - docs/plan/**
  - docs/research/**
  - docs/prompts/**
  - docs/sources/**
  - src/**
  - tests/**
  - pyproject.toml
  - uv.lock
  - dependency_or_lock_files
  - .github/workflows/**
  - secrets
  - runtime_or_production_data
```

Exception: exact Skill 5 continuity targets are governed by Skill 5, not Skill 9.

The permanent remediation lock is stricter than this ordinary exclusion list and cannot be overridden by another skill.

## 5. Required execution chain

```text
Human Owner requests an exact skill/rule correction or update
→ Router selects Skill 9
→ Context Engineer supplies minimum verified repository evidence
→ first check permanent CrewAI remediation lock
→ if target or semantic effect collides with permanent remediation set: BLOCK
→ otherwise verify target is inside docs/skills/chatgpt/** or docs/rules/**
→ ChatGPT directly edits/updates the exact allowed skill/rule file through the connected GitHub app when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner remains final acceptance authority for that allowed change
→ stop
```

Prompt Engineer Cline packaging is not required for a direct Skill 9 update because Cline is not the executor for this exact standing scope.

## 6. GitHub publication semantics

When ChatGPT uses the connected GitHub contents API:

```yaml
creates_remote_commit_directly: true
separate_local_commit_step: false
separate_push_step: false
```

ChatGPT must report the actual remote result truthfully.

## 7. Relationship to Cline-default execution

Outside the exact Skill 9 path scope and exact Skill 5 continuity scope:

```text
Cline capable
→ Cline executes.
```

Cline also cannot edit the permanent CrewAI remediation set; that is blocked by Skill 6 and the permanent lock rule.

## 8. Relationship to Skill 12

Skill 9 is a standing non-fallback direct ChatGPT exception for allowed skills/rules only.

Skill 12 remains the only way ChatGPT may directly execute other repository work after its separate verified gate and explicit Human Owner authorization.

Skill 12 cannot override the permanent CrewAI remediation lock.

## 9. Final contract

```text
ChatGPT standing repository jobs:
1. Skill 5 → update length problem in repo.
2. Skill 9 → edit/update ChatGPT skills and rules only.
3. Skill 5 → update achievement in repo.

Permanent CrewAI remediation blueprint / lock / canonical narrow supersession:
→ never editable by Skill 9.
→ never unlockable, including by Human Owner.
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK.

Everything else:
→ Cline-default when capable.
→ Skill 12 only for separately proven and owner-authorized fallback.
```
