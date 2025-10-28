import pytest
from app import login

@pytest.mark.unit
def test_login_success(monkeypatch):
    monkeypatch.setenv("ADMIN_PASS", "secret123")
    assert login("admin@example.com", "secret123") is True