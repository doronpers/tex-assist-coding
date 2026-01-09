# API Basics

Learn the fundamental patterns for building web APIs. Start here for backend development!

## What You'll Learn

- Creating simple endpoints
- Handling different HTTP methods
- Working with path and query parameters
- Structuring JSON responses
- Error handling patterns
- Configuration management
- Logging and monitoring

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

### Explanation
- `@app.get("/")` - Decorator that registers this function for GET requests to "/"
- Function name doesn't matter to the API (but use descriptive names)
- Return value is automatically converted to JSON

### When to Use
✅ Retrieving data
✅ Read-only operations
❌ Creating or modifying data (use POST, PUT, DELETE instead)

### Common Mistakes
- Using GET for operations that modify data
- Not returning consistent structure
- Missing type hints

### Test It

```bash
curl http://localhost:8000/
# Output: {"message":"Hello, World!"}
```

---

## Pattern 2: Path Parameters

### Problem
You need to accept dynamic values in the URL path.

### Solution

```python
@app.get("/hello/{name}")
def greet_user(name: str) -> dict[str, str]:
    """Greet a user by name."""
    return {"message": f"Hello, {name}!"}
```

### Explanation
- `{name}` in the path is a variable
- `name: str` parameter receives the value
- FastAPI automatically validates the type
- Return type hint improves documentation

### When to Use
✅ Resource identifiers (user ID, item ID)
✅ Required parameters
❌ Optional parameters (use query parameters instead)

### Variations

**Numeric path parameters:**
```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """FastAPI automatically converts and validates as integer."""
    return {"item_id": item_id}
```

**Multiple path parameters:**
```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user": user_id, "post": post_id}
```

### Common Mistakes
- Using path parameters for optional values
- Not validating parameter values
- Using complex objects in path (use request body instead)

---

## Pattern 3: Input Validation

### Problem
User input might be invalid, missing, or outside acceptable ranges.

### Solution

```python
from fastapi import HTTPException

def validate_item_id(item_id: int) -> None:
    """Validate item ID is within acceptable range."""
    MIN_ID, MAX_ID = 1, 1000

    if item_id < MIN_ID or item_id > MAX_ID:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found. Valid range: {MIN_ID}-{MAX_ID}"
        )

@app.get("/items/{item_id}")
def read_item(item_id: int):
    validate_item_id(item_id)
    return {"item_id": item_id, "name": f"Item #{item_id}"}
```

### Explanation
- Separate validation logic makes it reusable and testable
- `HTTPException` returns proper HTTP error responses
- Include helpful error messages for debugging
- Validate early, fail fast

### When to Use
✅ All user input
✅ Business rule validation
✅ Range checking

### When NOT to Use
❌ Internal function calls (trust your own code)
❌ Already-validated data

### Common Mistakes
- Validating only in the frontend (always validate on server)
- Generic error messages that don't help users
- Not handling all edge cases

---

## Pattern 4: Configuration Management

### Problem
Hard-coded values make code inflexible and difficult to deploy.

### Solution

```python
import os

class Config:
    """Centralized configuration."""
    HOST: str = os.getenv("API_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("API_PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    MIN_ITEM_ID: int = 1
    MAX_ITEM_ID: int = 1000

# Use throughout your code
def validate_item_id(item_id: int):
    if item_id < Config.MIN_ITEM_ID or item_id > Config.MAX_ITEM_ID:
        raise HTTPException(status_code=404, detail="Invalid ID")
```

### Explanation
- Environment variables allow configuration without code changes
- Defaults make development easier
- Centralized class makes config easy to find and modify
- Type annotations document expected types

### When to Use
✅ Anything that changes between environments (dev/prod)
✅ API keys and secrets
✅ Feature flags
✅ Business rules that might change

### Variations

**Using .env files:**
```python
from dotenv import load_dotenv

load_dotenv()  # Load .env file
config = Config()  # Now reads from .env
```

**Validation:**
```python
class Config:
    PORT: int = int(os.getenv("API_PORT", "8000"))

    def __post_init__(self):
        if self.PORT < 1 or self.PORT > 65535:
            raise ValueError(f"Invalid port: {self.PORT}")
```

### Common Mistakes
- Hard-coding secrets in code
- Not providing sensible defaults for development
- Mixing config with business logic

---

## Pattern 5: Logging

### Problem
You need visibility into what your API is doing.

### Solution

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.get("/items/{item_id}")
def read_item(item_id: int):
    logger.info(f"Retrieving item: {item_id}")

    try:
        item = get_item_from_db(item_id)
        return item
    except Exception as e:
        logger.error(f"Failed to retrieve item {item_id}: {e}")
        raise
```

### Explanation
- `logging.basicConfig()` sets up logging format
- `logger.info()` for normal operations
- `logger.error()` for problems
- Include context (item_id) in log messages

### When to Use
✅ API requests and responses
✅ Errors and exceptions
✅ Important business operations
❌ Sensitive data (passwords, tokens)

### Log Levels

```python
logger.debug("Detailed diagnostic info")      # Development only
logger.info("Normal operations")              # Production
logger.warning("Something unexpected")        # Investigate
logger.error("Operation failed")              # Requires attention
logger.critical("System-level failure")       # Wake someone up
```

### Common Mistakes
- Logging too much (noisy logs are useless)
- Logging too little (can't debug issues)
- Logging sensitive information
- Using `print()` instead of proper logging

---

## Pattern 6: Structured Error Responses

### Problem
Errors should be consistent and helpful.

### Solution

```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Catch all unhandled exceptions."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

