from fastapi import FastAPI
from magnum import Magnum

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

handler = Magnum(app)
