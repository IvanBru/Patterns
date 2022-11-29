from factory import *


User1_Interface = Interface("Facebook", "danbbo@gmail.com", "123456")
User2_Interface = Interface("LinkdIn", "ivanka", "5464322!")

print("------------")
User1_Interface.login()
User1_Interface.post("My first post on Facebook")

print("------------\n")
User2_Interface.login()
User2_Interface.post("My first Post on LinkdIn")
print("------------\n")
