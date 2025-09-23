from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/recursos")
def generate_random_number():
    num = random.randint(1,10)
    print(num)
    return num