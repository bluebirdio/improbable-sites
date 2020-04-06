def path_delete(client, path):
    response = client.delete(path)
    assert response.status_code == 204

    response = client.get(path)
    assert response.status_code == 404
