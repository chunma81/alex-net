#!/usr/bin/python2.7
import subprocess


def SNMP_OT():
    SW = raw_input("Switch IP address: ")
    result = subprocess.Popen(["snmpwalk", "-r", "1", "-t", "2", "-v2c", "-c", "Cummunity", SW, "sysDescr.0"],stdout=subprocess.PIPE)
    print result.communicate()[0]

def SNMP_LIST():
    with open('snmplists.txt', 'r') as f:
        for SWL in f:
            result = subprocess.Popen(["snmpwalk", "-r", "1", "-t", "2", "-v2c", "-c", "Cummunity", SWL.replace("\n",""), "sysDescr.0"],stdout=subprocess.PIPE)
            print result.communicate()[0]


print("########################### Select Mode ############################")
print("###   [1] SNMP Check    [2] SNMP Check for SWlists    [3] EXIT   ###")
print("####################################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    SNMP_OT()
elif Menu == "2" :
    SNMP_LIST()
elif Menu == "3" :
    pass
else:
    print("Exit!Plaese try to Select")
