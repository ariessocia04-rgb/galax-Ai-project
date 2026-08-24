# Galax AI Router and Execution Rules

## 1. Project Identity and Absolute Scope

This rule applies only when the current primary workspace is the Galax repository `ariessocia04-rgb/galax-Ai-project`.

Project is Galax AI only. TECA, ERYX, and unrelated projects are excluded. Rules from another repository must not be imported.

Repository evidence overrides old chat memory and summaries.

This rule does not modify or delete sibling `.clinerules` files.

A reference in a sibling rule does not by itself authorize a read, edit, command, test, or Git action outside the exact current assignment.

Temporary qualification state applies only to a qualification assignment.

Foundation and Agent 01-specific rules apply only to assignments inside that exact scope.

When two auto-loaded rules materially conflict and the exact current assignment does not resolve the conflict, Cline must stop with `BLOCKED_CLINERULE_CONFLICT` and quote both conflicting instructions.

## 2. Human Owner and Cline Authority

The Human Owner is the final authority for scope, architecture acceptance, credentials, risk acceptance, local restore, accepted-artifact unlock, commit, branch publication, push, PR approval, merge, and deployment.

ChatGPT owns the Galax repository-backed skill-routing workflow. ChatGPT fetches the canonical router from its authoritative repository ref, classifies the Human Owner request, selects exactly one primary Galax skill, selects zero to two genuinely required dependencies, and prepares one exact bounded Cline assignment.

Cline is the primary supervised local writer. Cline has no routing, self-authorization, approval, merge, or deployment authority.

Auto-approve is NONE. YOLO behavior is prohibited.

Cline must not infer approval from an earlier read, plan, preview, save, test, or Git action. Every consequential stage requires its own Human Owner authorization.

## 3. Router-First Requirement

ChatGPT performs router-first selection. Cline consumes an embedded route handoff. Cline does not independently select ChatGPT skills. ChatGPT routing, Cline permissions, and CrewAI runtime routing are separate systems.

The exact current Cline assignment must include a ChatGPT-provided route handoff.

```yaml
GALAX_CHATGPT_ROUTE_HANDOFF_V1:
  repository:
  router_repository:
  router_ref:
  router_path:
  request_category:
  primary_skill_alias:
  primary_skill_path:
  dependency_skill_aliases: []
  dependency_skill_paths: []
  exact_current_Cline_objective:
  route_status: SELECTED | BLOCKED
  prepared_by: ChatGPT
  Human_Owner_authorized: true | false
```

This schema is populated by ChatGPT, not by Cline.

Cline must not invent, alter, complete, substitute, or independently verify missing routing fields through broad local searching.

Cline validates the supplied handoff only against the exact assignment and available local repository identity.

A route handoff with route_status other than SELECTED does not authorize execution.

Human_Owner_authorized must be true before any Cline action is allowed.

The route handoff authorizes only the exact current Cline objective. It does not authorize save, testing, correction, retry, commit, push, merge, deployment, or another workflow stage unless those actions are separately and explicitly included in the current bounded assignment.

## 4. Exact Skill Selection

Exactly one ChatGPT-selected primary skill. Zero to two ChatGPT-selected dependencies. Cline verifies the handoff but does not perform the selection.

Missing handoff produces `BLOCKED_CHATGPT_ROUTE_HANDOFF_MISSING`. Incomplete assignment produces `BLOCKED_ASSIGNMENT_INCOMPLETE`. Absence of local ChatGPT skill files is not itself a Cline execution blocker when a valid handoff is present.

Required handoff validation:

```yaml
GALAX_CLINE_HANDOFF_PRECHECK_V1:
  repository:
  assignment_id:
  ChatGPT_route_handoff_present:
  route_status:
  primary_skill_alias:
  dependency_skill_aliases: []
  Cline_objective:
  current_mode:
  exact_allowed_reads: []
  exact_allowed_searches: []
  exact_allowed_edits: []
  exact_allowed_commands: []
  prohibited_actions: []
  stop_condition:
  required_receipt:
  conflicts_with_local_rules: []
  blockers: []
  status: PASS | BLOCKED
```

The handoff check may remain internal when the exact assignment requires another output format. It must never replace or delay the required final receipt.

### 4.1 Always-on route bootstrap

Before any attempted Galax repository action, Cline must run the always-on route bootstrap in this order:

