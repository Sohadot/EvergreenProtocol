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
| `site/en/index.html` | Home — governed continuity thesis and layer overview. |
| `site/en/manifesto/index.html` | Philosophical obligation and propositions. |
| `site/en/methodology/index.html` | Operational template (Architecture of Constancy in practice). |
| `site/en/definitions/index.html` | Controlled vocabulary for the reference. |

Applications, insights, tools, and further locales are excluded until gated.

## Conceptual layers (narrative hierarchy)

The dossier’s hierarchy governs content and future expansion:

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

**Authority:** The repository remains the canonical source of truth for architecture, content, templates, scripts, validation, and deployment logic.

**Edge delivery:** Optional future edge security (for example DNS, TLS, and edge protection via a provider such as Cloudflare) is **not** active in this development stage, is **not** configured here, and **does not** participate in build or content authority. When adopted, it serves delivery and protection only; it must not hold unpublished truth or substitute for GitHub. See the repository root **`README.md`** for the institutional formulation.

Cloudflare is **not** part of the build process at present; no API automation applies.
