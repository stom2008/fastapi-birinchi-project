
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "salom dunyo"}


@app.get("/about")
def about():
    return {"xabar": "men haqimda page"}


@app.get("/student/{name}/familya/{surname}")
def about(name: str, surname):
    return {"salom": name + " " + surname}


@app.get("/ikkinchi")
def ikkinchi(s, b):
    if b:
        return {"s": s, "b": b}
    return {"s": s}

