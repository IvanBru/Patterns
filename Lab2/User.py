from singleton import *
class User:
    def __init__(self, username, connection):
        self.username = username
        self.connection = connection

    def get_connection(self):
        self.connection.get_connection()
        print("id:", self.connection)
        print(f"{self.username} connect to {self.connection.connect}")
        