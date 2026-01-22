wrote by deepseek :)

---

# API Math Solver (Tiếng Việt)

Một hệ thống API giải toán linh hoạt và mạnh mẽ, kết hợp sức mạnh của AI (DeepSeek V3 & Google Gemini) và công cụ giải toán symbolic (SymPy) để xử lý nhiều dạng bài toán từ cơ bản đến nâng cao.

## ✨ Tính Năng Nổi Bật

*   **🎯 Đa dạng Trình Giải (Solver)**: Hỗ trợ nhiều "engine" giải toán khác nhau, dễ dàng mở rộng.
*   **🤖 AI Mạnh Mẽ**: Tích hợp DeepSeek V3 và Google Gemini cho khả năng hiểu ngôn ngữ tự nhiên và giải thích chi tiết.
*   **🧮 Giải Toán Chính Xác**: Sử dụng SymPy cho các phép toán symbolic (giải phương trình, đạo hàm, tích phân) với độ chính xác tuyệt đối.
*   **📦 Kiến Trúc Module**: Thiết kế rõ ràng, dễ dàng tùy chỉnh, bảo trì và thêm các solver mới.
*   **🖥️ Giao Diện Console Thân Thiện**: Menu tương tác dễ sử dụng để chọn solver và nhập bài toán.

## 📁 Cấu Trúc Dự Án

```
api-math-solver-vi/
├── main.py                     # Ứng dụng chính, giao diện điều khiển
├── requirements.txt            # Danh sách các thư viện Python cần thiết
├── api_keys.txt                # Lưu trữ API Keys (CẨN THẬN với file này!)
└── solvers/                    # Thư mục chứa tất cả các trình giải (solver)
    ├── __init__.py
    ├── base_solver.py          # Lớp cơ sở (BaseMathSolver) định nghĩa giao diện chung
    ├── deepseek_solver.py      # Trình giải sử dụng DeepSeek V3 API
    ├── gemini_solver.py        # Trình giải sử dụng Google Gemini API
    └── sympy_solver.py         # Trình giải sử dụng thư viện SymPy (toán học thuần túy)
```

## 🚀 Bắt Đầu Nhanh

### 1. Cài Đặt

**1.1. Sao chép kho lưu trữ:**
```bash
git clone https://github.com/w111user/api-math-solver-vi.git
cd api-math-solver-vi
```

**1.2. Cài đặt các phụ thuộc:**
```bash
pip install -r requirements.txt
```

### 2. Cấu Hình API Keys

Để sử dụng các solver AI, bạn cần cung cấp API Key.

*   **Cách 1 (Được khuyến nghị - Bảo mật hơn)**: Sử dụng tính năng có sẵn của tool
    ```env
    chọn lựa chọn số 6 và dán api vào
    ```
    *(bỏ trống những AI api bạn không dùng)*

*   **Cách 2**: Tạo hoặc chỉnh sửa tệp `api_keys.txt` trong thư mục gốc:
    ```
    DEEPSEEK_API_KEY=<your deepseek api key here>
    GEMINI_API_KEY=<your gemini api key here>
    ```
    **⚠️ Cảnh báo:** Không bao giờ commit file chứa API Key thật lên GitHub!

