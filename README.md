# Evergreen Protocol

Governed digital asset for **evergreenprotocol.com**: sovereign-grade reference architecture, dossier, and English methodology surface under `assets/evergreenprotocol-com/`.

## System architecture

### Governance layer

GitHub is the canonical source of truth for asset architecture, content, templates, and validation logic. The repository defines what may exist and how it is structured; the governed corpus is anchored in `assets/evergreenprotocol-com/` (see `architecture.md` and `domain-dossier.md`).

### Deployment logic

Build and deploy are **GitHub-first**: validation, assembly, and publication originate from the repository (for example via GitHub Actions). No parallel authority path may supersede the repo.

### Cloudflare Edge Security Layer

Cloudflare is treated only as an additional edge security layer.

It is not the source of truth.

It is not the build system.

It is not the content management layer.

It is not the primary deployment workflow.

GitHub remains the canonical source of truth for all asset architecture, content, templates, scripts, validation, and deployment logic.

Cloudflare may support:

- DNS control
- nameserver delegation
- TLS / HTTPS
- basic security posture
- redirects when needed
- caching where appropriate
- edge protection

This system does not use Cloudflare API automation.

AI agents may assist with Cloudflare only through dashboard-guided operation, under owner supervision, and without requesting or storing credentials.

Cloudflare must never introduce hidden operational state, unmanaged deployment paths, or content changes outside GitHub.

Cloudflare exists to protect and serve the governed asset.

It must not govern the asset.

---

**Doctrine:** Cloudflare protects. GitHub governs. The repository builds. The asset remains sovereign.
