# NOT YET TOTALLY APPROVED — Backup Package (FULLY SEPARATE FROM APPROVED WORK)

**Created:** 2026-08-24
**Branch:** `backup/not-yet-totally-approved-2026-08-24` (dedicated backup branch)
**Purpose:** Emergency backup before Human Owner PC format.

## ⚠️ SEPARATION GUARANTEE — READ FIRST

This branch and this folder are **100% SEPARATE** from all previously approved / finalized / locked work
(e.g., the Phase 2A accepted plans approved last month on `main`, `plan/phase-2a-external-review-layer-2026-07-27`,
and `agent/agent-01-tool-inspection`).

- NOTHING here replaces, edits, overwrites, or merges with any approved file.
- NOTHING approved is copied INTO this package.
- This is an isolated, additive-only backup of DRAFT / NOT-YET-FINAL material.
- After PC format, pull out only what you need from this branch; approved history stays untouched on its own branches.

## Contents

- `docs/` — plans, rules drafts, prompts, research audits, source cards
- `research/` — Cline qualification framework methods + observation ledger
- `memory-bank/` — MEMORY.md
- `local-only-work-in-progress/` — ⚠️ CRITICAL: files that existed ONLY on the local PC (staged-but-uncommitted Phase 2B implementation code and untracked config). These were at risk of total loss on PC format:
  - `pyproject.toml`, `uv.lock`
  - `src/galax/__init__.py`
  - `src/galax/foundation/models.py`
  - `tests/test_foundation_contracts.py`
  - `.clinerules/00-galax-router-and-execution.md`
  - `.qwen/settings.json`

## How to restore after PC format

```powershell
git clone https://github.com/ariessocia04-rgb/galax-Ai-project.git
cd galax-Ai-project
git checkout backup/not-yet-totally-approved-2026-08-24
# Pull out whatever you need from "not yet totally approved/"
```
