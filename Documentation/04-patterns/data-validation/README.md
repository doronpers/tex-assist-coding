# Data Validation

Learn how to validate user input to prevent errors and security issues.

## Why Validation Matters

**Without validation:**
```python
# User sends: {"age": -5, "email": "notanemail"}
# Your app: Crashes or stores invalid data
```

**With validation:**
```python
# User sends: {"age": -5, "email": "notanemail"}
# Your app: Returns clear error message
# User fixes their input
```

## Key Principles

1. **Never trust user input** - Users make mistakes (or attack your system)
2. **Validate on the server** - Frontend validation is for UX, not security
3. **Give helpful error messages** - Tell users what's wrong and how to fix it
4. **Use validation libraries** - Don't reinvent the wheel

---

## Pattern 1: Manual Validation

### Problem
You need to validate simple inputs without external libraries.

### Solution

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Validate range
    if item_id < 1 or item_id > 1000:
        raise HTTPException(
            status_code=400,
            detail="Item ID must be between 1 and 1000"
        )

    return {"item_id": item_id}
```

### When to Use
✅ Simple validation logic
✅ Single field validation
❌ Complex validation rules (use Pydantic instead)
❌ Multiple fields with dependencies

### Common Mistakes
- Not validating at all
- Vague error messages ("Invalid input")
- Validating in multiple places inconsistently

---

## Pattern 2: Pydantic Models

### Problem
You need to validate complex data structures with multiple fields.

### Solution

```python
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    """User registration data."""
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    age: int = Field(..., ge=13, le=120)

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v or '.' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

    @validator('username')
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

@app.post("/users")
def create_user(user: User):
    """FastAPI automatically validates using the Pydantic model."""
    return {"message": f"User {user.username} created"}
```

### Explanation
- `Field(..., min_length=3)` - Built-in validation constraints
- `@validator` decorator - Custom validation logic
- FastAPI automatically validates request body against the model
- Returns 422 Unprocessable Entity with validation details

### When to Use
✅ Request bodies with multiple fields
✅ Complex validation rules
✅ Data that needs to be transformed (e.g., lowercase emails)

### Test It

```bash
# Valid request
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","age":25}'

# Invalid request (age too low)
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"bob","email":"bob@example.com","age":10}'
```

---

## Pattern 3: Field Constraints

### Problem
You need to enforce specific constraints on field values.

### Solution

```python
from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class Product(BaseModel):
    """Product with constrained fields."""
    name: constr(min_length=1, max_length=100)  # Constrained string
    price: float = Field(..., gt=0, le=1_000_000)  # Greater than 0
    quantity: conint(ge=0)  # Greater than or equal to 0
    description: Optional[str] = Field(None, max_length=500)
    sku: str = Field(..., regex=r'^[A-Z]{3}-\d{6}$')  # Pattern: ABC-123456

@app.post("/products")
def create_product(product: Product):
    return {"message": f"Product {product.name} created"}
```

### Available Constraints

| Constraint | Description | Example |
|------------|-------------|---------|
| `min_length` | Minimum string length | `Field(..., min_length=3)` |
| `max_length` | Maximum string length | `Field(..., max_length=100)` |
| `gt` | Greater than | `Field(..., gt=0)` |
| `ge` | Greater than or equal | `Field(..., ge=0)` |
| `lt` | Less than | `Field(..., lt=100)` |
| `le` | Less than or equal | `Field(..., le=100)` |
| `regex` | Regex pattern match | `Field(..., regex=r'^\d{3}$')` |
| `...` | Required field | `Field(...)` |
| `None` | Optional with default | `Field(None)` |

### When to Use
✅ Enforcing business rules
✅ Format validation (SKU, phone numbers, etc.)
✅ Range validation

---

## Pattern 4: Custom Validators

### Problem
You need validation logic that's specific to your business rules.

### Solution

```python
from pydantic import BaseModel, validator
from datetime import date

class BookingRequest(BaseModel):
    """Hotel booking request."""
    check_in: date
    check_out: date
    guests: int = Field(..., ge=1, le=10)

    @validator('check_out')
    def check_out_after_check_in(cls, v, values):
        """Ensure check-out is after check-in."""
        if 'check_in' in values and v <= values['check_in']:
            raise ValueError('Check-out must be after check-in')
        return v

    @validator('check_in')
    def check_in_not_in_past(cls, v):
        """Ensure check-in is not in the past."""
        if v < date.today():
            raise ValueError('Check-in date cannot be in the past')
        return v

