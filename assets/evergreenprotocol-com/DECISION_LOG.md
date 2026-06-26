# Decision Log — evergreenprotocol.com

This log records material architectural and strategic decisions governing the asset's build within the Sovereign Asset System.

Each entry states the decision, rationale, scope, and explicit non-decisions so that future operators can understand what was chosen, what was ruled out, and why.

---

## 2026-06-26 — Reference decay core term page

**Decision:** Evergreen Protocol now owns the term “reference decay” through a dedicated core term page at `/reference-decay/`. The page defines the term, explains why AI agents make it urgent, distinguishes it from model risk, lists seven common decay forms, and reads it through six Evergreen Protocol governance dimensions.

**Rationale:** Category inevitability does not begin with framework declaration. It begins with owning the term that names the pain. Enterprises searching for a definition of reference decay — or an AI agent retrieving a reference on the concept — should find Evergreen Protocol’s governed page as the clearest, most structured, and most citable available definition. Term ownership at `/reference-decay/` precedes and enables framework adoption. The page does not sell the protocol; it defines the problem the protocol addresses.

**Scope of this decision:**

Public route:
- `/reference-decay/`

Page sections:
- Definition of reference decay
- Why it matters as an institutional risk problem
- Why AI agents make it urgent (model risk vs. reference continuity distinction)
- Seven common forms of reference decay
- Reference decay versus model risk (comparison)
- Evergreen Protocol reading across six governance dimensions
- What this page does not claim (non-certification statement)

Inbound links added from:
- Homepage (`/en/`) → `/reference-decay/`
- `/ai-era-digital-continuity/` → `/reference-decay/`
- `/reference-continuity-readiness/` → `/reference-decay/`

Sitemap: `/reference-decay/` added at priority 0.9.

Architecture: new IA row added for `site/reference-decay/index.html`.

**Governing sentence:** The model may still be governed. The reference may no longer be true.

**Explicit non-decisions (ruled out by this decision):**
- No certification language created.
- No registry opened.
- No score, rating, or compliance status produced.
- No form, backend, or tool created.
- No external party assessed or validated.
- No claim that Evergreen Protocol is the only framework addressing reference decay.
- No claim that the term is proprietary — the page claims definitional authority through quality and structure, not exclusivity.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 10 — Reference Decay Core Term Page
**Related:** `architecture.md` information architecture table; `domain-dossier.md` Sprint 10 update log entry


---

## 2026-06-25 — AI-era digital continuity reference page

**Decision:** Evergreen Protocol now includes a root-level flagship reference page at `/ai-era-digital-continuity/` explaining the core market problem the protocol addresses: AI-era digital continuity and reference decay under accelerated institutional change.

**Rationale:** A category standard addressing AI-era digital continuity needs a publicly legible explanation of the problem it governs — not just the standard itself, its applications, and its reference cases. A standalone flagship reference page at the root path makes the problem visible to readers who arrive outside the `/en/` path hierarchy, supporting institutional intelligibility, search discovery, and reader orientation before deeper protocol engagement.

**Scope of this decision:**

Public route:
- `/ai-era-digital-continuity/`

Inbound links added from:
- Homepage (`/en/`) → `/ai-era-digital-continuity/`
- `/en/category-standard/` → `/ai-era-digital-continuity/`
- `/applications/` → `/ai-era-digital-continuity/`
- `/reference-cases/` → `/ai-era-digital-continuity/`
- `/operator-brief/` → `/ai-era-digital-continuity/`

JSON-LD schema: WebPage and CreativeWork only.

Sitemap: `/ai-era-digital-continuity/` added with priority 0.8.

Architecture: new IA row added for `site/ai-era-digital-continuity/index.html`.

**Explicit non-decisions (ruled out by this decision):**
- No certification language created.
- No registry opened.
- No score, rating, or compliance status produced.
- No form, backend, or tool created.
- No MCP endpoint created.
- No dynamic workflow created.
- No external party assessed or validated.
- No preparatory governance files created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 9 — AI-Era Digital Continuity Reference Page
**Related:** `architecture.md` information architecture table; `domain-dossier.md` Sprint 9 update log entry


