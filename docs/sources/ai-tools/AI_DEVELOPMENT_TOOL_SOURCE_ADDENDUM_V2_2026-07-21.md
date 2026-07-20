# AI Development Tool Source Addendum V2

**Record date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `CURRENT_STRICT_RESCREEN_SOURCE_ADDENDUM`  
**Purpose:** Re-screen the earlier shortlist against current maintenance, licensing, permission, sandbox, benchmark, and role-fit evidence.

## Evidence rules

1. Official repositories and documentation are primary evidence for license, maintenance, permissions, execution model, and supported workflows.
2. A benchmark percentage is accepted only as a score for the exact agent harness, model, prompt, environment, and benchmark version that produced it.
3. Benchmark performance is not a universal accuracy percentage and is not Galax approval.
4. GitHub stars, forks, release count, or vendor adoption claims are maintenance/adoption signals only; they are not correctness proof.
5. No candidate may be activated until it passes the Galax controlled-trial gate with the exact pinned version and model/provider.

## New official sources

### Cline

- **V2-S01 — Official repository:** https://github.com/cline/cline
  - Apache-2.0.
  - Available as SDK, IDE extension, and CLI.
  - Supports headless automation and local development workflows.
- **V2-S02 — Cline overview:** https://docs.cline.bot/cline-overview
  - Reads and writes files and runs terminal commands with explicit user approval.
- **V2-S03 — Checkpoints:** https://docs.cline.bot/core-workflows/checkpoints
  - Maintains a shadow Git repository and creates checkpoints after tool use; project Git history remains separate.
- **V2-S04 — Auto-approve and YOLO controls:** https://docs.cline.bot/features/auto-approve
  - Permissions are evaluated per tool call.
  - Galax must prohibit YOLO mode and keep edits, commands, browser, and MCP approval-gated.
- **V2-S05 — SDK:** https://docs.cline.bot/sdk/overview
  - Open-source agent runtime with tools, checkpoints, MCP, cron, and subagent support.
- **V2-S06 — CLI:** https://docs.cline.bot/usage/cli-overview
  - Interactive and headless execution with structured output.

### mini-SWE-agent

- **V2-S07 — Official repository:** https://github.com/SWE-agent/mini-swe-agent
  - MIT license.
  - Current successor candidate to the original SWE-agent.
  - Repository states a score above 74% on SWE-bench Verified for specific harness/model configurations.
- **V2-S08 — Releases:** https://github.com/SWE-agent/mini-swe-agent/releases
  - Current releases include wall-clock and cost-limit controls.
- **V2-S09 — Official SWE-bench leaderboard:** https://www.swebench.com/
  - SWE-bench reports results by exact model and mini-SWE-agent version.
  - Example current entries using mini-SWE-agent 2.0.0 vary substantially by model, demonstrating that the harness score is model-dependent.
- **V2-S10 — SWE-bench Verified methodology:** https://www.swebench.com/verified.html
  - Human-filtered 500-instance benchmark.
  - Results are not automatically comparable across different agent versions or configurations.

### OpenCode — current canonical project only

- **V2-S11 — Current repository:** https://github.com/anomalyco/opencode
  - MIT license.
  - Actively released current OpenCode project.
- **V2-S12 — Permissions:** https://opencode.ai/docs/permissions/
  - Supports allow, ask, and deny rules for read, edit, bash, web, external-directory, subagent, and other actions.
  - Defaults are relatively permissive; Galax must provide an explicit deny-first configuration.
- **V2-S13 — Agents:** https://opencode.ai/docs/agents
  - Supports primary agents and subagents with per-agent permissions.
  - A read-only review agent can deny edits and restrict Git commands.
- **V2-S14 — Security statement:** https://github.com/anomalyco/opencode/security
  - OpenCode does not sandbox the agent.
  - Permission prompts are a user-control layer, not process isolation.
- **V2-S15 — Rules:** https://opencode.ai/docs/rules/
  - Reads project `AGENTS.md` instructions, matching the Galax repository-governance model.

### OpenCode name-collision warning

- **V2-S16 — Archived unrelated predecessor:** https://github.com/opencode-ai/opencode
  - Archived and moved to another project.
  - Must not be confused with the active `anomalyco/opencode` repository.

### goose

- **V2-S17 — Official repository:** https://github.com/aaif-goose/goose
  - Apache-2.0.
  - Desktop, CLI, and API; provider-agnostic and extensible.
