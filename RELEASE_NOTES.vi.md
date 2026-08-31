# Ghi chú phát hành — v1.0.0

> 🌐 Language / Ngôn ngữ: [English](RELEASE_NOTES.md) | **Tiếng Việt**

## Bản phát hành public đầu tiên

v1.0.0 đóng gói runtime Qwen3-Embedding-8B dual-T4, semantic search Wikidata song ngữ, workflow Kaggle có khả năng tái lập, qualification tooling và Quick Demo public có hướng dẫn.

### Điểm nổi bật

- Qwen3-Embedding-8B load từ Kaggle Model input đã attach.
- Hai T4 worker persistent với bounded scheduler.
- FastAPI endpoint cho embedding/search.
- Corpus Wikidata 100K Anh/Việt đã xác minh.
- Retrieval tiếng Anh, tiếng Việt và xuyên ngôn ngữ.
- Instruction-aware embedding và flexible dimensions.
- Quick Demo, notebook build lại full index 100K và qualification chuyên sâu.
- Mã nguồn project dùng MIT, upstream Qwen model dùng Apache-2.0, structured data dùng CC0 và tài liệu public được duy trì song ngữ.

### Validation và khả năng tái lập

Bản phát hành đi kèm kết quả runtime, kiểm tra integrity và các artifact phục vụ khả năng tái lập để người dùng và reviewer có thể kiểm tra cách dự án được xác minh. Các thay đổi chỉ liên quan tài liệu không làm thay đổi hành vi runtime của model.

### Giấy phép

- Mã nguồn do project phát triển: MIT — xem `LICENSE`.
- Upstream model `Qwen/Qwen3-Embedding-8B`: Apache License 2.0 — xem `MODEL_LICENSE` và `MODEL_LICENSE.vi.md`.
- Structured corpus dẫn xuất từ Wikidata: CC0 1.0 — xem `dataset/LICENSE-DATA.vi.md`.

Copyright (c) 2026 Đăng Khoa <i.am@dangkhoa.dev>.
