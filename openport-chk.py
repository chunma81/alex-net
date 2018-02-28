#!/usr/bin/python2.7
import subprocess


def UDP_OT():
    SW1 = raw_input("Switch IP address: ")
    UDP = raw_input("UDP Port Number: ")
    result1 = subprocess.Popen(["nc", "-uzv", SW1, UDP, "-w", "3"],stdout=subprocess.PIPE)
    print result1.communicate()[0]

def TCP_OT():
    SW2 = raw_input("Switch IP address: ")
    TCP = raw_input("TCP Port Number: ")
    result2 = subprocess.Popen(["nc", "-zv", SW2, TCP, "-w", "3"],stdout=subprocess.PIPE)
    print result2.communicate()[0]


def UDP_LIST():
    UDP = raw_input("UDP Port Number: ")    
    with open('portchklists.txt', 'r') as f:
        for SWL in f:
            result3 = subprocess.Popen(["nc", "-uzv", SWL.replace("\n",""), UDP, "-w", "3"],stdout=subprocess.PIPE)
            print result3.communicate()[0]


print("########################################Select Mode ##########################################################")
print("### [1] UDP Onetime Check     [2] TCP Onetime Check     [3] UDP Check for lists swtiches         [4] EXIT ###")
print("##############################################################################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    UDP_OT()
elif Menu == "2" :
    TCP_OT()
elif Menu == "3" :
    UDP_LIST()
elif Menu == "4" :
    pass
else:
    print("Exit!Plaese try to Select")


