from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_read_predict_positive():
    response = client.post("/predict/",
        json={"url":"https://huggingface.co/Poliandr/moscow-attractions/resolve/main/images/Bolshoi_Theatre.jpg"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'Bolshoi Theatre'
