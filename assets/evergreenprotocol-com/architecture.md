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
|------|---------|
| `site/en/index.html` | Home — category standard declaration, AI-era continuity thesis, layer overview. |
| `site/en/category-standard/index.html` | Category Standard v1.0 — reference continuity governance declaration, scope, and boundary. |
| `site/en/ai-era-digital-continuity/index.html` | AI-Era Digital Continuity — market context, reference decay problem, governance gap. |
| `site/en/manifesto/index.html` | Philosophical obligation and propositions (Anti-Entropy Protocol layer). |
| `site/en/methodology/index.html` | Operational template (Architecture of Constancy in practice). |
| `site/en/definitions/index.html` | Controlled vocabulary — category terms and core terms, versioned. |
| `site/en/cite/index.html` | Citation guidance — plain text, APA, Chicago, BibTeX, and AI-system formats. |
| `site/en/changelog/index.html` | Version governance — self-applied change record, review cadence, and governance rules. |

Further applications (Reference Application Registry, Evergreen Readiness Checklist), machine-readable API layer (`/definitions.json`, `/protocol/v1/standard.json`), and additional locales are excluded until gated.

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
