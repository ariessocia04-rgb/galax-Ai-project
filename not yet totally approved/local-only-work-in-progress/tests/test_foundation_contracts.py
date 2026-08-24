"""Tests for custom validators in galax.foundation.models.

Covers 5 scalar BeforeValidator functions (via BaseModel wrappers)
and 16 model/field validators.
"""

from __future__ import annotations

import unicodedata
from datetime import datetime, timezone

import pytest
from pydantic import BaseModel, ValidationError

from galax.foundation.models import (
    AgentTaskResult,
    AwareDatetime,
    AuthenticatedHumanDecision,
    BlockerRecord,
    EvidenceRecord,
    FoundationCompletionRecord,
    FoundationFlowState,
    GitSHA40,
    HumanReviewRequest,
    InvocationLedger,
    LLMInvocationRecord,
    LLMProfileReadinessResult,
    LiveGitHubPermissionEvidence,
    ManifestValidationResult,
    OfflinePermissionDeclaration,
    PreflightToolAvailabilityResult,
    RepositoryId,
    RepositoryPreflightCheck,
    RepositoryPreflightResult,
    RouteTransitionRecord,
    RunManifest,
    SHA256Hex,
    StrictText,
    SupportedClaim,
    ToolInvocationRecord,
    TrustedRegistries,
)


# ===========================================================================
#  BaseModel wrappers for scalar alias testing
# ===========================================================================

class StrictTextModel(BaseModel):
    x: StrictText


class SHA256HexModel(BaseModel):
    x: SHA256Hex


class GitSHA40Model(BaseModel):
    x: GitSHA40


class RepositoryIdModel(BaseModel):
    x: RepositoryId


class AwareDatetimeModel(BaseModel):
    x: AwareDatetime


# ===========================================================================
#  Fixtures
# ===========================================================================

@pytest.fixture
def aware_dt() -> datetime:
    return datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc)


@pytest.fixture
def sha256() -> str:
    return "abcdef0123456789" * 4


@pytest.fixture
def offline_grant() -> dict:
    return {
        "permission_name": "contents",
        "level": "read",
        "source": "OFFLINE_DECLARATION",
    }


@pytest.fixture
def live_contents() -> dict:
    return {
        "permission_name": "contents",
        "level": "write",
        "source": "LIVE_GATEWAY",
    }


# ===========================================================================
#  1–5: Scalar BeforeValidator aliases (via BaseModel wrappers)
# ===========================================================================

class TestStrictText:
    def test_valid(self) -> None:
        assert StrictTextModel(x="a").x == "a"

    def test_non_string(self) -> None:
        with pytest.raises(ValidationError, match="requires str"):
            StrictTextModel(x=123)

    def test_empty(self) -> None:
        with pytest.raises(ValidationError, match="empty"):
            StrictTextModel(x="")

    def test_leading_whitespace(self) -> None:
        with pytest.raises(ValidationError, match="begin with whitespace"):
            StrictTextModel(x=" x")

    def test_trailing_whitespace(self) -> None:
        with pytest.raises(ValidationError, match="end with whitespace"):
            StrictTextModel(x="x ")

    def test_control_char(self) -> None:
        with pytest.raises(ValidationError, match="control"):
            StrictTextModel(x="a\nb")


class TestSHA256Hex:
    def test_valid(self) -> None:
        v = "abcdef0123456789" * 4
        assert SHA256HexModel(x=v).x == v

    def test_wrong_length(self) -> None:
        with pytest.raises(ValidationError, match="exactly 64"):
            SHA256HexModel(x="ab")

    def test_uppercase(self) -> None:
        v = "abcdef0123456789" * 4
        with pytest.raises(ValidationError, match="lowercase hex"):
            SHA256HexModel(x=v.upper())

    def test_non_hex(self) -> None:
        v = "abcdef0123456789" * 4
        with pytest.raises(ValidationError, match="lowercase hex"):
            SHA256HexModel(x="g" + v[1:])


class TestGitSHA40:
    def test_valid(self) -> None:
        assert GitSHA40Model(x="a" * 40).x == "a" * 40

    def test_39_chars(self) -> None:
        with pytest.raises(ValidationError, match="exactly 40"):
            GitSHA40Model(x="a" * 39)

    def test_41_chars(self) -> None:
        with pytest.raises(ValidationError, match="exactly 40"):
            GitSHA40Model(x="a" * 41)

    def test_uppercase(self) -> None:
        with pytest.raises(ValidationError, match="lowercase hex"):
            GitSHA40Model(x="A" + "a" * 39)

    def test_non_hex(self) -> None:
        with pytest.raises(ValidationError, match="lowercase hex"):
            GitSHA40Model(x="g" + "a" * 39)


class TestRepositoryId:
    def test_valid(self) -> None:
        assert RepositoryIdModel(x="owner/repo").x == "owner/repo"

    def test_no_slash(self) -> None:
        with pytest.raises(ValidationError, match="one slash"):
            RepositoryIdModel(x="owner_repo")

    def test_two_slashes(self) -> None:
        with pytest.raises(ValidationError, match="one slash"):
            RepositoryIdModel(x="a/b/c")

    def test_empty_owner(self) -> None:
        with pytest.raises(ValidationError, match="empty"):
            RepositoryIdModel(x="/repo")

    def test_empty_repo(self) -> None:
        with pytest.raises(ValidationError, match="empty"):
            RepositoryIdModel(x="owner/")


class TestAwareDatetime:
    def test_valid_utc(self) -> None:
        dt = datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc)
        assert AwareDatetimeModel(x=dt).x == dt

    def test_naive(self) -> None:
        with pytest.raises(ValidationError, match="timezone-aware"):
            AwareDatetimeModel(x=datetime(2026, 7, 21, 12, 0, 0))

    def test_non_datetime(self) -> None:
        with pytest.raises(ValidationError, match="datetime input"):
            AwareDatetimeModel(x="2026-07-21T12:00:00Z")


# ===========================================================================
#  6–9: RunManifest field_validator tests
# ===========================================================================

