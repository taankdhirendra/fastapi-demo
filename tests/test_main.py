from fastapi.testclient import TestClient
from app.main import app, students

client = TestClient(app)

def setup_function():
    students.clear()
    students.update({
        1: {"id": 1, "name": "Rahul", "age": 20},
        2: {"id": 2, "name": "Amit", "age": 22}
    })

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Student Management API"

def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_student():
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Rahul"

def test_create_student():
    response = client.post(
        "/students",
        json={"name": "Vikas", "age": 23}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Vikas"

def test_update_student():
    response = client.put(
        "/students/1",
        json={"name": "Raj", "age": 25}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Raj"

def test_delete_student():
    response = client.delete("/students/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"

def test_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404