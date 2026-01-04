# Hello API - Your First FastAPI Project

Build a simple "Hello World" API from scratch with AI assistance. Perfect first project!

## What You'll Build

A working web API with three endpoints:
- `GET /` - Returns "Hello, World!"
- `GET /hello/{name}` - Returns personalized greeting
- `GET /items/{item_id}` - Returns item information

## What You'll Learn

- Setting up a Python web server
- Creating API endpoints
- Path parameters
- JSON responses
- Testing APIs manually
- Using AI to build incrementally

## Prerequisites

**You need:**
- Python 3.8+ installed
- Basic terminal/command line knowledge
- A code editor (VS Code recommended)
- Curiosity and willingness to learn!

**You don't need:**
- Prior API experience
- Deep Python knowledge
- Database setup
- Deployment knowledge

This is intentionally simple!

## Time Estimate

- **Following step-by-step:** 30-45 minutes
- **With AI help:** 15-20 minutes
- **Just reading:** 10 minutes

No rush! Go at your own pace.

## Project Structure

```
01-hello-api/
├── README.md (you are here!)
├── HOW_TO_BUILD.md (step-by-step guide)
├── main.py (the code)
└── requirements.txt (dependencies pinned for this repo)
```

## Quick Start

Want to see it running first?

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
python main.py

# 3. Open browser to:
http://localhost:8000
```

You should see `{"message": "Hello, World!"}`

**Want to build it yourself?** → Continue to [HOW_TO_BUILD.md](HOW_TO_BUILD.md)

## What This Project Teaches

### Concept 1: Web APIs

**What's an API?**
A way for programs to talk to each other over the internet.

Think of it like a restaurant:
- You (client) order food
- Kitchen (API) prepares it
- Waiter (HTTP) delivers it back

### Concept 2: Endpoints

**What's an endpoint?**
A specific URL that does something.

Like buttons on a vending machine:
- `/` = the main button
- `/hello/Alice` = button that greets Alice
- `/items/5` = button that gets item #5

### Concept 3: HTTP Methods

**GET** = Retrieve information (like reading)
**POST** = Send information (like writing)
**PUT** = Update information
**DELETE** = Remove information

This project uses GET (simplest).

### Concept 4: JSON

**What's JSON?**
A way to structure data that both computers and humans can read.

```json
{
  "name": "Alice",
  "age": 30,
  "active": true
}
```

Like a dictionary in Python, object in JavaScript.

## Extensions to Try

Once you've built the basic version, try adding:

### Easy Extensions

**1. Add more greetings:**
```python
@app.get("/goodbye/{name}")
def say_goodbye(name: str):
    return {"message": f"Goodbye, {name}!"}
```

**2. Add a status endpoint:**
```python
@app.get("/status")
def get_status():
    return {"status": "running", "version": "1.0"}
```

**3. Add timestamp to responses:**
```python
from datetime import datetime

@app.get("/time")
def get_time():
    return {"current_time": datetime.now().isoformat()}
```

### Medium Extensions

**4. Add query parameters:**
```python
@app.get("/greet")
def greet(name: str = "World", lang: str = "en"):
    greetings = {
        "en": f"Hello, {name}!",
        "es": f"¡Hola, {name}!",
        "fr": f"Bonjour, {name}!"
    }
    return {"message": greetings.get(lang, greetings["en"])}
```

Test: http://localhost:8000/greet?name=Alice&lang=es

**5. Add data validation:**
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/items")
def create_item(item: Item):
    return {"created": item, "total": item.price * item.quantity}
```

### Challenge Extensions

**6. Add in-memory database:**
Store items in a dictionary, add GET/POST/DELETE endpoints.

**7. Add error handling:**
Return proper error messages for invalid inputs.

**8. Add logging:**
Log every request to a file.

## Common Issues

### Issue 1: "Port already in use"

**Error:** `Address already in use`

**Solution:**
```bash
# Kill the process using port 8000
# On Mac/Linux:
lsof -i :8000
kill -9 [PID]

# On Windows:
netstat -ano | findstr :8000
taskkill /PID [PID] /F

# Or use a different port:
uvicorn main:app --port 8001
```

### Issue 2: "Module not found"

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
pip install fastapi uvicorn
```

Make sure you're in the right directory!

### Issue 3: "Changes not reflecting"

**Problem:** You changed code but API still shows old version

**Solution:** Restart the server (Ctrl+C, then run again)

Or use auto-reload:
```bash
uvicorn main:app --reload
```

## Testing Your API

### Method 1: Browser

Just open http://localhost:8000 in any browser.

**Pros:** Easy, visual
**Cons:** Only works for GET requests

### Method 2: curl (Command Line)

```bash
# Test root endpoint
curl http://localhost:8000/

# Test with name parameter
curl http://localhost:8000/hello/Alice

# Test with item ID
curl http://localhost:8000/items/42
```

**Pros:** Fast, scriptable
**Cons:** Less friendly for beginners

### Method 3: Postman or Insomnia

Download free API testing tool.

**Pros:** Professional, feature-rich
**Cons:** Extra installation

### Method 4: FastAPI Docs

Go to http://localhost:8000/docs

**Pros:** Built-in, interactive, shows all endpoints
**Cons:** None! Use this!

## Next Steps

After building this project:

### If you want more API practice:
→ Explore the API basics section in the **[Patterns overview](../../docs/04-patterns/README.md)** and extend this project

### If you want to add features:
→ Try the extensions above

### If you want to understand patterns:
→ **[Patterns overview](../../docs/04-patterns/README.md)** - See the API basics section

### If you want to design a simple workflow:
→ **[Start simple](../../docs/03-workflow-building/start-simple.md)**

### If you want to deploy:
→ Look into Heroku, Railway, or Render (free tiers available)

## Questions?

### "Is this too simple?"

Not at all! Every complex API started as something like this. Master the basics.

### "Can I use this in production?"

This exact code? No - it's for learning.
But FastAPI itself? Yes! Production-ready framework used by major companies.

### "What if I break something?"

You can't! This is running locally on your computer. Delete it and start over anytime.

### "Do I need to memorize all this?"

Nope! Understanding concepts > memorizing syntax. You'll use docs and AI for specific syntax.

## Success Criteria

You've succeeded when:
- [ ] Your API runs without errors
- [ ] You can hit all three endpoints
- [ ] You understand what each line does (mostly)
- [ ] You feel curious to add more features

**Don't aim for perfect. Aim for working and understood.**

## Celebrate!

You just built a working web API! 🎉

Not everyone gets here. Many people give up before starting. You didn't. That's worth celebrating.

**Share your success:**
- Show a friend
- Tweet about it
- Add to your learning journal
- Try an extension

---

**Ready to build it? Head to [HOW_TO_BUILD.md](HOW_TO_BUILD.md)!** 🚀
