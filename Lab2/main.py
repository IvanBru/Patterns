from User import *
from singleton import *


connection_s3 = ConnectionS3()
connection_file_system = ConnectionFileSystem()

user1 = User("Ivan", connection_s3)
user2 = User("Danylo", connection_s3)

user3 = User("Kiril", connection_file_system)
user4 = User("Vasya", connection_file_system)

print("Connect to S3 Example:\n")
user1.get_connection()
user2.get_connection()

print("Connect to File System Example:\n")
user3.get_connection()
user4.get_connection()

