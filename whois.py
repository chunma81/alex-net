#!/usr/bin/python2.7
import subprocess


def WHOIS_AS():
    ASN = raw_input("AS Number: ")
    bashcmd = "whois -h whois.cymru.com AS"+ASN
    subprocess.call(bashcmd, shell=True)

def WHOIS_IP():
    IP = raw_input("IPv4 Address: ")
    bashcmd = "whois -h whois.cymru.com "+IP
    subprocess.call(bashcmd, shell=True)

def RADB_BL():
    IP = raw_input("IPv4 Block Address: ")
    bashcmd = "whois -h whois.radb.net "+IP
    subprocess.call(bashcmd, shell=True)

def ALTDB_BL():
    IP = raw_input("IPv4 Block Address: ")
    bashcmd = "whois -h whois.altdb.net "+IP
    subprocess.call(bashcmd, shell=True)

print("############################# Select Mode ################################")
print("### [1] Whois ASN  [2] Whois IP  [3] RADB.net  [4] ALTDB.net  [5] EXIT ###")
print("##########################################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    WHOIS_AS()
elif Menu == "2" :
    WHOIS_IP()
elif Menu == "3" :
    RADB_BL()
elif Menu == "4" :
    ALTDB_BL()
elif Menu == "5" :
    pass
else:
    print("Exit!Plaese try to Select")

