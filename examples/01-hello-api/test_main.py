"""
Tests for the Hello API example.

This demonstrates basic API testing patterns using pytest and FastAPI's TestClient.
"""

import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)


class TestRootEndpoint:
    """Tests for the root '/' endpoint."""

    def test_root_returns_200(self):
        """Root endpoint should return 200 status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_json(self):
        """Root endpoint should return JSON content."""
        response = client.get("/")
        assert response.headers["content-type"] == "application/json"

    def test_root_message_content(self):
        """Root endpoint should return correct message."""
        response = client.get("/")
        data = response.json()
        assert "message" in data
        assert data["message"] == "Hello, World!"


class TestGreetingEndpoint:
    """Tests for the '/hello/{name}' endpoint."""

    def test_greet_user_returns_200(self):
        """Greeting endpoint should return 200 status code."""
        response = client.get("/hello/Alice")
        assert response.status_code == 200

    def test_greet_user_with_name(self):
        """Greeting endpoint should personalize message."""
        response = client.get("/hello/Alice")
        data = response.json()
        assert data["message"] == "Hello, Alice!"

    def test_greet_user_different_names(self):
        """Greeting should work with different names."""
        names = ["Bob", "Charlie", "Diana"]
        for name in names:
            response = client.get(f"/hello/{name}")
            data = response.json()
            assert data["message"] == f"Hello, {name}!"

    def test_greet_with_special_characters(self):
        """Greeting should handle names with special characters."""
        # URL encoding is handled automatically by TestClient
        response = client.get("/hello/José")
        assert response.status_code == 200
        data = response.json()
        assert "José" in data["message"]

    def test_greet_with_numbers(self):
        """Greeting should handle names containing numbers."""
        response = client.get("/hello/User123")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Hello, User123!"


class TestItemsEndpoint:
    """Tests for the '/items/{item_id}' endpoint."""

    def test_get_valid_item(self):
        """Getting a valid item should return 200."""
        response = client.get("/items/1")
        assert response.status_code == 200

    def test_item_response_structure(self):
        """Item response should have correct structure."""
        response = client.get("/items/42")
        data = response.json()

        # Check all required fields are present
        assert "item_id" in data
        assert "name" in data
        assert "description" in data
        assert "in_stock" in data

    def test_item_id_matches_request(self):
        """Returned item_id should match the requested ID."""
        item_id = 123
        response = client.get(f"/items/{item_id}")
        data = response.json()
        assert data["item_id"] == item_id

    def test_item_boundary_lower(self):
        """Item ID at lower boundary (1) should work."""
        response = client.get("/items/1")
        assert response.status_code == 200
        data = response.json()
        assert data["item_id"] == 1

    def test_item_boundary_upper(self):
        """Item ID at upper boundary (1000) should work."""
        response = client.get("/items/1000")
        assert response.status_code == 200
        data = response.json()
        assert data["item_id"] == 1000

    def test_item_id_too_low(self):
        """Item ID below range should return 404."""
        response = client.get("/items/0")
        assert response.status_code == 404

    def test_item_id_negative(self):
        """Negative item ID should return 404."""
        response = client.get("/items/-1")
        assert response.status_code == 404

    def test_item_id_too_high(self):
        """Item ID above range should return 404."""
        response = client.get("/items/1001")
        assert response.status_code == 404

    def test_item_error_response_structure(self):
        """Error response should have correct structure."""
        response = client.get("/items/9999")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
        assert "9999" in data["detail"]

    def test_item_not_found_message(self):
        """404 response should include the requested ID."""
        response = client.get("/items/5000")
        data = response.json()
        assert "5000" in data["detail"]

    def test_item_invalid_type(self):
        """Non-integer item ID should return 422 validation error."""
        response = client.get("/items/abc")
        assert response.status_code == 422  # Validation error


class TestAPIDocumentation:
    """Tests for automatically generated API documentation."""

    def test_openapi_docs_available(self):
        """OpenAPI documentation should be accessible."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_openapi_json_available(self):
        """OpenAPI JSON schema should be accessible."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert "paths" in data


class TestEdgeCases:
    """Tests for edge cases and potential issues."""

    def test_nonexistent_endpoint(self):
        """Non-existent endpoints should return 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    def test_wrong_http_method(self):
        """Wrong HTTP method should return 405."""
        response = client.post("/")  # Root only supports GET
        assert response.status_code == 405

    def test_empty_name_parameter(self):
        """Empty name parameter should still work (FastAPI behavior)."""
        # FastAPI allows empty path parameters
        response = client.get("/hello/")
        # This will actually hit a different endpoint or 404
        # depending on trailing slash configuration
        assert response.status_code in [200, 404]

    def test_very_long_name(self):
        """Very long names should be handled."""
        long_name = "A" * 1000
        response = client.get(f"/hello/{long_name}")
        assert response.status_code == 200
        data = response.json()
        assert long_name in data["message"]


# Pytest fixtures for advanced test scenarios
@pytest.fixture
def valid_item_ids():
    """Fixture providing a list of valid item IDs."""
    return [1, 50, 100, 500, 1000]


@pytest.fixture
def invalid_item_ids():
    """Fixture providing a list of invalid item IDs."""
    return [0, -1, -100, 1001, 10000]


class TestWithFixtures:
    """Tests demonstrating the use of pytest fixtures."""

    def test_multiple_valid_items(self, valid_item_ids):
        """All valid item IDs should return 200."""
        for item_id in valid_item_ids:
            response = client.get(f"/items/{item_id}")
            assert response.status_code == 200

    def test_multiple_invalid_items(self, invalid_item_ids):
        """All invalid item IDs should return 404."""
        for item_id in invalid_item_ids:
            response = client.get(f"/items/{item_id}")
            assert response.status_code == 404


if __name__ == "__main__":
    # Allow running tests directly with: python test_main.py
    pytest.main([__file__, "-v"])
