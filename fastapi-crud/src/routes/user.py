from fastapi import FastAPI, HTTPException
from src.models.user import UserCreate, UserUpdate
from src.controller.user import c_create_user, c_delete_user, c_get_user, c_update_user

app = FastAPI()

@app.get("/users/{user_id}")
async def get_users(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user

@app.post("/users")
async def create_user(user: UserCreate):
    db_user = await c_get_user(user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="The user already exists.")
    user = await c_create_user(user)
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    await c_delete_user(user_id)
    return {"message:" "user deleted"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    
    update_fields = user.dict(exclude_unset=True)
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    result = await c_update_user(user_id, update_fields)
    if result is None:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    return {"message:" "user updated"}