class TestRunManifestFieldValidators:
    def test_repository_root_not_absolute(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="absolute path"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000001",
                repository_id="owner/repo",
                repository_root="relative/path",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_path_traversal(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="path traversal"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000002",
                repository_id="owner/repo",
                repository_root="/home/../repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_allowed_paths_duplicate(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="duplicate"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000003",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=["src/", "src/"],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_allowed_paths_as_string(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="must be a list or tuple"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000004",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths="src/",
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_protected_paths_duplicate(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="duplicate"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000005",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=["a/", "a/"],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_protected_paths_as_string(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="must be a list or tuple"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000006",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=".env",
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_wrong_approved_agent_ids(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="engineering_manager"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000007",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["agent_01"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )


# ===========================================================================
#  10–11: RunManifest model_validator tests
# ===========================================================================

class TestRunManifestModelValidators:
    def test_requires_github_no_evidence(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="github_permission_evidence_id is required"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000010",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=True,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )

    def test_no_github_with_evidence(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="must be None"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000011",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id="evt_001",
                created_at=aware_dt,
            )

    def test_overlapping_paths(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="must not overlap"):
            RunManifest(
                run_id="00000000-0000-0000-0000-000000000012",
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=["shared/"],
                protected_paths=["shared/"],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=aware_dt,
            )


# ===========================================================================
#  12: OfflinePermissionDeclaration.validate_grants
# ===========================================================================

class TestOfflinePermissionDeclarationGrants:
    def test_duplicate_permission_name(self, aware_dt, offline_grant) -> None:
        with pytest.raises(ValidationError, match="must be unique"):
            OfflinePermissionDeclaration(
                evidence_id="off_001",
                profile_id="p",
                repository_id="owner/repo",
                grants=[offline_grant, offline_grant],
                prohibited_permissions_present=[],
                checked_at=aware_dt,
                expires_at=None,
            )

    def test_wrong_source(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="OFFLINE_DECLARATION"):
            OfflinePermissionDeclaration(
                evidence_id="off_002",
                profile_id="p",
                repository_id="owner/repo",
                grants=[{
                    "permission_name": "contents",
                    "level": "read",
                    "source": "LIVE_GATEWAY",
                }],
                prohibited_permissions_present=[],
                checked_at=aware_dt,
                expires_at=None,
            )

    def test_expires_at_before_checked_at(self, aware_dt) -> None:
        past = datetime(2026, 7, 20, 12, 0, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="greater than or equal"):
            OfflinePermissionDeclaration(
                evidence_id="off_003",
                profile_id="p",
                repository_id="owner/repo",
                grants=[{
                    "permission_name": "contents",
                    "level": "read",
                    "source": "OFFLINE_DECLARATION",
                }],
                prohibited_permissions_present=[],
                checked_at=aware_dt,
                expires_at=past,
            )

    def test_expires_at_equals_checked_at(self, aware_dt) -> None:
        obj = OfflinePermissionDeclaration(
            evidence_id="off_004",
            profile_id="p",
            repository_id="owner/repo",
            grants=[{
                "permission_name": "contents",
                "level": "read",
                "source": "OFFLINE_DECLARATION",
            }],
            prohibited_permissions_present=[],
            checked_at=aware_dt,
            expires_at=aware_dt,
        )
        assert obj.expires_at == obj.checked_at


# ===========================================================================
#  13: LiveGitHubPermissionEvidence.validate_permissions
# ===========================================================================

class TestLiveGitHubPermissionEvidencePermissions:
    def test_wrong_permission_name(self, aware_dt, live_contents) -> None:
        with pytest.raises(ValidationError, match="permission_name"):
            LiveGitHubPermissionEvidence(
                evidence_id="live_001",
                authenticated_identity="octocat",
                target_repository="owner/repo",
                repository_access_confirmed=True,
                contents_permission=live_contents,
                pull_requests_permission={
                    "permission_name": "contents",
                    "level": "read",
                    "source": "LIVE_GATEWAY",
                },
                workflows_permission={
                    "permission_name": "workflows",
                    "level": "none",
                    "source": "LIVE_GATEWAY",
                },
                administration_permission={
                    "permission_name": "administration",
                    "level": "none",
                    "source": "LIVE_GATEWAY",
                },
                checked_at=aware_dt,
            )

    def test_wrong_source(self, aware_dt, live_contents) -> None:
        with pytest.raises(ValidationError, match="LIVE_GATEWAY"):
            LiveGitHubPermissionEvidence(
                evidence_id="live_002",
                authenticated_identity="octocat",
                target_repository="owner/repo",
                repository_access_confirmed=True,
                contents_permission=live_contents,
                pull_requests_permission={
                    "permission_name": "pull_requests",
                    "level": "read",
                    "source": "LIVE_GATEWAY",
                },
                workflows_permission={
                    "permission_name": "workflows",
                    "level": "none",
                    "source": "LIVE_GATEWAY",
                },
                administration_permission={
                    "permission_name": "administration",
                    "level": "admin",
                    "source": "OFFLINE_DECLARATION",
                },
                checked_at=aware_dt,
            )


# ===========================================================================
#  14: BlockerRecord.validate_resolved_at
# ===========================================================================

class TestBlockerRecordResolvedAt:
    def test_open_with_resolved_at(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="resolved_at must be None"):
            BlockerRecord(
                blocker_id="blk_001",
                code="B",
                reason="test",
                exact_remedy="fix",
                related_evidence_ids=[],
                status="OPEN",
                created_at=aware_dt,
                resolved_at=aware_dt,
            )

    def test_resolved_without_resolved_at(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="resolved_at is required"):
            BlockerRecord(
                blocker_id="blk_002",
                code="B",
                reason="test",
                exact_remedy="fix",
                related_evidence_ids=[],
                status="RESOLVED",
                created_at=aware_dt,
                resolved_at=None,
            )

    def test_resolved_at_before_created_at(self, aware_dt) -> None:
        past = datetime(2026, 7, 20, 12, 0, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="greater than or equal"):
            BlockerRecord(
                blocker_id="blk_003",
                code="B",
                reason="test",
                exact_remedy="fix",
                related_evidence_ids=[],
                status="RESOLVED",
                created_at=aware_dt,
                resolved_at=past,
            )

    def test_resolved_at_equals_created_at(self, aware_dt) -> None:
        obj = BlockerRecord(
            blocker_id="blk_004",
            code="B",
            reason="test",
            exact_remedy="fix",
            related_evidence_ids=[],
            status="RESOLVED",
            created_at=aware_dt,
            resolved_at=aware_dt,
        )
        assert obj.resolved_at == obj.created_at


# ===========================================================================
#  15: RepositoryPreflightCheck.validate_status_contract
# ===========================================================================

class TestRepositoryPreflightCheckStatus:
    def test_pass_missing_evidence(self) -> None:
        with pytest.raises(ValidationError, match="evidence_id is required"):
            RepositoryPreflightCheck(
                check_id="c1",
                status="PASS",
                evidence_id=None,
                redacted_summary="ok",
                exact_remedy=None,
            )

    def test_pass_with_remedy(self) -> None:
        with pytest.raises(ValidationError, match="exact_remedy must be None"):
            RepositoryPreflightCheck(
                check_id="c2",
                status="PASS",
                evidence_id="evt",
                redacted_summary="ok",
                exact_remedy="unnecessary",
            )

    def test_blocked_missing_remedy(self) -> None:
        with pytest.raises(ValidationError, match="exact_remedy is required"):
            RepositoryPreflightCheck(
                check_id="c3",
                status="BLOCKED",
                evidence_id=None,
                redacted_summary="blocked",
                exact_remedy=None,
            )

    def test_fail_missing_remedy(self) -> None:
        with pytest.raises(ValidationError, match="exact_remedy is required"):
            RepositoryPreflightCheck(
                check_id="c4",
                status="FAIL",
                evidence_id=None,
                redacted_summary="fail",
                exact_remedy=None,
            )


# ===========================================================================
#  16: ToolInvocationRecord.validate_status_contract
# ===========================================================================

class TestToolInvocationRecordStatus:
    def test_started_with_finished_at(self, aware_dt, sha256) -> None:
        with pytest.raises(ValidationError, match="finished_at must be None"):
            ToolInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000001",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="t1",
                owner="GalaxFoundationFlow",
                tool_profile_id="tp",
                operation="repository_preflight_tool",
                input_hash=sha256,
                started_at=aware_dt,
                finished_at=aware_dt,
                status="STARTED",
                raw_output_hash=None,
                affected_resources=[],
                external_evidence_ids=[],
                error_code=None,
                redacted_error_summary=None,
            )

    def test_succeeded_missing_raw_output(self, aware_dt, sha256) -> None:
        finished = datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="raw_output_hash is required"):
            ToolInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000002",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="t2",
                owner="GalaxFoundationFlow",
                tool_profile_id="tp",
                operation="repository_preflight_tool",
                input_hash=sha256,
                started_at=aware_dt,
                finished_at=finished,
                status="SUCCEEDED",
                raw_output_hash=None,
                affected_resources=[],
                external_evidence_ids=[],
                error_code=None,
                redacted_error_summary=None,
            )

    def test_failed_missing_error_code(self, aware_dt, sha256) -> None:
        finished = datetime(2026, 7, 21, 12, 3, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="error_code is required"):
            ToolInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000003",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="t3",
                owner="GalaxFoundationFlow",
                tool_profile_id="tp",
                operation="repository_preflight_tool",
                input_hash=sha256,
                started_at=aware_dt,
                finished_at=finished,
                status="FAILED",
                raw_output_hash=None,
                affected_resources=[],
                external_evidence_ids=[],
                error_code=None,
                redacted_error_summary="err",
            )

    def test_failed_missing_error_summary(self, aware_dt, sha256) -> None:
        finished = datetime(2026, 7, 21, 12, 3, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="redacted_error_summary"):
            ToolInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000004",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="t4",
                owner="GalaxFoundationFlow",
                tool_profile_id="tp",
                operation="repository_preflight_tool",
                input_hash=sha256,
                started_at=aware_dt,
                finished_at=finished,
                status="FAILED",
                raw_output_hash=None,
                affected_resources=[],
                external_evidence_ids=[],
                error_code="E001",
                redacted_error_summary=None,
            )

    def test_finished_at_equals_started_at(self, aware_dt, sha256) -> None:
        obj = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000005",
            run_id="00000000-0000-0000-0000-000000000001",
            task_id="t5",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash=sha256,
            started_at=aware_dt,
            finished_at=aware_dt,
            status="SUCCEEDED",
            raw_output_hash=sha256,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        assert obj.finished_at == obj.started_at


# ===========================================================================
#  17: InvocationLedger.validate_unique_invocation_ids
# ===========================================================================

class TestInvocationLedgerUnique:
    def test_duplicate(self, aware_dt, sha256) -> None:
        r = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000010",
            run_id="00000000-0000-0000-0000-000000000001",
            task_id="t",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash=sha256,
            started_at=aware_dt,
            finished_at=None,
            status="STARTED",
            raw_output_hash=None,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        with pytest.raises(ValidationError, match="invocation_id must be unique"):
            InvocationLedger(records=[r, r])


# ===========================================================================
#  18: RepositoryPreflightResult.validate_overall_status
# ===========================================================================

class TestRepositoryPreflightResultStatus:
    def test_pass_with_non_pass_check(self, sha256) -> None:
        with pytest.raises(ValidationError, match="all checks to be PASS"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="PASS",
                checks=[RepositoryPreflightCheck(
                    check_id="c1",
                    status="BLOCKED",
                    evidence_id=None,
                    redacted_summary="b",
                    exact_remedy="fix",
                )],
                blocking_reasons=[],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )

    def test_pass_with_blockers(self, sha256, aware_dt) -> None:
        with pytest.raises(ValidationError, match="blocking_reasons to be empty"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="PASS",
                checks=[RepositoryPreflightCheck(
                    check_id="c1",
                    status="PASS",
                    evidence_id="evt",
                    redacted_summary="ok",
                    exact_remedy=None,
                )],
                blocking_reasons=[BlockerRecord(
                    blocker_id="b1",
                    code="B",
                    reason="r",
                    exact_remedy="f",
                    related_evidence_ids=[],
                    status="OPEN",
                    created_at=aware_dt,
                    resolved_at=None,
                )],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )

    def test_blocked_with_fail_check(self, sha256) -> None:
        with pytest.raises(ValidationError, match="must not contain FAIL"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="BLOCKED",
                checks=[
                    RepositoryPreflightCheck(
                        check_id="c_blocked",
                        status="BLOCKED",
                        evidence_id=None,
                        redacted_summary="blocked",
                        exact_remedy="fix blocker",
                    ),
                    RepositoryPreflightCheck(
                        check_id="c_fail",
                        status="FAIL",
                        evidence_id=None,
                        redacted_summary="failed",
                        exact_remedy="fix failure",
                    ),
                ],
                blocking_reasons=[],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )

    def test_fail_without_fail_check(self, sha256) -> None:
        with pytest.raises(ValidationError, match="requires at least one FAIL"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="FAIL",
                checks=[RepositoryPreflightCheck(
                    check_id="c1",
                    status="PASS",
                    evidence_id="evt",
                    redacted_summary="ok",
                    exact_remedy=None,
                )],
                blocking_reasons=[],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )

    def test_blocker_not_open(self, sha256, aware_dt) -> None:
        resolved = datetime(2026, 7, 22, 12, 0, 0, tzinfo=timezone.utc)
        with pytest.raises(ValidationError, match="contain only OPEN"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="BLOCKED",
                checks=[RepositoryPreflightCheck(
                    check_id="c1",
                    status="BLOCKED",
                    evidence_id=None,
                    redacted_summary="b",
                    exact_remedy="fix",
                )],
                blocking_reasons=[BlockerRecord(
                    blocker_id="b1",
                    code="B",
                    reason="r",
                    exact_remedy="f",
                    related_evidence_ids=[],
                    status="RESOLVED",
                    created_at=aware_dt,
                    resolved_at=resolved,
                )],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )

    def test_duplicate_check_ids(self, sha256) -> None:
        c = RepositoryPreflightCheck(
            check_id="c1",
            status="PASS",
            evidence_id="evt",
            redacted_summary="ok",
            exact_remedy=None,
        )
        with pytest.raises(ValidationError, match="check_id values must be unique"):
            RepositoryPreflightResult(
                run_id="00000000-0000-0000-0000-000000000001",
                overall_status="PASS",
                checks=[c, c],
                blocking_reasons=[],
                invocation_id="00000000-0000-0000-0000-000000000001",
                input_hash=sha256,
                result_hash=sha256,
            )


# ===========================================================================
#  19: AgentTaskResult.validate_agent_identity
# ===========================================================================

class TestAgentTaskResultIdentity:
    def test_wrong_agent_id(self) -> None:
        with pytest.raises(ValidationError) as exc:
            AgentTaskResult(
                run_id="00000000-0000-0000-0000-000000000001",
                agent_id="agent_01",
                direct_tool_calls=0,
                task_id="evaluate_preflight_result",
                status="PASS",
                summary="s",
                supported_claims=[],
                unsupported_claims=[],
                next_transition="STOP",
                exact_remedies=[],
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                preflight_result_hash="a" * 64,
                llm_invocation_id="00000000-0000-0000-0000-000000000101",
                llm_profile_id="p",
                output_hash="a" * 64,
            )
        err = exc.value.errors()[0]
        assert err["type"] == "literal_error"
        assert err["loc"] == ("agent_id",)
        assert "engineering_manager" in err["msg"]

    def test_non_zero_direct_tool_calls(self) -> None:
        with pytest.raises(ValidationError) as exc:
            AgentTaskResult(
                run_id="00000000-0000-0000-0000-000000000002",
                agent_id="engineering_manager",
                direct_tool_calls=1,
                task_id="evaluate_preflight_result",
                status="PASS",
                summary="s",
                supported_claims=[],
                unsupported_claims=[],
                next_transition="STOP",
                exact_remedies=[],
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                preflight_result_hash="a" * 64,
                llm_invocation_id="00000000-0000-0000-0000-000000000101",
                llm_profile_id="p",
                output_hash="a" * 64,
            )
        err = exc.value.errors()[0]
        assert err["type"] == "literal_error"
        assert err["loc"] == ("direct_tool_calls",)
        assert "0" in err["msg"]


# ===========================================================================
#  20: HumanReviewRequest.validate_human_decision
# ===========================================================================

class TestHumanReviewRequestDecision:
    def test_non_pending_decision(self, aware_dt) -> None:
        with pytest.raises(ValidationError) as exc:
            HumanReviewRequest(
                request_id="00000000-0000-0000-0000-000000000050",
                run_id="00000000-0000-0000-0000-000000000001",
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                agent_llm_invocation_id="00000000-0000-0000-0000-000000000101",
                preflight_result_hash="a" * 64,
                agent_task_result_hash="a" * 64,
                requested_action="REVIEW_FOUNDATION_EVIDENCE",
                current_status="AWAITING_HUMAN_REVIEW",
                confirmed_evidence=[],
                missing_evidence=[],
                risks=[],
                recommended_next_step="AWAIT_AUTHENTICATED_HUMAN_DECISION",
                prohibited_next_steps=[
                    "merge_to_main_or_master",
                    "deployment",
                    "activation_of_Agents_02_to_15",
                    "enabling_unvalidated_LLM_profiles",
                ],
                human_decision="APPROVED",
                created_at=aware_dt,
            )
        err = exc.value.errors()[0]
        assert err["type"] == "literal_error"
        assert err["loc"] == ("human_decision",)
        assert "PENDING" in err["msg"]

    def test_missing_prohibited_step(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="prohibited_next_steps"):
            HumanReviewRequest(
                request_id="00000000-0000-0000-0000-000000000051",
                run_id="00000000-0000-0000-0000-000000000001",
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                agent_llm_invocation_id="00000000-0000-0000-0000-000000000101",
                preflight_result_hash="a" * 64,
                agent_task_result_hash="a" * 64,
                requested_action="REVIEW_FOUNDATION_EVIDENCE",
                current_status="AWAITING_HUMAN_REVIEW",
                confirmed_evidence=[],
                missing_evidence=[],
                risks=[],
                recommended_next_step="AWAIT_AUTHENTICATED_HUMAN_DECISION",
                prohibited_next_steps=[
                    "merge_to_main_or_master",
                    "deployment",
                    "activation_of_Agents_02_to_15",
                ],
                human_decision="PENDING",
                created_at=aware_dt,
            )

    def test_duplicate_prohibited_step(self, aware_dt) -> None:
        with pytest.raises(ValidationError, match="prohibited_next_steps"):
            HumanReviewRequest(
                request_id="00000000-0000-0000-0000-000000000052",
                run_id="00000000-0000-0000-0000-000000000001",
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                agent_llm_invocation_id="00000000-0000-0000-0000-000000000101",
                preflight_result_hash="a" * 64,
                agent_task_result_hash="a" * 64,
                requested_action="REVIEW_FOUNDATION_EVIDENCE",
                current_status="AWAITING_HUMAN_REVIEW",
                confirmed_evidence=[],
                missing_evidence=[],
                risks=[],
                recommended_next_step="AWAIT_AUTHENTICATED_HUMAN_DECISION",
                prohibited_next_steps=[
                    "merge_to_main_or_master",
                    "deployment",
                    "activation_of_Agents_02_to_15",
                    "enabling_unvalidated_LLM_profiles",
                    "merge_to_main_or_master",
                ],
                human_decision="PENDING",
                created_at=aware_dt,
            )


# ===========================================================================
#  21: TrustedRegistries.validate_registries
# ===========================================================================

class TestTrustedRegistries:
    def test_wrong_approved_agent_ids(self) -> None:
        with pytest.raises(ValidationError, match="approved_agent_ids"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager", "agent_02"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=[],
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            )

    def test_duplicate_llm_profile_id(self) -> None:
        with pytest.raises(ValidationError, match="unique"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=["a", "a"],
                approved_tool_profile_ids=[],
                evidence_records=[],
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            )

    def test_duplicate_tool_profile_id(self) -> None:
        with pytest.raises(ValidationError, match="unique"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=["a", "a"],
                evidence_records=[],
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            )

    def test_duplicate_evidence_record_id(self, aware_dt, sha256) -> None:
        e = EvidenceRecord(
            evidence_id="evt_001",
            source="GalaxFoundationFlow",
            content_hash=sha256,
            created_at=aware_dt,
            run_id="00000000-0000-0000-0000-000000000001",
            task_id="evaluate_preflight_result",
            agent_id="engineering_manager",
        )
        with pytest.raises(ValidationError, match="unique evidence_ids"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=[e, e],
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            )

    def test_duplicate_offline_declaration_id(self, aware_dt, offline_grant) -> None:
        d = OfflinePermissionDeclaration(
            evidence_id="off_001",
            profile_id="p",
            repository_id="owner/repo",
            grants=[offline_grant],
            prohibited_permissions_present=[],
            checked_at=aware_dt,
            expires_at=None,
        )
        with pytest.raises(ValidationError, match="unique evidence_ids"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=[],
                offline_permission_declarations=[d, d],
                live_github_permission_evidence=[],
            )

    def test_duplicate_live_evidence_id(self, aware_dt, live_contents) -> None:
        l = LiveGitHubPermissionEvidence(
            evidence_id="live_001",
            authenticated_identity="octocat",
            target_repository="owner/repo",
            repository_access_confirmed=True,
            contents_permission=live_contents,
            pull_requests_permission={
                "permission_name": "pull_requests",
                "level": "read",
                "source": "LIVE_GATEWAY",
            },
            workflows_permission={
                "permission_name": "workflows",
                "level": "none",
                "source": "LIVE_GATEWAY",
            },
            administration_permission={
                "permission_name": "administration",
                "level": "none",
                "source": "LIVE_GATEWAY",
            },
            checked_at=aware_dt,
        )
        with pytest.raises(ValidationError, match="unique evidence_ids"):
            TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=[],
                offline_permission_declarations=[],
                live_github_permission_evidence=[l, l],
            )


