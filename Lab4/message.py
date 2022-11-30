from abc import ABC, abstractmethod

class Notification(ABC):
    
    def send(self, title, message):
        pass

class EmailNotification(Notification):

    __admin_email = None

    def __init__(self, admin_email):
        self.__admin_email = admin_email

    def send(self, title, message):
        print(f"Send Email with title: {title} to {self.__admin_email} with message: {message}")

class SlackNotifications(Notification):

    __chat_id = None

    def __init__(self, chat_id):
        self.__chat_id = chat_id

    def send_slack(self, login, apiKey):
        print(f"Send message into Slack chat with id: {self.__chat_id}, login: {login}, apiKey: {apiKey}")


class SMSNotifications(Notification):

    __phone = None

    def __init__(self, phone):
        self.__phone = phone

    def send_sms(self, sender):
        print(f"Send SMS from: {sender} to number: {self.__phone}")