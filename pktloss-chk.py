#!/usr/bin/python2.7

import smtplib
import subprocess
from email.mime.text import MIMEText

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

subprocess.call ("/home/alex/CHK_LOSS.sh" , shell=True)

print "\n########################## [Feedback] ##############################”

#result =""
#try:
result = subprocess.check_output ("cat /home/alex/CHK_LOSS.log | grep packet |awk '$4 > 47 {print $4}'" , shell=True)
#except Exception as Err:
#    result = "error"

retmsg_loss = ""

#if result != "error":
if result:
    retmsg_loss = "No LOSS issue until now"
    print "No LOSS issue until now"

else:
    retmsg_loss = "Need to check LOSS ASAP"
    print "Need to check LOSS ASAP"

print "################################ [End] ##################################"

result_file = "/home/alex/CHK_LOSS.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_loss

msg = MIMEText( strmsg  )

gmail_user = "alex@gmail.com"
gmail_pwd = "alex123"

me = 'alex@gmail.com'
you = 'alex@yahoo.com'

msg['Subject'] = '[Automation][PKT A<=>Z] %s' % retmsg_loss
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "############################### [DONE] #######################################”

