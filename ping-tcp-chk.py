#!/usr/bin/python2.7
import os

def HTTP_80():
    HTTP = raw_input("TCP80 Host IP: ")
    bashcommand = "tcping -p 80 -i 0.5 -c 5 -h "+HTTP
    os.system (bashcommand)

def HTTPS_443():
    SSL = raw_input("TCP443 Host IP: ")
    bashcommand = "tcping -p 443 -i 0.5 -c 5 -h "+SSL
    os.system (bashcommand)

def DNS_53():
    DNS = raw_input("TCP53 Host IP: ")
    bashcommand = "tcping -p 53 -c 5 -i 0.5 -h "+DNS
    os.system (bashcommand)

print("############# Select Mode #########################")
print("### [1] TCP 80  [2] TCP 443 [3] DNS 53 [4] EXIT ###")
print("###################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    HTTP_80()
elif Menu == "2" :
    HTTPS_443()
elif Menu == "3" :
    DNS_53()
elif Menu == "4" :
    pass
else:
    print("Plaese Select")

