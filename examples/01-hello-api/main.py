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
    # Run the application
    # Access at: http://localhost:8000
    # Interactive docs at: http://localhost:8000/docs
    uvicorn.run(app, host="0.0.0.0", port=8000)
