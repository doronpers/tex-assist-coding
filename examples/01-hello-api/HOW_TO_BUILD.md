# How to Build Your First API

Step-by-step guide to building a FastAPI "Hello World" application with AI assistance.

## Overview

We'll build this incrementally:
1. **Setup** - Install tools and create project
2. **Minimal API** - Get something running
3. **Add Endpoints** - Build features one at a time
4. **Test** - Verify everything works

**Philosophy:** Small steps, test often, understand each piece.

## Part 1: Setup (5-10 minutes)

### Step 1.1: Create Project Folder

```bash
# Create and enter directory
mkdir 01-hello-api
cd 01-hello-api
```

### Step 1.2: Create Virtual Environment (Recommended)

**Why?** Keeps project dependencies separate.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal.

### Step 1.3: Install FastAPI and Uvicorn

```bash
pip install -r requirements.txt
```

**What we just installed:**
- **FastAPI** - The web framework (makes building APIs easy)
- **Uvicorn** - The web server (runs your API)
- **Pydantic** - Data validation library FastAPI relies on

> Tip: If you don't have `requirements.txt` yet, install the same packages individually (`pip install fastapi uvicorn pydantic`) and pin them later in Part 5.

### Step 1.4: Create Project Files

```bash
# Create empty files
touch main.py requirements.txt .gitignore

# Or on Windows:
type nul > main.py
type nul > requirements.txt  
type nul > .gitignore
```

> Note: In this repository, `main.py` and `requirements.txt` are already present. Add a `.gitignore` if you're starting from scratch.

## Part 2: The Minimal API (10-15 minutes)

### Step 2.1: The Three Questions

Before coding, ask:

**1. What am I building?**
A web API that responds to HTTP requests with "Hello, World!"

**2. How will I know it works?**
I can visit http://localhost:8000 in a browser and see the message.

**3. What could go wrong?**
The server might not start if the port is already in use.

Clear thinking = Clear code!

### Step 2.2: Write Minimal Code

Open `main.py` and type this (or ask AI to generate it):

```python
from fastapi import FastAPI

# Create the app
app = FastAPI()

# Create a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 2.3: Understand Each Line

Let's break it down:

```python
from fastapi import FastAPI
# Import the FastAPI class - this is the framework
```

```python
app = FastAPI()
# Create an instance of FastAPI
# This is your application
```

```python
@app.get("/")
# Decorator that says "when someone visits /, run the function below"
# @app.get means HTTP GET request
# "/" means the root URL
```

```python
def read_root():
    return {"message": "Hello, World!"}
# The function that runs when someone visits /
# Returns a Python dictionary (FastAPI converts to JSON automatically)
```

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# If we run this file directly (not import it), start the server
# Listen on all network interfaces (0.0.0.0) on port 8000
```

### Step 2.4: Run It!

```bash
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2.5: Test It!

**Option 1: Browser**
Open http://localhost:8000

You should see:
```json
{"message":"Hello, World!"}
```

**Option 2: Interactive Docs**
Open http://localhost:8000/docs

Click "Try it out" → "Execute"

**Success!** 🎉 You built an API!

### Step 2.6: Stop the Server

Press `Ctrl+C` in the terminal.

## Part 3: Add Personalized Greeting (10 minutes)

### Step 3.1: The Three Questions Again

**1. What?**
Add an endpoint that greets a specific person.

**2. Test?**
Visit /hello/Alice and see "Hello, Alice!"

**3. Edge case?**
What if no name is provided?

### Step 3.2: Ask AI for Help

**Prompt to AI (ChatGPT, Claude, or Copilot):**
```
I have a FastAPI app with a root endpoint.

Add a new endpoint at /hello/{name} that:
- Accepts a name as a path parameter
- Returns a JSON response with a personalized greeting

Current code:
[paste your main.py]
```

### Step 3.3: Or Write It Yourself

Add this to `main.py`:

```python
@app.get("/hello/{name}")
def greet_user(name: str):
    """Greet a specific user."""
    return {"message": f"Hello, {name}!"}
```

**What's new:**
- `{name}` in the path is a **path parameter**
- `name: str` tells FastAPI to expect a string
- `f"Hello, {name}!"` is an f-string (inserts the name)

### Step 3.4: Test the New Endpoint

Restart your server:
```bash
python main.py
```

Try these URLs:
- http://localhost:8000/hello/Alice
- http://localhost:8000/hello/Bob
- http://localhost:8000/hello/YourName

Each should return a personalized greeting!

## Part 4: Add Item Endpoint (10 minutes)

### Step 4.1: Add Item Endpoint

Let's add one more endpoint for practice.

**With AI:**
```
Add an endpoint at /items/{item_id} that:
- Accepts an integer item_id
- Returns the item_id and a fake item name
```

**Or write it:**
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Get item by ID."""
    return {
        "item_id": item_id,
        "name": f"Item #{item_id}",
        "description": "This is a sample item"
    }
```

### Step 4.2: Complete main.py

