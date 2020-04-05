import pytest


def path(action=""):
    prefix = "/v1/stacks/"
    return prefix + action


def test_stacks_get(client):
    response = client.get(path())
    assert response.status_code == 200


def test_stacks_crud(client):
    # CREATE a stack.
    response = client.post(path(), json={"name": "Test Python"})
    assert response.status_code == 201

    content = response.json()
    assert content["name"] == "Test Python"
    stack_id = content["id"]
    assert stack_id != ""

    # CREATE duplicate stack: should fail with 422.
    response = client.post(path(), json={"id": stack_id, "name": "Test Python"})
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

    # CREATE derivative stack with incorrect stack id.
    response = client.post(
        path(), json={"parent_stack_id": "invalid", "name": "Test FastAPI"}
    )
    assert response.status_code == 422

    # CREATE derivative stack with correct stack id.
    response = client.post(
        path(), json={"parent_stack_id": stack_id, "name": "Test FastAPI"}
    )
    assert response.status_code == 201
    child_stack_id = response.json()["id"]
    assert child_stack_id != ""

    # DELETE the original stack: should fail because it has a derivative.
    response = client.delete(path(stack_id))
    assert response.status_code == 422

    # DELETE the derivative first
    response = client.delete(path(child_stack_id))
    assert response.status_code == 204

    response = client.get(path(child_stack_id))
    assert response.status_code == 404

    # DELETE the original now that it has no dependency
    response = client.delete(path(stack_id))
    assert response.status_code == 204

    response = client.get(path(stack_id))
    assert response.status_code == 404
