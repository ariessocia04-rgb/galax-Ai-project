# Per-Agent LLM Compatibility Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Permanent:** No. This rule may be revised after exact provider/model and agent tests.  
**Current candidate:** `cerebras/gpt-oss-120b`

## 1. Core rule

A model approved for one agent is not automatically approved for every other agent.

Every agent must have a separate LLM profile and separate compatibility decision even when multiple agents share the same provider and model.

```text
SAME MODEL != SAME TASK REQUIREMENTS
```

## 2. Required fields in every agent description/source card

```yaml
llm_contract:
  source_id:
  provider:
  exact_model_id:
  crewai_model_id:
  status:

  required_capabilities:
    reasoning:
    system_instructions:
    tool_calling:
    tool_result_round_trip:
    strict_json_schema:
    pydantic_output:
    token_usage_reporting:
    context_window_tokens:
    maximum_completion_tokens:
    vision:

  assigned_profile:
    reasoning_effort:
    max_completion_tokens:
    temperature:
    timeout_seconds:
    max_retries:
    max_rpm:
    max_iter:
    max_execution_time_seconds:
    respect_context_window:
    crewai_reasoning_loop:
    memory:
    allow_delegation:
    allow_code_execution:
    async_execution:

  prohibited_uses: []
  mandatory_tests: []
  known_limitations: []
  revalidation_triggers: []
```

## 3. Shared mandatory settings

Until changed by an approved per-agent test:

```yaml
all_agents:
  provider: Cerebras
  model: cerebras/gpt-oss-120b
  temperature: 1.0
  timeout_seconds: 120
  max_retries: 1
  max_rpm: 4
  allow_delegation: false
  allow_code_execution: false
  async_execution: false
  memory: false
  respect_context_window: false
  crewai_reasoning_loop: false
```

Reasons:

```text
- max_rpm 4 leaves headroom below the documented free-trial 5 RPM.
- one retry limits token waste.
- delegation and async execution conflict with the strict sequential design.
- built-in code execution is deprecated.
- CrewAI memory is not approved and may create external LLM/embedder calls.
- exact tasks must fail rather than silently summarize away evidence.
- provider reasoning effort is used; CrewAI's additional reasoning loop is disabled
  to avoid a second planning cycle and extra tokens.
```

## 4. Required tool-calling test

Every agent has one assigned tool interface. Before enabling that agent, the exact LLM profile must prove:

```text
1. The model selects the correct single tool.
2. Arguments validate against the exact schema.
3. The actual tool executes.
4. The tool returns a trusted invocation ID.
5. The model receives the actual tool result.
6. The model does not invent a second tool.
7. The model does not fabricate a successful observation.
8. The final output references the actual invocation ID.
9. The final output validates against the task schema.
```

A model that produces a correct-looking answer without a real tool invocation fails the agent profile.

## 5. Reasoning rules

Reasoning effort must match the task, not the prestige of the role.

```yaml
low:
  use_for:
    - deterministic preflight summary
    - simple formatting
    - bounded status reporting

medium:
  use_for:
    - requirements transformation
    - scoped implementation
    - test design
    - CI configuration

high:
  use_for:
    - architecture tradeoffs
    - evidence synthesis
    - security threat analysis
    - database migration reasoning
    - integration failure analysis
    - final independent audit
```

High reasoning does not grant more permissions or make the result automatically correct.

Raw chain-of-thought must never be requested, logged, or committed. Required output is concise rationale plus evidence, assumptions, tests, and risks.

## 6. Context rules

The candidate model has a 131,072-token context window, but the provider limit does not mean the whole repository should be sent.

Every request must contain only:

```text
- the active agent description
- exact task contract
- one assigned tool schema
- active rule and plan hashes
- relevant repository excerpts
- required prior structured outputs
- no secrets
```

Prohibited:

```text
- all 15 agent prompts
- all tool schemas
- entire repository
- complete Git history
- raw logs unrelated to the task
- `.env` or credentials
```

If required exact information cannot fit, stop with `BLOCKED_CONTEXT_LIMIT`.

## 7. Output-token rules

The provider's maximum output is a technical ceiling, not an agent budget.

Galax per-agent completion caps must remain small and role-specific. Current draft caps:

