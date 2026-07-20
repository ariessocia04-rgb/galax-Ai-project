# AI Development Tool Source Index

**Record date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `CURRENT_RESEARCH_SOURCE_INDEX`  
**Scope:** External AI development contributors, PR reviewers, orchestration frameworks, and data infrastructure considered for Galax development.

## Evidence rules

1. Official product documentation, official repositories, official pricing/limits pages, and official security documentation are primary sources.
2. Independent empirical studies may support workflow decisions, but they do not prove that a candidate will achieve the same result in Galax.
3. Vendor benchmark percentages are contextual evidence only. They are not accepted as a Galax accuracy score.
4. A candidate is not approved until the exact version, model/provider, permissions, branch policy, task fixture, and test environment pass Galax qualification.
5. Pricing, quotas, models, permissions, and maintenance status are time-sensitive and require revalidation before activation.

## Official sources

### Jules

- **S01 — Limits and Plans:** https://jules.google/docs/usage-limits
  - Free Jules: 15 tasks in a rolling 24-hour window and 3 concurrent tasks as of the record date.
  - Limits may change and must be rechecked before scheduling work.
- **S02 — Tasks and repositories:** https://jules.google/docs/tasks-repos/
  - Each task runs in its own virtual machine with separate logs, environment, and changes.
- **S03 — Jules documentation:** https://jules.google/docs/
  - Repository tasks, plan review, code changes, tests, branch publication, and pull-request workflow.

### OpenAI Codex

- **S04 — Using Codex with a ChatGPT plan:** https://help.openai.com/en/articles/11369540
  - Usage varies with task size, complexity, model, context, and execution location.
  - A user may need to wait for reset, upgrade, or use approved credits depending on the plan.
- **S05 — Codex rate card:** https://help.openai.com/en/articles/20001106
  - Current Codex flexible pricing is token/credit based; rates and supported models are time-sensitive.
  - Usage must be checked in the Codex Usage panel.
- **S06 — Flexible credits:** https://help.openai.com/en/articles/12642688
  - Eligible plans may add credits after included usage is exhausted.

### OpenHands

- **S07 — Official repository and license:** https://github.com/OpenHands/OpenHands
  - Core OpenHands and agent-server are MIT-licensed; the `enterprise/` directory has separate terms.
- **S08 — GitHub integration permissions:** https://docs.openhands.dev/openhands/usage/cloud/github-installation
  - OpenHands Cloud requests read/write access across multiple repository permission classes, including contents, pull requests, Actions, webhooks, and workflows.
- **S09 — CLI installation:** https://docs.openhands.dev/openhands/usage/cli/installation
  - Local CLI is available and can be isolated from broad GitHub Cloud permissions.

### SWE-agent

- **S10 — Official current guidance:** https://swe-agent.com/latest/
  - SWE-agent has been superseded by mini-SWE-agent and is in maintenance-only mode.
- **S11 — User guides:** https://swe-agent.com/latest/usage/
- **S12 — Official repository:** https://github.com/SWE-agent/SWE-agent
  - MIT license; original SWE-agent remains available but is not the recommended current project.

### Aider

- **S13 — Official repository:** https://github.com/Aider-AI/aider
  - Open-source terminal pair programmer with repository mapping and Git integration.
- **S14 — Git integration:** https://aider.chat/docs/git.html
  - Aider can automatically commit changes; Galax must override defaults where necessary and require explicit branch and commit controls.
- **S15 — Linting and testing:** https://aider.chat/docs/usage/lint-test.html
  - Supports automatic linting and configured test commands after edits.
- **S16 — Token limits:** https://aider.chat/docs/troubleshooting/token-limits.html
  - Limits and cost are primarily determined by the selected model/provider and repository context.

### LangGraph

- **S17 — Overview:** https://docs.langchain.com/oss/python/langgraph/overview
  - LangGraph is a low-level orchestration runtime with durable execution, persistence, and human-in-the-loop support.
- **S18 — Persistence:** https://docs.langchain.com/oss/python/langgraph/persistence
  - Checkpointing supports interruption, resume, memory, and fault tolerance.

### PostgreSQL and pgvector

- **S19 — pgvector official repository:** https://github.com/pgvector/pgvector
  - Exact nearest-neighbor search is the default; HNSW and IVFFlat provide approximate search with speed/recall tradeoffs.
- **S20 — pgvector 0.8.2 security release:** https://www.postgresql.org/about/news/pgvector-082-released-3245/
  - Version 0.8.2 fixes CVE-2026-3172, a buffer overflow affecting parallel HNSW builds.
