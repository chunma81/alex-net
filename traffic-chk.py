#!/usr/bin/python2.7
import subprocess
import smtplib
from email.mime.text import MIMEText

print "############################ [Starting] ###############################"
print "Removing OLD Log files and the Notification Email will be sent soon"
print "############################ [Checking] ###############################"

subprocess.call ("/home/alex/CHK_TRAFFIC.sh" , shell=True)

print "########################### [Feedback] ################################"
result = subprocess.check_output ("cat /data/alex/CHK_TRAFFIC.log |egrep 'Out|In' |awk '$4 > 7000000000 {print $4}'" , shell=True)

retmsg_T = ""

if result:
    retmsg_T = "Need to check Traffic Usage ASAP"
    print "Need to check Traffic Usage ASAP"
else:
    retmsg_T = "No Traffic issue until now"
    print "No Traffic issue until now"

result_file = "/home/alex/CHK_TRAFFIC.log"
fp = open(result_file, 'rb')

strmsg = fp.read()
fp.close()
strmsg += "\n" + retmsg_T

msg = MIMEText( strmsg  )

gmail_user = "alex@gmail.com"
gmail_pwd = "alex123"

me = 'alex@gmail.com'
you = 'alex@yahoo.com'

msg['Subject'] = '[Automation][Uplink] %s ' % retmsg_T
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(gmail_user, gmail_pwd)
s.sendmail(me, [you], msg.as_string())
s.quit()

print "################################ [DONE] ##################################"

