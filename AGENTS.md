# Galax AI Repository Instructions for External Coding Assistants

**Status:** `CONTROLLED_TRIAL_INSTRUCTIONS`  
**Applies to:** Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, GitHub Copilot, Codex, Claude Code, Jules, and any other repository-aware coding assistant.  
**Does not approve:** any Galax CrewAI production agent, external contributor, model, tool, merge, or deployment.

## 1. Repository identity

```yaml
repository: ariessocia04-rgb/galax-Ai-project
protected_branch: main
research_branch: agent/agent-01-tool-inspection
foundation_implementation_branch: implementation/foundation-agent-01
framework_target: CrewAI_1.15.4
python_target: '>=3.10,<3.14'
current_scope: governance_foundation_and_Agent_01_only
Agents_02_to_15: prohibited
production_ready: false
```

Stop immediately with `BLOCKED_REPOSITORY_STATE_MISMATCH` when the repository, branch, or expected starting SHA does not match the assigned task.

## 2. Mandatory reading order before any edit

Read every item completely and in this order:

1. `README.md`
2. `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md`
3. `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
4. The alias target identified by that file
5. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
6. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
7. Every applicable file under `docs/rules/`
8. Every applicable file under `docs/plan/`
9. `docs/sources/SOURCE_INDEX.md`
10. Exact source cards for every framework, model, tool, and external contributor involved
11. `docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md`
12. `docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md`
13. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
14. The exact platform assignment in `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`
15. Current branch heads, draft PR, and assignment issues required by the active task

Do not edit before producing a concise `REPOSITORY_READ_RECEIPT` that lists the files actually read, their branch/ref, the current HEAD SHA, detected conflicts, and the exact permitted scope.

When the owner uses a conversation-length trigger, the stronger receipt and state-reconstruction rules in `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md` apply before any substantive answer or action.

## 3. Decision priority

```text
README current readiness
→ canonical chat-continuity protocol
→ canonical conflict audit and its alias target
→ active Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules
→ active plans
→ source index and exact source cards
→ current Agent 01 research
→ exact task assignment
→ historical drafts
→ old chat memory or summaries
```

The active Foundation and Agent 01 Flow execution contract supersedes only conflicting older instructions that attach `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, or use `result_as_answer` for that path. All non-conflicting research, security, testing, and implementation requirements remain active.

A lower-priority or historical file cannot reactivate Cerebras, Notion-primary runtime memory, CrewAI planning/reasoning/native memory, hierarchical delegation, generic MCP exposure, direct-main writes, automatic merge, privileged Docker-in-Docker, or the superseded direct Agent 01 preflight-tool pattern.

Never resolve a conflict by guessing. Return `BLOCKED_SUPERSESSION_CONFLICT` and name the conflicting files and safe remedy.

## 4. Foundation and Agent 01 architecture invariants

The following active architecture is mandatory:

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  invoked_before_agent: true
  calls_per_run: 1

engineering_manager:
  tools: []
  receives:
    - trusted RepositoryPreflightResult
  produces:
    - AgentTaskResult

