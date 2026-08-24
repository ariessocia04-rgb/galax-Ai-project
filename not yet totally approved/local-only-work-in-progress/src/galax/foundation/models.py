import unicodedata
from datetime import datetime
from pathlib import PurePosixPath, PureWindowsPath
from typing import Annotated, Literal
from uuid import UUID

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)


# --- Scalar alias validators ---

def _strict_text_validator(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("StrictText requires str input")
    if not value:
        raise ValueError("StrictText must not be empty")
    if value[0].isspace():
        raise ValueError("StrictText must not begin with whitespace")
    if value[-1].isspace():
        raise ValueError("StrictText must not end with whitespace")
    for char in value:
        if unicodedata.category(char) == "Cc":
            raise ValueError("StrictText must not contain Unicode control characters")
    return value


def _sha256_hex_validator(value: object) -> str:
    value = _strict_text_validator(value)
    if len(value) != 64:
        raise ValueError("SHA256Hex must be exactly 64 characters")
    allowed = "0123456789abcdef"
    for char in value:
        if char not in allowed:
            raise ValueError("SHA256Hex must contain only lowercase hexadecimal characters")
    return value


def _git_sha40_validator(value: object) -> str:
    value = _strict_text_validator(value)
    if len(value) != 40:
        raise ValueError("GitSHA40 must be exactly 40 characters")
    allowed = "0123456789abcdef"
    for char in value:
        if char not in allowed:
            raise ValueError("GitSHA40 must contain only lowercase hexadecimal characters")
    return value


def _repository_id_validator(value: object) -> str:
    value = _strict_text_validator(value)
    if value.count("/") != 1:
        raise ValueError("RepositoryId must contain exactly one slash")
    owner, repo = value.split("/", 1)
    _strict_text_validator(owner)
    _strict_text_validator(repo)
    return value


def _aware_datetime_validator(value: object) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("AwareDatetime requires datetime input")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("AwareDatetime must be timezone-aware")
    return value


# Locked scalar aliases
StrictText = Annotated[str, BeforeValidator(_strict_text_validator)]
EvidenceId = Annotated[str, BeforeValidator(_strict_text_validator)]
SHA256Hex = Annotated[str, BeforeValidator(_sha256_hex_validator)]
GitSHA40 = Annotated[str, BeforeValidator(_git_sha40_validator)]
RepositoryId = Annotated[str, BeforeValidator(_repository_id_validator)]
AwareDatetime = Annotated[datetime, BeforeValidator(_aware_datetime_validator)]


# --- Locked Literal types ---

OverallStatus = Literal["PASS", "BLOCKED", "FAIL"]
CheckStatus = Literal["PASS", "BLOCKED", "FAIL"]
InvocationStatus = Literal["STARTED", "SUCCEEDED", "BLOCKED", "FAILED"]
InvocationOperation = Literal[
    "repository_preflight_tool",
]
UnsupportedClaimReason = Literal["no_invocation_evidence", "fabricated", "out_of_scope"]
AgentNextTransition = Literal["STOP", "HUMAN_REVIEW"]
MissingEvidenceReason = Literal["ABSENT", "UNTRUSTED", "MISMATCHED", "EXPIRED"]
BlockerStatus = Literal["OPEN", "RESOLVED"]
PermissionName = Literal["contents", "pull_requests", "workflows", "administration"]
PermissionLevel = Literal["none", "read", "write", "admin"]
PermissionSource = Literal["OFFLINE_DECLARATION", "LIVE_GATEWAY"]
LLMInvocationStatus = Literal[
    "STARTED",
    "SUCCEEDED",
    "BLOCKED",
    "FAILED",
]
ToolAvailabilityStatus = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]
LLMProfileReadinessStatus = Literal[
    "APPROVED",
    "BLOCKED",
]
FlowRunStatus = Literal[
    "ACTIVE",
    "PAUSED",
    "BLOCKED",
    "FAILED",
    "COMPLETED",
]
HumanDecisionValue = Literal[
    "APPROVED",
    "REJECTED",
]
LLMReadinessFailure = Literal[
    "PROFILE_MISSING",
    "PROFILE_DISABLED",
    "PROVIDER_NOT_LIVE_TESTED",
    "AGENT_PROFILE_NOT_APPROVED",
    "AGENT_PROFILE_MISMATCH",
    "DATA_CLASSIFICATION_NOT_ALLOWED",
    "CREDENTIAL_MISSING",
    "CAPACITY_SNAPSHOT_INVALID",
]
FlowRoute = Literal[
    "initial",
    "manifest_valid",
    "manifest_blocked",
    "preflight_tool_available",
    "preflight_tool_unavailable",
    "preflight_requires_evaluation",
    "preflight_failed",
    "preflight_evidence_missing",
    "llm_profile_approved",
    "llm_profile_blocked",
    "human_review_required",
    "agent_recommends_stop",
    "agent_evaluation_failed",
    "human_decision_pending",
    "human_decision_approved",
    "human_decision_rejected",
    "foundation_completed",
]


# --- Models ---

