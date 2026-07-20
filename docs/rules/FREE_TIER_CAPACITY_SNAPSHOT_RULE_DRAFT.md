# Free-Tier Capacity Snapshot Rule — Draft

**Status:** `DRAFT_MUTABLE`

## 1. Core rule

Published model capacity is not automatically the usable free-tier capacity.

Before every run group, Galax must capture or conservatively derive the connected account's current provider capacity.

```text
effective capacity = minimum(
  model capability,
  plan/account capability,
  current organization limits,
  temporary provider reductions,
  Galax internal safety ceiling
)
```

## 2. Required snapshot

```yaml
ProviderCapacitySnapshot:
  provider:
  model_id:
  account_or_organization_id_hash:
  captured_at:
  api_version:
  model_context_window:
  account_context_window:
  effective_context_window:
  maximum_output_tokens:
  requests_per_minute:
  requests_per_day:
  tokens_per_minute:
  tokens_per_day:
  temporary_reduction_detected:
  source_links: []
  live_probe_results: []
  status:
```

## 3. Cerebras correction

Current official Cerebras pages expose two relevant values:

```text
model metadata: up to 131,072 tokens
free-tier pricing statement: 8,192-token context
```

Until the connected account and API Version 2 are tested:

```yaml
cerebras_capacity_status: BLOCKED_CAPACITY_UNKNOWN
provisional_effective_total_context: 8192
allow_12000_to_20000_input_context: false
```

The previous Galax 12K/16K input soft limits and 20K input hard limit are suspended for free-tier execution.

## 4. Prompt budget computation

The Flow computes a per-call budget after accounting for:

```text
system rules
+ task contract
+ memory context
+ LearningPacket
+ repository excerpts
+ tool schema
+ prior structured output
+ expected reasoning tokens
+ expected final output
+ safety margin
```

If the total exceeds the effective context:

```yaml
status: BLOCKED_CONTEXT_LIMIT
remedy:
  - reduce irrelevant context deterministically
  - split study or execution into checkpointed segments
  - reuse evidence by ID and hash
  - never silently summarize exact rules, paths, commands, or security constraints
```

## 5. Output cap rule

Agent output caps are upper policies, not guaranteed usable values. The runtime must calculate:

```text
actual_max_output = minimum(
  agent_profile_output_cap,
  provider_account_output_limit,
  remaining_effective_context_after_input_and_reasoning,
  remaining_run_token_budget
)
```

If the result is below the task's minimum required output:

```text
STATUS: BLOCKED_INSUFFICIENT_LLM_CAPACITY
```

## 6. Rate-limit rule

Do not use published base limits as permanent guarantees.

```text
effective_rpm = minimum(
  Galax internal RPM ceiling,
  current account RPM minus headroom
)
```

The provider's `Retry-After` or equivalent response controls retry timing. Only one Galax-level retry is permitted; provider SDK retries must be configured so total retries remain bounded.

## 7. Approval tests

```text
CAP-001 Capture primary provider limits.
CAP-002 Capture fallback provider limits.
CAP-003 Test effective context boundary.
CAP-004 Test maximum output boundary.
CAP-005 Confirm tool schema fits.
CAP-006 Confirm strict structured output fits.
CAP-007 Reject oversized LearningPacket.
CAP-008 Split a task into checkpointed segments.
CAP-009 Handle HTTP 429 without retry storm.
CAP-010 Record actual usage after each call.
```

Approval requires 10 of 10 tests.
