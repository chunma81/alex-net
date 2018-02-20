#!/usr/bin/python2.7
import os

def WHOIS_AS():
    ASN = raw_input("AS Number: ")
    bashcommand = "whois -h whois.cymru.com AS"+ASN
    os.system (bashcommand)

def WHOIS_IP():
    IP = raw_input("IPv4 Address: ")
    bashcommand = "whois -h whois.cymru.com "+IP
    os.system (bashcommand)

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

