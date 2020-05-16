import os
import sys
import platform
ops=platform.system()
try:
        import fbchat
except:
        if ops=="Linux":
                os.system("pip3 install fbchat")
        elif ops=="Windows":
                os.system("pip install fbchat")
        import fbchat
from fbchat.models import *
from fbchat import Client
from getpass import getpass
if ops=="Windows":
        os.system("color 84")
elif ops=="Linux":
        os.system("setterm -foreground red -store")
A=[]
while True:
        if ops=="Windows":
                os.system("cls")
        elif ops=="Linux":
                os.system("clear")

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
                if len(A)==0:
                        username=str(input("Your FB Username:~$ "))
                        password=getpass()
                        A.append(username)
                        A.append(password)

                else:
                        username=A[0]
                        password=A[1]
                """
                client=fbchat.Client(username,password)
                x=client.searchForUsers("")
                f=x[0]
                client.send(fbchat.models.Message(),f.uid )
                """
                ty=str(input("Want to message a group or user? [G/U]: "))
                if ty=="U":
                        name=str(input("Victim Name:~$ "))
                        friends=client.searchForUsers(name)
                        friend=friends[0]
                elif ty=="G":
                        name=str(input("Victim Group Name:~$ "))
                        friends=client.searchForGroups(name)
                        friendg=friends[0]
                s=str(input("Enter Text You Want To Send:~$ "))
                ff=str(input("Want to send message with message number [Y/N]: "))
                if ff=="Y":
                        for i in range(int(input("Number of messages:~$ "))):
                                msg="{} [{}]".format(s,i+1)
                                if ty=="U":
                                        sent = client.send(fbchat.models.Message(msg),friend.uid )
                                elif ty=="G":
                                        sent = client.send(Message(text=msg), thread_id=friendg.uid, thread_type=ThreadType.GROUP)
                                if sent:
                                        print("\n")
                                        print("-------------------------------")
                                        print("Successfully Sent",i+1,"no message")                
                        
                else:        
                        for i in range(int(input("Number of messages:~$ "))):
                                msg="{}".format(s)
                                if ty=="U":
                                        sent = client.send(fbchat.models.Message(msg),friend.uid )
                                elif ty=="G":
                                        sent = client.send(Message(text=msg), thread_id=friendg.uid, thread_type=ThreadType.GROUP)
                                if sent:
                                        print("\n")
                                        print("-------------------------------")
                                        print("Successfully Sent",i+1,"no message")
                print("\n")
                print("\n")
                olo=input("Successfully Sent Press Enter Button to continue.........")
        elif c==2:
                exit()
