#!/usr/bin/python2.6
import subprocess
import os
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 254):
                ip="123.103.50.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "is NOT Reachable"
                else:
                        print ip, "is Reachable"
