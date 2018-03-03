#!/usr/bin/python2.7
import subprocess


def PING():
    with open('pinglists.txt', 'r') as f:
        for IP in f:
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "3", IP],stdout=f, stderr=f).wait()
            if result:
                print IP.replace("\n",""),"is NOT Reachable"
            else:
                print IP.replace("\n",""),"is Reachable"

def PING_TCP():
    TCP = raw_input("TCP Port Number: ") 
    with open('pinglists.txt', 'r') as f:
        for IP in f:
            result = subprocess.Popen(["tcping", "-t", "1", IP, TCP],stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1)
            result_string = ''
            for i in iter(result.stdout):
                result_string += bytes.decode(i).split('\n')[0]
            if 'port '+TCP+' open' in result_string:
                print IP.replace("\n",""),"is Reachable"
            else:
                print IP.replace("\n",""),"is NOT Reachable"


print("################### Select Mode ####################")
print("###   [1] PING      [2] TCP PING     [3] EXIT    ###")
print("####################################################")
Menu = raw_input("Enter Number of Mode: ")
if Menu == "1" :
    PING()
elif Menu == "2" :
    PING_TCP()
elif Menu == "2" :
    pass
else:
    print("Exit!Plaese try to Select")
