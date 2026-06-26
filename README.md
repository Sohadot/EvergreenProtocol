# Evergreen Protocol

**Evergreen Protocol** is the governed intellectual and editorial frame behind **evergreenprotocol.com**: a **sovereign-grade reference asset** and declared category standard for AI-era digital continuity — developed as a public reference surface, not a product narrative, traffic asset, or informal content stack.

The asset is **governed by the Sovereign Asset System**: strategic posture, narrative hierarchy, authority discipline, and economic order are recorded in the dossier and formal architecture below. **GitHub is the sole source of truth** for what this asset is, how it is structured, and what may ship under its name.

---

## Conceptual core

Continuity for decisions, systems, and digital surfaces is treated as an **operational** property. The reference expresses that stance through three ordered layers:

| Layer | Name | Role |
|-------|------|------|
| Structural | **Architecture of Constancy** | Formal shape: charter, roles, artifacts, acceptance criteria, versioning — what can be built and audited. |
| Philosophical | **Anti-Entropy Protocol** | Necessity: unnecessary drift (tacit exceptions, definition fork, surface decay) made visible and reviewed. |
| Symbolic | **Zero-Season Algorithm** | Review timing tied to **validity and dependency change**, not arbitrary seasonal urgency or spectacle. |

Further narrative and strategic depth live in `domain-dossier.md`. Structural rules for this repository live in `architecture.md`. Material decisions live in `DECISION_LOG.md`.

---

## Canonical asset root

All governed material for this digital asset lives under:

```
assets/evergreenprotocol-com/
```

No second canonical tree may replace or mirror this root inside the repository.

---

## Repository structure (current)

```
assets/evergreenprotocol-com/
  architecture.md          # Formal repo/site structure and layer mapping
  domain-dossier.md        # Sovereign Asset System dossier (identity, thesis, gates)
  DECISION_LOG.md          # Material architectural and strategic decisions, newest-first
  site/
    assets/css/main.css    # Shared stylesheet for the entire public surface
    sitemap.xml            # Public sitemap (HTML pages only)
    definitions.json       # Public canonical definitions index
    protocol/v1/           # Version-pinned machine-readable reference files
      definitions.json
      standard.json
      citation.json
    en/                    # English-locale governed pages
      index.html                         # Home
      category-standard/index.html       # Category Standard v1.0
      ai-era-digital-continuity/index.html
      manifesto/index.html
      methodology/index.html
      definitions/index.html
      cite/index.html
      changelog/index.html
      machine-readable/index.html
    ai-era-digital-continuity/index.html # Flagship problem reference page (root-level)
    machine-readable/index.html
    applications/
      index.html
      ai-documentation-continuity/index.html
      knowledge-system-continuity/index.html
      digital-infrastructure-continuity/index.html
      strategic-digital-asset-continuity/index.html
    reference-continuity-readiness/index.html
    strategic-operating-partnership/index.html
    operator-brief/index.html
    reference-cases/
      index.html
      bisulfid-reference-atlas-continuity/index.html
      euraplan-regulatory-reference-continuity/index.html
      aielectronicchips-dependency-reference-continuity/index.html
      outmerchant-standard-continuity/index.html
```

---

## Public surface layers

| Layer | Routes | Purpose |
|-------|--------|---------|
| Category standard | `/en/category-standard/` | Reference continuity governance declaration, scope, boundary |
| Core problem | `/ai-era-digital-continuity/` | Flagship explanation of the market problem the protocol addresses |
| Machine-readable | `/machine-readable/`, `/definitions.json`, `/protocol/v1/*.json` | Static, versioned, AI-consumable reference files |
| Applications | `/applications/` + 4 sub-pages | Controlled proof of protocol applicability across domains |
| Readiness | `/reference-continuity-readiness/` | Self-orientation guide for institutional readers |
| Operating partnership | `/strategic-operating-partnership/` | Controlled commercial-readiness surface |
| Operator brief | `/operator-brief/` | Concise governed brief for qualified enterprise operators |
| Reference cases | `/reference-cases/` + 4 case pages | Self-applied proof-of-application within Sohadot-governed assets |

---

## Build and authority

- **GitHub-first:** Changes enter through this repository; reviews and history apply here.
- **No parallel output roots:** Do not introduce `docs/`, `dist/`, `public/`, or duplicate site roots as substitute corpora. The governed layout above remains authoritative.
- **No dynamic backend:** The public surface is static-first. No MCP endpoint, certification engine, compliance registry, or readiness checklist is open.
- **JSON-LD constraint:** All pages use `WebPage` and `CreativeWork` schema types only — no Product, Offer, Service, Rating, Certification, or AggregateRating.

### Cloudflare Edge Security (later only)

**Cloudflare** is reserved as an optional **later edge security layer**. It is **not** the build system, **not** the source of truth, **not** configured in this repository at this stage.

---

## Development stage

This repository is in **active reference construction**. Nine sprints complete:

| Sprint | Deliverable |
|--------|-------------|
| 1 | Category standard declaration, 8 governed English pages |
| 2 | Static versioned machine-readable reference layer |
| 3 | Reference applications hub (4 application pages) |
| 4 | Reference continuity readiness entry point |
| 5 | Strategic operating partnership layer |
| 6 | Operator brief layer |
| 8 | Self-applied reference cases layer (4 case pages) |
| 9 | AI-era digital continuity flagship reference page |

Further expansion (additional locales, external partner program, dynamic API, MCP endpoint, certification system) remains **gated** until dossier and architecture criteria are met.

---

## Where to read next

| Document | Purpose |
|----------|---------|
| [`assets/evergreenprotocol-com/domain-dossier.md`](assets/evergreenprotocol-com/domain-dossier.md) | Strategic and narrative posture of the asset |
| [`assets/evergreenprotocol-com/architecture.md`](assets/evergreenprotocol-com/architecture.md) | Structural rules and public IA boundaries |
| [`assets/evergreenprotocol-com/DECISION_LOG.md`](assets/evergreenprotocol-com/DECISION_LOG.md) | Material decisions, rationale, and explicit non-decisions |

---

**Doctrine:** GitHub governs. The repository builds. The asset remains sovereign.