- **S21 — PostgreSQL:** https://www.postgresql.org/

### Continue

- **S22 — Current official documentation:** https://docs.continue.dev/index
  - The repository is no longer actively maintained/read-only and has a final 2.0.0 release.
- **S23 — Repository:** https://github.com/continuedev/continue
  - Apache-2.0; source-controlled AI checks remain documented, but maintenance status is a qualification blocker.

### PR-Agent / Qodo

- **S24 — Current community repository:** https://github.com/The-PR-Agent/pr-agent
  - Open-source PR reviewer; supports describe, review, improve, and ask workflows.
  - Apache-2.0; this repository is distinct from the hosted Qodo free tier.
- **S25 — Security and version pinning:** https://github.com/The-PR-Agent/pr-agent/security
  - Supports fixed releases and Docker digest pinning. Galax must not use unpinned `@main` or nightly images.

### GitHub Copilot

- **S26 — Plans:** https://docs.github.com/en/copilot/get-started/plans
  - Free and paid plans differ in feature access, cloud-agent availability, and AI-credit allowances.
- **S27 — Individual plan benefits:** https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-started-with-copilot-on-your-personal-account/about-individual-copilot-plans-and-benefits
  - Free-plan usage is limited; exact limits and billing rules must be rechecked before use.

### Cursor

- **S28 — Pricing:** https://docs.cursor.com/account/pricing
  - Agent usage depends on model API pricing; heavy agent use can materially exceed entry-plan included usage.
- **S29 — Background-agent security:** https://docs.cursor.com/background-agent
  - Background agents use isolated VMs but receive repository read/write access, internet access, and automatic terminal execution, creating prompt-injection and exfiltration risk.

### Devin

- **S30 — Self-serve plans:** https://docs.devin.ai/admin/billing/self-serve
  - Free, Pro, Max, and Teams plans have different quotas and on-demand credit behavior.
- **S31 — Usage:** https://docs.devin.ai/admin/billing/usage
  - Consumption depends on task actions, complexity, VM time, and networking.
- **S32 — Billing overview:** https://docs.devin.ai/admin/billing

### Google Antigravity

- **S33 — Overview:** https://antigravity.google/docs/overview
  - Local command, file, web, MCP, subagent, and artifact capabilities.
- **S34 — Security settings:** https://antigravity.google/docs/ide-settings
  - Request Review, strict mode, workspace isolation, and terminal sandbox controls.
- **S35 — Artifact review:** https://antigravity.google/docs/artifact-review
  - Planning mode can stop for explicit artifact approval before implementation.

## Independent and benchmark evidence

- **E01 — AIDev dataset:** https://arxiv.org/abs/2602.09185
  - Preprint dataset containing 932,791 agent-authored pull requests across 116,211 repositories for five major coding agents.
  - Demonstrates real-world usage at scale, not correctness for a specific repository.
- **E02 — Cross-agent conflict study:** https://arxiv.org/abs/2607.04697
  - Preprint reports textual conflicts in 41.7% of sampled cross-agent concurrent PR pairs versus 19.8% for same-agent pairs.
  - Supports Galax's single-writer and serialized-integration policy.
- **E03 — Task-stratified PR acceptance:** https://arxiv.org/abs/2602.08915
  - Study of 7,156 pull requests reports that task type strongly affects acceptance and no single agent performs best across every task category.
  - Supports role specialization instead of a universal-agent claim.
- **E04 — Agentic PR decision rationale:** https://arxiv.org/abs/2605.22534
  - Shows that merge/rejection outcomes alone do not equal agent correctness and that reviewer involvement materially affects outcomes.
- **E05 — SWE-bench Verified:** https://www.swebench.com/verified.html
  - Human-filtered 500-instance coding benchmark.
- **E06 — Current benchmark limitation warning:** https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
  - Documents remaining benchmark defects and warns against treating one benchmark score as a complete capability measure.

## Source interpretation status

```yaml
accuracy_percentage_for_any_candidate: NOT_ESTABLISHED
reason: >
  No single public percentage is valid across Galax tasks, repository state,
  model/provider choices, prompts, permissions, and test environments.
required_replacement:
  - exact Galax fixture pass rate
  - unauthorized-operation rate
  - test and lint pass rate
  - deterministic repeatability
  - human review acceptance
  - cost and quota consumption per qualified task class
```
