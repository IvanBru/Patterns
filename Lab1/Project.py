from Task import *

class Project:
    Tasks = []
    Users = []

    def __init__(self, name, Project_Manager):
        self.name = name
        self.Project_Manager = Project_Manager

    def create_task(self, name, assigned, status):
        task = Task(name, assigned, status)
        message =  assigned.name + ", you have a new task " + task.name
        assigned.notifier(message)
        self.Tasks.append(task)
        return task

    def delete_task(self, task):
        self.Tasks.remove(task)

    def change_status(self, task, status, user):
        task.change_status(status, user)

    def add_user(self, user):
        self.Users.append(user)
        message = "User was added " + user.name 
        self.Project_Manager.notifier(message)

    def delete_user(self, user):
        self.Users.remove(user)

    def get_user_tasks(self, user):
        for task in self.Tasks:
            if task.assigned.name == user.name:
                print(task)
        
    

    