from flask import request
def test_insert_data():
    payload = request.get_json()
    response = client.post("/data", json=payload)
    assert response.status_code == 201
    assert response.json["message"] == "Data created"

