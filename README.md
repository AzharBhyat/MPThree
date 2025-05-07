
---

# 🎧 MPThree

A lightweight Python Flask API that **scrapes YouTube videos and returns MP3 audio**.

> ⚠️ **For educational and tinkering purposes only.**
> This project is not intended for public use or violation of YouTube's Terms of Service.

---

## 📖 Usage

### **GET**

#### `/mpthree?search=QUERY&limit=N`

* `search` – Search query (required)
* `limit` – Number of results (optional, default: 10)

**Example:**

```http
GET /mpthree?search=theweeknd&limit=8
```

**Returns:** JSON list of YouTube video results
Useful keys in each result:

* `title`
* `link`
* `thumbnails[0]` or `thumbnails[1]` (for different resolutions)

---

#### `/mpthree?download=YOUTUBE_LINK`

**Example:**

```http
GET /mpthree?download=https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

**Returns:** an MP3 file as an attachment

> ❗ **Do not** include both `search` and `download` in the same request.

---

### **POST or Other Methods**

The server will respond with:

```
"Oops thats a no no"
```

(Seriously, don't use anything other than GET, they are not implemented)

---
