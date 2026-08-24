# CrewAI GitHub Read/Write and Free LLM Audit — 2026-07-20

**Status:** `RESEARCH_RECORD`  
**Implementation status:** `NOT_IMPLEMENTED`  
**Full Galax build prompt:** `BLOCKED_NOT_READY`  
**Repository inspected:** `crewAIInc/crewAI` current `main` and versioned `v1.15.4` documentation

## 1. Scope and evidence standard

The CrewAI repository contains thousands of source, documentation, test, example, translation, and package files. This audit does not claim that every byte was manually read. It systematically inspected the relevant implementation paths for:

```text
GitHub and filesystem tools
MCP adapter and lifecycle
LLM construction and provider configuration
CrewAI versioned LLM documentation
sequential process and Flow boundaries
tool schemas and external capability ownership
provider compatibility and free-plan evidence
```

Approval requires three layers:

```text
current official documentation
→ current official source/adapter implementation
→ live test in the exact Galax environment
```

No provider or GitHub integration in this document is production-approved.

## 2. CrewAI GitHub capability findings

### 2.1 Built-in `GithubSearchTool` is read/search only

Official CrewAI source:

- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/github_search_tool/github_search_tool.py

The source describes a semantic GitHub repository search `RagTool` and explicitly says it is **not the GitHub API**. It indexes/searches repository, code, pull-request, and issue content. It does not implement file writes, commits, branch creation, pushes, or pull requests.

Decision:

```yaml
GithubSearchTool:
  repository_read_and_semantic_search: supported
  GitHub_API_write: unsupported
  branch_commit_push_PR: unsupported
```

### 2.2 Built-in `FileWriterTool` writes only to a local filesystem

Official CrewAI source:

- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/file_writer_tool/file_writer_tool.py

It writes a file under a local directory, creates directories when required, rejects path traversal/symlink escape, and requires explicit overwrite. It does not perform Git commits or GitHub API operations.

Decision:

```yaml
FileWriterTool:
  local_checked_out_repository_write: technically_supported
  Git_commit_push_PR: unsupported
  selected_for_Galax_direct_agent_use: no
```

Galax will use a stricter role-scoped repository workspace tool rather than exposing a generic file writer.

### 2.3 CrewAI can consume MCP tools

Official CrewAI source:

- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/adapters/mcp_adapter.py
- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/mcp/overview.mdx
- https://github.com/crewAIInc/crewAI-tools

Verified behavior:

```text
- MCP JSON schemas are adapted into CrewAI BaseTool objects.
- STDIO and HTTP/SSE-style server parameters are supported by the adapter path.
- Exact MCP tool names can be filtered.
- Adapter lifecycle must be stopped or managed by a context manager.
- The inspected adapter executes tool adaptation synchronously.
- Async adaptation is explicitly not supported by the inspected adapter class.
```

Required installation:

```bash
uv add 'crewai-tools[mcp]'
```

The exact pinned install must verify that both `mcp` and `mcpadapt` import correctly.

### 2.4 Official GitHub MCP Server provides real GitHub read/write operations

Official server and documentation:

- https://github.com/github/github-mcp-server
- https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server

Verified capabilities include repository/file reads, issue and pull-request operations, branch/file changes, and workflow information, subject to the GitHub credential's permissions. The local server has an official public Docker image:

```text
ghcr.io/github/github-mcp-server
```

The server supports toolset and exact-tool filtering plus a read-only mode.

### 2.5 Selected Galax repository integration

Galax must not expose the whole GitHub MCP tool catalog to every agent.

Selected architecture:

```text
CrewAI agent
→ exactly one Galax role-scoped repository workspace tool
→ trusted repository gateway
→ official GitHub API or filtered official GitHub MCP Server
→ dedicated run branch
→ one verified commit transaction
→ QA/audit
→ draft PR created by trusted Flow
```

Agent 01 remains read-only. Writer agents receive only their exact path and operation scope.

Direct writes to `main`, force push, automatic merge, unrestricted deletion, and broad GitHub tokens remain prohibited.

## 3. Minimal factual GitHub MCP connection path

This is a validation outline, not production-ready code.

### Install

```bash
uv add crewai==1.15.4
uv add 'crewai-tools[mcp]'
```

### Keep the token outside prompts and source control

```env
GITHUB_PERSONAL_ACCESS_TOKEN=
```

Use a fine-grained token or GitHub App token restricted to the Galax repository and only the required Contents/Pull Requests permissions.

### Local GitHub MCP server through Docker

```python
import os
from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter

server = StdioServerParameters(
    command="docker",
    args=[
        "run", "-i", "--rm",
        "-e", "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server",
    ],
    env={
        **os.environ,
        "GITHUB_PERSONAL_ACCESS_TOKEN": os.environ["GITHUB_PERSONAL_ACCESS_TOKEN"],
    },
)

with MCPServerAdapter(server, "get_file_contents") as selected_tools:
    # Assign only the exact filtered tool(s) required by the test agent.
    # Galax production policy still prefers one composite role-scoped tool.
    pass
```

This proves only the supported connection pattern. The exact GitHub MCP tool names, schemas, permissions, Docker image digest, and CrewAI behavior must be enumerated and live-tested before use.

