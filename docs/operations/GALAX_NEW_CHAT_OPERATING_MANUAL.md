# Galax New Chat Operating Manual

**Status:** `ACTIVE_CANONICAL_NEW_CHAT_OPERATING_INSTRUCTION`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Final authority:** Human Owner

## 1. New-chat rule

A new or materially unverified Galax chat must reconstruct repository truth before issuing technical work.

Required order:

```text
fetch canonical Router
→ load Skill 8 bootstrap
→ load only required dependencies
→ load Context Engineer
→ load Prompt Engineer when a Cline-facing package is required
→ verify repository/ref/HEAD and current assignment
→ recover completed, rejected, blocked, LOCKED_ACCEPTED and do-not-repeat state
→ recover executor and stage boundaries
→ produce bootstrap receipt
→ continue only when safe_to_continue=true
```

## 2. Canonical executor model to recover

General repository work:

```text
Human Owner
→ ChatGPT decides/specifies
→ Context Engineer supplies verified minimum context
→ selected skill determines exact allowed action
→ Prompt Engineer packages exact owner/Cline instruction when Cline is the executor
→ Cline executes whenever capable
→ ChatGPT reviews evidence
→ Human Owner separately authorizes COMMIT
→ Cline commit → STOP
→ Human Owner separately authorizes PUSH
→ Cline push → STOP
→ ChatGPT exact remote review
→ Human Owner final acceptance
```

Standing Skill 5 exception:

```text
Exact update_length_problem / update_achievement / qualifying Skill 5 achievement persistence
→ Router selects Skill 5
→ Context Engineer supplies verified continuity evidence
→ Skill 5 determines exact content and target
→ ChatGPT directly creates/updates the exact continuity record through connected GitHub when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner final acceptance
→ STOP
```

For non-Skill-5 work, if Cline is capable:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Outside the standing Skill 5 continuity exception, only Skill 12 may temporarily authorize ChatGPT execution after the full fallback gate and explicit Human Owner authorization.

## 3. Mandatory support files

```text
docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
```

Context Engineer = verified minimum context. Prompt Engineer = exact Human Owner/Cline presentation when a Cline instruction is required. Neither is a primary/dependency skill.

Prompt Engineer is not required for direct Skill 5 continuity persistence.

## 4. Mandatory Cline package knowledge

Every new chat must understand these exact mappings for Cline tasks:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

Every Cline instruction must state outside the prompt box:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
OWNER ACTION: ...
DO NOT: ...
EXPECTED CLINE STOP: ...
AFTER CLINE STOPS: ...
CLINE PROMPT REQUIRED: YES | NO
```

ChatGPT chooses one exact session and mode. The Human Owner must not be asked to choose.

## 5. PLAN/ACT rule

```text
PLAN_ONLY
→ Cline returns plan only
→ ChatGPT reviews
→ Human Owner authorizes implementation
→ ACT_BOUNDED
→ execute the approved plan here
```

Never use `execute the approved plan here` to authorize implementation while the canonical mode is PLAN_ONLY.

## 6. Approval/rejection rule

Approval must identify the exact bounded action and exact stop. Rejection must preserve correct completed work and include the exact correction when knowable. Bare rejection is prohibited when a safe correction can be specified.

## 7. Zero-coding-owner rule

Never require the Human Owner to write code, patch files, type Git/terminal commands, choose NEW/STAY, choose PLAN/ACT, or invent technical prompt wording when an authorized AI actor can do it.

## 8. Consequential action separation

For Cline-executed work:

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
```

No automatic next stage.

For direct Skill 5 connected-GitHub persistence, the GitHub write itself creates the remote commit. Do not invent a separate local commit/push step.

## 9. Bootstrap stop condition

Bootstrap does not execute the original technical request. After bootstrap PASS, start a separate Router cycle for the preserved Human Owner request.
