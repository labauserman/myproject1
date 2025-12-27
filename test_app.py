import requests
import pytest

# 1. Arrange: Define the URL we want to test
TEST_URL = "https://api.github.com/zen"

def test_github_api_status_code():
    """Test that the GitHub Zen API is reachable."""
    # 2. Act: Perform the action
    response = requests.get(TEST_URL)
    
    # 3. Assert: Check if the result is what we expected
    assert response.status_code == 200

def test_github_api_returns_text():
    """Test that the API actually returns a string of text."""
    response = requests.get(TEST_URL)
    
    # Assert that the content is a string and not empty
    assert isinstance(response.text, str)
    assert len(response.text) > 0

    