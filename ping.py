#!/usr/bin/python2.7
import os
import subprocess


with open('checklists.txt', 'r') as f:
    for ip in f:
        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "3", ip],stdout=f, stderr=f).wait()
        if result:
            print (ip, "is NOT Reachable")
        else:
            print (ip, "is Reachable")

