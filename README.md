
---

# 🎧 MPThree

A lightweight Python Flask API that **scrapes YouTube videos and returns audio streams**.

> ⚠️ **For educational and tinkering purposes only.**
> This project is **not intended for public use**, distribution, or violation of YouTube's Terms of Service.

---

## 📚 Purpose

MPThree is a backend tool created **for learning how APIs, scraping, and Flask work together**. It allows experimenting with:

* 🔧 Flask API routing
* ⏬ Streaming audio data from online sources
* 🧪 Understanding request/response cycles

---

## ⚙️ How It Works

* Accepts a YouTube URL via an endpoint
* Uses `yt_dlp` (a YouTube scraping library)
* Extracts and returns audio in a streamable format

---

## 🚀 Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/AzharBhyat/MPThree.git
   cd MPThree
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   python app.py
   ```

4. Example request:

   ```
   GET /audio?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

---

---

## ❗ Disclaimer

This code is for **educational and personal tinkering only**.
**Do not** deploy it or use it to download copyrighted content.
Respect creators and platform policies.

---

Want help adding Swagger docs or rate limiting for safer API experimentation?
