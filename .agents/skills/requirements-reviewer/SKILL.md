---
name: requirements-reviewer
description: Compare a feature specification with its implementation and report acceptance coverage, gaps, unsupported behavior, data or security concerns, and tests still needed. Use for evidence-based requirements reviews; does not modify project files.
---

# Requirements Reviewer

Review a feature specification against the current implementation and produce an evidence-based assessment. Treat the specification and code as read-only. Do not edit, generate, or delete project files, and do not run commands that modify repository state. The user must separately ask for implementation changes before any files are changed.

## Review workflow

1. Identify the applicable specification and implementation files. If multiple versions or scopes are plausible, state which ones you reviewed and the assumption used.
2. Extract the specification's acceptance criteria and any stated constraints, including data handling, permissions, validation, and failure behavior.
3. Trace each criterion into the implementation. Inspect relevant callers, data models, persistence, and tests where needed to confirm the behavior.
4. Report findings with precise evidence. Cite specification and code locations using clickable file links with line numbers when available, or `path:line` references. Each claim about expected behavior should cite the specification; each claim about implemented behavior should cite the code. Do not present inference as a directly stated requirement.
5. Call out uncertainty where the available files do not establish behavior. Do not treat absence of evidence as proof of absence; describe what was searched or inspected.

## Required report

Use these sections:

- **Satisfied acceptance criteria** — criteria supported by implementation evidence.
- **Gaps** — criteria that are missing, incomplete, or inconsistent with the implementation.
- **Unsupported behavior** — behavior implied by the specification or user expectation that the inspected implementation does not establish or support. Distinguish this from confirmed gaps when evidence is incomplete.
- **Data or security concerns** — relevant risks in validation, authorization, confidentiality, integrity, storage, logging, or exposure. Include only concerns grounded in the spec or code; otherwise say none were identified in the inspected scope.
- **Tests still needed** — scenarios not adequately covered by existing tests, tied to criteria or concerns. Recommend tests; do not create or run them unless the user asks.

Map every acceptance criterion to one outcome: satisfied, partial, unmet, or unclear. Keep findings concise, prioritize consequential issues, and include both requirement evidence and implementation evidence for each comparison. When a section has no findings, say so explicitly and identify any scope limitation that matters.
