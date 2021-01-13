from main import app
from json import loads


def test_catch_pages():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_api():
    response = app.test_client().get('/api/call')
    assert response.status_code == 200
    assert loads(response.data) == {'request': 'get'}

    response = app.test_client().post('/api/call')
    assert response.status_code == 200
    assert loads(response.data) == {'request': 'post'}
