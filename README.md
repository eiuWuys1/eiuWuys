
# Dockur (Windows) — Fork & Tối Ưu Hóa cho GitHub Codespaces

> **Lưu ý:** Đây là bản **fork** từ dự án gốc Dockur (không phải do tôi, **Wuys**, phát triển từ đầu).

---

## Giới thiệu

Dockur là một môi trường Windows chạy trong Docker. Tôi đã chỉnh sửa lại để phù hợp và chạy ổn định trên **GitHub Codespaces**, với cấu hình hợp lý để **tránh bị ban** và vẫn đảm bảo hiệu suất sử dụng.

---

## Cấu hình tối ưu đề xuất

### Cấu hình an toàn, ổn định:
- **CPU:** 2 core  
- **RAM:** 6 GB  
- **Ổ cứng:** 32 GB (tối đa GitHub Codespaces cho phép)

### Cấu hình hiệu suất cao:
- **CPU:** 4 core  
- **RAM:** 14 GB  
- **Ổ cứng:** 32 GB

---

## Hệ điều hành

- **Mặc định:** Windows 10 Pro sẽ được cài đặt.
- **Tùy chỉnh:** Bạn có thể thay đổi phiên bản Windows bằng cách chỉnh sửa biến môi trường `VERSION` trong `Dockerfile`.

### Cách thay đổi phiên bản Windows

Trong `Dockerfile`, bạn thêm hoặc chỉnh sửa các dòng sau:

```dockerfile
ENV VERSION="10"
ENV RAM_SIZE="4G"
ENV CPU_CORES="2"
ENV DISK_SIZE="64G"
````

**Danh sách giá trị hợp lệ của `VERSION`:**

| Giá trị | Phiên bản hệ điều hành    | Dung lượng |
| ------- | ------------------------- | ---------- |
| `11`    | Windows 11 Pro            | 5.4 GB     |
| `11l`   | Windows 11 LTSC           | 4.7 GB     |
| `11e`   | Windows 11 Enterprise     | 4.0 GB     |
| `10`    | Windows 10 Pro            | 5.7 GB     |
| `10l`   | Windows 10 LTSC           | 4.6 GB     |
| `10e`   | Windows 10 Enterprise     | 5.2 GB     |
| `8e`    | Windows 8.1 Enterprise    | 3.7 GB     |
| `7u`    | Windows 7 Ultimate        | 3.1 GB     |
| `vu`    | Windows Vista Ultimate    | 3.0 GB     |
| `xp`    | Windows XP Professional   | 0.6 GB     |
| `2k`    | Windows 2000 Professional | 0.4 GB     |
| `2025`  | Windows Server 2025       | 5.6 GB     |
| `2022`  | Windows Server 2022       | 4.7 GB     |
| `2019`  | Windows Server 2019       | 5.3 GB     |
| `2016`  | Windows Server 2016       | 6.5 GB     |
| `2012`  | Windows Server 2012       | 4.3 GB     |
| `2008`  | Windows Server 2008       | 3.0 GB     |
| `2003`  | Windows Server 2003       | 0.6 GB     |

---

## Tài khoản mặc định

* Trong quá trình cài đặt, một tài khoản có tên là `Docker` sẽ được tạo sẵn.
* **Mật khẩu mặc định là:** `admin`

> Bạn có thể sử dụng thông tin này để đăng nhập ngay sau khi hệ điều hành được khởi động.

---

## Hướng dẫn truy cập

Sau khi container đã khởi chạy thành công, bạn có thể truy cập giao diện điều khiển Windows thông qua trình duyệt.

### Nếu sử dụng **GitHub Codespaces**:

* Chỉ cần chờ đến khi xuất hiện thông báo **port 8006 đã được mở**.
* Sau đó click vào liên kết hoặc chọn **"Open in Browser"** để truy cập.

### Nếu chạy trên **localhost** (máy cá nhân):

* Mở trình duyệt và nhập một trong hai địa chỉ sau:

  ```
  http://127.0.0.1:8006
  ```

  hoặc

  ```
  http://localhost:8006
  ```

---

## Mẹo hay

### 1. Bypass giới hạn 60 giờ sử dụng Codespace

Thông thường, GitHub Codespaces giới hạn mỗi tài khoản miễn phí chỉ được **60 giờ sử dụng mỗi tháng**. Tuy nhiên, bạn có thể **vượt qua giới hạn này** bằng cách:

* Nhờ **một người đã có GitHub Student** (hoặc bất kỳ tài khoản có gói trả phí nào) tạo giúp bạn một **Codespace với cấu hình 4 core**.
* Sau khi họ tạo xong Codespace, bạn có thể truy cập và sử dụng như bình thường — gần như **không giới hạn thời gian**!

> **Cách đơn giản nhất:**
> Truy cập **[cs50.dev](https://cs50.dev)** và đăng nhập bằng tài khoản GitHub của bạn.
> Trang web này do Harvard CS50 quản lý và sẽ tạo sẵn cho bạn một Codespace đã trả phí — tức là bạn sẽ có một VPS Windows **gần như vĩnh viễn** mà **CS50 là bên trả tiền giúp bạn!**

---

### 2. Luôn giữ máy hoạt động

* Codespace sẽ **tự động ngắt** nếu bạn không tương tác trong một thời gian.
* Khi Codespace bị tắt, bạn **sẽ mất toàn bộ phiên Windows** và phải thiết lập lại từ đầu.

> Vì vậy, hãy đảm bảo có **tác vụ chạy nền liên tục** hoặc dùng tiện ích giữ máy luôn "tỉnh".

---

**Fork bởi \[Wuys]**
**Dự án gốc: [Dockur ](https://github.com/Makaix/Dockur)**

```
