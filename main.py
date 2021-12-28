from fastapi import FastAPI
from fanfic_generator import FanficGenerator

fanfic_generator = FanficGenerator()
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fanfic")
def generate_fanfic():
    return {"text": fanfic_generator.generate()}
