#!/usr/bin/python2.7
import subprocess


def HTTP_80():
    HTTP = raw_input("TCP80 Host IP: ")
    bashcmd1 = "tcping -p 80 -i 0.5 -c 5 -h "+HTTP
    subprocess.call(bashcmd1, shell=True)

def HTTPS_443():
    SSL = raw_input("TCP443 Host IP: ")
    bashcmd2 = "tcping -p 443 -i 0.5 -c 5 -h "+SSL
    subprocess.call(bashcmd2, shell=True)

def DNS_53():
    DNS = raw_input("TCP53 Host IP: ")
    bashcmd3 = "tcping -p 53 -c 5 -i 0.5 -h "+DNS
    subprocess.call(bashcmd3, shell=True)


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

