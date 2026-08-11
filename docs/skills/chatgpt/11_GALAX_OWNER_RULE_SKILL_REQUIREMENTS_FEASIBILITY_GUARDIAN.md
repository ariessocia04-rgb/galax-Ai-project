```yaml
skill_reference: $galax-owner-rule-skill-requirements-feasibility-guardian
skill_id: GALAX-SKILL-11
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 11: Galax Owner Rule / Skill Requirements and Feasibility Guardian

```yaml
skill_name: Galax Owner Rule Skill Requirements and Feasibility Guardian
skill_type: Human_Owner_plain_language_requirements_and_fact_check_gate
active_project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
runtime_agent: false
CrewAI_agent: false
repository_writer: false
implementation_executor: false
approval_authority: false
question_language: Tagalog
saved_rule_language: English
final_authority: Human_Owner
```

## 1. Purpose

This skill is the requirements and feasibility gate used when the Human Owner wants to create, add, change, expand, or restrict a Galax ChatGPT skill, router behavior, supervisory rule, continuity rule, or related control but the exact requirement or storage target is not yet sufficiently clear.

Its job is:

```text
Human Owner describes desired behavior in ordinary language
→ ask only the minimum useful questions in Tagalog
→ never require the Human Owner to write code, commands, YAML, JSON, Git syntax, or repository patches
→ reconstruct the desired allow / block / fallback behavior
→ verify current repository constraints
→ perform a bounded current web fact-check before making a feasibility conclusion
→ prefer official / primary sources for external capability claims
→ distinguish POSSIBLE, POSSIBLE_WITH_CONSTRAINTS, and NOT_POSSIBLE_AS_REQUESTED
→ when not possible, identify the factual reason and the smallest practical remedy or alternative
→ recommend the correct repository destination in plain Tagalog
→ obtain the Human Owner's decision
→ produce the final proposed rule/skill specification in English
→ hand off the exact approved specification to Skill 9 for repository writing
→ stop
```

Skill 11 does not itself write the repository. Skill 9 performs the later exact supervisory repository update after the Human Owner approves the specification.

## 2. Zero-coding-owner rule

The Human Owner is not expected to know coding or Git implementation details.

```yaml
GALAX_ZERO_CODING_OWNER_RULE_V1:
  ask_owner_to_write_code: prohibited
  ask_owner_to_edit_files_manually: prohibited
  ask_owner_to_type_terminal_commands: prohibited
  ask_owner_to_resolve_merge_conflicts_manually: prohibited
  ask_owner_to_design_YAML_or_JSON: prohibited
  ask_owner_to_choose_low_level_implementation_mechanism_without_explanation: prohibited

  owner_expected_actions:
    - state_goal_in_plain_language
    - describe_desired_allowed_behavior
    - describe_desired_blocked_behavior
    - choose_between_plain_language_recommendations
    - authorize_or_reject_a_bounded_action
    - provide_non_coding_business_or_product_decisions
