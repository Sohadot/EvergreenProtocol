# Sovereign asset architecture — evergreenprotocol.com

## Repository boundary

This directory (`assets/evergreenprotocol-com/`) is the governed corpus for the digital asset **evergreenprotocol.com** within the Sovereign Asset System. It is the single canonical tree for dossier, formal architecture, and the reference-grade public site sources.

## Artifact classes

| Artifact | Role |
|----------|------|
| `domain-dossier.md` | Canonical operating dossier: identity, thesis, narrative hierarchy, authority logic, economic order, gates, and posture. |
| `architecture.md` | Formal map of how the repository is structured, what may live where, and how public layers map to the three conceptual layers. |
| `site/` | Publishable reference surface: static HTML and shared presentation assets only under this subtree. |

No parallel roots (`docs/`, `dist/`, `public/`, or duplicate site roots) are permitted in this architecture.

## Public surface (`site/`)

- **Shared stylesheet:** `site/assets/css/main.css` — all page styling; HTML must not carry presentation in `<style>` or inline `style` attributes.
- **Locale:** English pages live under `site/en/` only. Additional locales are out of scope until explicitly approved.

### Information architecture (current)

| Path | Purpose |
|------|--------|
| `site/en/index.html` | Home — category standard declaration, AI-era continuity thesis, layer overview. |
| `site/en/category-standard/index.html` | Category Standard v1.0 — reference continuity governance declaration, scope, and boundary. |
| `site/en/ai-era-digital-continuity/index.html` | AI-Era Digital Continuity — market context, reference decay problem, governance gap. |
| `site/en/manifesto/index.html` | Philosophical obligation and propositions (Anti-Entropy Protocol layer). |
| `site/en/methodology/index.html` | Operational template (Architecture of Constancy in practice). |
| `site/en/definitions/index.html` | Controlled vocabulary — category terms and core terms, versioned. |
| `site/en/cite/index.html` | Citation guidance — plain text, APA, Chicago, BibTeX, and AI-system formats. |
| `site/en/changelog/index.html` | Version governance — self-applied change record, review cadence, and governance rules. |
| `site/machine-readable/index.html` | Machine-readable reference index — human-readable explanation of static JSON files, citation use, and exclusions. |
| `site/applications/index.html` | Reference applications hub — controlled public application layer. |
| `site/applications/*/index.html` | Application pages for AI documentation, knowledge systems, digital infrastructure, and strategic digital assets. |
| `site/reference-continuity-readiness/index.html` | Practical readiness entry point — self-orientation guide for institutional readers. |
| `site/strategic-operating-partnership/index.html` | Controlled commercial-readiness surface for qualified operating, licensing, and post-traction acquisition discussions. |
| `site/operator-brief/index.html` | Operator Brief — commercial-readiness narrative layer for qualified enterprise operators; not a pricing, partner application, certification, or acquisition page. |
| `site/reference-cases/index.html` | Self-Applied Reference Cases hub — proof-of-application layer showing protocol use within Sohadot-governed assets; not a registry, compliance surface, certification, or external assessment. |
| `site/reference-cases/bisulfid-reference-atlas-continuity/index.html` | Bisulfid — self-applied reference case; reference atlas continuity. |
| `site/reference-cases/euraplan-regulatory-reference-continuity/index.html` | EuraPlan — self-applied reference case; regulatory reference continuity (multi-country). |
| `site/reference-cases/aielectronicchips-dependency-reference-continuity/index.html` | AIElectronicChips — self-applied reference case; dependency reference continuity (compute/chip). |
| `site/reference-cases/outmerchant-standard-continuity/index.html` | Outmerchant — self-applied reference case; standard and diagnostic continuity (commerce evaluation). |
| `site/definitions.json` | Public canonical definitions index for governed terms. |
| `site/protocol/v1/definitions.json` | Version-pinned definitions for Evergreen Protocol v1.0. |
| `site/protocol/v1/standard.json` | Version-pinned machine-readable summary of Evergreen Protocol Standard v1.0. |
| `site/protocol/v1/citation.json` | Version-pinned machine-readable citation formats for Evergreen Protocol v1.0. |