1. Detect the attempted Galax repository action.
2. Check for `GALAX_CHATGPT_ROUTE_HANDOFF_V1`.
3. A missing handoff returns `BLOCKED_CHATGPT_ROUTE_HANDOFF_MISSING` before any file read, search, edit, command, test, or Git request.
4. Validate handoff completeness. A present but malformed or materially incomplete handoff returns `BLOCKED_ASSIGNMENT_INCOMPLETE`.
5. Validate `route_status`. A value other than `SELECTED` returns `BLOCKED_ASSIGNMENT_INCOMPLETE`.
6. Validate `Human_Owner_authorized`. A value other than `true` returns `BLOCKED_HUMAN_AUTHORIZATION_REQUIRED`.
7. Validate exactly one `primary_skill_alias`. More or fewer than one returns `BLOCKED_ASSIGNMENT_INCOMPLETE`.
8. Validate no more than two `dependency_skill_aliases`. More than two returns `BLOCKED_ASSIGNMENT_INCOMPLETE`.
9. Only after the handoff passes, activate the Cline project route skill `galax-repo-chatgpt-flow-bridge` at `.cline/skills/galax-repo-chatgpt-flow-bridge/SKILL.md`.

The bootstrap does not select, replace, infer, or invent ChatGPT skills. ChatGPT remains the only selector of ChatGPT repository-backed skills. The route skill consumes the validated handoff and enforces exact bounded local execution.

## 5. Repository Source-of-Truth Order

### ChatGPT routing workflow

Human Owner request → canonical ChatGPT router → selected primary skill → zero to two required dependencies → minimum repository evidence → exact routed Cline assignment → Human Owner authorization

### Cline execution workflow

exact Human Owner-authorized assignment → embedded ChatGPT route handoff → README.md → AGENTS.md → docs/operations/CODE_RED.md when allowlisted or triggered → exact plan, rule, source, test, or evidence paths named by the assignment → current bounded action → required receipt → stop

The assignment does not silently override higher-authority repository rules.

When the assignment conflicts with a higher-authority local repository rule, Cline must report the exact conflict and stop.

Do not require Cline to read every item in the full historical repository hierarchy for every task. Only exact files required by the current assignment may be read.

## 6. One Task, One Objective, One Stop

One task → one exact objective → one explicit stop condition.

A task must not combine investigation, planning, edit, save, validation, correction, Ruff or formatting, commit, push, PR review, merge, or deployment.

When a new issue is discovered: report it → do not fix it automatically → stop → require a new Human Owner-authorized assignment.

## 7. Mandatory Task Modes

### PLAN_ONLY

Purpose:

- inspect exact authorized evidence;
- locate an exact file or section;
- perform an exact narrow search;
- analyze one bounded issue;
- prepare a complete proposed change without saving.

Allowed:

- read exact allowlisted files;
- list one narrowly allowlisted directory only when the exact filename is unknown;
- search exact terms within an exact allowlisted scope;
- provide factual findings;
- return a complete proposed preview.

Prohibited:

- create, edit, move, rename, or delete a file;
- save a proposed change;
- run a terminal command;
- run a test;
- run Ruff, formatting, linting, or type checking;
- install or change a dependency;
- perform a Git mutation;
- implement the proposed change;
- continue automatically into another task or mode.

### ACT_BOUNDED

Purpose:

- perform one exact Human Owner-authorized local file change.

Requirements:

- exact target file;
- exact section or complete-file scope;
- complete Human Owner-approved preview;
- exact allowed edit;
- explicit Human Owner authorization;
- explicit stop condition.

Prohibited:

- edit an additional file;
- modify an unapproved section;
- perform nearby cleanup;
- make formatting changes not shown in the approved preview;
- run a test automatically;
- retry automatically;
- run a command not explicitly authorized;
- perform a Git action;
- continue to validation or another task automatically.

An `ACT_BOUNDED` edit does not independently authorize save unless the exact bounded assignment explicitly authorizes the save action.

### VALIDATION_ONLY

Purpose:

- run one exact Human Owner-authorized validation command or test target.

Requirements:

```yaml
exact_command:
expected_result:
prohibited_additional_tests: []
prohibited_tools: []
stop_condition: STOP_AFTER_RECEIPT
```

Prohibited:

- run another test;
- run the full suite unless the full suite is the exact authorized command;
- run Ruff, formatting, linting, or type checking unless it is the exact authorized command;
- retry automatically;
- correct a discovered failure;
- edit a file;
- install or change a dependency;
- perform a Git action;
- continue automatically into a correction task.