# ===========================================================================
#  22: ManifestValidationResult
# ===========================================================================

class TestManifestValidationResult:
    def test_pass_contract(self) -> None:
        with pytest.raises(ValidationError, match="evidence_ids must not be empty"):
            ManifestValidationResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="PASS",
                evidence_ids=[],
                blocker_ids=[],
                exact_remedy=None,
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_blocked_requires_blocker_ids(self) -> None:
        with pytest.raises(ValidationError, match="blocker_ids must not be empty"):
            ManifestValidationResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="BLOCKED",
                evidence_ids=[],
                blocker_ids=[],
                exact_remedy="fix",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_duplicate_evidence_ids(self) -> None:
        with pytest.raises(ValidationError, match="evidence_ids must not contain duplicates"):
            ManifestValidationResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="PASS",
                evidence_ids=["evt_1", "evt_1"],
                blocker_ids=[],
                exact_remedy=None,
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_duplicate_blocker_ids(self) -> None:
        with pytest.raises(ValidationError, match="blocker_ids must not contain duplicates"):
            ManifestValidationResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="BLOCKED",
                evidence_ids=[],
                blocker_ids=["b1", "b1"],
                exact_remedy="fix",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )


# ===========================================================================
#  23: PreflightToolAvailabilityResult
# ===========================================================================

