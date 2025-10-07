import psycopg2
from src.models.user import UserCreate

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host='localhost',port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname = self.dbname, 
                                         user=self.user, 
                                         password = self.password, 
                                         host = self.host, 
                                         port = self.port)
            print("Connected successfully")
        except psycopg2.Error as e:
            print("Error connecting to Postgres:", e)

    def select_user(self, query):
        if not self.conn:
            print("You are not connected to the db.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            print("Erorr executing the query: ", e)
            return None

    def insert_user(self, user: UserCreate):
        if not self.conn:
            print("You are not connected to the db.")
            None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (id, name, area, job_description, role, salary, is_active, last_evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (user.id, user.name, user.area, user.job_description, user.role, user.salary, user.is_active, user.last_evaluation)
            )
            self.conn.commit()
            cursor.close()
            print("User registered")
        except psycopg2.Error as e:
            print("It was not possible to register the user: ", e)

    def delete_user(self, user_id: int):
        if not self.conn:
            print("You are not connected to the db.")
            None
        try:
           cursor = self.conn.cursor()
           cursor.execute(
               "DELETE FROM users WHERE id = %s", 
               (user_id,)
           )
           self.conn.commit()
           cursor.close()
           print(f"User {user_id} deleted")
           return user_id
        except psycopg2.Error as e:
            print("It was not possible to delete the user: ", e) 
            return None

    def update_user(self, user_id: int, fields: dict):
        if not self.conn:
            print("You are not connected to the db.")
            return None
        try:
            set_parts = []
            values = []
            for key, value in fields.items():
                if value is None:
                    continue
                set_parts.append(f"{key} = %s")
                values.append(value)

            if not set_parts:
                print("No valid fields to update")
                return None
            
            query = f"UPDATE users SET {', '.join(set_parts)} WHERE id = %s"
            values.append(user_id)

            cursor = self.conn.cursor()
            cursor.execute(query, tuple(values))
            self.conn.commit()
            self.conn.close()
            print("User updated")
            return user_id
        except psycopg2.Error as e:
            print("It was not possible to update the user: ", e) 
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("connection closed")