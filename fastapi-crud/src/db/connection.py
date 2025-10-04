import psycopg2

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

    def insert_user():
        pass

    def delete_user():
        pass

    def update_user():
        pass

    def close(self):
        if self.conn:
            self.conn.close()
            print("connection closed")