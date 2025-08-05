import pytest
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_sum():
    resp = client.post("/tool", json={"tool": "sum", "a": 3, "b": 2})
    assert resp.status_code == 200
    assert resp.json()["result"] == 5

def test_divide():
    resp = client.post("/tool", json={"tool": "divide", "a": 10, "b": 5})
    assert resp.status_code == 200
    assert resp.json()["result"] == 2

def test_divide_by_zero():
    resp = client.post("/tool", json={"tool": "divide", "a": 10, "b": 0})
    assert resp.status_code == 400
    assert "Division by zero" in resp.json()["detail"]

def test_invalid_tool():
    resp = client.post("/tool", json={"tool": "invalid", "a": 1, "b": 2})
    assert resp.status_code == 400
    assert "Tool not found" in resp.json()["detail"]