```

If ChatGPT, Cline, another authorized contributor, or an available tool can perform the technical action, the Human Owner must be asked only for authorization or a plain-language decision. Do not transfer the coding work to the Human Owner.

## 3. Activation triggers

Use this skill when the Human Owner says or means:

```text
add a skill but ask me what I want
create a new rule
add another restriction
change how this skill behaves
where should this rule be saved
should this be a ChatGPT skill or GitHub rule
I want a rule but I am not sure where it belongs
check first if this is possible
fact-check this rule before adding it
if it is not possible recommend another way
```

If the Human Owner already supplied an exact, feasible, bounded supervisory change and exact target is clear, route directly to Skill 9 instead of asking unnecessary questions.

## 4. Mandatory Tagalog questioning behavior

Questions to the Human Owner must be in simple Tagalog and must avoid coding jargon unless immediately explained.

Ask only questions that materially affect the rule. Typical sequence, only when needed:

```text
1. Ano mismo ang gusto mong mangyari?
2. Ano ang gusto mong payagan?
3. Ano ang gusto mong awtomatikong i-block?
4. Kailan dapat gumana ang exception o fallback?
5. Kapag hindi puwedeng gawin ang original request, ano ang preferred outcome mo?
6. Gusto mo bang ito ay sariling skill, router rule, supervisory rule, o ipa-recommend mo sa ChatGPT ang tamang lagayan?
```

Do not ask all questions when the current conversation already answers them.
Do not repeat a question the Human Owner already answered.

When the Human Owner does not know the correct repository location, Skill 11 must recommend the destination instead of forcing the owner to guess.

## 5. Repository destination recommendation

Classify the intended destination from purpose, not filename preference alone.

```yaml
GALAX_RULE_DESTINATION_CLASSIFIER_V1:
  ChatGPT_skill:
    typical_path: docs/skills/chatgpt/**
    use_when: behavior_requires_a_distinct_reusable_ChatGPT_workflow_or_gate

  ChatGPT_router:
    typical_path: docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
    use_when: request_changes_skill_selection_or_routing

  supervisory_rule:
    typical_path: docs/rules/**
    use_when: request_defines_cross_skill_executor_authority_or_repository_boundary

  Context_Engineer:
    typical_path: docs/skills/chatgpt/context/**
    use_when: request_changes_verified_context_selection_or_reuse_only

  new_chat_operating_instruction:
    typical_path: docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
    use_when: request_must_be_recovered_in_every_new_or_unverified_chat

  continuity_or_achievement:
    owner: Skill_5
    use_when: request_is_length_problem_or_achievement_persistence
```

The Human Owner may override the recommendation when the requested destination remains compatible with higher-authority repository rules.

## 6. Mandatory fact-check before feasibility conclusion

Skill 11 must not say that a requested capability is possible or impossible from model memory alone.

Required evidence order:

```text
current live Galax repository authority and current tool availability
→ official or primary web documentation for external/current capability claims
→ exact current product/framework/version documentation when material
→ current connector/tool evidence when execution capability depends on the active ChatGPT environment
```

Rules:

1. Perform a bounded web search before the final feasibility conclusion.
2. Prefer official vendor documentation, primary specifications, or primary source repositories.
3. For OpenAI product/API capability claims, use official OpenAI sources.
4. For CrewAI capability claims, use official CrewAI documentation/source for the pinned version when available.
5. For Cline capability claims, prefer official Cline documentation/source and current observed Cline evidence.
6. Do not broaden research beyond what is needed to decide the requested rule.
7. Cite or record the exact factual basis in the feasibility receipt.
8. Never invent an unsupported feature, permission, API, UI control, Git behavior, or tool capability.

If current fact verification cannot be completed:

```text
BLOCKED_FACT_VERIFICATION_UNAVAILABLE
```

Then explain the missing evidence and recommend the smallest verification/remedy path. Do not guess.

## 7. Feasibility classifications

```yaml
GALAX_OWNER_RULE_FEASIBILITY_V1:
  result:
    POSSIBLE |
    POSSIBLE_WITH_CONSTRAINTS |
    NOT_POSSIBLE_AS_REQUESTED |
    BLOCKED_FACT_VERIFICATION_UNAVAILABLE

  requested_behavior:
  repository_constraints: []
  current_tool_constraints: []
  external_facts_verified: []
  unsupported_assumptions_rejected: []
  exact_constraints: []
  recommended_remedy_or_alternative: []
```

For `NOT_POSSIBLE_AS_REQUESTED`, Skill 11 must not stop at "cannot". It must identify, when factually possible:

```text
why it cannot be done exactly as requested
→ what part is still possible
→ what alternative actor/tool/workflow can perform it
→ what rule adjustment would make it feasible
→ what exact Human Owner authorization would be needed
```

## 8. English repository specification output

After the Human Owner's requirements and feasibility are sufficiently clear, produce the repository-ready specification in English even though questions and explanations to the owner are in Tagalog.

Required receipt:

```yaml
GALAX_OWNER_RULE_SKILL_REQUIREMENTS_RECEIPT_V1:
  Human_Owner_request:
  questions_asked_in_Tagalog: []
  owner_answers_preserved: []
  exact_goal:
  allowed_behavior: []
  prohibited_behavior: []
  trigger_conditions: []
  fallback_conditions: []
  requested_or_recommended_destination:
  destination_reason:
  feasibility_result:
  repository_evidence: []
  web_or_primary_source_evidence: []
  current_tool_capability_evidence: []
  remedy_if_needed: []
  English_rule_or_skill_specification:
  ready_for_Skill_9_write: true | false
  assumptions: []
```

Skill 11 must preserve the Human Owner's intent. Translation into English is not permission to add extra restrictions or capabilities that were never requested.

## 9. Handoff to Skill 9

When the receipt is complete and the Human Owner authorizes the proposed English specification:

```text
Skill 11 stops
→ new router cycle
→ Skill 9 becomes primary
→ Skill 9 writes only the exact approved supervisory target
```

Do not let Skill 11 write the repository directly.
Do not send this supervisory work to Cline.

## 10. Final contract

```text
unclear or exploratory owner rule/skill request
→ Skill 11
→ ask minimal Tagalog questions
→ never ask owner to code
→ live repo verification
→ bounded official/primary web fact-check
→ feasibility classification
→ if impossible, factual remedy/recommendation
→ recommend correct repository destination
→ owner decides/authorizes
→ English repository-ready specification
→ Skill 9 writes in a separate routing cycle
```
