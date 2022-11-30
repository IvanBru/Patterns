from adapter import *

class User:

    def __init__(self, adapter):
        self._adapter = adapter

    def send_message(self, *args):
        self._adapter.send(*args) 


adapterEmail = EMAILNotificationAdapter("ivam@gmail.com")
adapterSlack = SlackNotificationAdapter("asdga23r24tq")
adapterSMS = SMSNotificationAdapter("+3804730221")

user1 = User(adapterEmail)
user1.send_message("Lab5", "You've been done it!")

user2 = User(adapterSlack)
user2.send_message("ivantru", "34rdafad7fa3")

user3 = User(adapterSMS)
user3.send_message("Ivan")