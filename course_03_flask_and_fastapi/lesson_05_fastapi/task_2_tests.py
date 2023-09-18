from fastapi.testclient import TestClient
import pytest

from task_2_movies import app, Movie, fake_db as init_db

client = TestClient(app)

print(init_db)

def test_create_movie():
    new_movie = {"title": "Movie 4", "description": "Descr 4", "genre": "action"} 
    response = client.post(
        "/movies/",
        json=new_movie,
    )
    assert response.status_code == 200
    print(f"Response: {response.json()}")
    assert response.json() == {'id': 4, 'title': 'Movie 4', 'description': 'Descr 4', 'genre': 'action'}

if __name__ == '__main__':
    pytest.main(args=[__file__])