class TestPreflightToolAvailabilityResult:
    def test_available_requires_no_remedy(self) -> None:
        with pytest.raises(ValidationError, match="exact_remedy must be None"):
            PreflightToolAvailabilityResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="AVAILABLE",
                tool_profile_id="tp",
                evidence_id="evt",
                exact_remedy="unexpected",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_unavailable_requires_remedy(self) -> None:
        with pytest.raises(ValidationError, match="exact_remedy is required"):
            PreflightToolAvailabilityResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="UNAVAILABLE",
                tool_profile_id="tp",
                evidence_id="evt",
                exact_remedy=None,
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )


# ===========================================================================
#  24: LLMProfileReadinessResult
# ===========================================================================

class TestLLMProfileReadinessResult:
    def test_approved_requires_true_booleans(self) -> None:
        with pytest.raises(ValidationError, match="all readiness booleans must be True"):
            LLMProfileReadinessResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="APPROVED",
                profile_id="p",
                profile_defined=True,
                profile_enabled=False,
                provider_live_tested=True,
                agent_profile_approved=True,
                profile_matches_engineering_manager=True,
                data_classification_allowed=True,
                credential_available=True,
                capacity_snapshot_valid=True,
                failed_conditions=[],
                evidence_ids=["evt"],
                safe_remedy=None,
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_blocked_requires_failed_conditions(self) -> None:
        with pytest.raises(ValidationError, match="at least one readiness boolean must be False"):
            LLMProfileReadinessResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="BLOCKED",
                profile_id="p",
                profile_defined=True,
                profile_enabled=True,
                provider_live_tested=True,
                agent_profile_approved=True,
                profile_matches_engineering_manager=True,
                data_classification_allowed=True,
                credential_available=True,
                capacity_snapshot_valid=True,
                failed_conditions=["PROFILE_MISSING"],
                evidence_ids=["evt"],
                safe_remedy="fix",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_blocked_failed_conditions_mismatch(self) -> None:
        with pytest.raises(ValidationError, match="failed_conditions must exactly match false readiness fields"):
            LLMProfileReadinessResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="BLOCKED",
                profile_id="p",
                profile_defined=False,
                profile_enabled=True,
                provider_live_tested=True,
                agent_profile_approved=True,
                profile_matches_engineering_manager=True,
                data_classification_allowed=True,
                credential_available=True,
                capacity_snapshot_valid=True,
                failed_conditions=["PROFILE_DISABLED"],
                evidence_ids=["evt"],
                safe_remedy="fix",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_duplicate_failed_conditions(self) -> None:
        with pytest.raises(ValidationError, match="failed_conditions must not contain duplicates"):
            LLMProfileReadinessResult(
                run_id="00000000-0000-0000-0000-000000000001",
                status="BLOCKED",
                profile_id="p",
                profile_defined=False,
                profile_enabled=False,
                provider_live_tested=True,
                agent_profile_approved=True,
                profile_matches_engineering_manager=True,
                data_classification_allowed=True,
                credential_available=True,
                capacity_snapshot_valid=True,
                failed_conditions=["PROFILE_MISSING", "PROFILE_MISSING"],
                evidence_ids=["evt"],
                safe_remedy="fix",
                checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )


