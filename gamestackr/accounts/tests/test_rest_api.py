import pytest


@pytest.mark.django_db
def test_register_api_successfully(api_client):
    payload = {
        'username': 'JohnDoe',
        'email': 'johndoe@example.com',
        'password': 'password',
        'password_confirm': 'password',
    }
    response = api_client.post('/api/register/', payload)
    assert response.status_code == 201
    assert response.json() == {'message': 'User successfully created'}


def test_login_api_successfully(faker_account, api_client):
    payload = {
        'email': faker_account.email,
        'password': 'pass1234',
    }
    response = api_client.post('/api/login/', payload)
    assert response.status_code == 200
