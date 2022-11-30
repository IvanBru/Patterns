from message import *

class SlackNotificationAdapter(Notification):

    def __init__(self, chat_id):
        self.class_Slack = SlackNotifications(chat_id)

    def send(self, login, apiKey):
        self.class_Slack.send_slack(login, apiKey)


class SMSNotificationAdapter(Notification):

    def __init__(self, phone):
        self.class_SMS = SMSNotifications(phone)

    def send(self, sender):
        self.class_SMS.send_sms(sender)

class EMAILNotificationAdapter(Notification):

    def __init__(self, admin_email):
        self.class_EMAIL = EmailNotification(admin_email)

    def send(self, title, message):
        self.class_EMAIL.send(title, message)