# ===========================================================================
#  25: LLMInvocationRecord
# ===========================================================================

class TestLLMInvocationRecord:
    def test_started_requires_nulls(self) -> None:
        with pytest.raises(ValidationError, match="finished_at must be None"):
            LLMInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000001",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="evaluate_preflight_result",
                agent_id="engineering_manager",
                llm_profile_id="p",
                prompt_hash="a" * 64,
                started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                status="STARTED",
                raw_response_hash="a" * 64,
                structured_output_hash="a" * 64,
                error_code="E",
                redacted_error_summary="e",
            )

    def test_succeeded_contract(self) -> None:
        finished = datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)
        obj = LLMInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000002",
            run_id="00000000-0000-0000-0000-000000000001",
            task_id="evaluate_preflight_result",
            agent_id="engineering_manager",
            llm_profile_id="p",
            prompt_hash="a" * 64,
            started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            finished_at=finished,
            status="SUCCEEDED",
            raw_response_hash="a" * 64,
            structured_output_hash="a" * 64,
            error_code=None,
            redacted_error_summary=None,
        )
        assert obj.status == "SUCCEEDED"

    def test_blocked_requires_error(self) -> None:
        with pytest.raises(ValidationError, match="error_code is required"):
            LLMInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000003",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="evaluate_preflight_result",
                agent_id="engineering_manager",
                llm_profile_id="p",
                prompt_hash="a" * 64,
                started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                status="BLOCKED",
                raw_response_hash=None,
                structured_output_hash=None,
                error_code=None,
                redacted_error_summary="e",
            )


# ===========================================================================
#  26: AuthenticatedHumanDecision
# ===========================================================================

class TestAuthenticatedHumanDecision:
    def test_rejects_pending(self) -> None:
        with pytest.raises(ValidationError, match="decision must be APPROVED or REJECTED"):
            AuthenticatedHumanDecision(
                decision_id="00000000-0000-0000-0000-000000000001",
                request_id="00000000-0000-0000-0000-000000000002",
                run_id="00000000-0000-0000-0000-000000000003",
                decision="PENDING",
                authenticated_actor_id="actor",
                authentication_evidence_id="evt",
                decision_reason="r",
                decided_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                decision_hash="a" * 64,
            )


# ===========================================================================
#  27: RouteTransitionRecord
# ===========================================================================