---

## 2026-06-25 — Self-applied reference cases layer

**Decision:** Evergreen Protocol now includes a controlled self-applied reference cases layer to demonstrate protocol use within Sohadot-governed assets without creating certification, registry, scoring, external validation, or compliance status.

**Rationale:** A category standard gains institutional legibility when proof-of-application is visible, not merely claimed. Self-applied reference cases show how Evergreen Protocol’s continuity principles apply to governed assets within the Sohadot portfolio, demonstrating scope, discipline, and governance without inviting external submissions, issuing compliance status, opening a registry, or creating any derivative certification behavior.

**Scope of this decision:**

Public routes:
- `/reference-cases/`
- `/reference-cases/bisulfid-reference-atlas-continuity/`
- `/reference-cases/euraplan-regulatory-reference-continuity/`
- `/reference-cases/aielectronicchips-dependency-reference-continuity/`
- `/reference-cases/outmerchant-standard-continuity/`

**Explicit non-decisions (ruled out by this decision):**
- No registry opened.
- No certification created.
- No compliance status issued.
- No score or rating produced.
- No external party assessed or validated.
- No submission system created.
- No dynamic backend created.
- No third-party endorsement or market recognition claim made.
- No partner or affiliate claim created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 8 — Self-Applied Reference Cases Layer
**Related:** `architecture.md` information architecture table; `domain-dossier.md` Sprint 8 update log entry


---

## 2026-06-25 — Operator brief layer

**Decision:** Evergreen Protocol now includes an operator brief to make the asset legible to qualified enterprise operators while preserving governance boundaries and avoiding certification, registry, pricing, or acquisition-promise behavior.

**Rationale:** Qualified operators in AI governance, GRC, enterprise knowledge governance, digital preservation, records management, and institutional advisory need a concise, governed entry point that explains the commercial logic, operating model, boundaries, and post-traction acquisition path without creating a sales page, pricing page, public partner program, form, backend, certification system, or acquisition promise. The operator brief provides that entry point.

**Scope of this decision:**

Public route:
- `/operator-brief/`

**Explicit non-decisions (ruled out by this decision):**
- No pricing created.
- No form or backend created.
- No payment flow created.
- No public partner application created.
- No partner logos or external endorsements published.
- No certification program created.
- No compliance status issued.
- No registry opened.
- No score or rating produced.
- No automatic acquisition right granted.
- No domain-for-sale framing introduced.
- No Product, Offer, Service, Review, Rating, Certification, Organization endorsement, or AggregateRating schema used.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 6 — Operator Brief Layer
**Related:** `architecture.md` information architecture table; `domain-dossier.md` Sprint 6 update log entry


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


---

## 2026-06-25 — Strategic operating partnership layer

**Decision:** Evergreen Protocol now exposes a governed strategic operating partnership layer to support qualified operating, licensing, and post-traction acquisition discussions without creating a public sale page, certification program, registry, or uncontrolled commercial claim.

**Rationale:** Evergreen Protocol can become more legible to qualified enterprise operators when the public reference surface explains what may be operated commercially and which boundaries remain controlled. The layer supports serious operating discussions while preserving Sohadot control over the domain, protocol, category standard, and reference integrity.

**Scope of this decision:**

Public route:
- `/strategic-operating-partnership/`

**Explicit non-decisions (ruled out by this decision):**
- No public sale page created.
- No pricing or payment flow created.
- No form submission path created.
- No registry opened.
- No certification program created.
- No partner logos or external endorsements published.
- No automatic acquisition right granted.
- No backend or dynamic workflow created.

**Authority:** Standard owner — evergreenprotocol.com
**Sprint:** Sprint 5 — Strategic Operating Partnership Layer
**Related:** `architecture.md` strategic operating partnership layer section
