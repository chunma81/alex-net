#!/usr/bin/python2.7
import os
import subprocess


with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 9):
                ip="8.8.8.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "3", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "is NOT Reachable"
                else:
                        print ip, "is Reachable"