Localized English JSON mirrors may exist under `site/en/` for continuity with existing English pages, but root static JSON paths are the canonical machine-readable references.

Further registry behavior, readiness checklist, dynamic API surfaces, MCP-compatible endpoints, public partner program behavior, external submission systems, and additional locales are excluded until gated.

### Machine-readable layer

The machine-readable layer is static-first:

- `/definitions.json` is the public canonical definitions index.
- `/protocol/v1/definitions.json` is stable and citable for Evergreen Protocol v1.0.
- `/protocol/v1/standard.json` summarizes the v1.0 standard as machine-readable reference data.
- `/protocol/v1/citation.json` provides machine-readable citation formats.
- `/machine-readable/` explains the available files, citation use, and explicit exclusions.

Files under `/protocol/v1/` must not be silently overwritten after publication. Future versions must publish at new versioned paths such as `/protocol/v1.1/` or `/protocol/v2/`.

The MCP-compatible layer remains future-gated. No MCP endpoint, dynamic backend, calculation engine, compliance registry, readiness checklist, or certification system is opened by this architecture.

### Reference application layer

The application layer is a public reference layer, not an assessment surface:

- `/applications/` is the controlled hub.
- `/applications/ai-documentation-continuity/` applies the standard to AI documentation and evidence traces.
- `/applications/knowledge-system-continuity/` applies the standard to institutional knowledge systems.
- `/applications/digital-infrastructure-continuity/` applies the standard to infrastructure documentation and dependency references.
- `/applications/strategic-digital-asset-continuity/` applies the standard to strategic digital assets and reference-grade public properties.

Reference applications demonstrate protocol applicability without opening a registry, checklist, tool, calculated-output workflow, third-party evaluation workflow, certification system, dynamic backend, or external submission path.

### Self-applied reference cases layer

The self-applied reference cases layer is a proof-of-application surface, not a certification or assessment surface:

- `/reference-cases/` is the controlled hub.
- `/reference-cases/bisulfid-reference-atlas-continuity/` demonstrates reference atlas continuity principles within a Sohadot-governed asset.
- `/reference-cases/euraplan-regulatory-reference-continuity/` demonstrates regulatory reference continuity (multi-country) within a Sohadot-governed asset.
- `/reference-cases/aielectronicchips-dependency-reference-continuity/` demonstrates dependency reference continuity (compute/chip) within a Sohadot-governed asset.
- `/reference-cases/outmerchant-standard-continuity/` demonstrates standard and diagnostic continuity (commerce evaluation) within a Sohadot-governed asset.

Self-applied reference cases demonstrate protocol use within the Sohadot portfolio. They do not certify assets, rank systems, approve third parties, or create compliance status. No external party is assessed, registered, or validated.

## Conceptual layers (narrative hierarchy)

The dossier's hierarchy governs content and future expansion:

1. **Structural — Architecture of Constancy:** Formal shape (charter, roles, artifacts, acceptance, versioning). Primary operational anchor for methodology and site structure.
2. **Philosophical — Anti-Entropy Protocol:** Necessity of explicit protocols against unnecessary drift.
3. **Symbolic — Zero-Season Algorithm:** Review and validity tied to dependency and risk, not arbitrary seasonal hype.

The structural layer defines what may be built; the philosophical layer justifies it; the symbolic layer elevates without replacing formal clarity.

## Change discipline

- **Major:** New artifact classes, IA shifts, or obligations that alter what this architecture permits.
- **Minor:** Clarifications or subdivisions that do not change permitted roots or gates.
- **Patch:** Typographical or navigational fixes.

Updates to `domain-dossier.md` that imply build changes should be reflected here when they affect repository shape or gates.

## Hosting note

This tree defines source layout and governance only. Publication mechanics are **GitHub-first** and live outside this subdirectory specification.

The repository remains the canonical source of truth for architecture, content, templates, scripts, validation, and deployment logic.

### Cloudflare Edge Security (later only)

**Cloudflare** is treated only as a potential **later edge security layer**. It is **not** part of the build, **not** active here, **not** configured in this repository, and must **not** substitute GitHub as authority over architecture or content.
