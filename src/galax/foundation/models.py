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
    "agent_01_llm_evaluation",
    "agent_01_tool_invocation",
]
UnsupportedClaimReason = Literal["no_invocation_evidence", "fabricated", "out_of_scope"]
AgentNextTransition = Literal["STOP", "HUMAN_REVIEW", "CONTINUE_TO_TEST_ONLY_STAGE"]
MissingEvidenceReason = Literal["ABSENT", "UNTRUSTED", "MISMATCHED", "EXPIRED"]
BlockerStatus = Literal["OPEN", "RESOLVED"]
PermissionName = Literal["contents", "pull_requests", "workflows", "administration"]
PermissionLevel = Literal["none", "read", "write", "admin"]
PermissionSource = Literal["OFFLINE_DECLARATION", "LIVE_GATEWAY"]
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

    @model_validator(mode="after")
    def validate_unique_invocation_ids(self) -> "InvocationLedger":
        invocation_ids = [record.invocation_id for record in self.records]
        if len(invocation_ids) != len(set(invocation_ids)):
            raise ValueError("every invocation_id must be unique")
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

    @model_validator(mode="after")
    def validate_agent_identity(self) -> "AgentTaskResult":
        if self.agent_id != "engineering_manager":
            raise ValueError("agent_id must equal 'engineering_manager'")
        if self.direct_tool_calls != 0:
            raise ValueError("direct_tool_calls must equal 0")
        return self


class HumanReviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

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


class FoundationFlowState(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    run_manifest: RunManifest
    current_route: FlowRoute
    trusted_registries: TrustedRegistries
    invocation_ledger: InvocationLedger
    blockers: tuple[BlockerRecord, ...] = Field(default_factory=tuple)
    preflight_result: RepositoryPreflightResult | None = None
    agent_task_result: AgentTaskResult | None = None
    human_review_request: HumanReviewRequest | None = None


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
    checkpoint_hash: SHA256Hex