#!/usr/bin/python2.7
import subprocess


def SNMP_OT():
    SW = raw_input("Switch IP address: ")
    result1 = subprocess.Popen(["snmpwalk", "-t", "1", "-v2c", "-c", "Cummunity", SW, "sysDescr.0"],stdout=subprocess.PIPE)
    print result1.communicate()[0]

def SNMP_LIST():
    with open('snmplists.txt', 'r') as f:
        for SWL in f:
            result2 = subprocess.Popen(["snmpwalk", "-t", "1", "-v2c", "-c", "Community", SWL.replace("\n",""), "sysDescr.0"],stdout=subprocess.PIPE)
            print result2.communicate()[0]

print("############################# Select Mode ##############################")
print("### [1] SNMP CHK for one Switch  [2] SNMP CHK for SW lists  [3] EXIT ###")
print("########################################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    SNMP_OT()
elif Menu == "2" :
    SNMP_LIST()
elif Menu == "3" :
    pass
else:
    print("Plaese Select")


