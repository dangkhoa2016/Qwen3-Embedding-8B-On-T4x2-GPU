# Runtime Kaggle T4×2

> 🌐 Language / Ngôn ngữ: [English](kaggle.md) | **Tiếng Việt**

## Session bắt buộc

- Accelerator: **NVIDIA Tesla T4 ×2**
- Internet: bật trong bước bootstrap/cài package
- Model input: `dangkhoa2016/qwen-qwen3-embedding-8b`

Quick Demo cần thêm:

- Dataset: `dangkhoa2016/qwen3-embedding-8b-en-vi-100k-index`

Full production/qualification dùng canonical dataset:

- `dangkhoa2016/wikidata-en-vi-semantic-search-100k`

## Contract của input

Dùng **Add Input** của Kaggle. Không copy hoặc sửa artifact đã attach dưới `/kaggle/input`.

Quá trình setup sẽ dừng với thông báo lỗi rõ ràng nếu model/data artifact bắt buộc bị thiếu hoặc không thể xác định một cách duy nhất.

## Notebook

- Public showcase nhanh: `notebooks/kaggle-t4x2-quick-demo.ipynb`
- Build lại và validation full index 100K: `notebooks/kaggle-t4x2-production-demo.ipynb`
- Full qualification: `kaggle/demo.ipynb`

Hai full notebook phải chạy trong các fresh session riêng.

## Bootstrap

`kaggle/bootstrap.sh` kiểm tra CUDA/T4, chuẩn bị dependency, enforce read-only input policy và in environment được dùng cho lần chạy.
