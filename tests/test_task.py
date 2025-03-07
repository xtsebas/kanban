from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Nueva tarea", "description": "Descripción"})
    assert response.status_code == 200
    assert response.json()["title"] == "Nueva tarea"
