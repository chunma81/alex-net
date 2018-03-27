#!/usr/bin/python2.7

import smtplib
import subprocess
from email.mime.text import MIMEText
import pexpect , sys

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

pIP_A = “hostname”
pIP_B = “hostname”
pUser = “alex”
pPasswd = “alex123”

print "### /START-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s = pexpect.spawn('ssh -o "StrictHostKeyChecking no"  %s@%s' % (pUser, pIP_A))
s.timeout = 5
s.expect('[P|p]assword:')
s.sendline(pPasswd)
s.logfile = open('/home/alex/chk_rtt_a.log','w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('start shell')
s.expect('%')
s.sendline('mtr 8.8.8.8 -r -c 5 -n')
s.expect('%')
s.sendline('exit')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "### /START-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s = pexpect.spawn('ssh -o "StrictHostKeyChecking no"  %s@%s' % (pUser, pIP_B))
s.timeout = 5
s.expect('[P|p]assword:')
s.sendline(pPasswd)
s.logfile = open('/home/alex/chk_rtt_b.log,'w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('start shell')
s.expect('%')
s.sendline('mtr 8.8.4.4 -r -c 5 -n')
s.expect('%')
s.sendline('exit')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "######################## [ Feedback] ############################"
#result =""
#try:
result = subprocess.check_output ("cat /home/alex/chk_rtt_a.log | grep 8.8.8.8 | awk '$6 > 50 {print $6}'" , shell=True)
#except Exception as Errr:
#    result = "error"

retmsg_rtt = ""

#if result != "error":
if result:
   retmsg_rtt = "Need to check RTT ASAP"
   print "Need to check RTT ASAP"

else:
   retmsg_rtt = "No RTT issue until now"
   print "No RTT issue until now"
print "################################ [End] ##################################"

result_file = "/home/alex/chk_rtt_a.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_rtt

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][Latency A] %s' % retmsg_rtt
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "######################## [Feedback] ############################"
#result =""
#try:
result = subprocess.check_output ("cat /home/alex/chk_rtt_b.log | grep 8.8.4.4 | awk '$6 > 50 {print $6}'" , shell=True)
#except Exception as Errr:
#    result = "error"

retmsg_rtt = ""

#if result != "error":
if result:
   retmsg_rtt = "Need to check RTT ASAP"
   print "Need to check RTT ASAP"

else:
   retmsg_rtt = "No RTT issue until now"
   print "No RTT issue until now"
print "################################ [End] ##################################"

result_file = "/home/alex/chk_rtt_b.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_rtt

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][Latency B] %s' % retmsg_rtt
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "############################### [DONE] #######################################"
