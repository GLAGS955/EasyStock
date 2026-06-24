import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    r = await client.post("/api/v1/users/", json={
        "email": "test@example.com", "password": "pass123", "full_name": "Test"
    })
    assert r.status_code == 201
    assert r.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_login(client: AsyncClient):
    await client.post("/api/v1/users/", json={"email": "u@test.com", "password": "pass123"})
    r = await client.post("/api/v1/auth/login", data={"username": "u@test.com", "password": "pass123"})
    assert r.status_code == 200
    assert "access_token" in r.json()


@pytest.mark.asyncio
async def test_get_me(client: AsyncClient):
    await client.post("/api/v1/users/", json={"email": "me@test.com", "password": "pass123"})
    login = await client.post("/api/v1/auth/login", data={"username": "me@test.com", "password": "pass123"})
    token = login.json()["access_token"]
    r = await client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["email"] == "me@test.com"
