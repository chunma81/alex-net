#!/usr/bin/python2.7

import subprocess
import smtplib
from email.mime.text import MIMEText
import pexpect , sys

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

pIP = “hostname”
pUser = “alex”
pPasswd = “alex123”

print "### /START-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s = pexpect.spawn('ssh -o "StrictHostKeyChecking no"  %s@%s' % (pUser, pIP))
s.timeout = 5
s.expect('[P|p]assword:')
s.sendline(pPasswd)
s.logfile = open(‘/home/alex/chk_traffic.log','w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('show interfaces descriptions | match ge-1/’)
s.expect('>')
s.sendline('show interfaces ge-1/0/2 | match rate')
s.expect('>')
s.sendline('show interfaces ge-1/1/2 | match rate')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "######################## [Feedback] ############################"
result = subprocess.check_output ("cat /home/alex/chk_traffic.log |egrep 'Out|In' |awk '$4 > 100000000 {print $4}'" , shell=True)

retmsg_T = ""

if result:
    retmsg_T = "Need to check Traffic Usage ASAP"
    print "Need to check Traffic Usage ASAP"
else:
    retmsg_T = "No Traffic issue until now"
    print "No Traffic issue until now"

result_file = "/home/alex/chk_traffic.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_T

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][Uplink] %s ' % retmsg_T
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "################################ [DONE] ##################################"