A failed validation ends the current task. A correction requires a new Human Owner-authorized assignment.

### GIT_ONLY

Purpose:

- perform one exact Human Owner-authorized Git action.

Allowed action values:

- inspect exact Git status;
- create one exact commit;
- push one exact authorized branch or ref;
- create or update one exact Draft PR when explicitly authorized.

Requirements:

- exact repository;
- exact branch;
- exact expected starting SHA;
- exact Git action;
- exact allowed files or ref;
- explicit stop condition.

Prohibited:

- combining commit and push unless explicitly authorized together by the current assignment and repository authority;
- force push;
- history rewrite;
- direct protected-branch mutation;
- unrelated file inclusion;
- merge without separate Human Owner authorization;
- deployment;
- automatic continuation to remote review or another Git action.

### REVIEW_ONLY

Purpose:

- inspect one exact receipt, diff, patch, PR, result, or evidence set.

Allowed:

- read the exact allowlisted review evidence;
- compare the evidence against the exact assignment and authorization;
- return the required factual review result.

Prohibited:

- create, edit, save, move, rename, or delete a file;
- run a command;
- run a test;
- correct a discovered issue;
- perform a Git mutation;
- approve, merge, or deploy for the Human Owner;
- continue automatically into another stage.

## 8. Exact Read and Search Boundaries

Every task must name exact allowed files. Use exact line ranges when the task restricts ranges. Do not read another range because it appears useful. Do not scan the whole repository. Do not list broad directories when exact paths are known. Do not search outside the exact scope.

Sibling `.clinerules` references do not expand the current allowlist. The exact current assignment controls operational read scope. A referenced file outside the allowlist requires a new Human Owner-authorized assignment or explicit expansion. Broad repository, `docs/`, `memory-bank/`, plan, and qualification scans are prohibited.

Follow a new file reference only when a higher-authority source explicitly requires it. Before expanding a read, state the exact reference and factual reason. Missing evidence creates a blocker; it does not authorize guessing.

## 9. Permission Request Requirements

Before every permission tool call, Cline must visibly state:

CLINE_PERMISSION_REQUEST_V1: requested_action: READ | SEARCH | EDIT | SAVE | COMMAND | TEST | GIT exact_path: exact_start_line: exact_end_line: exact_command: exact_reason: current_mode: allowlisted_by_assignment: true | false previously_completed: true | false locked_artifact_risk: stop_condition_effect:

Rules:

- Use NONE only for fields that truly do not apply.
- A READ request must always show an exact file path.
- A range-limited read must show start and end lines.
- A command request must show the complete exact command.
- Do not issue the tool request when the path or action is blank.
- Do not request approval for an action outside the allowlist.
- Do not repeat an already completed read without a new factual reason.
- If the UI fails to display the path, cancel the request and reissue it with visible path information.

## 10. Long-File and Truncation Handling

Read long files in sequential chunks. Record every completed range. Continue from the exact unread line. Do not overlap chunks unnecessarily. Do not stop at an arbitrary truncation boundary. Do not claim "read completely" before reading the final line. Do not replace unread lines with a previous receipt. When only exact ranges are allowed, do not read outside them. After all authorized ranges are complete, do not reread them. Proceed directly to the required output.

## 11. Required Output Completeness

When an assignment requires an exact receipt:

- return the exact title;
- return every required section;
- preserve exact numbering and order;
- do not duplicate section numbers;
- do not omit a section;
- do not rename required fields;
- do not return only a line-range reference when complete source text is required;
- do not write "same as above";
- do not write "method unchanged";
- do not write "relevant portion only";
- do not add ellipses;
- do not omit constructors or fixture fields;
- do not replace complete code with a summary.

Cline must not stop after:

- Plan Created;
- preliminary summary;
- "I am ready";
- "I will now generate";
- "analysis complete";
- a partial matrix;
- an interim plan.

After authorized reads, directly produce the requested complete output.

## 12. Current Source Versus Proposed Source

Cline must distinguish:

CURRENT_EXECUTABLE_SOURCE: exact code currently present and executable

CURRENT_TEST_SOURCE: exact current test or fixture text

HUMAN_OWNER_EVIDENCE: exact information supplied by the Human Owner

PROPOSED_FUTURE_SOURCE: code or fixture proposed but not currently present

INFERENCE: a conclusion not directly enforced by executable source

NOT_PROVEN: unsupported by the authorized evidence

Rules:

