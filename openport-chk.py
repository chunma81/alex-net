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


print("#######################Select Mode ##########################")
print("### [1] UDP Port Check    [2] TCP Port Check     [3] EXIT ###")
print("#############################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    UDP_OT()
elif Menu == "2" :
    TCP_OT()
elif Menu == "3" :
    pass
else:
    print("Plaese Select")


