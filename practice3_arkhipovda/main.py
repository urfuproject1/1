from fastapi import FastAPI
from pydantic import BaseModel
from model import load_model


class Req(BaseModel):
    url: str


app = FastAPI()
image_to_text = load_model()


@app.get("/")
def root():
    return {'message': 'День добрый'}


@app.post("/predict/")
async def predict(req: Req):
    return await image_to_text(req.url)