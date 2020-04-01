from fastapi.testclient import TestClient

from main import api

client = TestClient(api)


def path(action=""):
    prefix = "/v1/stacks/"
    return prefix + action


def test_stacks_get():
    response = client.get(path())
    assert response.status_code == 200


def test_stacks_crud():
    # CREATE a stack.
    response = client.post(path(), json={"name": "Test Python",})
    assert response.status_code == 201

    content = response.json()
    assert content["name"] == "Test Python"
    stack_id = content["id"]
    assert stack_id != ""

    # CREATE duplicate stack: should fail with 422.
    response = client.post(path(), json={"id": stack_id, "name": "Test Python",})
    assert response.status_code == 422

    # GET the new stack.
    response = client.get(path(stack_id))
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == "Test Python"

    # UPDATE stack.
    response = client.put(
        path(stack_id), json={"name": "Test Python", "description": "DESC"}
    )
    assert response.status_code == 200

    content = response.json()
    assert content["description"] == "DESC"

    # DELETE the stack.
    response = client.delete(path(stack_id))
    assert response.status_code == 204

    response = client.get(path(stack_id))
    assert response.status_code == 404
