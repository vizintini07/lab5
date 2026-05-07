import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_time_route(client):
    response = client.get('/time')
    # Проверяем, что сервер ответил успешно
    assert response.status_code == 200
    
    data = response.get_json()
    # Проверяем, что ключ "time" есть в ответе
    assert "time" in data
    # Проверяем, что время не равно 0
    assert data["time"] != 0

def test_metrics_route(client):
    # Делаем 3 запроса к /time
    client.get('/time')
    client.get('/time')
    client.get('/time')
    
    # Проверяем метрики
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['count'] == 3
