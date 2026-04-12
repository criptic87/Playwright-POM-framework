import pytest
from playwright.sync_api import Playwright

""""
def test_get_single_user(playwright):
    request_context = playwright.request.new_context(
        base_url="https://reqres.in",
        extra_http_headers={"x-api-key": "reqres-free-v1"}
    )

    response = request_context.get("/api/users/2")
    print(f"Status: {response.status}")
    print(f"Body: {response.text()}")

    assert response.status == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "email" in data["data"]

    request_context.dispose()
"""
@pytest.fixture
def api_context(playwright: Playwright):
    """Reusable API context for all tests in this file."""
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield context
    context.dispose()


def test_get_single_user(api_context):
    response = api_context.get("/users/2")

    assert response.status == 200
    data = response.json()
    assert data["id"] == 2
    assert "email" in data
    assert "name" in data


def test_get_all_users(api_context):
    response = api_context.get("/users")

    assert response.status == 200
    users = response.json()
    assert len(users) == 10
    assert users[0]["id"] == 1

def test_create_user(api_context):
    """POST — create a new resource."""
    response = api_context.post("/users", data={
        "name": "Andrei",
        "job": "QA Automation Engineer"
    })

    assert response.status == 201    # 201 = Created
    data = response.json()
    assert data["name"] == "Andrei"
    assert data["job"] == "QA Automation Engineer"
    assert "id" in data              # server assigns an ID


def test_update_user(api_context):
    """PUT — replace an existing resource."""
    response = api_context.put("/users/2", data={
        "name": "Andrei Updated",
        "job": "Senior QA Engineer"
    })

    assert response.status == 200
    data = response.json()
    assert data["name"] == "Andrei Updated"
    assert data["job"] == "Senior QA Engineer"


def test_delete_user(api_context):
    """DELETE — remove a resource."""
    response = api_context.delete("/users/2")

    assert response.status == 200

def test_get_nonexistent_user(api_context):
    response = api_context.get("/users/9999")

    assert response.status == 404

@pytest.mark.parametrize("user_id",(1,2,3,4,5))
def test_get_specific_user(api_context, user_id):
    """GET with parametrized test"""
    response = api_context.get(f"/users/{user_id}")

    assert response.status == 200
    users = response.json()
    assert users["id"] == user_id

