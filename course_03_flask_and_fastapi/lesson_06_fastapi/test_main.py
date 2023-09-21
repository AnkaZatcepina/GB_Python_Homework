from fastapi.testclient import TestClient
import pytest
from init_fake_db import init_fake_db
from models.order import Status as OrderStatus

from main import app
import datetime

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

def test_create_fake_products():
    response = client.post(
        "/products/fake_products/7"
    )
    assert response.status_code == 200
    assert response.json() == {'message': f'7 fake products created'}

def test_create_product():
    new_product = {"name": "New", "description": "Descr", "price": 50} 
    response = client.post(
        "products/",
        json=new_product,
    )
    assert response.status_code == 200
    assert response.json() == {"name": "New", "description": "Descr", "price": 50, 'id': 8}

def test_edit_product():
    edited_product = {"name": "Edited", "description": "Edited", "price": 5000}  
    response = client.put(
        "/products/2",
        json=edited_product,
    )    
    assert response.status_code == 200
    assert response.json() == {"name": "Edited", "description": "Edited", "price": 5000, 'id': 2}
 
def test_delete_product():
    response = client.delete(
        "/products/3",
    )
    assert response.status_code == 200
    assert response.json() == {'message': f'Product 3 deleted'}

def test_create_fake_orders():
    response = client.post(
        "orders/fake_orders/7"
    )
    assert response.status_code == 200
    assert response.json() == {'message': f'7 fake orders created'}

def test_create_order():
    new_order = {"user_id": 2, 
                "product_id": 1, 
                "order_date": str(datetime.date(2000, 1, 1)), 
                "status": OrderStatus.SHIPPED.value} 
    response = client.post(
        "orders/",
        json=new_order,
    )
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"user_id": 2, 
                                "product_id": 1, 
                                "order_date": '2000-01-01', 
                                "status": 'shipped',
                                "id": 8}

def test_edit_order():
    edited_order = {"user_id": 1, 
                    "product_id": 1, 
                    "order_date": str(datetime.date(2022, 2, 2)), 
                    "status": OrderStatus.PAID.value}  
    response = client.put(
        "/orders/3",
        json=edited_order,
    )    
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1, 
        "product_id": 1, 
        "order_date": '2022-02-02', 
        "status": "paid",
        'id': 3}
 
def test_delete_order():
    response = client.delete(
        "/orders/5",
    )
    assert response.status_code == 200
    assert response.json() == {'message': f'Order 5 deleted'}

if __name__ == '__main__':
    pytest.main(args=[__file__])
