# Galax AI Repository Instructions for External Coding Assistants

**Status:** `ACTIVE_CONTROLLED_TRIAL_INSTRUCTIONS`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Final authority:** Human Owner

## 1. Repository identity

```yaml
protected_branch: main
framework_target: CrewAI_1.15.4
python_target: ">=3.10,<3.14"
current_scope: governance_foundation_and_Agent_01_only
Agents_02_to_15: prohibited_without_separate_live_authority
production_ready: false
```

Stop with `BLOCKED_REPOSITORY_STATE_MISMATCH` when the assigned repository/branch/expected SHA materially does not match.

## 2. Canonical authority order

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
→ docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
→ Context Engineer
→ Prompt Engineer
→ exact selected skill/dependencies
→ active technical contract/blueprint when relevant
→ exact assignment and current GitHub evidence
→ historical records
→ old chat memory last
```

Repository evidence overrides stale conversation memory.

## 3. Canonical execution model

```text
Human Owner
→ ChatGPT decides/specifies WHAT should be done
→ Router selects exactly one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill fixes exact scope/mode/permissions
→ Prompt Engineer packages exact Human Owner + Cline instruction
→ Cline executes whenever capable
→ Cline edits/saves authorized scope
→ Cline runs only separately authorized validation
→ ChatGPT reviews evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
→ Human Owner authorizes COMMIT
→ Cline commit
→ STOP
→ Human Owner separately authorizes PUSH
→ Cline push
→ STOP
→ ChatGPT reviews exact remote diff
→ Human Owner final acceptance
```

Cline is the default repository executor whenever capable, including governance, ChatGPT skills, router, Context Engineer, Prompt Engineer, continuity/achievement, documentation, and CrewAI implementation.

Cline may mechanically apply exact ChatGPT/Human-Owner-authored governance content but may not independently alter its meaning or broaden scope.

If ChatGPT attempts takeover while Cline is capable:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 4. Skill 12 fallback

ChatGPT direct execution is allowed only after:

- exact Cline limitation/repeated material mismatch/verified blocker is proven;
- ChatGPT exact current capability is proven;
- Human Owner explicitly authorizes exact fallback stages;
- LOCKED_ACCEPTED, scope, and writer-conflict gates pass;
- Router selects Skill 12 and the fallback gate returns PASS.

A single Cline mistake is not enough.

After verified fallback work, Cline resumes from that repository truth and must not redo/revert/overwrite it without new Human Owner authority.

## 5. Context Engineer

Canonical path:

`docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md`

Context Engineer preserves minimum verified repository/task context, executor identity, branch/SHA, assignment, locks, completed work, do-not-repeat, evidence class, and Cline session continuity. It does not route, approve, execute, or mutate files.

## 6. Prompt Engineer

Canonical path:

`docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md`

Prompt Engineer is mandatory whenever a Human Owner/Cline prompt package is required.

Every package must state outside the prompt box:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
OWNER ACTION: <exact action>
DO NOT: <exact prohibitions>
EXPECTED CLINE STOP: <exact stop>
AFTER CLINE STOPS: <exact return evidence>
CLINE PROMPT REQUIRED: YES | NO
```

ChatGPT chooses exactly one session and one mode. Do not ask the Human Owner to decide.

Exact mode mapping:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

## 7. PLAN/ACT discipline

```text
PLAN_ONLY
→ plan only
→ ChatGPT review
→ Human Owner authorization
→ ACT_BOUNDED
→ execute the approved plan here
```

Do not execute during PLAN_ONLY.

## 8. CrewAI implementation gate

For active CrewAI remediation-blueprint implementation, Skill 2 must use Skill 10 and require `PASS_CLINE_BLUEPRINT_ONLY` before issuing the real implementation task.

Skill 10 does not block authorized non-blueprint governance/continuity/documentation Cline work merely because it is not CrewAI blueprint implementation.

## 9. Approval/rejection discipline

Approvals must identify the exact bounded action and stop condition. Rejections must preserve correct completed work and provide the exact correction when knowable. Bare rejection is prohibited when a safe correction can be specified.

## 10. Human Owner zero-coding rule

Never require the Human Owner to write code, manually patch repository files, type terminal/Git commands, choose implementation syntax, choose NEW/STAY, choose PLAN/ACT, or invent prompt/rejection wording when an authorized AI actor can do it.

## 11. Consequential-stage separation

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
MERGE ≠ DEPLOY
```

No automatic next stage. No force push/history rewrite. No merge or deployment without separate Human Owner authorization.

## 12. CODE RED

When CODE RED/continuity recovery is triggered, reconstruct current repository-backed state and do not ask the Human Owner to repeat repository history that can be verified. Preserve this Cline-default execution model, Context Engineer, Prompt Engineer, fallback rule, locks, and do-not-repeat state.
