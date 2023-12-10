from fastapi.testclient import TestClient
from practice3_arkhipovda.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'День добрый'}


def test_predict():
    response = client.post(
        "/predict/",
        json={"url": "https://w.forfun.com/fetch/ac/ac4ab3ca5717e7787567def744601ce6.jpeg?w=1200&r=0.5625"})
    text = response.text
    assert response.status_code == 200
    assert isinstance(text, str)