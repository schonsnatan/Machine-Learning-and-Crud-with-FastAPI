from src.db.connection import PostgreSQLConnection
from src.models.user import UserCreate

db = PostgreSQLConnection(dbname="crud",
                          user = "postgres",
                          password="mypassword")

async def c_get_user(user_id: int):
    db.connect()
    user = db.select_user(f"SELECT * FROM users WHERE id = {user_id}")
    db.close()
    return user

async def c_create_user(user: UserCreate):
    db.connect()
    db.insert_user(user)
    db.close()
    return user

async def c_delete_user(user_id: int):
    db.connect()
    user = db.delete_user(user_id)
    db.close()
    return user

async def c_update_user(user_id: int, fields: dict):
    db.connect()
    user = db.update_user(user_id, fields)
    db.close()
    return user