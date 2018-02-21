#!/usr/bin/python2.7
import subprocess


def WHOIS_AS():
    ASN = raw_input("AS Number: ")
    bashcmd1 = "whois -h whois.cymru.com AS"+ASN
    subprocess.call(bashcmd1, shell=True)

def WHOIS_IP():
    IP = raw_input("IPv4 Address: ")
    bashcmd2 = "whois -h whois.cymru.com "+IP
    subprocess.call(bashcmd2, shell=True)


print("############# Select Mode #################")
print("### [1] Whois ASN [2] Whois IP [3] EXIT ###")
print("###########################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    WHOIS_AS()
elif Menu == "2" :
    WHOIS_IP()
elif Menu == "3" :
    pass
else:
    print("Plaese Select")

