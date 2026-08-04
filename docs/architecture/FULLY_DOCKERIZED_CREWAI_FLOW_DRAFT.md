# Fully Containerized Galax CrewAI Flow — Draft

**Status:** `DRAFT_MUTABLE`  
**Meaning of fully containerized:** All Galax application services run as containers. External hosted APIs such as Cerebras, GitHub, Google Drive, and managed Supabase/Notion remain external services.  
**Important exception:** The arbitrary-code sandbox daemon must not run as privileged Docker-in-Docker inside the ordinary application Compose stack.

## 1. Supported architecture boundary

```text
Docker Compose starts and isolates Galax application services.
CrewAI Flow controls deterministic application execution.
Process.sequential controls the selected Crew task order.
Role-specific gateways perform real external actions.
The LLM does not control Docker Compose or container permissions.
```

## 2. Core service topology

```text
owner/client
    │
    ▼
galax-api
    │ one accepted run
    ▼
galax-flow-runner
    ├── repository-gateway ── GitHub API
    ├── drive-knowledge-gateway ── Google Drive API
    ├── memory-gateway ── Supabase Postgres/pgvector
    ├── notion-mirror-gateway ── Notion API (optional curated mirror)
    ├── research-gateway ── official public sources (revalidation profile only)
    └── sandbox-controller ── separate rootless sandbox execution boundary
```

The Flow runner constructs only the approved agents and tasks needed for the current run.

## 3. Compose services

### Always-on core

```yaml
services:
  galax-api:
    purpose: accept owner prompt and return run status
    network: edge_and_internal
    secrets: none_or_session_only

  galax-flow-runner:
    purpose: execute deterministic Flow and selected sequential Crew
    network: internal_plus_allowlisted_provider_egress
    secrets:
      - cerebras_api_key
    concurrency: one_run_worker_initially

  repository-gateway:
    purpose: scoped GitHub read/write on run branch
    network: internal_plus_github_egress
    secrets:
      - github_app_credentials

  drive-knowledge-gateway:
    purpose: approved-folder read-only retrieval and LearningPacket creation
    network: internal_plus_google_apis_egress
    secrets:
      - google_drive_credentials

  memory-gateway:
    purpose: query and write validated machine memory
    network: internal_plus_supabase_or_postgres
    secrets:
      - memory_database_credentials
```

### Optional profiles

```yaml
profiles:
  research:
    - research-gateway
  notion-mirror:
    - notion-mirror-gateway
  local-memory:
    - postgres-pgvector
  full-supabase:
    - separate official Supabase Compose stack
  sandbox:
    - sandbox-controller-client
  observability:
    - otel-collector
    - prometheus
    - grafana
```

Compose profiles are activated by trusted operator/application commands. An LLM response cannot activate a profile.

## 4. Network design

```yaml
networks:
  edge:
    external_ingress: galax-api_only

  control_internal:
    internal: true
    members:
      - galax-api
      - galax-flow-runner
      - role_specific_gateways

  memory_internal:
    internal: true
    members:
      - memory-gateway
      - local_postgres_when_used

  observability_internal:
    internal: true

sandbox_default_network:
  mode: none
```

Where a service needs external access, egress is limited to its exact provider domains through the host firewall, proxy, or dedicated gateway policy. Compose network separation alone is not treated as a complete egress firewall.

## 5. Container security baseline

Every Galax-owned service must start with:

```yaml
user: non_root_numeric_uid
read_only: true
cap_drop:
  - ALL
security_opt:
  - no-new-privileges:true
init: true
pids_limit: explicit
mem_limit: explicit
cpus: explicit
tmpfs:
  - /tmp
```

Exceptions require a documented reason, separate test, and owner approval.

Prohibited:

```text
privileged: true
host PID namespace
host network mode
mounting host / into a container
mounting production SSH directories
sharing every secret with every service
unrestricted Docker socket mounted into CrewAI or an agent container
```

## 6. Secrets

Use Compose secrets granted per service:

```text
/run/secrets/cerebras_api_key
/run/secrets/github_app_private_key
/run/secrets/google_drive_credentials
/run/secrets/supabase_secret_or_database_password
/run/secrets/notion_token
```

The application reads the file at runtime. Secrets are not copied into images, committed to GitHub, placed in prompts, or printed in diagnostics.

## 7. Image build rules

```text
- Use multi-stage builds.
- Pin Python and system dependency versions.
- Commit the Python lockfile.
- Pin base image digest after validation.
- Build wheels/dependencies in a builder stage.
- Copy only runtime artifacts into final image.
- Run as non-root.
- Do not include Git credentials or `.env` files.
- Generate an SBOM and scan the final image.
```

A dependency or image-digest change triggers automatic revalidation.

## 8. Startup gates

Each stateful or gateway service defines a healthcheck. Dependencies use:

```yaml
depends_on:
  memory-gateway:
    condition: service_healthy
  repository-gateway:
    condition: service_healthy
```

The Flow runner must not accept work until mandatory gateways are healthy and their permission self-tests pass.

## 9. One-prompt execution

```text
POST owner request to galax-api
→ authenticate owner
→ create run ID
→ acquire single-run lock
→ record dependency fingerprints
→ run change detector
→ trigger revalidation research if required
→ retrieve GitHub rules, Notion mirror pointers when enabled, and Supabase memory
→ retrieve Google Drive learning material when required
→ create selected sequential Crew segment
→ execute one agent at a time
→ call one role-specific tool interface
→ validate actual tool evidence
→ checkpoint after each stage
→ QA/security/audit
→ create or update draft PR
→ release run lock
```

## 10. Sandbox design correction

### Rejected design

