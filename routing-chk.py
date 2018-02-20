#!/usr/bin/python2.7
import os

def TRACE():
    IP1 = raw_input("DST IP Address:")
    bashcommand = "traceroute -n -w 1 "+IP1 
    os.system (bashcommand)

def MTR():
    IP2 = raw_input("DST IP Address:")
    bashcommand = "mtr -n -r -c 1 "+IP2
    os.system (bashcommand)

print("############# Select Mode #################")
print("####[1] TraceRoute [2] MTR  [3] EXIT ######")
print("###########################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    TRACE()
elif Menu == "2" :
    MTR()
elif Menu == "3" :
    pass
else:
    print("Plaese Select")
