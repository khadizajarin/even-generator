

---

```markdown
# Even Number Generator API

A simple Flask-based API that generates a list of even numbers up to a given number `n`. Deployed on [Render](https://render.com).

---

## 🚀 Features

- Generate a list of even numbers up to `n`
- Lightweight and fast API built with Flask
- Production-ready deployment using Gunicorn

---

## 📦 Tech Stack

- Python 3.12
- Flask
- Gunicorn
- Render (for deployment)

---

## 📁 Project Structure

```

even-generator/
├── app.py
├── requirements.txt
├── Procfile
└── README.md

````

---

## 🔧 Local Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/khadizajarin/even-generator.git
   cd even-generator
````

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python3 app.py
   ```

---

## 🌐 API Usage

### Endpoint

```
GET /generate?n=<number>
```

### Example

```bash
curl http://localhost:5000/generate?n=5
```

### Response

```json
{
  "even_numbers": [ 2, 4, 6, 8, 10]
}
```

---

## ☁️ Deployment on Render

1. Push code to a GitHub repository.
2. Go to [https://render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Use these settings:

   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `gunicorn app:app`
   * **Environment**: `Python`
5. Wait for the build & access your live API at:

   ```
   https://even-generator.onrender.com/generate?n=10
   ```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Roza Jarin**


```

---

Let me know if you'd like to include a logo, test instructions, or link it with Postman for API testing!
```
