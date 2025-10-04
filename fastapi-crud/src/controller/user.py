from src.db.connection import PostgreSQLConnection

db = PostgreSQLConnection(dbname="crud",
                          user = "postgres",
                          password="mypassword")

async def c_get_user(user_id: int):
    db.connect()
    user = db.select_user(f"SELECT * FROM users WHERE id = {user_id}")
    db.close()
    return user