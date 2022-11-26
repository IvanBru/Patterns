import datetime
class Task:
    last_change = None
    user_change = None
    last_status = None

    def __init__(self, name, assigned, status):
        self.name = name
        self.assigned = assigned
        self.status = status
        
    def change_status(self, status, responder):
        self.last_status = self.status
        self.status = status
        self.last_change = datetime.datetime.now()
        self.user_change = responder.name
        