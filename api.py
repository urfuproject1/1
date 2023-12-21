from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from io import BytesIO
from PIL import Image
import requests

class Item(BaseModel):
    url: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    response = requests.get(item.url)
    image = Image.open(BytesIO(response.content))
    classifier = pipeline("image-classification", model="Poliandr/moscow-attractions")
    result = max(classifier(image), key=lambda x: x['score'])
    return result

