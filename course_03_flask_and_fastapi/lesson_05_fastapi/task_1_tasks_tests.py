from fastapi.testclient import TestClient
import pytest

from task_1_tasks import app, Task
from task_1_tasks import fake_db as init_db

client = TestClient(app)

print(init_db)


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    print(f"Tasks: {response.json()}")
    assert response.json() == [{'id': 1, 'title': 'Title 1', 'description': 'Descr 1', 'status': 'Created'}]

def test_create_task():
    new_task = {"title": "Title 2", "description": "Descr 2", "status": "Not done yet..."} 
    response = client.post(
        "/tasks/",
        json=new_task,
    )
    assert response.status_code == 200
    print(f"Response: {response.json()}")
    assert response.json() == [
        {'id': 1, 'title': 'Title 1', 'description': 'Descr 1', 'status': 'Created'}, 
        {'id': 2, 'title': 'Title 2', 'description': 'Descr 2', 'status': 'Not done yet...'}
    ]

def test_edit_task():
    edited_task = {"title": "Title Item 1 (Updated)", "description": "New description", "status": "Done"} 
    response = client.put(
        "/tasks/?task_id=1",
        json=edited_task,
    )
    assert response.status_code == 200
    print(f"Response: {response.json()}")
    assert response.json() == {
        "id": 1,
        **edited_task
    }

def test_edit_task_not_exist():
    edited_task = {"title": "Title Item 1 (Updated)", "description": "New description", "status": "Done"} 
    response = client.put(
        "/tasks/?task_id=5",
        json=edited_task,
    )
    assert response.status_code == 404

def test_delete_task():
    response = client.delete(
        "/tasks/?task_id=2",
    )
    assert response.status_code == 200
    print(f"Response: {response.json()}")
    assert response.json() == {"message": f"Task 2 was deleted"}

def test_delete_task_not_exist():
    response = client.delete(
        "/tasks/?task_id=5",
    )
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main(args=[__file__])