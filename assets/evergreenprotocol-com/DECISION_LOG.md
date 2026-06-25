# Decision Log — evergreenprotocol.com

This log records material architectural and strategic decisions governing the asset's build within the Sovereign Asset System.

Each entry states the decision, rationale, scope, and explicit non-decisions so that future operators can understand what was chosen, what was ruled out, and why.

---

## 2026-06-25 — Static versioned machine-readable reference layer

**Decision:** Evergreen Protocol now exposes a static, versioned machine-readable reference layer to support AI-era digital continuity, citation stability, and future operating partnerships — without creating a tool, certification system, or dynamic API.

**Rationale:** Reference standards that cannot be consumed by AI agents, institutional systems, and programmatic governance workflows are structurally incomplete in the AI era. Static JSON files at stable, versioned URLs fulfill the machine-readability requirement while preserving the governance integrity of a static-first architecture. A standard claiming to govern AI-era digital continuity must itself be AI-consumable.

**Scope of this decision:**

Files governed by this decision:
- `/en/definitions.json` — live canonical definitions index (24 terms)
- `/en/protocol/v1/definitions.json` — version-pinned definitions for v1.0
- `/en/protocol/v1/standard.json` — machine-readable standard summary for v1.0
- `/en/protocol/v1/citation.json` — machine-readable citation formats for v1.0

Human-readable index: `/en/machine-readable/`

**Version pinning rule:** Files under `/en/protocol/v1/` are immutable after publication. Future standard versions create new paths (`/en/protocol/v1.1/`, `/en/protocol/v2/`). The live index at `/en/definitions.json` may be updated on minor or major version change.

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
