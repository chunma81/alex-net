#!/usr/bin/python2.7

import smtplib
import subprocess
from email.mime.text import MIMEText
import pexpect, sys

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
s.logfile = open('/home/alex/chk_bgp_a.log','w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('show bgp summary | match xe-1/0/0’)
s.expect('>')
s.sendline('show interfaces descriptions | match NTT’)
s.expect('>')
s.sendline('show ospf neighbor')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "### /START-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s = pexpect.spawn('ssh -o "StrictHostKeyChecking no"  %s@%s' % (pUser, pIP_B))
s.timeout = 5
s.expect('[P|p]assword:')
s.sendline(pPasswd)
s.logfile = open('/home/alex/chk_bgp_b.log','w')
#s.logfile = sys.stdout
s.expect('>')
s.sendline('show bgp summary | match xe-2/0/0)
s.expect('>')
s.sendline('show interfaces descriptions | match GTT’)
s.expect('>')
s.sendline('show ospf neighbor')
s.expect('>')
s.sendline('exit')
print "### /END-SSH-SESSION via PYTHON PEXPECT Module/ ###"
s.close()

print "######################### [Feedback] ############################"
result =""
try:
    result = subprocess.check_output ("cat /home/alex/chk_bgp_a.log | awk '{print $8}' | egrep 'Active|Connect|Idle'" , shell=True)
except Exception as Errr:
    result = "error"

retmsg_HK = ""

if result != "error":
#if result:
   retmsg_HK = "Need to check ASAP"
   print "Need to check  ASAP"
else:
   retmsg_HK = "No BGP issue until now"
   print "No BGP issue until now"
print "################################ [End] ##################################"

result_file = "/home/alex/chk_bgp_b.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_HK

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][CID] %s' % retmsg_HK
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "######################## [Feedback] ############################"
result =""
try:
    result = subprocess.check_output ("cat /home/alex/chk_bgp_a.log | awk '{print $8}' | egrep 'Active|Connect|Idle'" , shell=True)
except Exception as Errr:
    result = "error"

retmsg_JP = ""

if result != "error":
#if result:
   retmsg_JP = "Need to check  ASAP"
   print "Need to check ASAP"
else:
   retmsg_JP = "No BGP issue until now"
   print "No BGP issue until now"
print "################################ [End] ##################################"

result_file = "/home/alex/chk_bgp_a.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_JP

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][CID] %s' % retmsg_JP
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "################################ [DONE] ##################################"