## 4. Tutorial search result

No reliable YouTube tutorial was found that demonstrates the exact current combination:

```text
CrewAI 1.15.4
+ official GitHub MCP Server
+ authenticated repository read/write
+ strict one-agent/one-tool filtering
+ safe run-branch commit
+ deterministic checkpoint and rollback
```

Therefore, Galax must use the official CrewAI MCP examples and official GitHub MCP documentation as the canonical setup references. Community videos or tutorials may be used only as supplemental hints and cannot approve the integration.

## 5. CrewAI LLM support facts

Official CrewAI versioned source:

- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/llms.mdx
- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai/src/crewai/utilities/llm_utils.py

CrewAI supports LLM configuration through environment variables, YAML, or Python. Native SDK integrations include Google Gemini, OpenAI, Anthropic, Azure, AWS Bedrock, and Snowflake. Other providers use LiteLLM:

```bash
uv add 'crewai[litellm]'
```

The inspected CrewAI LLM construction code creates one LLM configuration at a time. No native per-agent list of runtime provider fallbacks was found. Therefore provider failover remains deterministic Galax Flow logic, not an assumed CrewAI feature.

## 6. Trial-only provider removal

### Cerebras GPT-OSS 120B

Current official pricing describes free trial credits rather than a permanent free plan:

- https://www.cerebras.ai/pricing

Decision:

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: REJECTED_TRIAL_ONLY
active_primary: false
active_fallback: false
```

Historical source research remains for audit purposes, but Cerebras must be removed from active agent profiles.

## 7. Active free/open candidates

### 7.1 Groq GPT-OSS 120B — hosted private-repository candidate

```yaml
provider: Groq
model_id: openai/gpt-oss-120b
crewai_model_id: groq/openai/gpt-oss-120b
context_window: 131072
maximum_output: 65536
free_limits_base:
  RPM: 30
  RPD: 1000
  TPM: 8000
  TPD: 200000
status: SELECTED_FOR_VALIDATION
```

Official links:

- https://console.groq.com/docs/model/openai/gpt-oss-120b
- https://console.groq.com/docs/rate-limits
- https://console.groq.com/docs/tool-use/local-tool-calling
- https://console.groq.com/docs/openai
- https://console.groq.com/docs/your-data

Provider-documented capabilities include reasoning, local function/tool calls, JSON object/schema modes, and a 131K context window. Groq does not use inputs/outputs for model training unless explicitly permitted, and Zero Data Retention can be enabled.

Risks:

```text
- 8K tokens/minute is the practical throughput bottleneck.
- Groq is mostly, not completely, OpenAI compatible.
- Unsupported request parameters can return HTTP 400.
- Strict tool calling and strict structured output must be tested in the CrewAI/LiteLLM path.
```

### 7.2 Cloudflare Workers AI GPT-OSS 120B — hosted private fallback candidate

```yaml
provider: Cloudflare Workers AI
model_id: '@cf/openai/gpt-oss-120b'
connection: CrewAI custom OpenAI-compatible endpoint
context_window: 128000
function_calling: true
reasoning: true
structured_JSON: supported
free_allocation: 10000_neurons_per_day
status: SELECTED_FOR_VALIDATION_AS_HOSTED_FALLBACK
```

Official links:

- https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/
- https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/
- https://developers.cloudflare.com/workers-ai/features/function-calling/
- https://developers.cloudflare.com/workers-ai/features/json-mode/
- https://developers.cloudflare.com/workers-ai/platform/pricing/
- https://developers.cloudflare.com/workers-ai/platform/data-usage/

The free allocation is compute-based, not a fixed request or token quota. At current published unit rates, 10,000 free neurons is approximately equivalent to at most about 314K input-only tokens or 146K output-only tokens for this model; real mixed requests consume both.

Cloudflare states that customer content is not used to train models or improve services without explicit consent.

CrewAI connection must use a separately tested custom OpenAI-compatible profile with Cloudflare account ID, API token, base URL, and exact model ID.

### 7.3 Google Gemini 2.5 Flash — public/redacted long-context candidate

```yaml
provider: Google Gemini API
model_id: gemini-2.5-flash
crewai_model_id: gemini/gemini-2.5-flash
context_window: 1048576
maximum_output: 65536
function_calling: true
structured_outputs: true
thinking: true
status: PUBLIC_OR_REDACTED_CONTEXT_ONLY_PENDING_TESTS
```

Official links:

- https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://ai.google.dev/gemini-api/docs/pricing
- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/llms.mdx

CrewAI has a native Google Gen AI integration:

```bash
uv add 'crewai[google-genai]'
```

Free-tier inputs/outputs are currently free for supported models, but Google states free-tier content may be used to improve its products. Therefore private repository code, credentials, customer data, and confidential documents must not be sent through the free Gemini profile.

Actual rate limits are account/project-specific and must be captured from Google AI Studio before each run group.

### 7.4 Ollama GPT-OSS 20B — local no-API fallback candidate

```yaml
provider: local_Ollama
model_id: gpt-oss:20b
crewai_model_id: ollama/gpt-oss:20b
context_window: 128000
model_download_size: approximately_14GB
minimum_memory_claim: approximately_16GB_for_model_runtime
function_calling: documented
structured_outputs: documented
API_quota: none_local
status: OPTIONAL_PENDING_HARDWARE_AND_CREWAI_TESTS
```

Official links:

- https://ollama.com/library/gpt-oss
- https://ollama.com/library/gpt-oss:20b
- https://ollama.com/blog/gpt-oss

This is not a hosted free tier; it avoids provider API quotas but consumes the owner's RAM/VRAM, disk, electricity, and processing time. It may be too slow or unavailable on insufficient hardware.

No local model may be silently selected merely because a hosted provider fails. Hardware, tool calling, structured output, context, and latency must pass per-agent tests first.

## 8. Conditional candidate

### Mistral Free Mode

Mistral documents a no-card free API mode intended for evaluation/prototyping, and current models such as Mistral Small 4 provide 256K context, function calling, and structured outputs.

Official links:

- https://docs.mistral.ai/admin/billing-usage/subscriptions
- https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03
- https://docs.mistral.ai/studio-api/conversations/structured-output
- https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them

However:

```text
- exact free-mode model availability is account-specific;
- exact limits are shown in the Admin Console;
- public Mistral privacy pages contain potentially conflicting wording about API training behavior and opt-out controls;
- Zero Data Retention is not available on free mode.
```

Decision: `CANDIDATE_PENDING_ACCOUNT_AND_PRIVACY_VALIDATION`, not active fallback.

## 9. Rejected active candidates

```yaml
Cerebras:
  reason: current_offer_is_trial_credit
