#!/usr/bin/python2.7
import subprocess


def TRACE():
    IP1 = raw_input("DST IP Address:")
    bashcmd1 = "traceroute -n -w 1 "+IP1 
    subprocess.call(bashcmd1, shell=True)

def MTR():
    IP2 = raw_input("DST IP Address:")
    bashcmd2 = "mtr -n -r -c 1 "+IP2
    subprocess.call(bashcmd2, shell=True)


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
