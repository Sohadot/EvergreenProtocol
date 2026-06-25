# Decision Log — evergreenprotocol.com

This log records material architectural and strategic decisions governing the asset's build within the Sovereign Asset System.

Each entry states the decision, rationale, scope, and explicit non-decisions so that future operators can understand what was chosen, what was ruled out, and why.

---

## 2026-06-25 — Static versioned machine-readable reference layer

**Decision:** Evergreen Protocol now exposes a static, versioned machine-readable reference layer to support AI-era digital continuity, citation stability, and future operating partnerships — without creating a tool, certification system, or dynamic API.

**Rationale:** Reference standards that cannot be consumed by AI agents, institutional systems, and programmatic governance workflows are structurally incomplete in the AI era. Static JSON files at stable, versioned URLs fulfill the machine-readability requirement while preserving the governance integrity of a static-first architecture. A standard claiming to govern AI-era digital continuity must itself be AI-consumable.

**Scope of this decision:**

Files governed by this decision:
- `/definitions.json` — public canonical definitions index (15 governed terms)
- `/protocol/v1/definitions.json` — version-pinned definitions for v1.0
- `/protocol/v1/standard.json` — machine-readable standard summary for v1.0
- `/protocol/v1/citation.json` — machine-readable citation formats for v1.0

Localized English mirrors may exist under `/en/` for continuity with existing public pages.

Human-readable index: `/machine-readable/`

**Version pinning rule:** Files under `/protocol/v1/` are immutable after publication. Future standard versions create new paths (`/protocol/v1.1/`, `/protocol/v2/`). The live index at `/definitions.json` may be updated on minor or major version change.

**Explicit non-decisions (ruled out by this decision):**
- No dynamic API created.
- No MCP-compatible endpoint created (future-gated — not in this architecture).
- No certification engine created.
- No compliance registry opened.
- No readiness checklist opened.
- No external submission system created.
- No live scoring or assessment endpoint created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 2 — Versioned Machine-Readable Reference Layer
**Related:** `architecture.md` machine-readable layer section


---

## 2026-06-25 — Controlled reference application layer

**Decision:** Evergreen Protocol now exposes a controlled reference application layer to demonstrate applicability across AI documentation, knowledge systems, digital infrastructure, and strategic digital assets while preserving non-certification boundaries.

**Rationale:** A category standard becomes more legible when readers can see how its concepts apply to real continuity problems. The application layer demonstrates reference decay, evidence posture, version discipline, citation stability, and update governance without assessing outside parties or creating registry behavior.

**Scope of this decision:**

Public application routes:
- `/applications/`
- `/applications/ai-documentation-continuity/`
- `/applications/knowledge-system-continuity/`
- `/applications/digital-infrastructure-continuity/`
- `/applications/strategic-digital-asset-continuity/`

**Explicit non-decisions (ruled out by this decision):**
- No registry opened.
- No third-party assessment workflow created.
- No checklist, tool, calculated-output workflow, or readiness endpoint created.
- No dynamic backend created.
- No external company assessment created.
- No certification, validation, verification, endorsement, or external recognition created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 3 — Reference Application Layer v1
**Related:** `architecture.md` reference application layer section


---

## 2026-06-25 — Reference continuity readiness entry point

**Decision:** Evergreen Protocol now exposes a practical readiness entry point to make reference continuity legible to institutional readers while preserving non-certification boundaries.

**Rationale:** Institutional readers need a practical way to orient around the core dimensions of reference continuity before adopting formal protocols or machine-readable reference structures. A static self-orientation guide provides that entry point without creating a tool, backend, registry, form submission path, or external evaluation workflow.

**Scope of this decision:**

Public route:
- `/reference-continuity-readiness/`

Covered readiness dimensions:
- Version discipline
- Citation stability
- Evidence posture
- Definition control
- Changelog integrity
- Update governance
- Machine-readable reference structure

**Explicit non-decisions (ruled out by this decision):**
- No diagnostic tool created.
- No form submission path created.
- No registry opened.
- No dynamic backend created.
- No calculated-output workflow created.
- No certification or external evaluation workflow created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 4 — Reference Continuity Readiness Entry Point
**Related:** `architecture.md` reference continuity readiness layer section