```text
CrewAI container
→ mounted Docker socket
→ unrestricted docker run
```

This gives the container effective control of the Docker daemon and is not an acceptable least-privilege boundary.

Also rejected as default:

```text
privileged rootless Docker-in-Docker
```

Docker documents that rootless DIND still requires `--privileged`.

### Selected validation design

```text
workspace tool
→ authenticated sandbox-controller API
→ separate rootless Docker daemon or separate sandbox host
→ create ephemeral unprivileged container
→ mount only run worktree
→ network none by default
→ allowlisted command
→ resource/time limits
→ capture output and hashes
→ destroy container and temporary volume
```

The separate sandbox host may be the same physical machine during development, but it must use a distinct rootless daemon, protected socket/API, and dedicated storage root. Production approval requires testing that the Galax application containers cannot directly control that daemon outside the narrow controller API.

## 11. Sandbox execution policy

```yaml
sandbox:
  privileged: false
  root_user: false
  network: none_by_default
  filesystem:
    root: read_only
    worktree: scoped_read_write
    secrets: none
  limits:
    cpus: task_profile_specific
    memory: task_profile_specific
    pids: task_profile_specific
    timeout_seconds: task_profile_specific
  commands: allowlisted
  cleanup: mandatory
```

Dependency-download stages require a separate approved network-enabled image-build profile. Normal code/test sandboxes remain offline when dependencies are already present.

## 12. Supabase deployment choices

### Option A — Managed free Supabase pilot

Use the hosted platform for initial validation. Known free-plan constraints include 500 MB database size, project pausing after one week of inactivity, and no automatic backups. The gateway must handle pause/unavailability and the project must produce off-site logical backups.

### Option B — Minimal local Postgres + pgvector

Preferred lightweight fully containerized development memory:

```text
postgres image with pgvector extension
+ migrations
+ memory-gateway
```

This avoids running the entire Supabase product stack when only Postgres and vectors are required.

### Option C — Full self-hosted Supabase

Use Supabase's official tested Compose release as a separate stack/profile. Minimum documented full-stack resources are 4 GB RAM, 2 cores, and 40 GB SSD. Galax must own updates, backups, hardening, and monitoring.

## 13. Notion role

Notion is not part of the mandatory runtime path. It is an optional curated human-readable mirror of approved decisions, lessons, and summaries. If Notion is unavailable, the runtime memory remains in Supabase/Postgres and the Notion mirror is queued or skipped according to policy.

## 14. Observability

Record:

```text
run ID
agent and task IDs
container image digests
CrewAI/LiteLLM versions
provider/model/API version
prompt and tool schema hashes
actual tool invocation IDs
container start/stop and exit status
CPU/memory/time usage
provider token usage
checkpoint hashes
```

Never record raw secrets, unrestricted repository content, or hidden reasoning.

## 15. Failure behavior

```text
mandatory service unhealthy → BLOCKED_DOCKER_SERVICE_UNHEALTHY
fingerprint change → BLOCKED_REVALIDATION_REQUIRED
sandbox unavailable → BLOCKED_SANDBOX_NOT_AVAILABLE
memory unavailable → BLOCKED_MEMORY_UNAVAILABLE
rate limit reached → BLOCKED_LLM_RATE_LIMIT
checkpoint failure → FAILED_CANONICAL_CHECKPOINT
container cleanup failure → FAILED_SANDBOX_CLEANUP
```

A failed mandatory stage stops downstream sequential execution.

## 16. Required tests

```text
DOCKER-001 Build every Galax image from pinned lockfile.
DOCKER-002 Confirm images run as non-root.
DOCKER-003 Confirm root filesystem is read-only.
DOCKER-004 Confirm all Linux capabilities are dropped unless approved.
DOCKER-005 Confirm no-new-privileges is enforced.
DOCKER-006 Confirm secrets are visible only to declared services.
DOCKER-007 Confirm API cannot read gateway-only secrets.
DOCKER-008 Confirm health gates block premature startup.
DOCKER-009 Confirm optional profiles remain inactive by default.
DOCKER-010 Confirm one Flow run lock prevents parallel agent runs.
DOCKER-011 Confirm Process.sequential order inside the worker.
DOCKER-012 Confirm sandbox network is none by default.
DOCKER-013 Confirm sandbox cannot access host filesystem outside worktree.
DOCKER-014 Confirm sandbox cannot access Docker daemon directly.
DOCKER-015 Confirm no privileged DIND service exists.
DOCKER-016 Confirm CPU, memory, PID, and timeout enforcement.
DOCKER-017 Confirm failed sandbox is destroyed.
DOCKER-018 Confirm stale image/dependency fingerprint triggers revalidation.
DOCKER-019 Confirm gateway egress is provider-scoped.
DOCKER-020 Confirm direct main write and automatic merge remain impossible.
DOCKER-021 Confirm restart resumes from canonical checkpoint, not stage one.
DOCKER-022 Confirm logs contain no secret material.
DOCKER-023 Generate and scan SBOMs.
DOCKER-024 Restore memory from tested backup.
DOCKER-025 Stop safely when any mandatory service is unhealthy.
```

Approval requires 25 of 25 tests in the pinned Docker Engine, Compose, OS, CrewAI, LiteLLM, and provider environment.

## 17. Current status

```yaml
application_containerization: FACT_CHECKED_SUPPORTED
docker_compose_topology: SPECIFIED_NOT_IMPLEMENTED
privileged_dind: REJECTED
separate_rootless_sandbox_boundary: SELECTED_FOR_VALIDATION
minimal_postgres_pgvector_profile: SELECTED_FOR_VALIDATION
full_supabase_profile: OPTIONAL_NOT_IMPLEMENTED
production_ready: false
```
