from abc import ABC, abstractmethod

class Factory(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def post(text):
        pass


class LinkedIn(Factory):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Login with username: {self.username}, password: {self.password}")
    
    def post(self, text):
        print(f"User: {self.username} post: {text}")
    
class Facebook(Factory):

    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def login(self):
        print(f"Login with email: {self.email}, password: {self.password}")
    
    def post(self, text):
        print(f"User: {self.email} post: {text}")

class Interface:
    
    def __init__(self, messager, login, password):
        if messager == "Facebook":
            self.messager = Facebook(login, password)
        elif messager == "LinkdIn":
            self.messager = LinkedIn(login, password)

    def login(self):
        self.messager.login()

    def post(self, text):
        self.messager.post(text)
            
