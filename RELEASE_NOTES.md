# Release Notes — v1.0.0

> 🌐 Language / Ngôn ngữ: **English** | [Tiếng Việt](RELEASE_NOTES.vi.md)

## First public release

v1.0.0 packages the dual-T4 Qwen3-Embedding-8B runtime, bilingual Wikidata semantic search, reproducible Kaggle workflows, qualification tooling, and guided public Quick Demo.

### Highlights

- Qwen3-Embedding-8B loaded from attached Kaggle Model input.
- Two persistent T4 workers with bounded scheduling.
- FastAPI embedding/search endpoints.
- Verified English/Vietnamese Wikidata 100K corpus.
- English, Vietnamese and cross-lingual retrieval.
- Instruction-aware embeddings and flexible dimensions.
- Quick Demo, full 100K index rebuild, and deeper qualification notebooks.
- MIT-licensed project source, Apache-2.0 upstream Qwen model licensing, CC0 structured data licensing, and bilingual public documentation.

### Validation and reproducibility

The release includes runtime results, integrity checks, and reproducibility artifacts so users and reviewers can inspect how the project was validated. Documentation-only updates do not change the model runtime behavior.

### Licensing

- Project source code: MIT — see `LICENSE`.
- Upstream `Qwen/Qwen3-Embedding-8B` model: Apache License 2.0 — see `MODEL_LICENSE` and `MODEL_LICENSE.md`.
- Structured Wikidata-derived corpus: CC0 1.0 — see `dataset/LICENSE-DATA.md`.

Copyright (c) 2026 Đăng Khoa <i.am@dangkhoa.dev>.
