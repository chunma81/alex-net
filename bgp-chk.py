#!/usr/bin/python2.7

import smtplib
import subprocess
from email.mime.text import MIMEText

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

subprocess.call (“/home/alex/CHK_LINK_STATUS.sh" , shell=True)

print "\n########################### [Feedback] ##############################"

result =""
try:
    result = subprocess.check_output ("cat /home/alex/CHK_LINK_STATUS.log | awk '{print $9}' | egrep 'Active|Connect|Idle'" , shell=True)
except Exception as Err:
    result = "error"

retmsg_HK = ""

if result != "error":
#if result:
   retmsg_HK = "Need to check uplink ASAP"
   print "Need to check uplink ASAP"
else:
   retmsg_HK = "No BGP issue uplink until now"
   print "No BGP issue uplink until now"

print "################################ [End] ##################################"

result_file = “/home/alex/CHK_LINK_STATUS.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_HK

msg = MIMEText( strmsg  )

gmail_user = “alex@gmail.com"
gmail_pwd = “alex123"

me = ‘alex@gmail.com'
you = ‘alex@yahoo.com'

msg['Subject'] = '[Automation][Uplink] %s' % retmsg_HK
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "################################ [DONE] ##################################”

