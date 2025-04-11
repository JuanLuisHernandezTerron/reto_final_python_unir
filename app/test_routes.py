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
    assert response.status_code == 201
    assert response.json["message"] == "Data created"
