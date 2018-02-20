#!/usr/bin/python2.6
import subprocess
import os

with open('checklists.txt', 'r') as f:
    for ip in f:
        result=subprocess.Popen(["ping", "-c", "3", "-n", "-W", "2", ip],stdout=f, stderr=f).wait()
        if result:
            print(ip, "is NOT REACHABLE")
        else:
            print(ip, "is REACHABLE")

# this is test
