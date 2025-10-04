from fastapi import FastAPI, HTTPException
from src.models.user import User
from src.controller.user import c_get_user

app = FastAPI()

@app.get("/users/{user_id}")
async def get_users(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@app.post("/users")
async def create_user(user: User):
    print("post")
    return 

@app.delete("/users")
async def delete_user(user_id: int):
    print("delete")
    return 

@app.put("/users{user_id}")
async def update_user(user_id: int, user: User):
    print("update")
    return