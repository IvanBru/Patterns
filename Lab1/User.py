from abc import abstractmethod
class User:
    def __init__(self, name):
        pass
    
    @abstractmethod
    def notiffier(self, message):
        pass

class Project_Manager(User):
    def __init__(self, name):
        self.name = name

    def notifier(self, message):
        print(f"PM: {message}")


class Developer(User):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def notifier(self, message):
        print(f"Developer: {message}")

    
