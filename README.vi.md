# Qwen3-Embedding-8B trên Kaggle GPU T4×2

> 🌐 Language / Ngôn ngữ: [English](README.md) | **Tiếng Việt**

[![CI](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU?display_name=tag&sort=semver)](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/releases/tag/v1.0.0)
[![Source License: MIT](https://img.shields.io/badge/Source%20License-MIT-yellow.svg)](LICENSE)
[![Model License: Apache 2.0](https://img.shields.io/badge/Model%20License-Apache%202.0-blue.svg)](MODEL_LICENSE.vi.md)
[![Python](https://img.shields.io/badge/Python-3.10--3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/Kaggle-T4%20%C3%972-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/)
[![Model](https://img.shields.io/badge/Qwen3--Embedding--8B-4096d-6C63FF)](https://huggingface.co/Qwen/Qwen3-Embedding-8B)

Một dự án **Qwen3-Embedding-8B** có khả năng tái lập và dễ review trên Kaggle **NVIDIA Tesla T4 ×2**. Dự án kết hợp embedding API, semantic search Anh/Việt, corpus Wikidata 100K đã xác minh, dual-GPU serving và các notebook giúp người dùng nhìn thấy rõ cách runtime hoạt động thay vì chỉ gọi vào một endpoint được host sẵn.

Nếu bạn chỉ muốn xem model hoạt động, hãy bắt đầu bằng **Quick Demo**. Nếu bạn muốn build lại toàn bộ index 100K hoặc xem sâu hơn các bước qualification/evidence, hãy dùng các notebook đầy đủ được mô tả bên dưới.

> **v1.0.0** là bản phát hành public ổn định đầu tiên dành cho cộng đồng sử dụng, review và kiểm tra khả năng tái lập.

## Vì sao dự án này tồn tại?

Nói “chạy một embedding model lớn trên Kaggle” thì đơn giản, nhưng để người khác có thể chạy lại một cách rõ ràng và đáng tin cậy lại khó hơn nhiều. Một project public hữu ích cần nhiều hơn một notebook chỉ chạy thành công một lần.

Repository này tập trung vào bốn mục tiêu thực tế:

- **Dễ thử model.** Quick Demo có hướng dẫn giúp tránh phải build lại toàn bộ corpus trong mỗi session.
- **Giữ phần quan trọng chạy live.** Query của người dùng được model encode tại runtime; retrieval và comparison không phải kết quả dựng sẵn.
- **Sử dụng cả hai T4 một cách có chủ đích.** Hai persistent worker là hai model replica độc lập phía sau bounded scheduler.
- **Để kết quả dễ kiểm tra.** Model/data identity, checksum, input validation, tests, qualification notebook và release artifact đều được mô tả rõ.

## Bạn có thể làm gì?

Với các public notebook và runtime của dự án, bạn có thể:

- tạo normalized Qwen3 embedding với nhiều kích thước khác nhau;
- tìm kiếm theo ý nghĩa trên corpus Wikidata **100.000 dòng Anh/Việt**;
- so sánh retrieval tiếng Anh, tiếng Việt và xuyên ngôn ngữ EN ↔ VI;
- so sánh instruction-aware query embedding với text embedding thông thường;
- tính semantic similarity giữa các đoạn text;
- phục vụ embedding/search request qua FastAPI;
- chạy concurrent requests trên hai persistent Tesla T4 worker;
- build lại toàn bộ corpus index từ source data;
- kiểm tra kết quả validation và release artifact thay vì chỉ dựa vào screenshot hoặc claim không có căn cứ.

## Tổng quan nhanh

| Hạng mục | Public v1.0.0 |
|---|---|
| Model | `Qwen/Qwen3-Embedding-8B` |
| Kaggle accelerator | NVIDIA Tesla T4 ×2 |
| Worker topology | Hai model replica persistent độc lập |
| Embedding size tối đa dùng trong project | 4096 chiều |
| Quick Demo corpus | 100.000 dòng Wikidata song ngữ |
| Ngôn ngữ demo | Tiếng Anh và tiếng Việt |
| Cross-lingual retrieval | EN ↔ VI |
| Query execution | Chạy live |
| Corpus vector của Quick Demo | Tính sẵn và kiểm tra integrity |
| Build lại full index | Build lại canonical index 100K |
| API | FastAPI embedding + semantic search |
| Exposure mặc định | Local-only |
| External demo tùy chọn | Cloudflare Quick Tunnel có authentication |

Dự án **không** tuyên bố hai GPU luôn nhanh chính xác gấp 2 lần một GPU. Dual-worker ở đây chủ yếu là topology phục vụ concurrency, không phải tensor sharding.

## Nên bắt đầu từ đâu?

Có ba điểm bắt đầu khác nhau. Hãy chọn theo mục tiêu của bạn.

### 1. Tôi chỉ muốn xem project chạy

Dùng:

`notebooks/kaggle-t4x2-quick-demo.ipynb`

Đây là trải nghiệm đầu tiên được khuyến nghị. Notebook được thiết kế để dễ hiểu nhưng vẫn giữ phần model/query/retrieval chạy thực.

### 2. Tôi muốn build lại index 100K từ đầu

Dùng:

`notebooks/kaggle-t4x2-production-demo.ipynb`

Đây là workflow build lại full index. Nó chạy lâu hơn nhiều vì tự build lại canonical corpus vector thay vì dùng verified prebuilt index của Quick Demo.

### 3. Tôi muốn xem workflow qualification sâu hơn

Dùng:

`kaggle/demo.ipynb`

Notebook này chạy các check sâu hơn về semantic, model capability, hardware, long-context, regression và evidence.

## Quick start trên Kaggle

### Yêu cầu Kaggle

Tạo một Kaggle Notebook mới và cấu hình:

- **Accelerator:** GPU T4 ×2
- **Internet:** ON trong bước source/bootstrap/cài package
- **Model input:** `dangkhoa2016/qwen-qwen3-embedding-8b`
- **Quick Demo dataset:** `dangkhoa2016/qwen3-embedding-8b-en-vi-100k-index`

Kaggle mount các input đã attach ở chế độ read-only dưới `/kaggle/input`. Dự án chủ động để mutable state dưới `/kaggle/working`.

### Chạy Quick Demo

Mở:

`notebooks/kaggle-t4x2-quick-demo.ipynb`

Sau đó chọn **Run All**.

Notebook sẽ kiểm tra environment, resolve local model/index đã attach, khởi động worker và đi lần lượt qua các khả năng chính theo một flow dễ theo dõi.

### Phần nào được tính sẵn và phần nào chạy live?

Đây là điểm quan trọng.

**Được tính sẵn:**

- embedding matrix của corpus 100K;
- 100.000 dòng Wikidata song ngữ đã căn hàng;
- model/data fingerprints và integrity metadata.

**Vẫn chạy live trong mỗi Quick Demo:**

- khởi động model;
- mọi query embedding của người dùng;
- semantic-search scoring;
- retrieval tiếng Anh/tiếng Việt;
- cross-lingual EN ↔ VI;
- instruction-aware query calls;
- semantic-similarity calculations;
- embedding calls với kích thước linh hoạt;
- dual-worker concurrency.

Như vậy Quick Demo bỏ đi bước full-corpus rebuild tốn thời gian nhưng không biến demo thành một bản replay tĩnh.

## Demo cho thấy những gì?

### Semantic search tiếng Anh

Query tiếng Anh được embed live rồi so sánh với verified corpus index.

### Semantic search tiếng Việt

Query tiếng Việt đi qua cùng một runtime path và cùng multilingual embedding model.

### Cross-lingual retrieval EN ↔ VI

Các concept tương đương hoặc liên quan có thể được query bằng một ngôn ngữ và retrieve entity song ngữ trong cùng semantic space.

### Instruction-aware retrieval

Qwen3 Embedding hỗ trợ query instruction. Demo thể hiện rõ sự khác nhau thay vì âm thầm áp dụng instruction phía sau.

### Semantic similarity

Các cặp text được embed và so sánh bằng normalized vectors.

### Flexible embedding dimensions

Public workflow minh họa một số kích thước nhỏ hơn bên cạnh representation đầy đủ 4096 chiều.

### Kết quả dễ đọc nhưng vẫn giữ identity

Bảng search giữ canonical **Wikidata QID** đồng thời hiển thị label tiếng Anh/tiếng Việt. Người dùng dễ đọc kết quả mà không làm mất stable entity identifier.

## Mô hình public serving

Repository được thiết kế để người dùng **clone/run trong Kaggle T4×2 session của chính mình**. Luồng mặc định giữ `EXPOSE_MODE=off`, vì vậy API chỉ tồn tại trong notebook runtime trừ khi người dùng chủ động bật exposure mode.

**Cloudflare Quick Tunnel chỉ là tùy chọn**. Khi được bật, nó chỉ nên được xem như một bề mặt demo tạm thời có authentication. Project **không phải permanently hosted public inference endpoint** và không dùng runtime riêng của maintainer như một public service dùng chung.

Ranh giới này là chủ đích của project: người review có thể tự tái lập workflow thay vì phụ thuộc vào endpoint do tác giả kiểm soát.

## Kiến trúc

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

Mỗi GPU worker sở hữu một model replica độc lập. Dự án **không** tensor-shard một model duy nhất qua hai T4.

Xem [Kiến trúc](docs/architecture.vi.md) để đọc runtime contract chi tiết.

## Local REST API

Service cung cấp một API nhỏ và rõ ràng:

| Method | Path | Mục đích |
|---|---|---|
| GET | `/health` | Process liveness |
| GET | `/ready` | Worker/index readiness |
| GET | `/metrics` | Scheduler và worker metrics |
| GET | `/info` | Runtime/model metadata |
| POST | `/v1/embeddings` | Tạo embedding |
| POST | `/v1/search` | Semantic search |

Ví dụ embedding request:

```json
{
  "model": "qwen3-embedding-8b-kaggle",
  "input": ["hello", "xin chào"],
  "dimensions": 1024,
  "is_query": true
}
```

Ví dụ search request:

```json
{
  "query": "nhà khoa học Marie Curie",
  "top_k": 5,
  "language": "vi"
}
```

Xem [REST API](docs/api.vi.md) để biết chi tiết.

## Kiểm tra đầy đủ

Quick Demo ngắn không thay thế các workflow validation sâu hơn.

Hãy chạy các notebook sau trong **các fresh Kaggle T4 ×2 session riêng biệt**:

| Notebook | Mục đích | Historical runtime |
|---|---|---:|
| `notebooks/kaggle-t4x2-production-demo.ipynb` | Build lại canonical index 100K và kiểm tra production lifecycle | khoảng một giờ |
| `kaggle/demo.ipynb` | Qualification semantic/model/hardware/long-context | khoảng 75 phút |

Không tái sử dụng mutable `/kaggle/working` state giữa hai full run này.

## Khả năng tái lập và kiểm tra

GitHub Release đi kèm runtime evidence, kiểm tra integrity và các artifact có thể tải về để reviewer xác minh. Runtime material lịch sử được tách riêng khỏi tài liệu hiện tại để người đọc hiểu rõ những gì đã được chạy mà không phụ thuộc vào các commit link cũ.

Đọc thêm về khả năng tái lập:

- [Qualification](docs/qualification.vi.md)
- [Khả năng tái lập](docs/reproducibility.vi.md)

## Cấu trúc project

```text
app/                 FastAPI service, inference workers, scheduler, search
benchmark/           Reproducible benchmark helpers
dataset/             Wikidata acquisition, normalization, packaging
docs/                Public English/Vietnamese documentation
fixtures/            Frozen semantic/retrieval fixtures
kaggle/              Bootstrap, validation, qualification workflow
notebooks/           Guided Quick Demo và production notebook
scripts/             Build, verify, package, qualification utilities
tests/               CPU-safe regression và contract tests
.github/             CI, release workflow, templates, community metadata
```

## Phát triển và kiểm tra

Các validation CPU-safe:

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

GPU/model qualification vẫn chạy trên Kaggle T4 ×2 vì CPU-only CI không thể tái hiện CUDA topology, VRAM behavior hoặc real model loading.

## Tài liệu

| Chủ đề | English | Tiếng Việt |
|---|---|---|
| Mục lục tài liệu | [Open](docs/index.md) | [Mở](docs/index.vi.md) |
| Kiến trúc | [Open](docs/architecture.md) | [Mở](docs/architecture.vi.md) |
| REST API | [Open](docs/api.md) | [Mở](docs/api.vi.md) |
| Kaggle runtime | [Open](docs/kaggle.md) | [Mở](docs/kaggle.vi.md) |
| Quick Demo | [Open](docs/quick-demo.md) | [Mở](docs/quick-demo.vi.md) |
| Qualification | [Open](docs/qualification.md) | [Mở](docs/qualification.vi.md) |
| Reproducibility | [Open](docs/reproducibility.md) | [Mở](docs/reproducibility.vi.md) |
| Development | [Open](docs/development.md) | [Mở](docs/development.vi.md) |
| Limitations | [Open](docs/limitations.md) | [Mở](docs/limitations.vi.md) |
| Troubleshooting | [Open](docs/troubleshooting.md) | [Mở](docs/troubleshooting.vi.md) |

## Model và dữ liệu

### Model

Upstream model:

`Qwen/Qwen3-Embedding-8B`

Kaggle model mirror dùng bởi public workflow:

`dangkhoa2016/qwen-qwen3-embedding-8b`

Project load model từ read-only Kaggle input đã attach thay vì phụ thuộc việc download model trực tiếp trong inference path thông thường.

### Quick Demo index

`dangkhoa2016/qwen3-embedding-8b-en-vi-100k-index`

Artifact bao gồm:

- 100.000 bản ghi Wikidata song ngữ đã căn hàng;
- 100.000 × 4096 normalized `float32` corpus vectors;
- model/dataset fingerprints;
- provenance metadata;
- SHA-256 integrity checksums.

### Canonical source corpus

`dangkhoa2016/wikidata-en-vi-semantic-search-100k`

Canonical corpus được build từ structured Wikidata fields và giữ QID để làm entity identity ổn định.

## Giấy phép

Repository này có **ba lớp license khác nhau**. Không nên nhầm lẫn chúng với nhau.

| Thành phần | License | Tài liệu |
|---|---|---|
| Mã nguồn do project này phát triển | MIT | [LICENSE](LICENSE) |
| Upstream model `Qwen/Qwen3-Embedding-8B` | Apache License 2.0 | [MODEL_LICENSE](MODEL_LICENSE), [ghi chú license model](MODEL_LICENSE.vi.md) |
| Structured corpus dẫn xuất từ Wikidata | CC0 1.0 | [dataset/LICENSE-DATA.vi.md](dataset/LICENSE-DATA.vi.md) |

MIT License của repository **không thay thế và không tái cấp phép** upstream Qwen model.

## Các giới hạn quan trọng

- Accelerator profile public được hỗ trợ là Kaggle Tesla T4 ×2.
- Thiết kế hai GPU dùng hai model replica độc lập, không phải tensor sharding.
- Corpus vector của Quick Demo được tính sẵn; query người dùng vẫn chạy live.
- Full rebuild 100K mất nhiều thời gian hơn Quick Demo đáng kể.
- Search quality phụ thuộc cả embedding model lẫn corpus coverage.
- Runtime có thể dao động giữa các Kaggle session.
- Cloudflare Quick Tunnel là tùy chọn tạm thời; project không phải permanently hosted inference service.

Xem [Giới hạn](docs/limitations.vi.md) để biết chi tiết.

## Cộng đồng và hỗ trợ

- Dùng GitHub Issues cho bug có thể tái lập và feature request.
- Khi báo runtime bug, hãy ghi exact Git SHA và accelerator Kaggle.
- Không đăng token, API key, private URL hoặc credential lên issue.
- Vấn đề nhạy cảm về bảo mật làm theo [.github/SECURITY.vi.md](.github/SECURITY.vi.md).
- Contribution nên theo [.github/CONTRIBUTING.vi.md](.github/CONTRIBUTING.vi.md).

## Lời cảm ơn

Dự án được xây dựng dựa trên:

- **Qwen / Alibaba Cloud** cho Qwen3-Embedding-8B;
- **Wikidata / Wikimedia** cho nguồn structured corpus song ngữ;
- **Kaggle** cho môi trường notebook T4 ×2 public;
- hệ sinh thái mã nguồn mở Python, PyTorch, Transformers, FastAPI, NumPy và các thư viện liên quan.

## Tác giả

**Đăng Khoa**  
<i.am@dangkhoa.dev>

## Bản phát hành

Bản public hiện tại: [v1.0.0](https://github.com/dangkhoa2016/Qwen3-Embedding-8B-On-T4x2-GPU/releases/tag/v1.0.0)

Release artifact, checksum, runtime evidence và các bản ghi verification được công bố trên GitHub Release page.
