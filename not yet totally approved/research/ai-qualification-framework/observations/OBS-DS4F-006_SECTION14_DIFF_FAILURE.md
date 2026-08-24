# OBS-DS4F-006 — Section 14 diff failure

```yaml
profile_id: CLINE-DS4F-XHIGH-001
short_name: DS4F-XH
task_freshness: FRESH
mode: ACT
requested_action: replace Section 14 only
immediate_instruction_pickup: PASS
tool_selection_compliance: PASS
anchor_compliance: PASS
scope_compliance: PASS
old_task_memory_intrusion: NONE_OBSERVED
semantic_content_accuracy: PASS
patch_serialization_accuracy: FAIL
stop_condition_compliance: PASS
first_failure_stage: T4
review_decision: Reject
repository_change_saved: false
```

Cline read the target file and kept the requested Section 14 scope. The intended replacement text was correct, but the visible diff wrapper was malformed. The SEARCH block did not close cleanly, the separator was escaped, and an unrelated empty code block appeared after the replacement marker.

Remedy: allow one short same-task retry that reuses the exact approved Section 14 text, does not reread the file, shows complete visible SEARCH and REPLACE blocks, keeps control markers outside Markdown fences, and stops for Save or Reject. Start a fresh task if that retry fails.
