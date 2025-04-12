from flask import request
import pytest
from app import create_app, db
@pytest.fixture
def client():
    app = create_app("testing")
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()
        
def test_insert_data(client):
    payload = {'id':999,'name':'Jose'}
    response = client.post("/data", json=payload)
    assert response.status_code == 200
    assert response.json["message"] == "Data inserted successfully"


def test_get_data(client):
    response = client.get("/data")
    assert response.status_code == 200

def test_delete_data(client):
    client.post("/data", json={"name": "Aux"})
    response = client.delete("/data/1")
    assert response.status_code == 200
    assert response.json["message"] == "Data deleted successfully"
