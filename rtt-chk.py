#!/usr/bin/python2.7

import smtplib
import subprocess
from email.mime.text import MIMEText

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

subprocess.call ("/home/alex/CHK_RTT.sh" , shell=True)

print “\n########################## [Feedback] ###############################”
#result =""
#try:
result = subprocess.check_output ("cat /home/alex/CHK_RTT.log | grep 8.8.8.8 | awk '$6 > 130 {print $6}'" , shell=True)
#except Exception as Err:
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

result_file = "/home/alex/CHK_RTT.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_rtt

msg = MIMEText( strmsg  )

gmail_user = "alex@gmail.com"
gmail_pwd = "alex123"

me = 'alex@gmail.com'
you = 'alex@yahoo.com’

msg['Subject'] = '[Automation][Latency] %s' % retmsg_rtt
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "############################### [DONE] #######################################”