class RunManifest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    repository_id: RepositoryId
    repository_root: StrictText
    expected_branch: StrictText
    expected_head_sha: GitSHA40
    approved_agent_ids: tuple[Literal["engineering_manager"], ...]
    approved_llm_profile_id: StrictText
    approved_tool_profile_id: StrictText
    allowed_paths: tuple[StrictText, ...]
    protected_paths: tuple[StrictText, ...]
    data_classification: Literal["public", "private_scoped", "sensitive_restricted"]
    phase_authorization: Literal["PHASE_0", "PHASE_1"]
    requires_live_github_access: bool
    github_permission_evidence_id: EvidenceId | None
    created_at: AwareDatetime

    @field_validator("repository_root", mode="before")
    @classmethod
    def validate_repository_root(cls, value: object) -> str:
        value = _strict_text_validator(value)
        if not value:
            raise ValueError("repository_root must not be empty")
        if not (
            PurePosixPath(value).is_absolute()
            or PureWindowsPath(value).is_absolute()
        ):
            raise ValueError("repository_root must be an absolute path")
        normalized = value.replace("\\", "/")
        parts = [p for p in normalized.split("/") if p]
        if ".." in parts:
            raise ValueError("repository_root must not contain path traversal")
        return value

    @field_validator("allowed_paths", mode="before")
    @classmethod
    def validate_allowed_paths(cls, value: object) -> tuple[str, ...]:
        if not isinstance(value, (list, tuple)):
            raise ValueError("allowed_paths must be a list or tuple")
        result: list[str] = []
        seen: set[str] = set()
        for path in value:
            strict = _strict_text_validator(path)
            if strict in seen:
                raise ValueError(f"allowed_paths contains duplicate: {strict}")
            seen.add(strict)
            result.append(strict)
        return tuple(result)

    @field_validator("protected_paths", mode="before")
    @classmethod
    def validate_protected_paths(cls, value: object) -> tuple[str, ...]:
        if not isinstance(value, (list, tuple)):
            raise ValueError("protected_paths must be a list or tuple")
        result: list[str] = []
        seen: set[str] = set()
        for path in value:
            strict = _strict_text_validator(path)
            if strict in seen:
                raise ValueError(f"protected_paths contains duplicate: {strict}")
            seen.add(strict)
            result.append(strict)
        return tuple(result)

    @field_validator("approved_agent_ids", mode="before")
    @classmethod
    def validate_approved_agent_ids(
        cls,
        value: object,
    ) -> tuple[Literal["engineering_manager"], ...]:
        if isinstance(value, list):
            value = tuple(value)
        if value != ("engineering_manager",):
            raise ValueError(
                "approved_agent_ids must equal exactly "
                "('engineering_manager',)"
            )
        return ("engineering_manager",)

    @model_validator(mode="after")
    def validate_live_github_evidence(self) -> "RunManifest":
        if self.requires_live_github_access:
            if self.github_permission_evidence_id is None:
                raise ValueError(
                    "github_permission_evidence_id is required when "
                    "requires_live_github_access is true"
                )
        else:
            if self.github_permission_evidence_id is not None:
                raise ValueError(
                    "github_permission_evidence_id must be None when "
                    "requires_live_github_access is false"
                )
        return self

    @model_validator(mode="after")
    def validate_path_sets(self) -> "RunManifest":
        allowed = set(self.allowed_paths)
        protected = set(self.protected_paths)
        overlap = allowed & protected
        if overlap:
            raise ValueError(f"allowed_paths and protected_paths must not overlap: {overlap}")
        return self