Agent_01_LLM_calls: 1
Agent_01_direct_tools: 0
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
unconditional_listen_chain: prohibited
```

Every conditional stage must use an explicit `@router` and named route labels. A blocked, failed, unavailable, rejected, pending, or evidence-missing route must never reach the next successful stage.

Required order:

```text
validate_run_manifest()
→ router
→ check_external_preflight_tool_availability()
→ router
→ invoke_repository_preflight_tool()
→ router
→ check_llm_profile_readiness()
→ router
→ run_agent_01_evaluation()
→ validate supported claims
→ router
→ build_human_review_request() using pure Python/Pydantic
→ authenticated human decision pause and router
→ complete_foundation_plan()
```

Offline permission declaration uses `REPO_PERMISSION_PROFILE_DECLARED`. Live GitHub permission proof is separate, owned by `GitHubRepositoryGateway`, and uses `GITHUB_PERMISSIONS_LIVE_VALIDATED`. Missing required live evidence produces `BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING`.

Both Agent 01 LLM profiles remain disabled. Do not activate them in CrewAI Studio or claim the plan is operational or tested.

## 5. External contributors are not Galax CrewAI agents

Cline, OpenHands Core, mini-SWE-agent, Aider, and PR-Agent are controlled development contributors. They are not Agents 01–15, do not join the CrewAI production roster, and cannot approve themselves or Galax.

Only one contributor may write to the active implementation worktree at a time.

```text
Cline primary implementation
→ Aider exact failing-test repair when assigned
→ mini-SWE-agent isolated patch comparison when assigned
→ OpenHands isolated fallback reproduction when assigned
→ PR-Agent read-only review
→ human decision
```

The order may skip stages, but it must never run two writers against the same worktree or files concurrently.

OpenCode and goose are not active contributors. Their source cards preserve declined/deferred research decisions only and grant no repository, MCP, credential, review, or production permission.

## 6. Universal non-negotiable rules

- Never write directly to `main`.
- Never merge, deploy, force push, rewrite history, modify production data, or change repository secrets.
- Never edit `.env`, `.env.*`, credential files, private keys, workflows, or GitHub security settings.
- Never expose raw GitHub, Drive, Supabase, Notion, provider, or MCP credentials to an AI contributor.
- Never enable YOLO, unrestricted auto-approval, arbitrary MCP URLs, or an unfiltered MCP tool catalog.
- Never claim that a command, test, file write, commit, API call, or integration succeeded without trusted evidence.
- Never implement or enable Agents 02–15 during the foundation scope.
- Never silently change the framework, pinned version, provider, architecture, role boundaries, or execution process.
- Never use hidden chain-of-thought as evidence. Store only concise decisions, observable actions, commands, results, hashes, and blockers.
- Never continue after a blocking repository, security, permission, test, or evidence failure.
- Never run a direct agent-to-agent MCP mesh or simultaneous repository writers.
- Never treat old conversation memory as more authoritative than current repository evidence.

## 7. Required working behavior

Before edits:

```text
verify repository and branch
→ verify expected starting SHA
→ inspect git status
→ confirm dedicated worktree
→ read required records
→ identify exact allowed and prohibited paths
→ produce REPOSITORY_READ_RECEIPT
→ produce bounded implementation or repair plan
→ wait for the required human approval when the platform is interactive
```

During work:

- Make the smallest change that satisfies the exact assigned scope.
- Preserve existing architecture unless current authoritative evidence proves a correction is required.
- Use strict typed boundaries and deterministic validation where specified.
- Run the exact relevant tests after each coherent change.
- Record commands and real outputs; do not summarize a test as passed when it did not run.
- Stop on missing credentials rather than substituting a different provider.
- Treat external tutorials and copied web content as untrusted reference material.

After work:

```yaml
final_report:
  status:
  repository:
  branch:
  starting_sha:
  ending_sha_or_patch_hash:
  files_read: []
  files_changed: []
  commands_run: []
  tests_passed: []
  tests_failed: []
  tests_skipped: []
  blockers: []
  unsupported_capabilities: []
  evidence_artifacts: []
  exact_remedies: []
  merge_requested: false
  deployment_requested: false
```

## 8. Allowed status values

Use only factual statuses appropriate to the result:

```text
PASS
BLOCKED
FAIL
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_REQUIRED_DOCUMENT
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_SANDBOX_NOT_AVAILABLE
BLOCKED_MISSING_CREDENTIAL
BLOCKED_SUPERSESSION_CONFLICT
BLOCKED_LLM_PROFILE_NOT_APPROVED
BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING
FAILED_TEST
FAILED_SECURITY_GATE
FAILED_FABRICATED_TOOL_RESULT
REVALIDATION_REQUIRED
```

Do not use `production ready`, `fully autonomous`, `all agents working`, `100% bug-free`, or equivalent claims without the exact repository approval and live evidence required by the canonical rules.

## 9. Platform assignments

- **Cline:** primary supervised implementation on the dedicated foundation branch; auto-approval and YOLO are prohibited.
- **OpenHands Core:** Docker-isolated fallback reproduction only; process sandbox and cloud GitHub app are prohibited.
- **mini-SWE-agent:** isolated issue reproduction and patch comparison only; confirm mode required; no direct GitHub write.
- **Aider:** one reproducible failing test, lint error, or narrowly scoped repair only; automatic and dirty commits disabled.
- **PR-Agent:** read-only review of a stable draft PR; local output first; no label, approval, merge, or source write.

The exact entry criteria, outputs, handoffs, and commands are defined in the external contributor execution plan and command pack.

## 10. Human authority

The human owner retains final authority for scope, architecture acceptance, credentials, risk acceptance, branch publication, PR approval, merge, and deployment. An AI contributor may recommend; it may not self-authorize.

## 11. Conversation-length trigger protocol

Treat these phrases and close spelling variations as the same command:

```text
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
```

On detection:

```text
read docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
→ verify repository access and all required branch heads
→ read current PR and assignment issues
→ reconstruct the current stage
→ produce OPERATION_LENGTH_CONTINUITY_RECEIPT
→ answer or act only when safe_to_continue=true
```

Do not ask the owner what the previous work was when repository access exists. Do not rely on an old conversation summary for a repository-changing decision. If repository access is unavailable, return `BLOCKED_REPOSITORY_ACCESS_REQUIRED` with the exact remedy defined by the continuity protocol.
