"""
Hello API - A beginner-friendly FastAPI example.

This simple API demonstrates:
- Basic GET endpoints
- Path parameters
- Input validation
- Error handling
- Logging
- Configuration management
"""

import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncIterator, Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# Configuration
class Config:
    """Application configuration."""
    MIN_ITEM_ID: int = 1
    MAX_ITEM_ID: int = 1000
    HOST: str = os.getenv("API_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("API_PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """
    Manage application lifespan events.

    This modern approach replaces the deprecated on_event decorators.
    """
    # Startup
    logger.info("Starting Hello API")
    logger.info(f"Item ID range: {Config.MIN_ITEM_ID} - {Config.MAX_ITEM_ID}")

    yield

    # Shutdown
    logger.info("Shutting down Hello API")


# Initialize FastAPI app with metadata
app = FastAPI(
    title="Hello API",
    description="A simple API for learning FastAPI basics",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/", tags=["General"])
def read_root() -> Dict[str, str]:
    """
    Root endpoint - returns a simple greeting.

    Returns:
        A welcome message
    """
    logger.info("Root endpoint accessed")
    return {"message": "Hello, World!"}


@app.get("/hello/{name}", tags=["Greetings"])
def greet_user(name: str) -> Dict[str, str]:
    """
    Greet a specific user by name.

    Args:
        name: The user's name

    Returns:
        A personalized greeting message
    """
    logger.info(f"Greeting user: {name}")
    return {"message": f"Hello, {name}!"}


def validate_item_id(item_id: int) -> None:
    """
    Validate that an item ID is within the allowed range.

    Args:
        item_id: The item ID to validate

    Raises:
        HTTPException: If item_id is out of valid range
    """
    if item_id < Config.MIN_ITEM_ID or item_id > Config.MAX_ITEM_ID:
        logger.warning(f"Invalid item ID requested: {item_id}")
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found. Valid range: {Config.MIN_ITEM_ID}-{Config.MAX_ITEM_ID}",
        )


@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int) -> Dict:
    """
    Get item information by ID.

    Args:
        item_id: The item's unique identifier (1-1000)

    Returns:
        Item details including ID, name, and description

    Raises:
        HTTPException: If item_id is out of valid range
    """
    validate_item_id(item_id)

    logger.info(f"Retrieving item: {item_id}")

    return {
        "item_id": item_id,
        "name": f"Item #{item_id}",
        "description": "This is a sample item",
        "in_stock": True,
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """
    Global exception handler for unexpected errors.

    This catches any unhandled exceptions and logs them.
    """
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


if __name__ == "__main__":
    import uvicorn

    logger.info(f"Starting server on {Config.HOST}:{Config.PORT}")
    logger.info(f"Access at: http://localhost:{Config.PORT}")
    logger.info(f"Interactive docs at: http://localhost:{Config.PORT}/docs")

    uvicorn.run(
        app,
        host=Config.HOST,
        port=Config.PORT,
        log_level=Config.LOG_LEVEL.lower(),
    )
