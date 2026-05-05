# Project status — Evergreen Protocol

Last aligned branch: **main**  
Document role: **repository-facing status** (not the public site).

---

## Current phase

**Phase A — Governed reference core (in progress / stabilizing)**

The Sovereign Asset System dossier, formal architecture, and English methodology surface exist as the canonical corpus under `assets/evergreenprotocol-com/`. Work emphasizes clarity, structural discipline, and GitHub-first governance—not expansion of page count.

---

## Completed (baseline)

- Canonical asset root fixed under `assets/evergreenprotocol-com/`.
- `domain-dossier.md` and `architecture.md` govern identity, gates, and layout.
- English reference pages: home, manifesto, methodology, definitions; shared stylesheet under `site/assets/css/`.
- Repository README documents source-of-truth posture and structural rules.

---

## Active priorities

- Harden repository presentation and documentation for institutional readability.
- Maintain alignment between dossier, architecture, and public copy.
- Prepare for GitHub Actions–style validation and deploy **from this repo only** (pipelines to be added when scoped).

---

## Gated (not started here without explicit gate passage)

| Item | Gate |
|------|------|
| Additional site sections (applications, insights, tools) | Dossier build gates + architecture update |
| Further locales | Architecture approval + IA amendment |
| Monetization surfaces | Revenue compatibility gate in dossier |
| Cloudflare or other edge configuration | Post–stable build; dashboard-only; never source of truth |

---

## Explicit non-goals (current)

- No parallel documentation or site roots (`docs/`, `dist/`, `public/` as substitute corpora).
- No Cloudflare API usage or token handling in this repository.
- No positioning of external edge services as build systems or content authorities.

---

## Change control

Material moves in phase or scope should update this file together with `architecture.md` when repository obligations shift.
