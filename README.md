# Galax AI Project

Galax AI is being designed as a fact-checked, strictly sequential CrewAI multi-agent software-development assistant system.

## Current readiness

```yaml
production_ready: false
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
Foundation_Agent01_Flow_contract: ACTIVE_CANONICAL
CODE_RED_protocol: ACTIVE_CANONICAL
ChatGPT_skill_router: ACTIVE_CANONICAL
ChatGPT_Cline_execution_role_separator: ACTIVE_CANONICAL
Context_Engineer: ACTIVE_CANONICAL
Prompt_Engineer: ACTIVE_CANONICAL
```

Do not activate or implement Agents 02–15 without separate live authority. Repository evidence overrides stale chat memory.

## Canonical governance records

Read as applicable:

1. `AGENTS.md`
2. `docs/operations/CODE_RED.md`
3. `docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md`
4. `docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md`
5. `docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md`
6. `docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md`
7. exact selected skill and required dependencies
8. active CrewAI contracts/blueprints only when technically relevant
9. exact current branch/HEAD/assignment/evidence

## Canonical capability-first workflow

```text
Human Owner
→ ChatGPT determines WHAT should be done
→ Router selects exactly one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines exact authority/scope/mode
→ Prompt Engineer creates exact owner-facing + Cline-facing package
→ Cline executes whenever capable
→ Cline edits/saves only authorized scope
→ Cline runs only separately authorized validation
→ ChatGPT reviews evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
→ Human Owner authorizes COMMIT
→ Cline commit
→ STOP
→ Human Owner separately authorizes PUSH
→ Cline push
→ STOP
→ ChatGPT independently reviews exact remote diff
→ Human Owner final acceptance
```

Cline is the default repository executor whenever capable. This includes CrewAI implementation, documentation, ChatGPT skills, router, supervisory rules, Context Engineer, Prompt Engineer, continuity/achievement files, and other bounded repository work.

ChatGPT may author/specify exact content but must not take over execution merely because it has GitHub access or would be faster.

If Cline is capable:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## Skill 12 fallback

ChatGPT may execute only through a separately selected Skill 12 cycle when the exact Cline capability limitation/repeated material mismatch/verified blocker is proven, ChatGPT exact tool capability is proven, the Human Owner explicitly authorizes the exact fallback stages, and lock/scope/writer-conflict gates pass.

Connected GitHub direct-write actions create remote commits directly; report that mechanism truthfully.

After a verified fallback, Cline resumes from the new repository truth and must not redo/revert/overwrite it without new Human Owner authority.

## Context Engineer and Prompt Engineer

```text
Context Engineer = minimum verified context, authority, branch/SHA, assignment, locks, do-not-repeat, evidence class, session continuity.
Prompt Engineer = exact NEW/STAY + mode + owner action + do-not + stop + Cline prompt packaging.
```

Neither is a primary/dependency skill.

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

Mode mapping:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

ChatGPT chooses one exact session and mode. Never require the Human Owner to choose `NEW/STAY` or `PLAN/ACT`.

`execute the approved plan here` is an ACT/ACT_BOUNDED instruction and must not be used to authorize execution during PLAN_ONLY.

## Consequential stages

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
MERGE ≠ DEPLOY
```

No automatic next stage.

## Human Owner rule

The Human Owner states goals, makes plain-language decisions, authorizes/rejects bounded actions, separately authorizes commit and push, and gives final acceptance. The Human Owner is not required to code, patch files, type terminal/Git commands, or design technical prompt syntax when an authorized AI actor can perform the work.
