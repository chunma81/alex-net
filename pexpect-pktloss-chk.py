#!/usr/bin/python2.7

import smtplib
import subprocess
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
s.logfile = open(‘/home/alex/chk_net.log','w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('show bgp summary | match 65100’)
s.expect('>')
s.sendline('show interfaces descriptions | match iplc')
s.expect('>')
s.sendline('ping 192.168.10.100 rapid count 50 size 1450')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "############# [Feedback] ##############"
#result =""
#try:
result = subprocess.check_output ("cat /home/alex/chk_net.log | grep packet |awk '$4 > 47 {print $4}'" , shell=True)
#except Exception as Errr:
#    result = "error"

retmsg_loss = ""

#if result != "error":
if result:
    retmsg_loss = "No NET issue until now"
    print "No NET issue until now"

else:
    retmsg_loss = "Need to check NET ASAP"
    print "Need to check NET ASAP"
print "################################ [End] ##################################"

result_file = "/home/alex/chk_net.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_loss

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][NET] %s' % retmsg_loss
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "############################### [DONE] #######################################"
