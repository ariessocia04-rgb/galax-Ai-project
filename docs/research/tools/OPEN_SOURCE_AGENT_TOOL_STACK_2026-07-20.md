# Open-Source Agent Tool Stack — 2026-07-20

**Status:** `DISCOVERY_AND_CAPABILITY_RECORD`  
**Implementation:** `NOT_STARTED`  
**Approved tools:** `0`  
**Rule:** These components are underlying dependencies of Galax role-scoped composite tools. They are not exposed as separate direct tools to agents, and none is approved until an exact version, license, configuration, output parser, security boundary, and test suite is pinned.

## 1. Architecture rule

```text
one CrewAI agent
→ one Galax role-specific BaseTool interface
→ trusted gateway/controller
→ zero or more pinned underlying open-source components
→ normalized typed evidence
```

The agent never receives an unrestricted shell or the raw command line for these components. The gateway chooses fixed commands/options from an allowlist, enforces paths and limits, and returns typed evidence with invocation IDs and artifact hashes.

## 2. Research discovery — SearXNG

**Candidate use:** Agent 03 search discovery backend.  
**Status:** `SELECTED_FOR_VALIDATION_NOT_AUTHORITY`.

Official sources:

- [SearXNG container installation](https://docs.searxng.org/admin/installation-docker)
- [SearXNG Search API](https://docs.searxng.org/dev/search_api.html)
- [SearXNG source repository](https://github.com/searxng/searxng)

Verified primitives:

```text
- self-hosted container/Compose deployment
- GET or POST search API
- JSON/CSV/RSS result formats when enabled
- configurable engines, categories, language, time range, and safe search
```

Limitations and remedy:

```text
- Search results are discovery pointers, not factual authority.
- Queries are sent to configured upstream engines and may be throttled or blocked.
- Public instances may disable JSON output and are not selected for trusted automation.
- Galax must self-host a pinned image/configuration.
- A separate strict fetcher reads only approved official sources and records hashes/dates.
- Search-engine and website terms, robots rules, and rate limits must be respected.
```

## 3. UI and accessibility evidence — Playwright

**Candidate use:** Agents 05 and 12 through `UXWorkspaceTool` and `TestRunnerTool`.  
**Status:** `SELECTED_FOR_LOCAL_AND_STAGING_VALIDATION`.

Official sources:

- [Playwright documentation](https://playwright.dev/docs/intro)
- [ARIA snapshot testing](https://playwright.dev/docs/aria-snapshots)
- [Accessibility testing](https://playwright.dev/docs/accessibility-testing)
- [Playwright repository](https://github.com/microsoft/playwright)

Verified primitives:

```text
- browser automation and assertions
- page and locator ARIA snapshots
- accessibility-tree structural comparison
- integration with @axe-core/playwright for common automated accessibility findings
- screenshots, traces, console/network evidence, and test artifacts
```

Limitations and remedy:

```text
- Automated accessibility tests find only some issues.
- They do not certify WCAG/legal compliance.
- Snapshot updates can hide regressions if accepted without review.
- Targets are local or approved staging only.
- Production customer sessions/data are prohibited.
- Snapshot updates require explicit reviewed change evidence.
```

## 4. Python static security — Bandit

**Candidate use:** Agent 11 through `SecurityAuditTool`.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [Bandit documentation](https://bandit.readthedocs.io/en/latest/)
- [Bandit command reference](https://bandit.readthedocs.io/en/latest/man/bandit.html)
- [Bandit repository](https://github.com/PyCQA/bandit)

Verified primitive:

```text
Bandit parses Python files into an AST, runs security-oriented plugins, and produces reports for common Python code security issues.
```

Limitations:

```text
- Findings can be false positives or context dependent.
- It does not prove an application is secure.
- It is Python-specific and does not replace dependency, secret, container, or runtime testing.
- Suppressions/baselines require explicit reviewed evidence.
```

## 5. Python dependency audit — pip-audit

**Candidate use:** Agents 11 and 13 through their assigned composite tools.  
**Status:** `SELECTED_FOR_VALIDATION_READ_ONLY_MODE`.

Official sources:

- [pip-audit repository and documentation](https://github.com/pypa/pip-audit)
- [Python Packaging Advisory Database](https://github.com/pypa/advisory-database)

Verified primitives:

```text
- audits Python environments, requirements, lock/project inputs, and dependency trees for known vulnerabilities
- supports PyPI and OSV vulnerability services
- machine-readable output and CycloneDX SBOM output
```

Galax restrictions:

```text
- Automatic --fix is prohibited for Agent 11.
- Audit only already pinned/approved environments or hashed requirements where possible.
- The tool's own security model warns that auditing dependency inputs can involve dependency resolution similar to installation.
- It does not detect arbitrary malicious packages or all transitive native-library risks.
```

## 6. Repository, filesystem, image, secret, license, and misconfiguration scan — Trivy

**Candidate use:** Agents 11 and 13.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [Trivy documentation](https://trivy.dev/docs/latest/)
- [Filesystem scanning](https://trivy.dev/docs/latest/target/filesystem/)
- [Repository scanning](https://trivy.dev/docs/latest/target/repository/)
- [Trivy repository](https://github.com/aquasecurity/trivy)

Verified primitives:

```text
- vulnerability scanning
- secret scanning
- opt-in misconfiguration scanning
- opt-in license scanning
- repository/filesystem/image/SBOM targets
- SBOM generation
```

Limitations and remedy:

```text
- Not every scanner is enabled by default.
- Vulnerability databases and policy checks change and must be fingerprinted.
- License classification is opinionated and unknown results require human review.
- Findings require validation; no automatic remediation.
- Scans run in a bounded sandbox with explicit timeout, cache/database policy, and redacted output.
```

## 7. Dedicated secret scanning — Gitleaks

**Candidate use:** repository write preflight, Agents 11 and 13.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [Gitleaks repository](https://github.com/gitleaks/gitleaks)
- [Gitleaks organization](https://github.com/gitleaks)

Verified primitives:

```text
- scans Git history, directories/files, or stdin for secrets
- supports JSON, CSV, JUnit, SARIF, and other reports
- supports redaction, baselines, allowlists, configuration, and timeouts
```

Important current note:

The project currently describes Gitleaks as feature complete, with future releases focused on security patches. This is not a rejection, but exact release/version maintenance and security support must be monitored.

Galax restrictions:

```text
- use full redaction in stored outputs
- never save matched secret values
- allowlists/baselines require reviewed evidence
- a clean scan does not prove no secret exists
- no agent may bypass the scanner or add an ignore without owner/security approval
```

## 8. Dockerfile linting — Hadolint

**Candidate use:** Agent 13 through `CIBuildWorkspaceTool`.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [Hadolint repository](https://github.com/hadolint/hadolint)
- [Hadolint README](https://github.com/hadolint/hadolint/blob/master/README.md)

Verified primitives:

```text
- parses Dockerfiles into an AST
- applies Dockerfile best-practice rules
- uses ShellCheck for Bash within RUN instructions
- supports machine-readable formats and configured severity/ignore rules
```

Limitations:

```text
- lint findings do not prove an image is secure or functional
- ignored rules require explicit justification
- image builds, runtime tests, SBOM, and vulnerability scans remain separate gates
```

## 9. GitHub Actions workflow checking — actionlint

**Candidate use:** Agent 13 through `CIBuildWorkspaceTool`.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [actionlint repository](https://github.com/rhysd/actionlint)
- [actionlint README](https://github.com/rhysd/actionlint/blob/main/README.md)

Verified primitives:

```text
- syntax and schema checks for GitHub Actions workflows
- expression type checks
- action input/output checks
- reusable workflow checks
- optional ShellCheck and pyflakes integrations
```

Limitations:

```text
- static validation does not prove the workflow succeeds in GitHub Actions
- no production workflow execution or secret access is granted to the agent
- workflow modifications require a separately approved repository path/permission profile
```

## 10. Observability — OpenTelemetry Python

**Candidate use:** Galax instrumentation and Agent 14 read-only evidence.  
**Status:** `SELECTED_FOR_VALIDATION`.

Official sources:

- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/)
- [OpenTelemetry Python repository](https://github.com/open-telemetry/opentelemetry-python)

Verified current component status from official documentation:

```yaml
traces: stable
metrics: stable
logs: development
python_support: '3.10+'
```

Galax restrictions:

```text
- telemetry must exclude raw prompts, secrets, customer data, and unrestricted repository contents
- Agent 14 receives bounded redacted evidence only
- logs being development-status means exact log SDK/exporter behavior needs separate validation
```

## 11. Metrics querying — Prometheus

**Candidate use:** Agent 14 through `ObservabilityReadTool`.  
**Status:** `SELECTED_FOR_READ_ONLY_VALIDATION`.

Official sources:

- [Prometheus documentation](https://prometheus.io/docs/introduction/overview/)
- [PromQL querying basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [Prometheus repository](https://github.com/prometheus/prometheus)

Verified primitives:

```text
- PromQL selects and aggregates time-series data
- instant and range queries
- HTTP API retrieval of query results
```

Galax restrictions:

```text
- approved read-only endpoint and query templates
- cardinality/result-size/time-range limits
- no configuration, rule, silence, target, or production mutation
- root-cause statements require correlated traces, metrics, logs, and deployment evidence
```

## 12. Additional candidates requiring separate source cards before use

```text
- pytest and pytest-asyncio for Python tests
- Ruff and mypy for lint/type evidence
- Semgrep for approved SAST rulesets
- axe-core through @axe-core/playwright
- Syft or Trivy for SBOM generation
- Docker BuildKit/buildx and Docker Compose validation
- PostgreSQL disposable test database
- official MCP SDK and mock MCP servers
```

Listing a component here does not approve it. Its exact version, license, command policy, schema, and tests must be added to a source card before implementation.

## 13. Common wrapper contract

Every scanner/runner wrapper returns normalized evidence equivalent to:

```yaml
component_invocation:
  invocation_id:
  component_id:
  exact_version:
  binary_or_image_digest:
  configuration_hash:
  target_hash:
  command_profile_id:
  started_at:
  finished_at:
  exit_code:
  status:
  findings_summary:
  raw_artifact_path:
  raw_artifact_sha256:
  redactions_applied:
  errors: []
```

The raw command is selected by trusted code, not generated freely by the LLM.

## 14. Approval gate

```text
OFFICIAL SOURCE AND LICENSE
→ EXACT RELEASE/IMAGE DIGEST PIN
→ COMMAND AND PATH ALLOWLIST
→ INPUT/OUTPUT SCHEMA
→ SANDBOX AND RESOURCE LIMITS
→ REDACTION
→ POSITIVE/NEGATIVE/FALSE-POSITIVE TESTS
→ ROLE-SPECIFIC WRAPPER TEST
→ SECURITY REVIEW
→ STATUS = APPROVED_COMPONENT
```

## 15. Current decision

```yaml
SearXNG: candidate_not_authority
Playwright: candidate_local_staging_only
Bandit: candidate_read_only_scanner
pip_audit: candidate_read_only_dependency_audit
Trivy: candidate_read_only_multi_scanner
Gitleaks: candidate_read_only_secret_scanner
Hadolint: candidate_Dockerfile_linter
actionlint: candidate_workflow_checker
OpenTelemetry: candidate_instrumentation
Prometheus: candidate_read_only_metrics
all_exact_versions_pinned: false
all_wrappers_implemented: false
all_components_approved: false
```