class TestRouteTransitionRecord:
    def test_allowed_transitions(self) -> None:
        RouteTransitionRecord(
            from_route="initial",
            to_route="manifest_valid",
            router_name="r",
            evidence_ids=["evt"],
            transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
        )
        RouteTransitionRecord(
            from_route="preflight_requires_evaluation",
            to_route="llm_profile_approved",
            router_name="r",
            evidence_ids=["evt"],
            transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
        )

    def test_rejected_transition(self) -> None:
        with pytest.raises(ValidationError, match="is not allowed"):
            RouteTransitionRecord(
                from_route="llm_profile_approved",
                to_route="initial",
                router_name="r",
                evidence_ids=["evt"],
                transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_transition_from_terminal(self) -> None:
        with pytest.raises(ValidationError, match="no transition is allowed from terminal route"):
            RouteTransitionRecord(
                from_route="foundation_completed",
                to_route="initial",
                router_name="r",
                evidence_ids=["evt"],
                transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_empty_evidence_ids(self) -> None:
        with pytest.raises(ValidationError, match="evidence_ids must not be empty"):
            RouteTransitionRecord(
                from_route="initial",
                to_route="manifest_valid",
                router_name="r",
                evidence_ids=[],
                transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_duplicate_evidence_ids(self) -> None:
        with pytest.raises(ValidationError, match="evidence_ids must not contain duplicates"):
            RouteTransitionRecord(
                from_route="initial",
                to_route="manifest_valid",
                router_name="r",
                evidence_ids=["evt", "evt"],
                transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )


# ===========================================================================
#  28: FoundationFlowState cross-model validation
# ===========================================================================

class TestFoundationFlowState:
    def test_mutable_state_by_config(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        state = FoundationFlowState(
            run_manifest=RunManifest(
                run_id=run_id,
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            ),
            current_route="initial",
            trusted_registries=TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=[],
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            ),
            invocation_ledger=InvocationLedger(),
        )
        state.current_route = "manifest_valid"
        assert state.current_route == "manifest_valid"

    def test_frozen_nested_evidence_records(self) -> None:
        evidence = EvidenceRecord(
            evidence_id="evt",
            source="GalaxFoundationFlow",
            content_hash="a" * 64,
            created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            run_id="00000000-0000-0000-0000-000000000001",
            task_id="evaluate_preflight_result",
            agent_id="engineering_manager",
        )
        with pytest.raises(ValidationError):
            EvidenceRecord(**{**evidence.model_dump(), "source": "Unknown"})

    def test_route_history_contiguous(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        route = RouteTransitionRecord(
            from_route="initial",
            to_route="manifest_valid",
            router_name="r",
            evidence_ids=["evt"],
            transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
        )
        bad_route = RouteTransitionRecord(
            from_route="preflight_tool_available",
            to_route="preflight_requires_evaluation",
            router_name="r",
            evidence_ids=["evt2"],
            transitioned_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
        )
        with pytest.raises(ValidationError, match="route history is not contiguous"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="preflight_requires_evaluation",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                route_history=[route, bad_route],
            )

    def test_current_route_tail_mismatch(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        route = RouteTransitionRecord(
            from_route="initial",
            to_route="manifest_valid",
            router_name="r",
            evidence_ids=["evt"],
            transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
        )
        with pytest.raises(ValidationError, match="current_route must match the route-history tail"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="manifest_blocked",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                route_history=[route],
            )

    def test_nested_run_id_mismatch(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        other_run_id = "00000000-0000-0000-0000-000000000002"
        with pytest.raises(ValidationError, match="run_id must match run_manifest.run_id"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="initial",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                agent_task_result=AgentTaskResult(
                    run_id=other_run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[SupportedClaim(statement="x", evidence_id="evt")],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
            )

    def test_completion_requires_pass_preflight(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires PASS preflight_result"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                route_history=[
                    RouteTransitionRecord(
                        from_route="initial",
                        to_route="manifest_valid",
                        router_name="r",
                        evidence_ids=["evt_route_1"],
                        transitioned_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="manifest_valid",
                        to_route="preflight_tool_available",
                        router_name="r",
                        evidence_ids=["evt_route_2"],
                        transitioned_at=datetime(2026, 7, 21, 12, 2, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="preflight_tool_available",
                        to_route="preflight_requires_evaluation",
                        router_name="r",
                        evidence_ids=["evt_route_3"],
                        transitioned_at=datetime(2026, 7, 21, 12, 3, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="preflight_requires_evaluation",
                        to_route="llm_profile_approved",
                        router_name="r",
                        evidence_ids=["evt_route_4"],
                        transitioned_at=datetime(2026, 7, 21, 12, 4, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="llm_profile_approved",
                        to_route="human_review_required",
                        router_name="r",
                        evidence_ids=["evt_route_5"],
                        transitioned_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_review_required",
                        to_route="human_decision_pending",
                        router_name="r",
                        evidence_ids=["evt_route_6"],
                        transitioned_at=datetime(2026, 7, 21, 12, 6, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_decision_pending",
                        to_route="human_decision_approved",
                        router_name="r",
                        evidence_ids=["evt_route_7"],
                        transitioned_at=datetime(2026, 7, 21, 12, 7, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_decision_approved",
                        to_route="foundation_completed",
                        router_name="r",
                        evidence_ids=["evt_route_8"],
                        transitioned_at=datetime(2026, 7, 21, 12, 8, 0, tzinfo=timezone.utc),
                    ),
                ],
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="FAIL",
                    checks=[
                        RepositoryPreflightCheck(
                            check_id="c_fail",
                            status="FAIL",
                            evidence_id=None,
                            redacted_summary="failed",
                            exact_remedy="fix",
                        )
                    ],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[
                        SupportedClaim(
                            statement="x",
                            evidence_id="evt",
                        )
                    ],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )

    def test_completion_requires_zero_open_blockers(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires zero open blockers"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                route_history=[
                    RouteTransitionRecord(
                        from_route="initial",
                        to_route="manifest_valid",
                        router_name="r",
                        evidence_ids=["evt_route_1"],
                        transitioned_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="manifest_valid",
                        to_route="preflight_tool_available",
                        router_name="r",
                        evidence_ids=["evt_route_2"],
                        transitioned_at=datetime(2026, 7, 21, 12, 2, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="preflight_tool_available",
                        to_route="preflight_requires_evaluation",
                        router_name="r",
                        evidence_ids=["evt_route_3"],
                        transitioned_at=datetime(2026, 7, 21, 12, 3, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="preflight_requires_evaluation",
                        to_route="llm_profile_approved",
                        router_name="r",
                        evidence_ids=["evt_route_4"],
                        transitioned_at=datetime(2026, 7, 21, 12, 4, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="llm_profile_approved",
                        to_route="human_review_required",
                        router_name="r",
                        evidence_ids=["evt_route_5"],
                        transitioned_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_review_required",
                        to_route="human_decision_pending",
                        router_name="r",
                        evidence_ids=["evt_route_6"],
                        transitioned_at=datetime(2026, 7, 21, 12, 6, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_decision_pending",
                        to_route="human_decision_approved",
                        router_name="r",
                        evidence_ids=["evt_route_7"],
                        transitioned_at=datetime(2026, 7, 21, 12, 7, 0, tzinfo=timezone.utc),
                    ),
                    RouteTransitionRecord(
                        from_route="human_decision_approved",
                        to_route="foundation_completed",
                        router_name="r",
                        evidence_ids=["evt_route_8"],
                        transitioned_at=datetime(2026, 7, 21, 12, 8, 0, tzinfo=timezone.utc),
                    ),
                ],
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                blockers=[BlockerRecord(
                    blocker_id="b1",
                    code="B",
                    reason="r",
                    exact_remedy="f",
                    related_evidence_ids=[],
                    status="OPEN",
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                    resolved_at=None,
                )],
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="PASS",
                    checks=[
                        RepositoryPreflightCheck(
                            check_id="c_fail",
                            status="PASS",
                            evidence_id="evt",
                            redacted_summary="failed",
                            exact_remedy=None,
                        )
                    ],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[
                        SupportedClaim(
                            statement="x",
                            evidence_id="evt",
                        )
                    ],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )


# ===========================================================================
#  29–40: Additional deterministic contract tests
# ===========================================================================

class TestAdditionalContracts:
    def test_prohibited_tool_in_tool_invocation(self) -> None:
        with pytest.raises(ValidationError, match="repository_preflight_tool"):
            ToolInvocationRecord(
                invocation_id="00000000-0000-0000-0000-000000000001",
                run_id="00000000-0000-0000-0000-000000000001",
                task_id="evaluate_preflight_result",
                owner="GalaxFoundationFlow",
                tool_profile_id="tp",
                operation="agent_01_tool_invocation",
                input_hash="a" * 64,
                started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                finished_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
                status="SUCCEEDED",
                raw_output_hash="a" * 64,
                affected_resources=[],
                external_evidence_ids=[],
                error_code=None,
                redacted_error_summary=None,
            )

    def test_duplicate_invocation_id_across_ledger(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        r1 = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000001",
            run_id=run_id,
            task_id="t1",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash="a" * 64,
            started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            finished_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
            status="SUCCEEDED",
            raw_output_hash="a" * 64,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        r2 = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000001",
            run_id=run_id,
            task_id="t2",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash="a" * 64,
            started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            finished_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
            status="SUCCEEDED",
            raw_output_hash="a" * 64,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        with pytest.raises(ValidationError, match="every invocation_id must be unique across tool and LLM records"):
            InvocationLedger(records=[r1, r2])

    def test_second_preflight_call_for_one_run(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        r1 = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000001",
            run_id=run_id,
            task_id="t",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash="a" * 64,
            started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            finished_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
            status="SUCCEEDED",
            raw_output_hash="a" * 64,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        r2 = ToolInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000002",
            run_id=run_id,
            task_id="t",
            owner="GalaxFoundationFlow",
            tool_profile_id="tp",
            operation="repository_preflight_tool",
            input_hash="a" * 64,
            started_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            finished_at=datetime(2026, 7, 21, 12, 1, 0, tzinfo=timezone.utc),
            status="SUCCEEDED",
            raw_output_hash="a" * 64,
            affected_resources=[],
            external_evidence_ids=[],
            error_code=None,
            redacted_error_summary=None,
        )
        with pytest.raises(ValidationError, match="repository_preflight_tool invocation count must not exceed 1 per run"):
            InvocationLedger(records=[r1, r2])

    def test_llm_profile_mismatch(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="llm_profile_readiness profile must match run manifest approved profile"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="profile_a",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="initial",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                llm_profile_readiness=LLMProfileReadinessResult(
                    run_id=run_id,
                    status="APPROVED",
                    profile_id="profile_b",
                    profile_defined=True,
                    profile_enabled=True,
                    provider_live_tested=True,
                    agent_profile_approved=True,
                    profile_matches_engineering_manager=True,
                    data_classification_allowed=True,
                    credential_available=True,
                    capacity_snapshot_valid=True,
                    failed_conditions=[],
                    evidence_ids=["evt"],
                    safe_remedy=None,
                    checked_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
            )

    def test_non_contiguous_route_history(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="route history is not contiguous"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="preflight_tool_available",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                route_history=[RouteTransitionRecord(
                    from_route="initial",
                    to_route="preflight_tool_available",
                    router_name="r",
                    evidence_ids=["evt"],
                    transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                )],
            )

    def test_transition_after_terminal_route(self) -> None:
        with pytest.raises(ValidationError, match="no transition is allowed from terminal route"):
            RouteTransitionRecord(
                from_route="agent_recommends_stop",
                to_route="human_review_required",
                router_name="r",
                evidence_ids=["evt"],
                transitioned_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            )

    def test_unsupported_supported_claim(self) -> None:
        # Required/missing evidence => ABSENT; an unsupported supported claim
        # cannot reach PASS (empty trusted evidence means the referenced
        # evidence_id is ABSENT).
        with pytest.raises(ValidationError, match="reason=ABSENT"):
            self._failure2_state(
                evidence_records=(),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def _human_review_route_history(self) -> tuple[RouteTransitionRecord, ...]:
        ts = datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc)
        return (
            RouteTransitionRecord(from_route="initial", to_route="manifest_valid", router_name="r", evidence_ids=["evt_r1"], transitioned_at=ts),
            RouteTransitionRecord(from_route="manifest_valid", to_route="preflight_tool_available", router_name="r", evidence_ids=["evt_r2"], transitioned_at=ts),
            RouteTransitionRecord(from_route="preflight_tool_available", to_route="preflight_requires_evaluation", router_name="r", evidence_ids=["evt_r3"], transitioned_at=ts),
            RouteTransitionRecord(from_route="preflight_requires_evaluation", to_route="llm_profile_approved", router_name="r", evidence_ids=["evt_r4"], transitioned_at=ts),
            RouteTransitionRecord(from_route="llm_profile_approved", to_route="human_review_required", router_name="r", evidence_ids=["evt_r5"], transitioned_at=ts),
        )

    def _llm_record(
        self,
        *,
        finished_at,
        run_id="00000000-0000-0000-0000-000000000001",
        task_id="evaluate_preflight_result",
        agent_id="engineering_manager",
        status="SUCCEEDED",
    ) -> LLMInvocationRecord:
        started = datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc)
        succeeded = status == "SUCCEEDED"
        return LLMInvocationRecord(
            invocation_id="00000000-0000-0000-0000-000000000101",
            run_id=run_id,
            task_id=task_id,
            agent_id=agent_id,
            llm_profile_id="p",
            prompt_hash="a" * 64,
            started_at=started,
            finished_at=finished_at,
            status=status,
            raw_response_hash="a" * 64 if succeeded else None,
            structured_output_hash="a" * 64 if succeeded else None,
            error_code=None if succeeded else "err_code",
            redacted_error_summary=None if succeeded else "redacted",
        )

    def _evidence_record(
        self,
        *,
        evidence_id: str = "evt",
        run_id: str = "00000000-0000-0000-0000-000000000001",
        task_id: str = "evaluate_preflight_result",
        agent_id: str = "engineering_manager",
        created_at=None,
        expires_at=None,
    ) -> EvidenceRecord:
        return EvidenceRecord(
            evidence_id=evidence_id,
            source="GalaxFoundationFlow",
            content_hash="a" * 64,
            created_at=created_at or datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            run_id=run_id,
            task_id=task_id,
            agent_id=agent_id,
            expires_at=expires_at,
        )

    def _failure2_state(
        self,
        evidence_records,
        *,
        status="PASS",
        exact_remedies=(),
        current_route="initial",
        route_history=(),
        llm_records=(),
    ) -> FoundationFlowState:
        run_id = "00000000-0000-0000-0000-000000000001"
        return FoundationFlowState(
            run_manifest=RunManifest(
                run_id=run_id,
                repository_id="owner/repo",
                repository_root="/tmp/repo",
                expected_branch="main",
                expected_head_sha="a" * 40,
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_id="p",
                approved_tool_profile_id="t",
                allowed_paths=[],
                protected_paths=[],
                data_classification="public",
                phase_authorization="PHASE_0",
                requires_live_github_access=False,
                github_permission_evidence_id=None,
                created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
            ),
            current_route=current_route,
            route_history=route_history,
            trusted_registries=TrustedRegistries(
                approved_agent_ids=["engineering_manager"],
                approved_llm_profile_ids=[],
                approved_tool_profile_ids=[],
                evidence_records=evidence_records,
                offline_permission_declarations=[],
                live_github_permission_evidence=[],
            ),
            invocation_ledger=InvocationLedger(llm_records=llm_records),
            agent_task_result=AgentTaskResult(
                run_id=run_id,
                agent_id="engineering_manager",
                direct_tool_calls=0,
                task_id="evaluate_preflight_result",
                status=status,
                summary="s",
                supported_claims=[SupportedClaim(statement="x", evidence_id="evt")],
                unsupported_claims=[],
                next_transition="HUMAN_REVIEW",
                exact_remedies=exact_remedies,
                preflight_invocation_id="00000000-0000-0000-0000-000000000100",
                preflight_result_hash="a" * 64,
                llm_invocation_id="00000000-0000-0000-0000-000000000101",
                llm_profile_id="p",
                output_hash="a" * 64,
            ),
        )

    def test_supported_claim_trusted_matching_valid(self) -> None:
        state = self._failure2_state(
            evidence_records=(self._evidence_record(),),
            llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
        )
        assert state.agent_task_result
        assert state.agent_task_result.supported_claims[0].evidence_id == "evt"

    def test_supported_claim_untrusted_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="reason=UNTRUSTED"):
            self._failure2_state(
                evidence_records=(self._evidence_record(evidence_id="other_evt"),),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def test_supported_claim_mismatched_run_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="reason=MISMATCHED"):
            self._failure2_state(
                evidence_records=(self._evidence_record(run_id="00000000-0000-0000-0000-000000000002"),),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def test_supported_claim_mismatched_task_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="reason=MISMATCHED"):
            self._failure2_state(
                evidence_records=(self._evidence_record(task_id="other_task"),),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def test_supported_claim_mismatched_agent_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="reason=MISMATCHED"):
            self._failure2_state(
                evidence_records=(self._evidence_record(agent_id="other_agent"),),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def test_supported_claim_expired_cannot_pass(self) -> None:
        record = self._evidence_record(
            created_at=datetime(2026, 7, 21, 11, 50, 0, tzinfo=timezone.utc),
            expires_at=datetime(2026, 7, 21, 12, 3, 0, tzinfo=timezone.utc),
        )
        with pytest.raises(ValidationError, match="reason=EXPIRED"):
            self._failure2_state(
                evidence_records=(record,),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            )

    def test_supported_claim_missing_validity_context_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="supported claim validity cannot be established"):
            self._failure2_state(evidence_records=(), llm_records=())

    def test_supported_claim_failed_llm_validity_cannot_pass(self) -> None:
        with pytest.raises(ValidationError, match="supported claim validity cannot be established"):
            self._failure2_state(
                evidence_records=(self._evidence_record(),),
                llm_records=(self._llm_record(
                    finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                    status="FAILED",
                ),),
            )

    def test_bad_evidence_blocked_human_review_route_valid(self) -> None:
        state = self._failure2_state(
            evidence_records=(self._evidence_record(run_id="00000000-0000-0000-0000-000000000002"),),
            llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
            status="BLOCKED",
            exact_remedies=("resolve supported-claim evidence trust",),
            current_route="human_review_required",
            route_history=self._human_review_route_history(),
        )
        assert state.agent_task_result
        assert state.agent_task_result.status == "BLOCKED"
        assert state.agent_task_result.next_transition == "HUMAN_REVIEW"
        assert state.current_route == "human_review_required"

    def test_bad_evidence_cannot_remain_on_unrelated_route(self) -> None:
        with pytest.raises(ValidationError, match="current_route='initial'"):
            self._failure2_state(
                evidence_records=(self._evidence_record(run_id="00000000-0000-0000-0000-000000000002"),),
                llm_records=(self._llm_record(finished_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc)),),
                status="BLOCKED",
                exact_remedies=("resolve supported-claim evidence trust",),
                current_route="initial",
                route_history=(),
            )

    def test_preflight_binding_mismatch(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        other_run_id = "00000000-0000-0000-0000-000000000002"
        with pytest.raises(ValidationError, match="run_id must match run_manifest.run_id"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="preflight_tool_available",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=other_run_id,
                    overall_status="PASS",
                    checks=[],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
            )

    def test_human_decision_request_mismatch(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="run_id must match run_manifest.run_id"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="initial",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                human_review_request=HumanReviewRequest(
                    request_id="00000000-0000-0000-0000-000000000053",
                    run_id=run_id,
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    agent_llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    preflight_result_hash="a" * 64,
                    agent_task_result_hash="a" * 64,
                    requested_action="REVIEW_FOUNDATION_EVIDENCE",
                    current_status="AWAITING_HUMAN_REVIEW",
                    confirmed_evidence=[],
                    missing_evidence=[],
                    risks=[],
                    recommended_next_step="AWAIT_AUTHENTICATED_HUMAN_DECISION",
                    prohibited_next_steps=[
                        "merge_to_main_or_master",
                        "deployment",
                        "activation_of_Agents_02_to_15",
                        "enabling_unvalidated_LLM_profiles",
                    ],
                    human_decision="PENDING",
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
            )

    def test_decision_before_review_creation(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="decided_at must not be earlier than human_review_request.created_at"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="initial",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                human_review_request=HumanReviewRequest(
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    agent_llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    preflight_result_hash="a" * 64,
                    agent_task_result_hash="a" * 64,
                    requested_action="REVIEW_FOUNDATION_EVIDENCE",
                    current_status="AWAITING_HUMAN_REVIEW",
                    confirmed_evidence=[],
                    missing_evidence=[],
                    risks=[],
                    recommended_next_step="AWAIT_AUTHENTICATED_HUMAN_DECISION",
                    prohibited_next_steps=[
                        "merge_to_main_or_master",
                        "deployment",
                        "activation_of_Agents_02_to_15",
                        "enabling_unvalidated_LLM_profiles",
                    ],
                    human_decision="PENDING",
                    created_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 5, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
            )

    def test_completion_requires_pass_agent_task_result(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires PASS agent_task_result"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="PASS",
                    checks=[],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="BLOCKED",
                    summary="s",
                    supported_claims=[],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )

    def test_completion_requires_authenticated_approval(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires authenticated APPROVED decision"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="PASS",
                    checks=[],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[
                        SupportedClaim(
                            statement="x",
                            evidence_id="evt",
                        )
                    ],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="REJECTED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )

    def test_completion_requires_exactly_one_preflight_tool(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires exactly one preflight tool record"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="PASS",
                    checks=[],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=0,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[
                        SupportedClaim(
                            statement="x",
                            evidence_id="evt",
                        )
                    ],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )

    def test_completion_requires_zero_direct_agent_tools(self) -> None:
        run_id = "00000000-0000-0000-0000-000000000001"
        with pytest.raises(ValidationError, match="completion requires zero direct Agent 01 tools"):
            FoundationFlowState(
                run_manifest=RunManifest(
                    run_id=run_id,
                    repository_id="owner/repo",
                    repository_root="/tmp/repo",
                    expected_branch="main",
                    expected_head_sha="a" * 40,
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_id="p",
                    approved_tool_profile_id="t",
                    allowed_paths=[],
                    protected_paths=[],
                    data_classification="public",
                    phase_authorization="PHASE_0",
                    requires_live_github_access=False,
                    github_permission_evidence_id=None,
                    created_at=datetime(2026, 7, 21, 12, 0, 0, tzinfo=timezone.utc),
                ),
                current_route="foundation_completed",
                trusted_registries=TrustedRegistries(
                    approved_agent_ids=["engineering_manager"],
                    approved_llm_profile_ids=[],
                    approved_tool_profile_ids=[],
                    evidence_records=[],
                    offline_permission_declarations=[],
                    live_github_permission_evidence=[],
                ),
                invocation_ledger=InvocationLedger(),
                preflight_result=RepositoryPreflightResult(
                    run_id=run_id,
                    overall_status="PASS",
                    checks=[],
                    blocking_reasons=[],
                    invocation_id="00000000-0000-0000-0000-000000000010",
                    input_hash="a" * 64,
                    result_hash="a" * 64,
                ),
                agent_task_result=AgentTaskResult(
                    run_id=run_id,
                    agent_id="engineering_manager",
                    direct_tool_calls=1,
                    task_id="evaluate_preflight_result",
                    status="PASS",
                    summary="s",
                    supported_claims=[],
                    unsupported_claims=[],
                    next_transition="HUMAN_REVIEW",
                    exact_remedies=[],
                    preflight_invocation_id="00000000-0000-0000-0000-000000000010",
                    preflight_result_hash="a" * 64,
                    llm_invocation_id="00000000-0000-0000-0000-000000000101",
                    llm_profile_id="p",
                    output_hash="a" * 64,
                ),
                authenticated_human_decision=AuthenticatedHumanDecision(
                    decision_id="00000000-0000-0000-0000-000000000020",
                    request_id="00000000-0000-0000-0000-000000000021",
                    run_id=run_id,
                    decision="APPROVED",
                    authenticated_actor_id="actor",
                    authentication_evidence_id="evt",
                    decision_reason="r",
                    decided_at=datetime(2026, 7, 21, 12, 10, 0, tzinfo=timezone.utc),
                    decision_hash="a" * 64,
                ),
                completion_record=FoundationCompletionRecord(
                    completion_id="00000000-0000-0000-0000-000000000030",
                    run_id=run_id,
                    decision_id="00000000-0000-0000-0000-000000000020",
                    final_checkpoint_id="00000000-0000-0000-0000-000000000031",
                    final_output_hash="a" * 64,
                    completed_at=datetime(2026, 7, 21, 12, 20, 0, tzinfo=timezone.utc),
                    status="COMPLETED",
                ),
            )