Bạn có thể lấy API Key tại:
*   **DeepSeek**: [https://platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
*   **Google AI Studio (Gemini)**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 3. Chạy Ứng Dụng

Chạy lệnh sau từ thư mục gốc của dự án:
```bash
python main.py
```

## 🧩 Cách Sử Dụng

Sau khi khởi động, bạn sẽ thấy một menu tương tác trong console:
1.  **Giải một bài toán (dùng tất cả solver)**: Gửi bài toán tới mọi solver đã được cấu hình để so sánh kết quả.
2.  **Giải một bài toán (chọn solver)**: Chọn một solver cụ thể (ví dụ: chỉ dùng DeepSeek hoặc SymPy).
3.  **Xem ví dụ về đề bài**: Hiển thị một số mẫu câu hỏi để bạn thử nghiệm.
4.  **Thoát chương trình**.

### Ví Dụ Đề Bài
Bạn có thể nhập các dạng bài toán như:
*   "Giải phương trình bậc hai: x^2 - 5x + 6 = 0"
*   "Tính đạo hàm của hàm số: sin(x) * cos(x)"
*   "Tính tích phân: ∫ x^2 dx"
*   "Tính giá trị biểu thức: 15 + 7 * (3 - 1)"

## 🔧 Các Thành Phần Chính

### `BaseMathSolver` (Lớp Cơ Sở)
Định nghĩa giao diện chung (`solve()` method) mà tất cả các solver cụ thể phải tuân theo, đảm bảo tính nhất quán.

### `DeepSeekSolver`
*   **Mô tả**: Sử dụng DeepSeek V3 API (`deepseek-chat` hoặc `deepseek-reasoner`).
*   **Ưu điểm**: Khả năng hiểu ngôn ngữ tự nhiên tốt, giải thích logic từng bước, phù hợp với bài toán phức tạp.
*   **Chi phí**: Cần có API Key và có thể phát sinh chi phí theo token.

### `GeminiSolver`
*   **Mô tả**: Sử dụng Google Gemini API (ví dụ: `gemini-2.5-flash`).
*   **Ưu điểm**: Tốc độ nhanh, chi phí thấp, giải thích mạch lạc.
*   **Chi phí**: Cần có API Key, có hạn mức miễn phí nhất định.

### `SympySolver`
*   **Mô tả**: Sử dụng thư viện SymPy thuần túy.
*   **Ưu điểm**: **Miễn phí, không cần mạng**, độ chính xác tuyệt đối cho các phép toán symbolic (đại số, giải tích).
*   **Hạn chế**: Yêu cầu đầu vào có cú pháp rõ ràng, chưa xử lý tốt ngôn ngữ tự nhiên.

## 📝 Ví Dụ Đầu Ra

```
🤖 CHÀO MỪNG ĐẾN HỆ THỐNG GIẢI TOÁN AI DEMO v2
============================================================
🎯 Các trình giải sẵn sàng: SymPy (Local), DeepSeek V3, Google Gemini

✍️  Nhập đề bài toán của bạn: Giải phương trình x^2 - 5x + 6 = 0

⏳ Đang xử lý với SymPy (Local)...
============================================================
🧮 TRÌNH GIẢI: SympySolver
============================================================
📝 CÁC BƯỚC GIẢI:
Giải phương trình: x**2 - 5*x + 6 = 0
Nghiệm tìm được: [2, 3]
--------------------------------------------------------
✅ ĐÁP ÁN:
Phương trình có nghiệm: [2, 3]
============================================================
```

## 🛠️ Phát Triển & Mở Rộng

### Thêm Solver Mới
1.  Tạo một tệp mới trong thư mục `solvers/`, ví dụ: `my_new_solver.py`.
2.  Kế thừa lớp `BaseMathSolver` và triển khai phương thức `solve(problem_statement)`.
3.  Import và thêm solver mới vào danh sách khởi tạo trong `main.py`.

### Hướng Phát Triển Tiếp Theo
*   **Chuyển đổi thành Web API**: Sử dụng FastAPI hoặc Flask để biến hệ thống thành một dịch vụ web.
*   **Cải thiện SympySolver**: Tích hợp mô hình ngôn ngữ nhỏ để phân tích câu hỏi tự nhiên và chuyển đổi thành lệnh SymPy.
*   **Thêm Solver**: Tích hợp các API AI khác (OpenAI GPT, Claude, v.v.).
*   **Giao diện Web Đơn giản**: Xây dựng frontend bằng Streamlit hoặc HTML/JS để nhập bài toán và xem kết quả.

## 👏 Đóng Góp
Mọi đóng góp, báo cáo lỗi (bug reports) và yêu cầu tính năng (feature requests) đều được hoan nghênh! Vui lòng tạo một **Issue** hoặc **Pull Request** trên GitHub.

---

*Nếu bạn gặp bất kỳ vấn đề nào, vui lòng kiểm tra phần cấu hình API Key và đảm bảo bạn đã cài đặt đủ các thư viện trong `requirements.txt`.*

---

