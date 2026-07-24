"""Tests for custom validators in galax.foundation.models.

Covers 5 scalar BeforeValidator functions (via BaseModel wrappers)
and 16 model/field validators.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest
from pydantic import BaseModel, ValidationError

from galax.foundation.models import (
    AgentTaskResult,
    AwareDatetime,
    BlockerRecord,
    EvidenceRecord,
    GitSHA40,
    HumanReviewRequest,
    InvocationLedger,
    LiveGitHubPermissionEvidence,
    OfflinePermissionDeclaration,
    RepositoryId,
    RepositoryPreflightCheck,
    RepositoryPreflightResult,
    RunManifest,
    SHA256Hex,
    StrictText,
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