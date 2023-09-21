from fastapi.testclient import TestClient
import pytest
from init_fake_db import init_fake_db

from main import app

client = TestClient(app)

def test_create_users():
    response = client.post(
        "users/fake_users/5"
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'message': f'5 fake users created'}

def test_create_user():
    new_user = {"username": "New user", "email": "new@mail.ru", "password": "123456"} 
    response = client.post(
        "users/",
        json=new_user,
    )
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"username": "New user", "email": "new@mail.ru", 'id': 6}
 
def test_create_user_incorrect():
    new_user = {"username": "New user", "email": "new@mail.ru", "password": "123"} 
    response = client.post(
        "users/",
        json=new_user,
    )
    #print(f"Response: {response.json()}")
    assert response.status_code == 422
       
def test_edit_user():
    edited_user = {"username": "Changed user", "email": "changed@mail.ru", "password": "changed_pass"} 
    response = client.put(
        "/users/2",
        json=edited_user,
    )    
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"username": "Changed user", "email": "changed@mail.ru", 'id': 2}
 
def test_delete_user():
    response = client.delete(
        "/users/3",
    )
    assert response.status_code == 200
    assert response.json() == {'message': f'User 3 deleted'}


def test_delete_user_not_exist():
    response = client.delete(
        "/users/19",
    )
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main(args=[__file__])