- **V2-S18 — Official documentation:** https://block.github.io/goose/index.html
  - Tool permission controls, sandbox mode, prompt-injection detection, and adversary review are documented.
  - Supports many MCP extensions and parallel subagents.
  - Galax generic-MCP restrictions mean only an allowlisted custom distribution can be considered.

### OpenHands current controls

- **V2-S19 — Docker sandbox:** https://docs.openhands.dev/openhands/usage/sandboxes/docker
  - Docker is the recommended local sandbox.
  - Read-write mounts can be modified by the agent.
- **V2-S20 — Sandbox overview:** https://docs.openhands.dev/openhands/usage/sandboxes/overview
  - Docker, process, and remote sandbox providers exist.
  - Process mode has no isolation and is prohibited for Galax trials.
- **V2-S21 — FAQ and safety:** https://docs.openhands.dev/overview/faqs
  - OpenHands is designed primarily for a single user locally, not an unauthenticated multi-tenant service.
  - Agents can use provided credentials and network access; mounted directories can be modified or deleted.
- **V2-S22 — GitHub permissions:** https://docs.openhands.dev/openhands/usage/cloud/github-installation
  - Cloud integration requests broad write permissions including workflows and Actions.
  - Broad Cloud App use remains rejected for the current Galax phase.
- **V2-S23 — Benchmark report:** https://www.openhands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model
  - Reports a 60.6% base OpenHands score on SWE-bench Verified before inference-time scaling in the described setup.
  - Vendor benchmark evidence only; not a Galax accuracy score.

### Aider current maintenance and benchmark context

- **V2-S24 — Official repository:** https://github.com/Aider-AI/aider
  - Apache-2.0 and actively maintained.
- **V2-S25 — Aider benchmark harness:** https://github.com/Aider-AI/aider/blob/main/benchmark/README.md
  - Evaluates model plus Aider editing performance in Docker.
  - Warns that generated code can be dangerous and must run in isolation.
- **V2-S26 — Historical SWE-bench Lite harness:** https://github.com/Aider-AI/aider-swe-bench
  - Reports 26.3% on an older SWE-bench Lite setup.
  - Too old and not directly comparable to current Verified results; retained only as historical evidence.

### PR-Agent current status correction

- **V2-S27 — Current community repository:** https://github.com/The-PR-Agent/pr-agent
  - Current repository reports Apache-2.0 and active releases.
  - Specialized PR review role.
- **V2-S28 — Legacy Qodo path:** https://github.com/qodo-ai/pr-agent
  - Search/indexed copies may show legacy/community transition and different historical license metadata.
  - Galax must pin the exact canonical repository, commit, and license file before use.

### Roo Code exclusion

- **V2-S29 — Roo Code repository:** https://github.com/RooCodeInc/Roo-Code
  - Archived and read-only as of 2026-05-15.
  - Explicitly excluded as a new Galax dependency.

## Independent and benchmark cautions

- **V2-E01 — Claw-SWE-Bench:** https://arxiv.org/abs/2606.12344
  - Under a fixed model, adapter/harness choice changed pass rate by 27.4 percentage points in the reported experiments.
  - Supports evaluating the exact harness rather than attributing all performance to the model.
- **V2-E02 — AgentLens:** https://arxiv.org/abs/2605.12925
  - Reports that 10.7% of passing trajectories in its evaluated subset showed “Lucky Pass” behavior such as regressions, blind retries, or missing verification.
  - Passing tests alone is insufficient; Galax must audit process quality.
- **V2-E03 — SWE-bench limitations study:** https://arxiv.org/abs/2602.04449
  - Shows leaderboard diversity and strong dependence on proprietary models and submission setup.
  - Supports conservative interpretation of rankings.

## Source conclusion

```yaml
universal_accuracy_percentage_available: false
open_source_agent_automatically_free: false
reason:
  - inference provider or local hardware is still required
  - sandbox and CI resources have cost
  - benchmark results depend on model and harness
  - repository permission and security setup change capability
required_Galax_proof:
  - exact version and commit pin
  - exact model/provider pin
  - deny-first permission profile
  - isolated workspace or sandbox
  - repeated Galax fixtures
  - unauthorized-operation test
  - process-quality review
  - cost and quota record
  - human approval
```
