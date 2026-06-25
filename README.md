# AA Clinic — Voice API

Backend FastAPI độc lập cho voicebot **AA International Aesthetic Clinic** (demo chính Botox + 8 demo bổ sung).

Mint ephemeral token Gemini Live — `GEMINI_API_KEY` chỉ lưu trên server (Render), không expose ra browser.

## API

| Method | Path | Mô tả |
|--------|------|--------|
| GET | `/api/health` | Health check + danh sách demo |
| GET | `/api/demo/{demo_id}/schema` | Schema form theo demo |
| POST | `/api/demo/live-token` | Body: `{ "demo_id": "00".."08", "language": "vi" \| "en" }` |

**Demo `00`** — Tư vấn Botox AA Clinic (kịch bản chính theo PDF).  
**Demo `01`–`08`** — Các mô-đun Voice AI bổ sung.

## Chạy local

```bash
cd voice-api
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env          # điền GEMINI_API_KEY
uvicorn app.main:app --port 8001 --reload
```

## Deploy Render (repo GitHub mới — tách khỏi `vnclinic-voice-ap`)

Dùng **repo mới** để không ảnh hưởng backend cũ. Thư mục `voice-api` là root của repo đó.

### Bước 1 — Tạo repo trống trên GitHub

Ví dụ tên: `aa-clinic-voice-api` (Private hoặc Public, **không** tick README/.gitignore).

### Bước 2 — Đổi remote và push (từ máy local)

```bash
cd voice-api

# Gỡ liên kết repo cũ (không xóa code, không đụng GitHub cũ)
git remote remove origin

# Gắn repo mới — thay <user> và tên repo
git remote add origin https://github.com/<user>/aa-clinic-voice-api.git

git add .
git commit -m "AA Clinic voice API — demo Botox 00 + 8 module bổ sung"
git push -u origin main
```

Nếu branch local không phải `main`, đổi tên trước khi push: `git branch -M main`.

### Bước 3 — Tạo Web Service trên Render

1. [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint** (dùng `render.yaml`)  
   hoặc **Web Service** → Runtime: **Docker**, Root Directory: `.`
2. Kết nối repo GitHub vừa tạo.
3. Thêm biến môi trường:

| Biến | Bắt buộc | Ví dụ |
|------|----------|-------|
| `GEMINI_API_KEY` | Có | Key từ [Google AI Studio](https://aistudio.google.com/apikey) |
| `GEMINI_LIVE_MODEL` | Không | `gemini-3.1-flash-live-preview` (mặc định) |
| `CORS_ORIGINS` | Có | URL frontend, phân tách bằng dấu phẩy |

Ví dụ `CORS_ORIGINS`:

```
https://hai1975.com,https://www.hai1975.com,http://localhost:8080
```

Thêm domain preview/staging nếu có (vd. URL Vercel/Netlify).

### Bước 4 — Kiểm tra sau deploy

```bash
curl https://<ten-service>.onrender.com/api/health
```

Kết quả mong đợi: `"status": "ok"`, `"demos"` có `"00"` … `"08"`, `"gemini_configured": true`.

**Production (đã deploy):**

- URL: `https://aa-clinic-voice-api.onrender.com`
- Blueprint ID: `exs-d8ufmtsm0tmc73a67l10`
- Health: `GET /api/health`

### Bước 5 — Gắn frontend

Trong repo frontend (`VN_Clinic_HAI`), set trước khi build production:

```env
VITE_VOICE_API_BASE=https://<ten-service>.onrender.com
```

Không có dấu `/` ở cuối URL.

## Lưu ý

- Plan **free** trên Render có thể sleep sau ~15 phút không dùng — request đầu tiên có thể chậm ~30–60 giây.
- Nếu voice báo lỗi CORS: kiểm tra `CORS_ORIGINS` đã có đúng origin frontend (kể cả `http://localhost:8080` khi dev).
