from fastapi.testclient import TestClient
import pytest

from hw_task_users import app, User, fake_db as init_db

client = TestClient(app)

print(init_db)

def test_create_user():
    new_user = {"name": "Test User", "email": "test@gmail.com", "password": "123test"} 
    response = client.post(
        "/users/",
        json=new_user,
    )
    assert response.status_code == 200
    print(f"Response: {response.json()}")
    assert response.json() == {'id': 11, 'name': 'Test User', 'email': 'test@gmail.com'}

if __name__ == '__main__':
    pytest.main(args=[__file__])