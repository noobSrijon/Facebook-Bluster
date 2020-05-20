import os
import sys
import platform
import base64
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
def n(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def o(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
key='ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
   'abcdefghijklmnopqrstuvwxyz' + \
   '0123456789' + \
   ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'
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
        print("2. Logout")
        print("3. Exit")
        c=int(input(":~$ "))
        if c==1:
                a=os.stat('data.txt')
                a=a.st_size
                f=open("data.txt","r+")
                ccc=f.readlines()
                f.close()
                if len(ccc)==1:
                        if len(A)==0:
                                username=str(input("Your FB Username:~$ "))
                                password=getpass()
                                A.append(username)
                                A.append(password)

                        else:
                                username=A[0]
                                password=A[1]
                                
                        client=Client(username,password)
                        
                        f=open("data.txt","w+")
                        f.write("{}\n{}".format(n(key,username),n(key,password)))
                        f.close()

                else:
                        username=ccc[0]
                        password=ccc[1]
                        username=o(key,username)
                        password=o(key,password)
                        client=Client(username,password)
                """
                x=client.searchForUsers("Srijon Kumar")
                f=x[0]
                client.send(fbchat.models.Message(password),f.uid )
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
                A.clear()
                f=open("data.txt","w+")
                f.write("")
                print("Successfully logged out!!")
                f.write("{}".format("#Keep This File Secure"))
                f.close()
                q=open("data.txt","a")
                q.write("#Keep This File Secure")
                a=input("Press Enter to continue...")
        elif c==3:
                exit()