@app.post("/bookings")
def create_booking(booking: BookingRequest):
    days = (booking.check_out - booking.check_in).days
    return {
        "message": "Booking created",
        "nights": days,
        "guests": booking.guests
    }
```

### Validator Features

```python
@validator('field_name')
def validate_field(cls, v):
    """Basic validator - receives field value."""
    if not is_valid(v):
        raise ValueError('Error message')
    return v  # Can transform the value

@validator('field2')
def validate_with_other_fields(cls, v, values):
    """Access other fields via 'values' dict."""
    if v < values.get('field1', 0):
        raise ValueError('field2 must be >= field1')
    return v

@validator('field3', pre=True)
def preprocess(cls, v):
    """Run before type conversion."""
    return v.strip() if isinstance(v, str) else v

@validator('field4', always=True)
def always_run(cls, v):
    """Run even if field is not provided."""
    return v or default_value()
```

### When to Use
✅ Cross-field validation
✅ Business logic validation
✅ Data transformation/normalization

---

## Pattern 5: List and Nested Validation

### Problem
You need to validate lists and nested data structures.

### Solution

```python
from typing import List
from pydantic import BaseModel, Field

class Item(BaseModel):
    """Individual item in an order."""
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=100)
    price: float = Field(..., gt=0)

class Order(BaseModel):
    """Order with multiple items."""
    customer_email: str
    items: List[Item] = Field(..., min_items=1, max_items=50)
    notes: Optional[str] = Field(None, max_length=500)

    @validator('items')
    def validate_total(cls, v):
        """Custom validation on the entire list."""
        total = sum(item.price * item.quantity for item in v)
        if total > 10_000:
            raise ValueError('Order total cannot exceed $10,000')
        return v

@app.post("/orders")
def create_order(order: Order):
    total = sum(item.price * item.quantity for item in order.items)
    return {
        "message": "Order created",
        "items_count": len(order.items),
        "total": total
    }
```

### Test It

```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customer_email": "customer@example.com",
    "items": [
      {"product_id": 1, "quantity": 2, "price": 19.99},
      {"product_id": 2, "quantity": 1, "price": 49.99}
    ]
  }'
```

### When to Use
✅ Shopping carts
✅ Batch operations
✅ Complex nested data

---

## Pattern 6: Optional and Default Values

### Problem
Some fields should be optional or have default values.

### Solution

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserProfile(BaseModel):
    """User profile with optional fields."""
    username: str  # Required
    email: str  # Required
    bio: Optional[str] = None  # Optional, defaults to None
    age: Optional[int] = Field(None, ge=13, le=120)  # Optional with validation
    notifications_enabled: bool = True  # Required, but has default
    theme: str = Field(default="light", regex=r'^(light|dark)$')

@app.put("/profile")
def update_profile(profile: UserProfile):
    return {"message": "Profile updated", "profile": profile}
```

### Usage

```bash
# Minimal request (only required fields)
curl -X PUT http://localhost:8000/profile \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com"}'

# Full request
curl -X PUT http://localhost:8000/profile \
  -H "Content-Type: application/json" \
  -d '{
    "username":"alice",
    "email":"alice@example.com",
    "bio":"Developer",
    "age":30,
    "theme":"dark"
  }'
```

### When to Use
✅ Update endpoints (partial updates)
✅ Configuration settings
✅ Fields with sensible defaults

---

## Pattern 7: Query Parameter Validation

### Problem
URL query parameters need validation too.

### Solution

```python
from fastapi import Query
from typing import Optional

@app.get("/search")
def search_items(
    q: str = Query(..., min_length=2, max_length=100),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort: str = Query(default="name", regex=r'^(name|price|date)$')
):
    """Search items with validated query parameters."""
    return {
        "query": q,
        "limit": limit,
        "offset": offset,
        "sort": sort
    }
```

### Test It

```bash
# Valid
curl "http://localhost:8000/search?q=laptop&limit=20&sort=price"

# Invalid (query too short)
curl "http://localhost:8000/search?q=a"

# Invalid (limit out of range)
curl "http://localhost:8000/search?q=laptop&limit=500"
```

### When to Use
✅ Search endpoints
✅ Pagination
✅ Filtering and sorting

---

## Pattern 8: Error Response Handling

### Problem
Validation errors should return helpful messages.