# Specific errors
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 1:
        raise HTTPException(
            status_code=400,
            detail="Item ID must be positive"
        )

    if item_id > 1000:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found"
        )

    return {"item_id": item_id}
```

### Explanation
- Global handler catches unexpected errors
- Specific errors provide helpful messages
- Don't expose internal details to users
- Log detailed errors for debugging

### HTTP Status Codes

```
200 OK              - Success
201 Created         - Resource created
400 Bad Request     - Invalid input
401 Unauthorized    - Authentication required
403 Forbidden       - No permission
404 Not Found       - Resource doesn't exist
422 Validation Error - Invalid data format
500 Internal Error  - Server problem
```

### When to Use
✅ All APIs
✅ User-facing error messages
✅ Debugging information in logs

### Common Mistakes
- Exposing stack traces to users
- Using wrong status codes
- Generic "error occurred" messages

---

## Pattern 7: API Metadata and Documentation

### Problem
Developers need to understand how to use your API.

### Solution

```python
from fastapi import FastAPI

app = FastAPI(
    title="Hello API",
    description="A simple API for learning FastAPI basics",
    version="1.0.0",
)

@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int):
    """
    Get item information by ID.

    Args:
        item_id: The item's unique identifier (1-1000)

    Returns:
        Item details including ID, name, and description

    Raises:
        HTTPException: If item_id is out of valid range
    """
    return {"item_id": item_id}
```

### Explanation
- FastAPI auto-generates documentation at `/docs`
- Docstrings appear in the interactive documentation
- Tags organize endpoints by category
- Type hints define request/response schemas

### When to Use
✅ Always - good documentation is essential
✅ Public APIs
✅ Team APIs

### View Documentation

```bash
# Start your API
python main.py

# Open in browser:
http://localhost:8000/docs       # Interactive Swagger UI
http://localhost:8000/redoc      # Alternative ReDoc UI
http://localhost:8000/openapi.json  # OpenAPI schema
```

---

## Pattern 8: Application Lifespan Events

### Problem
You need to run code when the application starts or stops.

### Solution

```python
from contextlib import asynccontextmanager
from typing import AsyncIterator

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage application lifecycle."""
    # Startup
    logger.info("Starting API")
    # Initialize database connection, load ML models, etc.

    yield

    # Shutdown
    logger.info("Shutting down API")
    # Close connections, cleanup resources, etc.

app = FastAPI(lifespan=lifespan)
```

### Explanation
- Code before `yield` runs at startup
- Code after `yield` runs at shutdown
- Modern approach (replaces deprecated `on_event`)
- Properly handles cleanup with async context manager

### When to Use
✅ Database connections
✅ Cache initialization
✅ Loading configuration
✅ Resource cleanup

### Common Mistakes
- Using deprecated `@app.on_event()` decorators
- Not cleaning up resources on shutdown
- Long-running startup tasks blocking the server

---

## Complete Example

Here's how these patterns work together:

```python
"""Complete API example with all patterns."""
import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncIterator, Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# Configuration
class Config:
    MIN_ITEM_ID: int = 1
    MAX_ITEM_ID: int = 1000
    HOST: str = os.getenv("API_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("API_PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# Logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Lifespan
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting API")
    yield
    logger.info("Shutting down API")

# App initialization
app = FastAPI(
    title="Hello API",
    description="A complete example API",
    version="1.0.0",
    lifespan=lifespan,
)

# Validation
def validate_item_id(item_id: int) -> None:
    if item_id < Config.MIN_ITEM_ID or item_id > Config.MAX_ITEM_ID:
        logger.warning(f"Invalid item ID: {item_id}")
        raise HTTPException(
            status_code=404,
            detail=f"Item not found. Valid range: {Config.MIN_ITEM_ID}-{Config.MAX_ITEM_ID}",
        )

# Endpoints
@app.get("/", tags=["General"])
def read_root() -> Dict[str, str]:
    """Root endpoint."""
    logger.info("Root endpoint accessed")
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int) -> Dict:
    """Get item by ID."""
    validate_item_id(item_id)
    logger.info(f"Retrieving item: {item_id}")

    return {
        "item_id": item_id,
        "name": f"Item #{item_id}",
        "in_stock": True,
    }

# Error handling
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
```

See the full working example at [examples/01-hello-api](../../../examples/01-hello-api/)

---

## Next Steps

**Add validation:**
→ [Data Validation](../data-validation/)

**Add tests:**
→ [Testing Patterns](../testing/)

**Secure your API:**
→ [Security Patterns](../security/)

**Try the example:**
→ [Hello API Example](../../../examples/01-hello-api/)

---

## Quick Reference

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Simple GET | Retrieve data | `@app.get("/items")` |
| Path Parameters | Required values | `@app.get("/items/{id}")` |
| Validation | All user input | `if not valid: raise HTTPException` |
| Configuration | Environment-specific values | `os.getenv("API_KEY")` |
| Logging | Track operations | `logger.info("message")` |
| Error Handling | Consistent errors | `raise HTTPException(404)` |
| Documentation | Always | Use docstrings + type hints |
| Lifespan | Startup/shutdown | `@asynccontextmanager` |

---

**Start simple, add complexity when needed!** 🚀