class PermissionGrant(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    permission_name: PermissionName
    level: PermissionLevel
    source: PermissionSource


class OfflinePermissionDeclaration(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    evidence_id: EvidenceId
    profile_id: StrictText
    repository_id: RepositoryId
    grants: tuple[PermissionGrant, ...]
    prohibited_permissions_present: tuple[PermissionName, ...]
    checked_at: AwareDatetime
    expires_at: AwareDatetime | None

    @model_validator(mode="after")
    def validate_grants(self) -> "OfflinePermissionDeclaration":
        names = [g.permission_name for g in self.grants]
        if len(names) != len(set(names)):
            raise ValueError("permission_name values in grants must be unique")
        for grant in self.grants:
            if grant.source != "OFFLINE_DECLARATION":
                raise ValueError("every grant.source must equal 'OFFLINE_DECLARATION'")
        if self.expires_at is not None and self.expires_at < self.checked_at:
            raise ValueError("expires_at must be greater than or equal to checked_at")
        return self


class LiveGitHubPermissionEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    evidence_id: EvidenceId
    authenticated_identity: StrictText
    target_repository: RepositoryId
    repository_access_confirmed: bool
    contents_permission: PermissionGrant
    pull_requests_permission: PermissionGrant
    workflows_permission: PermissionGrant
    administration_permission: PermissionGrant
    checked_at: AwareDatetime

    @model_validator(mode="after")
    def validate_permissions(self) -> "LiveGitHubPermissionEvidence":
        mapping = [
            (self.contents_permission, "contents"),
            (self.pull_requests_permission, "pull_requests"),
            (self.workflows_permission, "workflows"),
            (self.administration_permission, "administration"),
        ]
        for grant, expected in mapping:
            if grant.permission_name != expected:
                raise ValueError(f"permission_name must equal '{expected}' for {expected}_permission")
            if grant.source != "LIVE_GATEWAY":
                raise ValueError("every permission source must equal 'LIVE_GATEWAY'")
        return self


class EvidenceRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    evidence_id: EvidenceId
    source: Literal[
        "GalaxFoundationFlow",
        "RepositoryPreflightTool",
        "GitHubRepositoryGateway",
        "LLMProfileReadinessGate",
    ]
    content_hash: SHA256Hex
    created_at: AwareDatetime
    run_id: UUID
    task_id: StrictText
    agent_id: StrictText
    expires_at: AwareDatetime | None = None

    @model_validator(mode="after")
    def validate_expiry_window(self) -> "EvidenceRecord":
        if self.expires_at is not None and self.expires_at < self.created_at:
            raise ValueError("expires_at must not be earlier than created_at")
        return self


class MissingEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    check_id: StrictText
    expected_evidence_id: EvidenceId | None
    reason: MissingEvidenceReason
    exact_remedy: StrictText


class BlockerRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    blocker_id: EvidenceId
    code: StrictText
    reason: StrictText
    exact_remedy: StrictText
    related_evidence_ids: tuple[EvidenceId, ...]
    status: BlockerStatus
    created_at: AwareDatetime
    resolved_at: AwareDatetime | None

    @model_validator(mode="after")
    def validate_resolved_at(self) -> "BlockerRecord":
        if self.status == "OPEN" and self.resolved_at is not None:
            raise ValueError("resolved_at must be None when status is OPEN")
        if self.status == "RESOLVED":
            if self.resolved_at is None:
                raise ValueError("resolved_at is required when status is RESOLVED")
            elif self.resolved_at < self.created_at:
                raise ValueError(
                    "resolved_at must be greater than or equal to created_at"
                )
        return self


class RepositoryPreflightCheck(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    check_id: StrictText
    status: CheckStatus
    evidence_id: EvidenceId | None
    redacted_summary: StrictText
    exact_remedy: StrictText | None

    @model_validator(mode="after")
    def validate_status_contract(self) -> "RepositoryPreflightCheck":
        if self.status == "PASS":
            if self.evidence_id is None:
                raise ValueError("evidence_id is required when status is PASS")
            if self.exact_remedy is not None:
                raise ValueError("exact_remedy must be None when status is PASS")
        else:  # BLOCKED or FAIL
            if self.exact_remedy is None:
                raise ValueError("exact_remedy is required when status is BLOCKED or FAIL")
        return self


class ToolInvocationRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    invocation_id: UUID
    run_id: UUID
    task_id: StrictText
    owner: Literal["GalaxFoundationFlow"]
    tool_profile_id: StrictText
    operation: InvocationOperation
    input_hash: SHA256Hex
    started_at: AwareDatetime
    finished_at: AwareDatetime | None
    status: InvocationStatus
    raw_output_hash: SHA256Hex | None
    affected_resources: tuple[StrictText, ...]
    external_evidence_ids: tuple[EvidenceId, ...]
    error_code: StrictText | None
    redacted_error_summary: StrictText | None

    @model_validator(mode="after")
    def validate_status_contract(self) -> "ToolInvocationRecord":
        if self.status == "STARTED":
            if self.finished_at is not None:
                raise ValueError("finished_at must be None when status is STARTED")
        else:  # SUCCEEDED, BLOCKED, FAILED
            if self.finished_at is None:
                raise ValueError("finished_at is required when status is not STARTED")
            if self.finished_at < self.started_at:
                raise ValueError("finished_at must be greater than or equal to started_at")
        if self.status == "SUCCEEDED" and self.raw_output_hash is None:
            raise ValueError("raw_output_hash is required when status is SUCCEEDED")
        if self.status == "FAILED":
            if self.error_code is None:
                raise ValueError("error_code is required when status is FAILED")
            if self.redacted_error_summary is None:
                raise ValueError("redacted_error_summary is required when status is FAILED")
        return self


class InvocationLedger(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    records: tuple[ToolInvocationRecord, ...] = Field(default_factory=tuple)
    llm_records: tuple["LLMInvocationRecord", ...] = Field(default_factory=tuple)

    @model_validator(mode="after")
    def validate_unique_invocation_ids(self) -> "InvocationLedger":
        all_records = list(self.records) + list(self.llm_records)
        invocation_ids = [record.invocation_id for record in all_records]
        if len(invocation_ids) != len(set(invocation_ids)):
            raise ValueError("every invocation_id must be unique across tool and LLM records")
        return self

    @model_validator(mode="after")
    def validate_preflight_tool_count(self) -> "InvocationLedger":
        preflight_count = sum(
            1 for r in self.records
            if r.operation == "repository_preflight_tool"
        )
        if preflight_count > 1:
            raise ValueError("repository_preflight_tool invocation count must not exceed 1 per run")
        return self

    @model_validator(mode="after")
    def validate_llm_count(self) -> "InvocationLedger":
        if len(self.llm_records) > 1:
            raise ValueError("engineering_manager LLM invocation count must not exceed 1 per run")
        return self

    @model_validator(mode="after")
    def validate_tool_llm_separation(self) -> "InvocationLedger":
        for record in self.records:
            if getattr(record, "task_id", None) == "evaluate_preflight_result" and getattr(record, "agent_id", None) == "engineering_manager":
                raise ValueError("LLM operation must not be represented as ToolInvocationRecord")
        for record in self.llm_records:
            if getattr(record, "operation", None) == "repository_preflight_tool":
                raise ValueError("tool operation must not be represented as LLMInvocationRecord")
        return self

    @model_validator(mode="after")
    def validate_agent_zero_direct_tools(self) -> "InvocationLedger":
        for record in self.records:
            if getattr(record, "owner", None) != "GalaxFoundationFlow":
                raise ValueError("Agent 01 must have zero direct tool calls")
        return self


class RepositoryPreflightResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    overall_status: OverallStatus
    checks: tuple[RepositoryPreflightCheck, ...]
    blocking_reasons: tuple[BlockerRecord, ...]
    invocation_id: UUID
    input_hash: SHA256Hex
    result_hash: SHA256Hex

    @model_validator(mode="after")
    def validate_overall_status(self) -> "RepositoryPreflightResult":
        check_statuses = [c.status for c in self.checks]
        if self.overall_status == "PASS":
            if any(s != "PASS" for s in check_statuses):
                raise ValueError("PASS requires all checks to be PASS")
            if self.blocking_reasons:
                raise ValueError("PASS requires blocking_reasons to be empty")
        elif self.overall_status == "BLOCKED":
            has_blocked = any(s == "BLOCKED" for s in check_statuses)
            has_open_blocker = any(b.status == "OPEN" for b in self.blocking_reasons)
            if not has_blocked and not has_open_blocker:
                raise ValueError("BLOCKED requires at least one BLOCKED check or OPEN blocker")
            if any(s == "FAIL" for s in check_statuses):
                raise ValueError("BLOCKED must not contain FAIL checks")
        elif self.overall_status == "FAIL":
            if not any(s == "FAIL" for s in check_statuses):
                raise ValueError("FAIL requires at least one FAIL check")
        for blocker in self.blocking_reasons:
            if blocker.status != "OPEN":
                raise ValueError("blocking_reasons must contain only OPEN blockers")
        check_ids = [c.check_id for c in self.checks]
        if len(check_ids) != len(set(check_ids)):
            raise ValueError("check_id values must be unique within checks")
        return self


class SupportedClaim(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    statement: StrictText
    evidence_id: EvidenceId


class UnsupportedClaim(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    statement: StrictText
    reason: UnsupportedClaimReason


class AgentTaskResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    agent_id: Literal["engineering_manager"]
    direct_tool_calls: Literal[0]
    task_id: Literal["evaluate_preflight_result"]
    status: OverallStatus
    summary: StrictText
    supported_claims: tuple[SupportedClaim, ...]
    unsupported_claims: tuple[UnsupportedClaim, ...]
    next_transition: AgentNextTransition
    exact_remedies: tuple[StrictText, ...]
    preflight_invocation_id: UUID
    preflight_result_hash: SHA256Hex
    llm_invocation_id: UUID
    llm_profile_id: StrictText
    output_hash: SHA256Hex

    @model_validator(mode="after")
    def validate_agent_identity(self) -> "AgentTaskResult":
        if self.agent_id != "engineering_manager":
            raise ValueError("agent_id must equal 'engineering_manager'")
        if self.direct_tool_calls != 0:
            raise ValueError("direct_tool_calls must equal 0")
        return self

    @model_validator(mode="after")
    def validate_status_contract(self) -> "AgentTaskResult":
        if self.status == "PASS":
            if self.next_transition != "HUMAN_REVIEW":
                raise ValueError("PASS requires next_transition to be HUMAN_REVIEW")
            if not self.supported_claims:
                raise ValueError("PASS requires at least one supported_claim")
            if self.unsupported_claims:
                raise ValueError("PASS requires unsupported_claims to be empty")
            if self.exact_remedies:
                raise ValueError("PASS requires exact_remedies to be empty")
        elif self.status == "BLOCKED":
            if self.next_transition != "HUMAN_REVIEW":
                raise ValueError("BLOCKED requires next_transition to be HUMAN_REVIEW")
            if not self.exact_remedies:
                raise ValueError("BLOCKED requires at least one exact_remedy")
        elif self.status == "FAIL":
            if self.next_transition != "STOP":
                raise ValueError("FAIL requires next_transition to be STOP")
            if not self.exact_remedies:
                raise ValueError("FAIL requires at least one exact_remedy")
        return self


class HumanReviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    request_id: UUID
    run_id: UUID
    preflight_invocation_id: UUID
    agent_llm_invocation_id: UUID
    preflight_result_hash: SHA256Hex
    agent_task_result_hash: SHA256Hex
    requested_action: Literal["REVIEW_FOUNDATION_EVIDENCE"]
    current_status: Literal["AWAITING_HUMAN_REVIEW"]
    confirmed_evidence: tuple[EvidenceId, ...]
    missing_evidence: tuple[MissingEvidence, ...]
    risks: tuple[StrictText, ...]
    recommended_next_step: Literal["AWAIT_AUTHENTICATED_HUMAN_DECISION"]
    prohibited_next_steps: tuple[
        Literal[
            "merge_to_main_or_master",
            "deployment",
            "activation_of_Agents_02_to_15",
            "enabling_unvalidated_LLM_profiles",
        ],
        ...,
    ]
    human_decision: Literal["PENDING"] = "PENDING"
    created_at: AwareDatetime

    @model_validator(mode="after")
    def validate_human_decision(self) -> "HumanReviewRequest":
        if self.human_decision != "PENDING":
            raise ValueError("human_decision must equal 'PENDING'")
        required_prohibited = [
            "merge_to_main_or_master",
            "deployment",
            "activation_of_Agents_02_to_15",
            "enabling_unvalidated_LLM_profiles",
        ]
        actual_list = list(self.prohibited_next_steps)
        if len(actual_list) != len(required_prohibited):
            raise ValueError("prohibited_next_steps must contain exactly the required values")
        for item in required_prohibited:
            if item not in actual_list:
                raise ValueError("prohibited_next_steps must contain exactly the required values")
        unique_count = len(set(actual_list))
        if unique_count != len(actual_list):
            raise ValueError("prohibited_next_steps must not contain duplicates")
        return self


class TrustedRegistries(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    approved_agent_ids: tuple[Literal["engineering_manager"], ...]
    approved_llm_profile_ids: tuple[StrictText, ...]
    approved_tool_profile_ids: tuple[StrictText, ...]
    evidence_records: tuple[EvidenceRecord, ...]
    offline_permission_declarations: tuple[OfflinePermissionDeclaration, ...]
    live_github_permission_evidence: tuple[LiveGitHubPermissionEvidence, ...]

    @model_validator(mode="after")
    def validate_registries(self) -> "TrustedRegistries":
        if self.approved_agent_ids != ("engineering_manager",):
            raise ValueError("approved_agent_ids must equal exactly ('engineering_manager',)")
        for name, registry in [
            ("approved_llm_profile_ids", self.approved_llm_profile_ids),
            ("approved_tool_profile_ids", self.approved_tool_profile_ids),
        ]:
            ids = list(registry)
            if len(ids) != len(set(ids)):
                raise ValueError(f"{name} must contain unique values")
        evidence_ids = [r.evidence_id for r in self.evidence_records]
        if len(evidence_ids) != len(set(evidence_ids)):
            raise ValueError("evidence_records must contain unique evidence_ids")
        offline_ids = [d.evidence_id for d in self.offline_permission_declarations]
        if len(offline_ids) != len(set(offline_ids)):
            raise ValueError("offline_permission_declarations must contain unique evidence_ids")
        live_ids = [e.evidence_id for e in self.live_github_permission_evidence]
        if len(live_ids) != len(set(live_ids)):
            raise ValueError("live_github_permission_evidence must contain unique evidence_ids")
        return self


# --- Contract additions ---

class ManifestValidationResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    status: Literal["PASS", "BLOCKED"]
    evidence_ids: tuple[EvidenceId, ...]
    blocker_ids: tuple[EvidenceId, ...]
    exact_remedy: StrictText | None
    checked_at: AwareDatetime

    @model_validator(mode="after")
    def validate_status_contract(self) -> "ManifestValidationResult":
        if self.status == "PASS":
            if not self.evidence_ids:
                raise ValueError("evidence_ids must not be empty when status is PASS")
            if self.blocker_ids:
                raise ValueError("blocker_ids must be empty when status is PASS")
            if self.exact_remedy is not None:
                raise ValueError("exact_remedy must be None when status is PASS")
        else:
            if not self.blocker_ids:
                raise ValueError("blocker_ids must not be empty when status is BLOCKED")
            if self.exact_remedy is None:
                raise ValueError("exact_remedy is required when status is BLOCKED")
        if len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise ValueError("evidence_ids must not contain duplicates")
        if len(set(self.blocker_ids)) != len(self.blocker_ids):
            raise ValueError("blocker_ids must not contain duplicates")
        return self


class PreflightToolAvailabilityResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    status: ToolAvailabilityStatus
    tool_profile_id: StrictText
    evidence_id: EvidenceId
    exact_remedy: StrictText | None
    checked_at: AwareDatetime

    @model_validator(mode="after")
    def validate_status_contract(self) -> "PreflightToolAvailabilityResult":
        if self.status == "AVAILABLE":
            if self.exact_remedy is not None:
                raise ValueError("exact_remedy must be None when status is AVAILABLE")
        else:
            if self.exact_remedy is None:
                raise ValueError("exact_remedy is required when status is UNAVAILABLE")
        return self


class LLMProfileReadinessResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_id: UUID
    status: LLMProfileReadinessStatus
    profile_id: StrictText
    profile_defined: bool
    profile_enabled: bool
    provider_live_tested: bool
    agent_profile_approved: bool
    profile_matches_engineering_manager: bool
    data_classification_allowed: bool
    credential_available: bool
    capacity_snapshot_valid: bool
    failed_conditions: tuple[LLMReadinessFailure, ...]
    evidence_ids: tuple[EvidenceId, ...]
    safe_remedy: StrictText | None
    checked_at: AwareDatetime

    @model_validator(mode="after")
    def validate_status_contract(self) -> "LLMProfileReadinessResult":
        booleans = (
            self.profile_defined,
            self.profile_enabled,
            self.provider_live_tested,
            self.agent_profile_approved,
            self.profile_matches_engineering_manager,
            self.data_classification_allowed,
            self.credential_available,
            self.capacity_snapshot_valid,
        )
        failure_map = {
            "PROFILE_MISSING": not self.profile_defined,
            "PROFILE_DISABLED": not self.profile_enabled,
            "PROVIDER_NOT_LIVE_TESTED": not self.provider_live_tested,
            "AGENT_PROFILE_NOT_APPROVED": not self.agent_profile_approved,
            "AGENT_PROFILE_MISMATCH": not self.profile_matches_engineering_manager,
            "DATA_CLASSIFICATION_NOT_ALLOWED": not self.data_classification_allowed,
            "CREDENTIAL_MISSING": not self.credential_available,
            "CAPACITY_SNAPSHOT_INVALID": not self.capacity_snapshot_valid,
        }
        expected_failures = [key for key, value in failure_map.items() if value]
        if self.status == "APPROVED":
            if not all(booleans):
                raise ValueError("all readiness booleans must be True when status is APPROVED")
            if self.failed_conditions:
                raise ValueError("failed_conditions must be empty when status is APPROVED")
            if not self.evidence_ids:
                raise ValueError("evidence_ids must not be empty when status is APPROVED")
            if self.safe_remedy is not None:
                raise ValueError("safe_remedy must be None when status is APPROVED")
        else:
            if all(booleans):
                raise ValueError("at least one readiness boolean must be False when status is BLOCKED")
            if len(set(self.failed_conditions)) != len(self.failed_conditions):
                raise ValueError("failed_conditions must not contain duplicates")
            if tuple(expected_failures) != tuple(self.failed_conditions):
                raise ValueError("failed_conditions must exactly match false readiness fields")
            if self.safe_remedy is None:
                raise ValueError("safe_remedy is required when status is BLOCKED")
        if len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise ValueError("evidence_ids must not contain duplicates")
        return self


class LLMInvocationRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    invocation_id: UUID
    run_id: UUID
    task_id: Literal["evaluate_preflight_result"]
    agent_id: Literal["engineering_manager"]
    llm_profile_id: StrictText
    prompt_hash: SHA256Hex
    started_at: AwareDatetime
    finished_at: AwareDatetime | None
    status: LLMInvocationStatus
    raw_response_hash: SHA256Hex | None
    structured_output_hash: SHA256Hex | None
    error_code: StrictText | None
    redacted_error_summary: StrictText | None

    @model_validator(mode="after")
    def validate_status_contract(self) -> "LLMInvocationRecord":
        if self.status == "STARTED":
            if self.finished_at is not None:
                raise ValueError("finished_at must be None when status is STARTED")
            if self.raw_response_hash is not None:
                raise ValueError("raw_response_hash must be None when status is STARTED")
            if self.structured_output_hash is not None:
                raise ValueError("structured_output_hash must be None when status is STARTED")
            if self.error_code is not None:
                raise ValueError("error_code must be None when status is STARTED")
            if self.redacted_error_summary is not None:
                raise ValueError("redacted_error_summary must be None when status is STARTED")
        elif self.status == "SUCCEEDED":
            if self.finished_at is None:
                raise ValueError("finished_at is required when status is SUCCEEDED")
            if self.raw_response_hash is None:
                raise ValueError("raw_response_hash is required when status is SUCCEEDED")
            if self.structured_output_hash is None:
                raise ValueError("structured_output_hash is required when status is SUCCEEDED")
            if self.error_code is not None:
                raise ValueError("error_code must be None when status is SUCCEEDED")
            if self.redacted_error_summary is not None:
                raise ValueError("redacted_error_summary must be None when status is SUCCEEDED")
        else:
            if self.finished_at is None:
                raise ValueError("finished_at is required when status is BLOCKED or FAILED")
            if self.raw_response_hash is not None:
                raise ValueError("raw_response_hash must be None when status is BLOCKED or FAILED")
            if self.structured_output_hash is not None:
                raise ValueError("structured_output_hash must be None when status is BLOCKED or FAILED")
            if self.error_code is None:
                raise ValueError("error_code is required when status is BLOCKED or FAILED")
            if self.redacted_error_summary is None:
                raise ValueError("redacted_error_summary is required when status is BLOCKED or FAILED")
        if self.finished_at is not None and self.finished_at < self.started_at:
            raise ValueError("finished_at must be greater than or equal to started_at")
        return self


class AuthenticatedHumanDecision(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    decision_id: UUID
    request_id: UUID
    run_id: UUID
    decision: HumanDecisionValue
    authenticated_actor_id: StrictText
    authentication_evidence_id: EvidenceId
    decision_reason: StrictText
    decided_at: AwareDatetime
    decision_hash: SHA256Hex

    @field_validator("decision", mode="before")
    @classmethod
    def validate_decision(cls, value: object) -> object:
        if value not in ("APPROVED", "REJECTED"):
            raise ValueError("decision must be APPROVED or REJECTED")
        return value


class RouteTransitionRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    from_route: FlowRoute
    to_route: FlowRoute
    router_name: StrictText
    evidence_ids: tuple[EvidenceId, ...]
    transitioned_at: AwareDatetime

    @model_validator(mode="after")
    def validate_transition(self) -> "RouteTransitionRecord":
        allowed = {
            ("initial", "manifest_valid"),
            ("initial", "manifest_blocked"),
            ("manifest_valid", "preflight_tool_available"),
            ("manifest_valid", "preflight_tool_unavailable"),
            ("preflight_tool_available", "preflight_requires_evaluation"),
            ("preflight_tool_available", "preflight_failed"),
            ("preflight_tool_available", "preflight_evidence_missing"),
            ("preflight_requires_evaluation", "llm_profile_approved"),
            ("preflight_requires_evaluation", "llm_profile_blocked"),
            ("llm_profile_approved", "human_review_required"),
            ("llm_profile_approved", "agent_recommends_stop"),
            ("llm_profile_approved", "agent_evaluation_failed"),
            ("human_review_required", "human_decision_pending"),
            ("human_decision_pending", "human_decision_approved"),
            ("human_decision_pending", "human_decision_rejected"),
            ("human_decision_approved", "foundation_completed"),
        }
        terminal = {
            "manifest_blocked",
            "preflight_tool_unavailable",
            "preflight_failed",
            "preflight_evidence_missing",
            "llm_profile_blocked",
            "agent_recommends_stop",
            "agent_evaluation_failed",
            "human_decision_rejected",
            "foundation_completed",
        }
        if self.from_route in terminal:
            raise ValueError(f"no transition is allowed from terminal route {self.from_route}")
        if (self.from_route, self.to_route) not in allowed:
            raise ValueError(
                f"transition from {self.from_route} to {self.to_route} is not allowed"
            )
        if not self.evidence_ids:
            raise ValueError("evidence_ids must not be empty")
        if len(set(self.evidence_ids)) != len(self.evidence_ids):
            raise ValueError("evidence_ids must not contain duplicates")
        return self


class FoundationCompletionRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    completion_id: UUID
    run_id: UUID
    decision_id: UUID
    final_checkpoint_id: UUID
    final_output_hash: SHA256Hex
    completed_at: AwareDatetime
    status: Literal["COMPLETED"]


# --- Core state ---

def classify_supported_claim_evidence(
    *,
    evidence_id: str,
    evidence_records: tuple[EvidenceRecord, ...],
    context_run_id: UUID,
    context_task_id: str,
    context_agent_id: str,
    valid_at: datetime,
) -> MissingEvidenceReason | None:
    """Classify a supported claim's evidence against the trusted registries.

    Returns ``None`` when ``evidence_id`` resolves to a trusted evidence
    record that matches the current ``run_id`` / ``task_id`` / ``agent_id``
    execution context and has not expired. Otherwise returns the first
    blocking ``MissingEvidenceReason``:

    - ``ABSENT``: no trusted evidence record exists at all (required evidence
      missing).
    - ``UNTRUSTED``: the evidence identifier does not resolve to a trusted
      record.
    - ``MISMATCHED``: the record resolves but does not match the current
      run/task/agent execution context.
    - ``EXPIRED``: the trusted record is no longer valid relative to
      ``valid_at``.
    """
    if not evidence_records:
        return "ABSENT"
    record = next((r for r in evidence_records if r.evidence_id == evidence_id), None)
    if record is None:
        return "UNTRUSTED"
    if (
        record.run_id != context_run_id
        or record.task_id != context_task_id
        or record.agent_id != context_agent_id
    ):
        return "MISMATCHED"
    if record.expires_at is not None and record.expires_at < valid_at:
        return "EXPIRED"
    return None


class FoundationFlowState(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=False,
        validate_default=True,
    )

    run_manifest: RunManifest
    run_status: FlowRunStatus = "ACTIVE"
    current_route: FlowRoute = "initial"
    route_history: tuple[RouteTransitionRecord, ...] = Field(
        default_factory=tuple,
    )
    trusted_registries: TrustedRegistries
    invocation_ledger: InvocationLedger
    blockers: tuple[BlockerRecord, ...] = Field(default_factory=tuple)
    manifest_validation_result: ManifestValidationResult | None = None
    preflight_tool_availability: PreflightToolAvailabilityResult | None = None
    preflight_result: RepositoryPreflightResult | None = None
    llm_profile_readiness: LLMProfileReadinessResult | None = None
    agent_task_result: AgentTaskResult | None = None
    human_review_request: HumanReviewRequest | None = None
    authenticated_human_decision: AuthenticatedHumanDecision | None = None
    completion_record: FoundationCompletionRecord | None = None

    @model_validator(mode="after")
    def validate_cross_model_contracts(self) -> "FoundationFlowState":
        if not self.route_history:
            if self.current_route != "initial":
                raise ValueError("route_history must begin from initial")
        else:
            first = self.route_history[0]
            if first.from_route != "initial":
                raise ValueError("route_history must begin from initial")
            for index, record in enumerate(self.route_history):
                if index == 0:
                    if record.from_route != "initial":
                        raise ValueError("route_history must begin from initial")
                    continue
                previous = self.route_history[index - 1]
                if previous.to_route != record.from_route:
                    raise ValueError("route history is not contiguous")
            tail = self.route_history[-1].to_route
            if tail != self.current_route:
                raise ValueError("current_route must match the route-history tail")

        if self.manifest_validation_result and self.manifest_validation_result.run_id != self.run_manifest.run_id:
            raise ValueError("manifest_validation_result run_id must match run_manifest.run_id")
        if self.llm_profile_readiness and self.llm_profile_readiness.profile_id != self.run_manifest.approved_llm_profile_id:
            raise ValueError("llm_profile_readiness profile must match run manifest approved profile")
        if self.agent_task_result and self.agent_task_result.run_id != self.run_manifest.run_id:
            raise ValueError("agent_task_result run_id must match run_manifest.run_id")
        if self.human_review_request and self.human_review_request.run_id != self.run_manifest.run_id:
            raise ValueError("human_review_request run_id must match run_manifest.run_id")
        if self.authenticated_human_decision and self.authenticated_human_decision.run_id != self.run_manifest.run_id:
            raise ValueError("authenticated_human_decision run_id must match run_manifest.run_id")
        if (
            self.human_review_request
            and self.authenticated_human_decision
            and self.authenticated_human_decision.decided_at < self.human_review_request.created_at
        ):
            raise ValueError("decided_at must not be earlier than human_review_request.created_at")

        if self.completion_record:
            if self.completion_record.run_id != self.run_manifest.run_id:
                raise ValueError("completion_record run_id must match run_manifest.run_id")
            if self.preflight_result and self.preflight_result.overall_status != "PASS":
                raise ValueError("completion requires PASS preflight_result")
            if self.agent_task_result and self.agent_task_result.status != "PASS":
                raise ValueError("completion requires PASS agent_task_result")
            if not self.authenticated_human_decision or self.authenticated_human_decision.decision != "APPROVED":
                raise ValueError("completion requires authenticated APPROVED decision")
            if any(blocker.status == "OPEN" for blocker in self.blockers):
                raise ValueError("completion requires zero open blockers")
            preflight_tool_records = [
                record for record in self.invocation_ledger.records
                if record.operation == "repository_preflight_tool"
            ]
            if len(preflight_tool_records) != 1:
                raise ValueError("completion requires exactly one preflight tool record")
            llm_records = [
                record for record in self.invocation_ledger.records
                if getattr(record, "task_id", None) == "evaluate_preflight_result"
                and getattr(record, "agent_id", None) == "engineering_manager"
            ]
            if len(llm_records) != 1:
                raise ValueError("completion requires exactly one agent_01 LLM record")
            if self.agent_task_result and self.agent_task_result.direct_tool_calls != 0:
                raise ValueError("completion requires zero direct Agent 01 tools")

        if self.agent_task_result and self.agent_task_result.supported_claims:
            llm_record = next(
                (
                    r
                    for r in self.invocation_ledger.llm_records
                    if r.invocation_id == self.agent_task_result.llm_invocation_id
                ),
                None,
            )
            validity_context_proven = (
                llm_record is not None
                and llm_record.run_id == self.agent_task_result.run_id
                and llm_record.task_id == self.agent_task_result.task_id
                and llm_record.agent_id == self.agent_task_result.agent_id
                and llm_record.status == "SUCCEEDED"
                and llm_record.finished_at is not None
            )
            human_review_route = self.current_route == "human_review_required"
            if not validity_context_proven:
                if not (
                    self.agent_task_result.status == "BLOCKED"
                    and human_review_route
                ):
                    raise ValueError(
                        "supported claim validity cannot be established: "
                        f"no linked completed Agent 01 LLM invocation for "
                        f"invocation_id={self.agent_task_result.llm_invocation_id!r}"
                    )
            else:
                for claim in self.agent_task_result.supported_claims:
                    reason = classify_supported_claim_evidence(
                        evidence_id=claim.evidence_id,
                        evidence_records=self.trusted_registries.evidence_records,
                        context_run_id=self.agent_task_result.run_id,
                        context_task_id=self.agent_task_result.task_id,
                        context_agent_id=self.agent_task_result.agent_id,
                        valid_at=llm_record.finished_at,
                    )
                    if reason is not None and not (
                        self.agent_task_result.status == "BLOCKED"
                        and human_review_route
                    ):
                        raise ValueError(
                            "unsupported or untrusted supported claim: "
                            f"evidence_id={claim.evidence_id!r}, reason={reason}, "
                            f"status={self.agent_task_result.status!r}, "
                            f"current_route={self.current_route!r}"
                        )
        return self


class CheckpointRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    checkpoint_id: UUID
    run_id: UUID
    current_route: FlowRoute
    manifest_hash: SHA256Hex
    registries_hash: SHA256Hex
    ledger_hash: SHA256Hex
    blockers_hash: SHA256Hex
    preflight_result_hash: SHA256Hex | None
    agent_task_result_hash: SHA256Hex | None
    human_review_request_hash: SHA256Hex | None
    previous_checkpoint_hash: SHA256Hex | None
    created_at: AwareDatetime
    route_history_hash: SHA256Hex | None = None
    manifest_validation_result_hash: SHA256Hex | None = None
    preflight_tool_availability_hash: SHA256Hex | None = None
    llm_profile_readiness_hash: SHA256Hex | None = None
    authenticated_human_decision_hash: SHA256Hex | None = None
    completion_record_hash: SHA256Hex | None = None
    checkpoint_hash: SHA256Hex