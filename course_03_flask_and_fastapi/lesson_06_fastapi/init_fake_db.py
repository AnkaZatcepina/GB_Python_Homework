import requests

def init_fake_db():
    requests.post('http://127.0.0.1:8000/users/fake_users/5')

if __name__ == '__main__':
    init_fake_db()