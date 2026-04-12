from playwright.sync_api import Page, Route
import json


def test_mocked_user_list(page: Page):

    fake_response = {
        "page": 1,
        "data": [
            {"id": 1, "first_name": "Alice", "email": "alice@test.com"},
            {"id": 2, "first_name": "Bob", "email": "bob@test.com"},
        ]
    }

    def handle_route(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(fake_response)
        )

    page.route("**/api/users**", handle_route)

    page.goto("https://reqres.in/api/users")

    # Read what the browser received (the mocked response)
    content = page.content()
    assert "Alice" in content
    assert "bob@test.com" in content

def test_server_returns_empty_list(page: Page):

    def handle_route(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({"data": []})
        )

    page.route("**/api/users**", handle_route)
    page.goto("https://reqres.in/api/users")

    content = page.content()
    assert "Alice" not in content
    assert "[]" in content or "data" in content


def test_server_returns_error(page: Page):

    def handle_route(route: Route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body=json.dumps({"error": "Internal Server Error"})
        )

    page.route("**/api/users**", handle_route)
    response = page.goto("https://reqres.in/api/users")

    assert response.status == 500

def test_server_returns_unauthorized(page: Page):

    def handle_route(route: Route):
        route.fulfill(
            status = 401,
            content_type="application/json",
            body=json.dumps({"error": "Unauthorized"})
        )

    page.route("**/api/users**", handle_route)
    response = page.goto("https://reqres.in/api/users")

    assert response.status == 401