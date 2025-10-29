import pytest
from app import register, login
from unittest.mock import patch

@pytest.mark.integration
def test_register_then_login(monkeypatch):
    monkeypatch.setenv("ADMIN_PASS", "123")
    register("admin@example.com", "123")
    assert login("admin@example.com", "123") is True
