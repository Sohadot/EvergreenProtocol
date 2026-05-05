# Evergreen Protocol

**Evergreen Protocol** is the governed intellectual and editorial frame behind **evergreenprotocol.com**: a **sovereign-grade reference asset** developed as a public methodology surface—not a product narrative, traffic asset, or informal content stack.

The asset is **governed by the Sovereign Asset System**: strategic posture, narrative hierarchy, authority discipline, and economic order are recorded in the dossier and formal architecture below. **GitHub is the sole source of truth** for what this asset is, how it is structured, and what may ship under its name.

---

## Conceptual core

Continuity for decisions, systems, and digital surfaces is treated as an **operational** property. The reference expresses that stance through three ordered layers:

| Layer | Name | Role |
|-------|------|------|
| Structural | **Architecture of Constancy** | Formal shape: charter, roles, artifacts, acceptance criteria, versioning—what can be built and audited. |
| Philosophical | **Anti-Entropy Protocol** | Necessity: unnecessary drift (tacit exceptions, definition fork, surface decay) made visible and reviewed. |
| Symbolic | **Zero-Season Algorithm** | Review timing tied to **validity and dependency change**, not arbitrary seasonal urgency or spectacle. |

Further narrative and strategic depth live in `domain-dossier.md`. Structural rules for this repository live in `architecture.md`.

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
  architecture.md       # Formal repo/site structure and layer mapping
  domain-dossier.md     # Sovereign Asset System dossier (identity, thesis, gates)
  site/
    assets/css/main.css # Shared presentation for the English reference surface
    en/
      index.html
      manifesto/index.html
      methodology/index.html
      definitions/index.html
```

**English-only** reference pages are intentional for this phase. Additional locales, applications, insights, and tooling are **gated** until they meet dossier and architecture criteria.

---

## Build and authority

- **GitHub-first:** Changes enter through this repository; reviews and history apply here.
- **No parallel output roots:** Do not introduce `docs/`, `dist/`, `public/`, or duplicate site roots as substitute corpora. The governed layout above remains authoritative.
- **Edge security (later):** A **Cloudflare-class edge security layer** may support DNS, TLS, and edge protection **after** publication pipelines are stable. It is **not** part of the build today, **not** configured in this repository, and **must not** hold source-of-truth content or replace GitHub-governed workflows. No Cloudflare API automation is used here.

---

## Development stage

This repository is in **active reference construction**: the methodology core (home, manifesto, methodology, definitions) and governed documentation are in place; broader expansion remains gated. See **`PROJECT_STATUS.md`** for the explicit phase line and immediate priorities.

---

## Where to read next

| Document | Purpose |
|----------|---------|
| [`assets/evergreenprotocol-com/domain-dossier.md`](assets/evergreenprotocol-com/domain-dossier.md) | Strategic and narrative posture of the asset |
| [`assets/evergreenprotocol-com/architecture.md`](assets/evergreenprotocol-com/architecture.md) | Structural rules and public IA boundaries |

---

**Doctrine:** GitHub governs. The repository builds. The asset remains sovereign. Edge platforms—when adopted—protect delivery; they do not define the asset.