Your complete `main.py` should look like:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    """Root endpoint - returns a simple greeting."""
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def greet_user(name: str):
    """
    Greet a specific user by name.
    
    Args:
        name: The user's name
        
    Returns:
        A personalized greeting message
    """
    return {"message": f"Hello, {name}!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Get item information by ID.
    
    Args:
        item_id: The item's unique identifier
        
    Returns:
        Item details including ID, name, and description
        
    Raises:
        HTTPException: If item_id is out of valid range
    """
    # Simple validation - items must be between 1 and 1000
    if item_id < 1 or item_id > 1000:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found"
        )

    return {
        "item_id": item_id,
        "name": f"Item #{item_id}",
        "description": "This is a sample item",
        "in_stock": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 4.3: Test All Endpoints

Restart and test:
- http://localhost:8000/ ← Hello World
- http://localhost:8000/hello/Alice ← Personalized greeting
- http://localhost:8000/items/42 ← Item info
- http://localhost:8000/docs ← Interactive documentation

All working? Great! 🎉

## Part 5: Requirements File (5 minutes)

### Step 5.1: Create requirements.txt

This file lists all dependencies so others can install them.

```bash
# If you're following along in THIS repo, requirements.txt is already provided
# If you're recreating from scratch, pin the versions you used
```

If you need to create `requirements.txt`, use the pinned versions from this repo:
```
fastapi==0.124.4
uvicorn==0.34.0
pydantic==2.9.0
```
These are the exact versions in `examples/01-hello-api/requirements.txt`.

### Step 5.2: Create .gitignore

Create `.gitignore` file:
```
# Virtual environment
venv/
env/
.venv/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# IDE
.vscode/
.idea/
*.swp
```

## Part 6: Error Handling (Optional Advanced)

### Add Better Error Handling

```python
from fastapi import FastAPI, HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Get item by ID."""
    # Validate item_id
    if item_id < 1 or item_id > 1000:
        raise HTTPException(
            status_code=404, 
            detail="Item not found"
        )
    
    return {
        "item_id": item_id,
        "name": f"Item #{item_id}",
        "description": "This is a sample item"
    }
```

Test with an invalid ID:
http://localhost:8000/items/9999

Should return a 404 error!

## Using AI Throughout

### AI Prompts That Worked

**Starting out:**
```
Create a minimal FastAPI application with a single endpoint that returns "Hello, World!" in JSON format.
```

**Adding features:**
```
Add an endpoint to my FastAPI app that accepts a name as a path parameter and returns a personalized greeting.
```

**Understanding:**
```
Explain what @app.get("/") means in FastAPI. What's a decorator?
```

**Debugging:**
```
I'm getting "Address already in use" error when starting my FastAPI server. How do I fix this?
```

### AI Tips for This Project

1. **Be specific about what you want**
2. **Share your current code when asking for additions**
3. **Ask for explanations of unfamiliar concepts**
4. **Test each change before moving to the next**

## Common Issues and Solutions

### Issue: "Module not found: fastapi"

**Solution:**
```bash
pip install fastapi uvicorn
```

### Issue: "Address already in use"

**Solution:**
```bash
# Check what's using port 8000
lsof -i :8000

# Kill it or use different port
uvicorn main:app --port 8001
```

### Issue: "Changes not showing"

**Solution:** Restart the server, or use auto-reload:
```bash
uvicorn main:app --reload
```

## What You Built

Congratulations! You now have:
- ✅ A working web API
- ✅ Three functional endpoints
- ✅ Understanding of basic FastAPI concepts
- ✅ Experience using AI to build
- ✅ A foundation for more complex projects

## Next Challenges

Try these on your own:

### Challenge 1: Add More Endpoints
Create `/goodbye/{name}` and `/status` endpoints.

### Challenge 2: Add Query Parameters
```python
@app.get("/search")
def search(query: str, limit: int = 10):
    return {"query": query, "limit": limit, "results": []}
```

Test: http://localhost:8000/search?query=hello&limit=5

### Challenge 3: Add Data Validation
Use Pydantic models to validate request data.

### Challenge 4: Add Tests
Create `test_main.py` with pytest.

## Where to Go From Here

**Next project:**
→ Extend this API using the API basics section in the [Patterns overview](../../documentation/04-patterns/README.md) (no separate todo app in this repo yet)

**Learn patterns:**
→ API basics section in the [Patterns overview](../../documentation/04-patterns/README.md) - Common API patterns

**Understand workflows:**
→ [Start Simple](../../documentation/03-workflow-building/start-simple.md) - Basic workflow approach
→ [AI Tools](../../documentation/02-ai-tools/README.md) - Using AI effectively

## Reflect on Your Process

Before moving on, think about:
- What was hardest?
- What was easiest?
- How did AI help (or not help)?
- What would you do differently next time?

Write it down in your [learning journal](../../templates/learning-journal.md)!

---

**You did it! Time to celebrate!** 🎉🚀

Keep building, keep learning, keep growing!