OpenRouter_free_router:
  reason: model_can_change_and_normal_free_quota_is_low
HuggingFace_free_credit:
  reason: approximately_0_10_USD_monthly_credit_is_insufficient
Vercel_AI_Gateway_free_credit:
  reason: routing_credit_not_a_pinned_model_runtime
GitHub_Models:
  reason: restrictive_prototyping_limits
trial_credit_providers:
  reason: finite_trial_not_durable_free_runtime
```

NVIDIA NIM, Cohere, and other free developer plans may remain research candidates, but they are not selected until exact model, context, tool, privacy, quota, and CrewAI compatibility evidence is complete.

## 10. Selected Galax LLM routing policy

```yaml
private_repository_and_code_tasks:
  primary_candidate: groq/openai/gpt-oss-120b
  hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
  local_fallback_candidate: ollama/gpt-oss:20b

public_or_fully_redacted_long_context_tasks:
  candidate: gemini/gemini-2.5-flash

conditional_research_candidate:
  model: mistral/mistral-small-2603

rejected_active:
  - cerebras/gpt-oss-120b
  - openrouter/free
  - all_trial_credit_only_providers
```

Each provider profile requires independent per-agent validation. No cross-provider switch is allowed during a non-idempotent tool operation.

## 11. Deterministic failover requirement

CrewAI does not provide the approved Galax failover policy automatically.

```text
safe LLM-only stage fails
→ classify provider error
→ verify no write transaction is active
→ save canonical checkpoint
→ confirm alternate profile is APPROVED_FOR_AGENT
→ capture current alternate quota/capacity
→ instantiate alternate LLM explicitly
→ rerun only the safe LLM stage
→ record provider/model/profile switch
```

If no validated alternate exists:

```text
BLOCKED_ALL_VALIDATED_LLMS_UNAVAILABLE
```

## 12. Required live proof before the build prompt

```text
1. Pin Python, CrewAI, crewai-tools, MCP, mcpadapt, and provider SDK/LiteLLM versions.
2. Test official GitHub MCP Server startup and cleanup.
3. Enumerate exact GitHub MCP read/write tool schemas.
4. Verify read-only mode and exact tool filtering.
5. Implement one Galax composite repository preflight tool.
6. Prove a read from the Galax repository.
7. Prove an allowed write to a temporary run branch.
8. Prove direct-main, force-push, secret-path, and unauthorized-path rejection.
9. Test Groq completion, tool call, tool result, and structured output through CrewAI.
10. Test Cloudflare completion, tool call, tool result, and structured output through CrewAI custom OpenAI mode.
11. Test Gemini only with public/redacted fixtures.
12. Test Ollama only after hardware qualification.
13. Prove deterministic provider transition only from a safe checkpoint.
14. Run a real two-agent `Process.sequential` smoke test.
15. Preserve invocation IDs, provider usage, Git commit evidence, and failure remedies.
```

## 13. Current decision

```yaml
GitHub_read_write_path_found: true
built_in_GithubSearchTool_writes: false
official_GitHub_MCP_read_write: true
CrewAI_MCP_adapter_path_found: true
exact_Galax_integration_live_tested: false
reliable_exact_YouTube_tutorial_found: false

active_hosted_primary_candidate: groq/openai/gpt-oss-120b
active_hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
public_long_context_candidate: gemini/gemini-2.5-flash
local_fallback_candidate: ollama/gpt-oss:20b
Cerebras_active: false

full_build_prompt_ready: false
agents_enabled: 0
```
