import os
import sys
import platform
ops=platform.system()
try:
        import fbchat
except:
        os.system("pip install fbchat")
        import fbchat
if ops=="Windows":
        os.system("color 84")
elif ops=="Linux":
        os.system("setterm -foreground red -store")

if ops=="Windows":
        os.system("cls")
elif ops=="Linux":
        os.system("clear")
from fbchat import Client
from getpass import getpass
print(" _____   ____      ____    _       _   _   ____    _____   _____   ____")
print("|  ___| | __ )    | __ )  | |     | | | | / ___|  |_   _| | ____| |  _ \ ")
print("| |_    |  _ \    |  _ \  | |     | | | | \___ \    | |   |  _|   | |_) |")
print("|  _|   | |_) |   | |_) | | |___  | |_| |  ___) |   | |   | |___  |  _ <")
print("|_|     |____/    |____/  |_____|  \___/  |____/    |_|   |_____| |_| \_\ ")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("\n                         Author: Srijon Kumar                                   ")
#main
print("---You are using {} {}---\n".format(platform.system(),platform.release()))
print("1. Sent Messages")
print("2. Exit")
c=int(input(":~$ "))
if c==1:
        if ops=="Linux":
                username=raw_input("Your FB Username:~$ ")
        elif ops=="Windows":
                username=str(input("Your FB Username:~$ "))
        client=fbchat.Client(username,getpass())
        if ops=="Linux":
                name=raw_input("Victim Name:~$ ")
        elif ops=="Windows":
                name=str(input("Victim Name:~$ "))
        friends=client.searchForUsers(name)
        friend=friends[0]
        s=str(input("Enter Text You Want To Send:~$ "))
        ff=str(input("Want to send message with message number [Y/N]: "))
        if ff=="Y":
                for i in range(int(input("Number of messages:~$ "))):
                        msg="{} [{}]".format(s,i+1)
                        sent = client.send(fbchat.models.Message(msg),friend.uid)
                        if sent:
                                print("\n")
                                print("-------------------------------")
                                print("Successfully Sent",i+1,"no message")                
                
        else:        
                for i in range(int(input("Number of messages:~$ "))):
                        msg="{}".format(s)
                        sent = client.send(fbchat.models.Message(msg),friend.uid)
                        if sent:
                                print("\n")
                                print("-------------------------------")
                                print("Successfully Sent",i+1,"no message")

elif c==2:
        exit()
