# Security Patterns

Learn how to protect your applications from common vulnerabilities.

## Why Security Matters

One vulnerability can:
- Leak user data
- Cost money
- Damage reputation
- Get you sued

**Security isn't optional!**

## Coming Soon

Comprehensive security patterns are being developed. For now:

## Essential Security Rules

### 1. Never Store Plain Passwords
```python
# ❌ BAD
password = "secret123"

# ✅ GOOD
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

### 2. Validate All Input
```python
# ❌ BAD
sql = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ GOOD
sql = "SELECT * FROM users WHERE id = ?"
cursor.execute(sql, (user_id,))
```

### 3. Use HTTPS
Always. No exceptions for production.

### 4. Keep Secrets Secret
```python
# ❌ BAD
API_KEY = "sk_live_abc123"  # in code

# ✅ GOOD
import os
API_KEY = os.getenv("API_KEY")  # from environment
```

## Get Help

Use AI for security reviews:
```
"Review this code for security vulnerabilities:
[paste your code]"
```

Claude is especially good at security reviews.

---

**Security first, features second!** 🔒
