#!/usr/bin/python2.7
import subprocess


def UDP_OT():
    SW = raw_input("Switch IP address: ")
    UDP = raw_input("UDP Port Number: ")
    result = subprocess.Popen(["nc", "-uzv", SW, UDP, "-w", "3"],stdout=subprocess.PIPE)
    print result.communicate()[0]

def TCP_OT():
    SW = raw_input("Switch IP address: ")
    TCP = raw_input("TCP Port Number: ")
    result = subprocess.Popen(["nc", "-zv", SW, TCP, "-w", "3"],stdout=subprocess.PIPE)
    print result.communicate()[0]

def UDP_LIST():
    UDP = raw_input("UDP Port Number: ")    
    with open('portchklists.txt', 'r') as f:
        for SWL in f:
            result = subprocess.Popen(["nc", "-uzv", SWL.replace("\n",""), UDP, "-w", "3"],stdout=subprocess.PIPE)
            print result.communicate()[0]

def TCP_LIST():
    TCP = raw_input("TCP Port Number: ")
    with open('portchklists.txt', 'r') as f:
        for SWL in f:
            result = subprocess.Popen(["nc", "-zv", SWL.replace("\n",""), TCP, "-G", "1", "-w", "3"],stdout=subprocess.PIPE)
            print result.communicate()[0]

def NMAP_OT():
    SW = raw_input("Switch IP address: ")
    print "It will take some time to search an openning ports. Please wait for 30 seconds"
    result = subprocess.Popen(["sudo", "nmap", "-sT", "-sU", SW, "--host-timeout", "30"],stdout=subprocess.PIPE)
    print result.communicate()[0]


print("############################################ Select Mode ##################################################")
print("###  [1] NC UDP  [2] NC TCP  [3] NC UDP for lists  [4] NC TCP for lists  [5] NMAP Open ports  [6] EXIT  ###")
print("###########################################################################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    UDP_OT()
elif Menu == "2" :
    TCP_OT()
elif Menu == "3" :
    UDP_LIST()
elif Menu == "4" :
    TCP_LIST()
elif Menu == "5" :
    NMAP_OT()
elif Menu == "6" :
    pass
else:
    print("Exit!Plaese try to Select")


