```yaml
skill_reference: $galax-owner-direct-repository-update-guardian
skill_id: GALAX-SKILL-09
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 9: Galax ChatGPT Skill and Rule Update Guardian

## 1. Purpose

Skill 9 is the standing ChatGPT direct-update authority for **ChatGPT skills and repository rules only**.

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

## 3. Exact exclusions

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

## 4. Required execution chain

```text
Human Owner requests an exact skill/rule correction or update
→ Router selects Skill 9
→ Context Engineer supplies minimum verified repository evidence
→ Skill 9 verifies the target is inside docs/skills/chatgpt/** or docs/rules/**
→ ChatGPT directly edits/updates the exact skill/rule file through the connected GitHub app when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner remains final acceptance authority
→ stop
```

Prompt Engineer Cline packaging is not required for a direct Skill 9 update because Cline is not the executor for this exact standing scope.

## 5. GitHub publication semantics

When ChatGPT uses the connected GitHub contents API:

```yaml
creates_remote_commit_directly: true
separate_local_commit_step: false
separate_push_step: false
```

ChatGPT must report the actual remote result truthfully.

## 6. Relationship to Cline-default execution

Outside the exact Skill 9 path scope and exact Skill 5 continuity scope:

```text
Cline capable
→ Cline executes.
```

ChatGPT must not use Skill 9 to take over source, tests, documentation outside the allowed path classes, dependencies, workflows, implementation work, merge, or deployment.

## 7. Relationship to Skill 12

Skill 9 is a standing non-fallback direct ChatGPT exception for skills/rules only.

Skill 12 remains the only way ChatGPT may directly execute other repository work after its separate verified gate and explicit Human Owner authorization.

## 8. Final contract

```text
ChatGPT standing repository jobs:
1. Skill 5 → update length problem in repo.
2. Skill 9 → edit/update ChatGPT skills and rules only.
3. Skill 5 → update achievement in repo.

Everything else:
→ Cline-default when capable.
→ Skill 12 only for separately proven and owner-authorized fallback.
```