```yaml
engineering_manager: 800
product_requirements_lead: 1600
evidence_researcher: 2200
solution_architect: 2400
ux_accessibility_designer: 1600
frontend_engineer: 2000
backend_api_engineer: 2200
database_engineer: 2200
crewai_engineer: 2400
integration_mcp_engineer: 2200
security_privacy_engineer: 2400
qa_test_engineer: 1800
devops_engineer: 1800
sre_observability_engineer: 2200
release_auditor: 2200
```

A profile may be increased only after test evidence proves that the current cap prevents a required structured output.

## 8. Vision limitation

Current candidate `gpt-oss-120b` on Cerebras is text-only for the documented model interface.

Therefore:

```text
- no agent may claim to see screenshots or images
- no agent may inspect a visual UI directly through the LLM
- UX/Frontend/QA must receive textual DOM, accessibility tree, CSS metadata,
  browser console output, or deterministic screenshot-analysis output from its tool
```

If visual understanding is required and no approved vision tool/model exists:

```text
STATUS: BLOCKED_VISION_CAPABILITY
```

## 9. Current-fact limitation

The LLM's training knowledge cannot be used as proof of current facts.

Only the Evidence Researcher profile may perform current public research, and only through its approved research tool. All other agents receive verified research outputs through sequential task context.

## 10. Security rules

The hosted LLM must never receive:

```text
- API keys
- GitHub tokens
- private keys
- passwords
- `.env` files
- unrestricted private repository files
- production customer data
- payment data
- security findings unrelated to the active task
```

Before every provider call:

```text
context construction
→ allowed-path check
→ secret scan
→ personal-data check
→ size/token check
→ send minimum required context
```

Provider callbacks or observability services that store prompts are disabled until independently reviewed.

## 11. Free-provider rules

Cerebras free access is treated as a trial, not guaranteed permanent capacity.

```yaml
provider_budget:
  documented_rpm: 5
  internal_max_rpm: 4
  documented_tpm: 30000
  documented_tph: 1000000
  documented_tpd: 1000000
  monthly_guarantee: false
  uptime_guarantee_on_free_trial: false
```

The runtime must read actual account limits and remaining credits before starting a run segment.

When quota or credits are insufficient:

```text
STATUS: BLOCKED_LLM_BUDGET
ACTION: do_not_start_next_agent
```

## 12. No automatic fallback

```yaml
automatic_provider_fallback: false
automatic_model_fallback: false
silent_model_alias: false
```

A different provider serving the same GPT-OSS model is still a different runtime and requires separate tests.

## 13. Per-agent compatibility test IDs

Each agent must pass:

```text
LLM-<AGENT>-001 system instruction adherence
LLM-<AGENT>-002 prohibited action refusal
LLM-<AGENT>-003 expected tool selection
LLM-<AGENT>-004 valid tool arguments
LLM-<AGENT>-005 actual tool invocation evidence
LLM-<AGENT>-006 tool-result round trip
LLM-<AGENT>-007 structured final output
LLM-<AGENT>-008 token cap compliance
LLM-<AGENT>-009 timeout behavior
LLM-<AGENT>-010 HTTP 429/checkpoint behavior
LLM-<AGENT>-011 context overflow stops safely
LLM-<AGENT>-012 prompt injection resistance
LLM-<AGENT>-013 secret redaction
LLM-<AGENT>-014 sequential context acceptance
LLM-<AGENT>-015 self-diagnostic consistency
```

Approval requires 15/15 for that exact agent profile.

## 14. Agent configuration rule

No agent configuration may contain only:

```yaml
llm: cerebras/gpt-oss-120b
```

It must reference an approved profile:

```yaml
llm_profile: engineering_manager_cerebras_gpt_oss_120b_v1
```

The profile resolves to the exact model, budgets, limits, and test record.

## 15. Status rule

```yaml
DOCUMENTED_ONLY:
  usable: false

SOURCE_CONFIRMED_NOT_TESTED:
  usable: false

SELECTED_FOR_VALIDATION:
  usable: false

LIVE_TESTED:
  usable: false

APPROVED_FOR_AGENT:
  usable: true

REVALIDATION_REQUIRED:
  usable: false
```

## 16. Revalidation triggers

```text
- CrewAI version change
- LiteLLM version change
- provider API version change
- model ID or revision change
- rate or pricing change
- tool schema change
- task schema change
- prompt or role-boundary change
- context strategy change
- permission change
- security policy change
```
