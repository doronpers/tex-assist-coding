# API Basics

Learn the fundamental patterns for building web APIs. Start here for backend development!

## What You'll Learn

- Creating simple endpoints
- Handling different HTTP methods
- Working with path and query parameters
- Structuring JSON responses
- Basic error handling

## Prerequisites

**You should know:**
- Basic Python (or your chosen language)
- What an API is (see [Hello API example](../../../examples/01-hello-api/))

**You don't need:**
- Database knowledge
- Frontend skills
- Deployment experience

## Quick Start

Try the Hello API example first: [examples/01-hello-api](../../../examples/01-hello-api/)

Then come back here to learn the patterns!

---

## Pattern 1: Simple GET Endpoint

### Problem
You need to return data when someone visits a URL.

### Solution

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### When to Use
✅ Retrieving data  
✅ Read-only operations  
❌ Creating or modifying data

### Test It

```bash
curl http://localhost:8000/
```

---

## More Patterns Coming Soon

We're building out comprehensive API pattern documentation. For now, see the [Hello API example](../../../examples/01-hello-api/) for a complete working example.

## Next Steps

**Add validation:**
→ [Data Validation](../data-validation/)

**Add tests:**
→ [Testing Patterns](../testing/)

**Secure your API:**
→ [Security Patterns](../security/)

---

**Start simple, add complexity when needed!** 🚀
