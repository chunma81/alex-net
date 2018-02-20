#!/usr/bin/python2.7
import os

def HTTP_80():
    HTTP = raw_input("TCP80 Host IP: ")
    bashcommand = "tcping -p 80 -c 3 -h "+HTTP
    os.system (bashcommand)

def HTTPS_443():
    SSL = raw_input("TCP443 Host IP: ")
    bashcommand = "tcping -p 443 -c 3 -h "+SSL
    os.system (bashcommand)

def OTHERS():
    PORT = raw_input("What TCP Port: ")
    HOST = raw_input("Host IP: ")
    bashcommand = "tcping -c 3 -p "+PORT -h +HOST
    os.system (bashcommand)

print("############# Select Mode #########################")
print("### [1] TCP 80  [2] TCP 443 [3] OTHER  [4] EXIT ###")
print("###################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    HTTP_80()
elif Menu == "2" :
    HTTPS_443()
elif Menu == "3" :
    OTHERS()
elif Menu == "4" :
    pass
else:
    print("Plaese Select")

