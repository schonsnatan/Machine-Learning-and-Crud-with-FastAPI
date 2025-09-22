from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/outro-recurso")
def pegar_recurso():
    return "message"

@app.post("/outro-recurso/{id}")
def criar_recurso():
    return {"message": id}