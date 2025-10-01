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
            print()

    def select_user():
        pass

    def insert_user():
        pass

    def delete_user():
        pass

    def update_user():
        pass

    def close():
        pass