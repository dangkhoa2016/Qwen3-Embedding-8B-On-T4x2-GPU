# Qwen3-Embedding-8B on Kaggle GPU T4×2

> 🌐 Language / Ngôn ngữ: **English** | [Tiếng Việt](README.vi.md)

[![CI](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU?display_name=tag&sort=semver)](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/releases/tag/v1.0.0)
[![Source License: MIT](https://img.shields.io/badge/Source%20License-MIT-yellow.svg)](LICENSE)
[![Model License: Apache 2.0](https://img.shields.io/badge/Model%20License-Apache%202.0-blue.svg)](MODEL_LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.10--3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-T4%20%C3%972-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/)
[![Model](https://img.shields.io/badge/Qwen3--Embedding--8B-4096d-6C63FF)](https://huggingface.co/Qwen/Qwen3-Embedding-8B)

A reproducible, reviewable **Qwen3-Embedding-8B** project for Kaggle **NVIDIA Tesla T4 ×2**. It combines a practical embedding API, English/Vietnamese semantic search, a verified 100K Wikidata corpus, dual-GPU serving, and notebooks that make the runtime easy to inspect instead of hiding the interesting parts behind a hosted endpoint.

If you only want to see the model working, start with the **Quick Demo**. If you want to reproduce the full 100K build or inspect the qualification evidence, use the deeper notebooks documented below.

> **v1.0.0** is the first public stable release intended for community use, review, and reproducibility testing.

## Why this project exists

Running a large embedding model on Kaggle is easy to describe but surprisingly easy to make difficult to reproduce. A useful public project needs more than a notebook that happens to work once.

This repository focuses on four practical goals:

- **Make the model easy to try.** A guided Quick Demo avoids rebuilding the entire corpus every session.
- **Keep the interesting work live.** User queries are embedded at runtime; retrieval and comparison are not precomputed.
- **Use both T4 GPUs deliberately.** Two persistent workers are used as independent model replicas behind a bounded scheduler.
- **Make results easy to verify.** Model/data identity, checksums, input validation, tests, qualification notebooks, and release artifacts are documented explicitly.

## What you can do

With the public notebooks and runtime you can:

- generate normalized Qwen3 embeddings at flexible dimensions;
- search a verified **100,000-row English/Vietnamese Wikidata corpus** by meaning;
- compare English, Vietnamese, and EN ↔ VI cross-lingual retrieval;
- compare instruction-aware query embeddings with ordinary text embeddings;
- calculate semantic similarity between texts;
- serve embedding and search requests through FastAPI;
- exercise two persistent Tesla T4 workers concurrently;
- rebuild the full corpus index from source data;
- inspect validation results and release artifacts instead of relying only on screenshots or undocumented claims.

## Results at a glance

| Area | Public v1.0.0 profile |
|---|---|
| Model | `Qwen/Qwen3-Embedding-8B` |
| Kaggle accelerator | NVIDIA Tesla T4 ×2 |
| Worker topology | Two independent persistent model replicas |
| Maximum embedding size used by the project | 4096 dimensions |
| Quick Demo corpus | 100,000 bilingual Wikidata rows |
| Languages demonstrated | English and Vietnamese |
| Cross-lingual retrieval | EN ↔ VI |
| Query execution | Live |
| Quick Demo corpus vectors | Precomputed and integrity-checked |
| Full index rebuild | Rebuilds the canonical 100K index |
| API | FastAPI embedding + semantic search |
| Default exposure | Local-only |
| Optional external demo | Authenticated Cloudflare Quick Tunnel |

The project does **not** claim that two GPUs always deliver exactly 2× the speed of one GPU. The dual-worker design is primarily a serving/concurrency topology, not tensor sharding.

## Start here

There are three useful entry points. Choose the one that matches what you want to learn.

### 1. I just want to see the project working

Use:

`notebooks/kaggle-t4x2-quick-demo.ipynb`

This is the recommended first experience. It is designed to be understandable while still showing live model behavior.

### 2. I want to rebuild the 100K index from scratch

Use:

`notebooks/kaggle-t4x2-production-demo.ipynb`

This is the full index rebuild workflow. It takes much longer because it recreates the canonical corpus vectors instead of using the verified prebuilt Quick Demo index.

### 3. I want the deeper model/hardware qualification workflow

Use:

`kaggle/demo.ipynb`

This notebook exercises semantic, model-capability, hardware, long-context, regression, and evidence checks.

## Quick start on Kaggle

### Kaggle requirements

Create a fresh Kaggle Notebook and configure:

- **Accelerator:** GPU T4 ×2
- **Internet:** ON during source/bootstrap/package installation
- **Model input:** `dangkhoa2016/qwen-qwen3-embedding-8b`
- **Quick Demo dataset:** `dangkhoa2016/qwen3-embedding-8b-en-vi-100k-index`

Kaggle mounts attached inputs read-only under `/kaggle/input`. The project intentionally keeps mutable state below `/kaggle/working`.

### Run the Quick Demo

Open:

`notebooks/kaggle-t4x2-quick-demo.ipynb`

Then use **Run All**.

The notebook verifies the expected environment, resolves the attached local model and index, starts the workers, and walks through the main capabilities in a predictable order.

### What is precomputed and what is live?

The distinction matters.

**Precomputed:**

- the 100K corpus embedding matrix;
- the aligned bilingual Wikidata rows;
- model/data fingerprints and integrity metadata.

**Still live during every Quick Demo run:**

- model startup;
- every user query embedding;
- semantic-search scoring;
- English/Vietnamese retrieval;
- EN ↔ VI cross-lingual retrieval;
- instruction-aware query calls;
- semantic-similarity calculations;
- flexible-dimension embedding calls;
- dual-worker concurrency.

So the Quick Demo removes the slow full-corpus rebuild without turning the demonstration into a static replay.

## What the demo shows

### English semantic search

An English query is embedded live and compared with the verified corpus index.

### Vietnamese semantic search

A Vietnamese query follows the same path using the same multilingual embedding model.

### Cross-lingual EN ↔ VI retrieval

Equivalent or related concepts can be queried in one language while retrieving bilingual entities from the shared semantic space.

### Instruction-aware retrieval

Qwen3 Embedding supports query instructions. The demo makes the distinction visible rather than silently applying an instruction behind the scenes.

### Semantic similarity

Pairs of texts are embedded and compared using normalized vectors.

### Flexible embedding dimensions

The public workflow demonstrates selected smaller dimensions in addition to the full 4096-dimensional representation.

### Human-readable search results

Search tables retain the canonical **Wikidata QID** while also displaying English/Vietnamese labels. This keeps results friendly to read without throwing away the stable entity identifier.

## Public serving model

This repository is designed to **clone/run in your own Kaggle T4×2 session**. The normal path keeps `EXPOSE_MODE=off`, so the API remains local to the notebook runtime unless you deliberately opt into an exposure mode.

**Cloudflare Quick Tunnel is optional**. When enabled, it is intended only as a temporary authenticated demonstration surface. This project is **not a permanently hosted public inference endpoint** and does not present the maintainer's own runtime as a shared public service.

This distinction is intentional: the repository is meant to be reproducible by the person reviewing it, not dependent on an endpoint controlled by the project author.

## Architecture

```text
Kaggle Model + Dataset inputs
          │
          ├── Qwen3-Embedding-8B
          └── canonical dataset / verified Quick Demo index
          │
          ▼
offline-first local resolver
          │
          ▼
FastAPI gateway
          │
          ▼
bounded scheduler
      ┌───┴───┐
      ▼       ▼
 T4 worker 0  T4 worker 1
      │       │
      └───┬───┘
          ▼
normalized embeddings
          │
          ▼
semantic search / API response
```

Each GPU worker owns an independent model replica. The project does **not** tensor-shard a single model across both T4s.

See [Architecture](docs/architecture.md) for the detailed runtime contract.

## Local REST API

The service exposes a compact API:

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Process liveness |
| GET | `/ready` | Worker/index readiness |
| GET | `/metrics` | Scheduler and worker metrics |
| GET | `/info` | Runtime/model metadata |
| POST | `/v1/embeddings` | Generate embeddings |
| POST | `/v1/search` | Semantic search |

Example embedding request:

```json
{
  "model": "qwen3-embedding-8b-kaggle",
  "input": ["hello", "xin chào"],
  "dimensions": 1024,
  "is_query": true
}
```

Example search request:

```json
{
  "query": "nhà khoa học Marie Curie",
  "top_k": 5,
  "language": "vi"
}
```

See [REST API](docs/api.md) for details.

## Full verification

The short Quick Demo is not a replacement for the deeper validation workflows.

Run these in **separate fresh Kaggle T4 ×2 sessions**:

| Notebook | Purpose | Historical runtime profile |
|---|---|---:|
| `notebooks/kaggle-t4x2-production-demo.ipynb` | Rebuild canonical 100K index and validate production lifecycle | roughly one hour |
| `kaggle/demo.ipynb` | Semantic/model/hardware/long-context qualification | roughly 75 minutes |

Do not reuse mutable `/kaggle/working` state between these two full runs.

## Reproducibility and verification

The GitHub Release includes runtime evidence, integrity checks, and downloadable verification artifacts. Historical runtime material is labeled separately from the current documentation so reviewers can understand what was executed without relying on stale commit links.

For deeper reproducibility details, read:

- [Qualification](docs/qualification.md)
- [Reproducibility](docs/reproducibility.md)

## Project layout

```text
app/                 FastAPI service, inference workers, scheduler, search
benchmark/           Reproducible benchmark helpers
dataset/             Wikidata acquisition, normalization, packaging
docs/                Public English/Vietnamese documentation
fixtures/            Frozen semantic/retrieval fixtures
kaggle/              Bootstrap, validation, qualification workflow
notebooks/           Guided Quick Demo and production notebook
scripts/             Build, verify, package, qualification utilities
tests/               CPU-safe regression and contract tests
.github/             CI, release workflow, templates, community metadata
```

## Development and validation

CPU-safe validation:

```bash
python -m pip install -r requirements-test.txt
python -m pytest -q
python scripts/check_bilingual_docs.py
python scripts/check_doc_links.py
python scripts/check_publication_policy.py
python -m compileall -q app dataset benchmark scripts
bash -n kaggle/*.sh scripts/*.sh
git diff --check
```

GPU/model qualification remains on Kaggle T4 ×2 because CPU-only CI cannot reproduce CUDA topology, VRAM behavior, or real model loading.

## Documentation

| Topic | English | Tiếng Việt |
|---|---|---|
| Documentation index | [Open](docs/index.md) | [Mở](docs/index.vi.md) |
| Architecture | [Open](docs/architecture.md) | [Mở](docs/architecture.vi.md) |
| REST API | [Open](docs/api.md) | [Mở](docs/api.vi.md) |
| Kaggle runtime | [Open](docs/kaggle.md) | [Mở](docs/kaggle.vi.md) |
| Quick Demo | [Open](docs/quick-demo.md) | [Mở](docs/quick-demo.vi.md) |
| Qualification | [Open](docs/qualification.md) | [Mở](docs/qualification.vi.md) |
| Reproducibility | [Open](docs/reproducibility.md) | [Mở](docs/reproducibility.vi.md) |
| Development | [Open](docs/development.md) | [Mở](docs/development.vi.md) |
| Limitations | [Open](docs/limitations.md) | [Mở](docs/limitations.vi.md) |
| Troubleshooting | [Open](docs/troubleshooting.md) | [Mở](docs/troubleshooting.vi.md) |

## Model and data

### Model

Upstream model:

`Qwen/Qwen3-Embedding-8B`

Kaggle model mirror used by the public workflow:

`dangkhoa2016/qwen-qwen3-embedding-8b`

The project loads model files from the attached read-only Kaggle input instead of depending on a live model download during normal inference.

### Quick Demo index

`dangkhoa2016/qwen3-embedding-8b-en-vi-100k-index`

The artifact contains:

- 100,000 aligned bilingual Wikidata records;
- 100,000 × 4096 normalized `float32` corpus vectors;
- model/dataset fingerprints;
- provenance metadata;
- SHA-256 integrity checksums.

### Canonical source corpus

`dangkhoa2016/wikidata-en-vi-semantic-search-100k`

The canonical corpus is built from structured Wikidata fields and retains QIDs for entity identity.

## License

This repository uses **three different licensing layers**. They should not be confused.

| Component | License | Where to read it |
|---|---|---|
| Repository source code written for this project | MIT | [LICENSE](LICENSE) |
| Upstream `Qwen/Qwen3-Embedding-8B` model | Apache License 2.0 | [MODEL_LICENSE](MODEL_LICENSE), [model license notes](MODEL_LICENSE.md) |
| Structured Wikidata-derived corpus | CC0 1.0 | [dataset/LICENSE-DATA.md](dataset/LICENSE-DATA.md) |

The repository's MIT license does **not** replace or relicense the upstream Qwen model.

## Important limitations

- The supported public accelerator profile is Kaggle Tesla T4 ×2.
- The two-GPU design uses independent model replicas, not tensor sharding.
- Quick Demo corpus vectors are precomputed; user queries remain live.
- A full 100K rebuild takes substantially longer than the Quick Demo.
- Search quality depends on both the embedding model and corpus coverage.
- Runtime timings vary between Kaggle sessions.
- Cloudflare Quick Tunnel is optional and temporary; this project is not a permanently hosted inference service.

See [Limitations](docs/limitations.md) for the detailed list.

## Community and support

- Use GitHub Issues for reproducible bugs and feature requests.
- Include the exact Git SHA and Kaggle accelerator in runtime bug reports.
- Never post tokens, API keys, private URLs, or credentials in issues.
- Security-sensitive reports should follow [.github/SECURITY.md](.github/SECURITY.md).
- Contributions should follow [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Acknowledgements

This project builds on:

- **Qwen / Alibaba Cloud** for Qwen3-Embedding-8B;
- **Wikidata / Wikimedia** for the structured bilingual corpus source;
- **Kaggle** for the public T4 ×2 notebook environment;
- the Python, PyTorch, Transformers, FastAPI, NumPy, and broader open-source ecosystems used by the runtime.

## Author

**Đăng Khoa**  
<i.am@dangkhoa.dev>

## Release

Current public release: [v1.0.0](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/releases/tag/v1.0.0)

For release artifacts, checksums, runtime evidence, and verification records, see the GitHub Release page.