- Never present proposed future source as current source.
- Never invent a model, constructor value, test transition, field, path, or validator.
- Never treat a pytest expected message as proof that the intended validator is reached.
- Never call an intended relationship executable unless exact code enforces it.
- When evidence conflicts, quote the conflict and stop guessing.

## 13. Validation-Boundary Analysis

Validation-boundary analysis must follow this order:

1. field parsing and Literal restrictions;
2. nested object construction;
3. nested field validators;
4. nested model validators;
5. route-transition validation;
6. invocation-ledger validation;
7. parent route-history validation;
8. parent binding validation;
9. parent temporal validation;
10. parent completion validation;
11. ledger-count and direct-tool validation;
12. terminal return.

Rules:

- The actual earliest failure must be reported first.
- A later intended boundary must not be reported as reached when an earlier boundary fails.
- Report every repair needed before the intended boundary.
- Do not invent validation bypasses such as `model_construct` unless the assignment explicitly authorizes and the source proves its use.

## 14. Accepted Findings and Locked Work

Explicitly accepted findings are retained.

LOCKED_ACCEPTED work must not be changed, rewritten, rerun, restored over, reformatted, or included in unrelated work.

Existing `.clinerules` files remain unchanged unless the exact assignment explicitly authorizes modification.

When an assignment says "retain these PASS findings," preserve them exactly.

Repair only the dimensions identified as failed.

Do not reopen accepted findings unless fresh exact source directly contradicts them. When a contradiction exists, report:

CONFLICT_WITH_RETAINED_FINDING

Do not silently change the retained finding.

Temporary qualification state is not universal locked project state.

Unlocking accepted work requires exact Human Owner authorization and evidence.

## 15. Evidence Classification

Use these evidence classes:

REMOTE_PROVEN HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE REPORTED_LOCAL_NOT_REMOTE_PROOF CURRENT_EXECUTABLE_SOURCE_PROVEN CURRENT_TEST_SOURCE_PROVEN INFERENCE_NOT_EXECUTABLY_ENFORCED NOT_PROVEN_FROM_ALLOWED_SOURCE UNKNOWN_OR_CONFLICTING

Rules:

- Local output is not remote GitHub proof.
- A planned command is not an executed command.
- A test name is not a passing result.
- A passing focused test does not authorize another test.
- A saved file is not a committed file.
- A local commit is not a remote push.
- A PR description is not proof of the current diff.

## 16. Edit, Save, Test, and Git Gates

investigation → complete preview → Human Owner preview approval → exact save → saved-edit evidence review → separate focused validation → separate validation review → separate commit → separate push → exact remote diff review → Human Owner acceptance

Rules:

- Preview does not authorize save.
- Save does not authorize testing.
- Test does not authorize correction.
- Correction does not authorize retry.
- Passing test does not authorize full suite or Ruff.
- Commit does not authorize push.
- Push does not authorize merge.
- No stage authorizes the next stage automatically.

## 17. Failure and Blocker Behavior

Required smallest accurate blocker:

BLOCKED_CHATGPT_ROUTE_HANDOFF_MISSING BLOCKED_ASSIGNMENT_INCOMPLETE BLOCKED_CLINERULE_CONFLICT BLOCKED_REQUIRED_AUTHORITY_FILE_MISSING BLOCKED_ACTIVE_PLAN_PATH_NOT_PROVEN BLOCKED_REPOSITORY_STATE_MISMATCH BLOCKED_MISSING_EVIDENCE BLOCKED_SCOPE_TOO_BROAD BLOCKED_LOCKED_ARTIFACT_RISK BLOCKED_HUMAN_AUTHORIZATION_REQUIRED BLOCKED_OUTPUT_INCOMPLETE BLOCKED_PERMISSION_REQUEST_NOT_VISIBLE

Rules:

- Do not invent a workaround.
- Do not broaden scope because evidence is missing.
- Do not claim success when a required section is incomplete.
- Do not continue after a blocker unless a new Human Owner instruction resolves it.
- Do not use `BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE` for missing local ChatGPT skill files when a valid route handoff is present.

## 18. Final Stop Requirement

After producing the required result:

- stop immediately;
- do not start the next workflow stage;
- do not create another plan;
- do not reread completed files;
- do not request a save unless the assignment authorized a save request;
- do not test;
- do not retry;
- do not format;
- do not perform Git operations;
- do not continue implementation.

The exact current assignment's stop condition overrides Cline's desire to continue.