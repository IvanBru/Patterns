from Project import Project
from Task import *
from User import *

PM = Project_Manager("Ivan")
Project_Test = Project("NoSQL", PM)

Developer1 = Developer("Danylo", "Developer")
Developer2 = Developer("Kirilo", "QC")

Project_Test.add_user(Developer1)
Project_Test.add_user(Developer2)


Project_Test.create_task("Lab 1", Project_Test.Users[0], "To Do")
Project_Test.create_task("Lab 2", Project_Test.Users[1], "To Do")


Project_Test.change_status(Project_Test.Tasks[0], "In Progress", Project_Test.Users[0])

message = f"User {Project_Test.Tasks[0].user_change} change status from {Project_Test.Tasks[0].last_status} to {Project_Test.Tasks[0].status} at {Project_Test.Tasks[0].last_change}"
print(message)