### Solution

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Custom validation error response."""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(x) for x in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation failed",
            "errors": errors
        }
    )
```

### Response Example

```json
{
  "detail": "Validation failed",
  "errors": [
    {
      "field": "body.email",
      "message": "Invalid email format",
      "type": "value_error"
    },
    {
      "field": "body.age",
      "message": "ensure this value is greater than or equal to 13",
      "type": "value_error.number.not_ge"
    }
  ]
}
```

---

## Validation Checklist

Before deploying, ensure you're validating:

- [ ] **All user inputs** (path params, query params, request body)
- [ ] **Data types** (string, int, email, URL, etc.)
- [ ] **Ranges** (min/max length, min/max value)
- [ ] **Formats** (email, phone, postal codes, etc.)
- [ ] **Business rules** (dates, relationships between fields)
- [ ] **Lists** (min/max items, item validation)
- [ ] **Optional fields** (with sensible defaults)

---

## Security Considerations

### SQL Injection Prevention

```python
# ✅ Good: Using Pydantic + ORMs
class SearchQuery(BaseModel):
    term: str = Field(..., max_length=100, regex=r'^[a-zA-Z0-9\s]+$')

@app.get("/search")
def search(query: SearchQuery):
    # Validated input is safe to use
    results = db.query(Item).filter(Item.name.contains(query.term))
    return results

# ❌ Bad: Raw user input in SQL
@app.get("/search")
def search(term: str):
    # NEVER DO THIS - vulnerable to SQL injection
    results = db.execute(f"SELECT * FROM items WHERE name LIKE '%{term}%'")
    return results
```

### XSS Prevention

```python
class Comment(BaseModel):
    """Comment with XSS protection."""
    text: str = Field(..., max_length=1000)

    @validator('text')
    def sanitize(cls, v):
        # Remove potentially dangerous content
        dangerous_patterns = ['<script', 'javascript:', 'onerror=']
        v_lower = v.lower()
        for pattern in dangerous_patterns:
            if pattern in v_lower:
                raise ValueError('Invalid content detected')
        return v
```

---

## Common Validation Patterns

### Email Validation

```python
from pydantic import BaseModel, EmailStr  # Requires: pip install email-validator

class UserEmail(BaseModel):
    email: EmailStr  # Validates email format
```

### URL Validation

```python
from pydantic import HttpUrl

class Website(BaseModel):
    url: HttpUrl  # Validates URL format
```

### Date Validation

```python
from datetime import date, datetime

class Event(BaseModel):
    event_date: date  # Automatically parses "2024-12-31"
    event_time: datetime  # Parses ISO datetime strings
```

---

## Testing Validation

```python
import pytest
from fastapi.testclient import TestClient

def test_valid_user():
    """Test that valid data is accepted."""
    response = client.post("/users", json={
        "username": "alice",
        "email": "alice@example.com",
        "age": 25
    })
    assert response.status_code == 200

def test_invalid_email():
    """Test that invalid email is rejected."""
    response = client.post("/users", json={
        "username": "bob",
        "email": "not-an-email",
        "age": 30
    })
    assert response.status_code == 422
    assert "email" in response.json()["detail"][0]["loc"]

def test_age_validation():
    """Test age range validation."""
    # Too young
    response = client.post("/users", json={
        "username": "charlie",
        "email": "charlie@example.com",
        "age": 10
    })
    assert response.status_code == 422

    # Too old
    response = client.post("/users", json={
        "username": "diana",
        "email": "diana@example.com",
        "age": 150
    })
    assert response.status_code == 422
```

---

## Quick Reference

| Validation Type | Pattern | Example |
|----------------|---------|---------|
| Range | `Field(ge=1, le=100)` | Age, quantity |
| Length | `Field(min_length=3)` | Username, password |
| Format | `Field(regex=r'^\d{3}$')` | Postal code, SKU |
| Email | `EmailStr` | Email addresses |
| URL | `HttpUrl` | Website URLs |
| Custom | `@validator` | Business rules |
| Optional | `Optional[str] = None` | Optional fields |
| List | `List[Item]` | Multiple items |

---

## Next Steps

**Test your validation:**
→ [Testing Patterns](../testing/)

**Secure your API:**
→ [Security Patterns](../security/)

**Build complete APIs:**
→ [API Basics](../api-basics/)

**Try the example:**
→ [Hello API Example](../../../examples/01-hello-api/)

---

**Remember: Validate early, validate always, and give helpful errors!** ✅
