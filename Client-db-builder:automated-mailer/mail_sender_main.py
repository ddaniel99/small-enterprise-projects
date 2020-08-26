import sqlite3
import smtplib, ssl
import getpass
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

text = '''\
Weekly Mark-to-Market Report
Dear {title} {last_name},

Please find below and attached your weekly Market-to-Market report, outlining the value of your positions as well as a summary of your most recent instruction to us as of the date of this e-mail.

As always, I am at your disposal to clarify any questions you may have. Please do not hesitate to contact me or the Team.

# INSERT E-MAIL SIGNATURE

This email and any files transmitted with it are confidential and intended solely for the use of the individual or entity to whom they are addressed. If you have received this email in error, please notify the system manager. This message contains confidential information and is intended only for the individual named. If you are not the named addressee, you should not disseminate, distribute or copy this email. Please notify the sender immediately by email if you have received this email by mistake and delete this email from your system. If you are not the intended recipient, you are notified that disclosing, copying, distributing or taking any action in reliance on the contents of this information is strictly prohibited.

Please consider the environment before printing this email.
'''
html = '''\
<html>
  <body style="font-family:'Calibri'">
    <h2>Weekly Mark-to-Market Report</h2>
      <p>Dear {title} {last_name},<br><br>
      Please find below and attached your weekly] Mark-to-Market report, outlining the value of your positions as well as a summary of your most recent instruction to us as of the date of this e-mail.<br><br>

      As always, I am at your disposal to clarify any questions you may have. Please do not hesitate to contact me or the Team.<br><br>

      # INSERT E-MAIL SIGNATURE
      Kind regards,<br>
      Stephen SMITH<br>
      <small>Mobile: +44 (0) 1234 45 7899</small><br>
      <small>E-mail: sample@e-mail.com</small><br>
      <small><a href="https://www.samplewebsite.com">VISIT WEBSITE</a></small>

      </p>

      <img src="https://logodomain/logo.gif" alt="COMPANY NAME" > <br><br>

      <p style="font-size:10px">This email and any files transmitted with it are confidential and intended solely for the use of the individual or entity to whom they are addressed. If you have received this email in error, please notify the system manager. This message contains confidential information and is intended only for the individual named. If you are not the named addressee, you should not disseminate, distribute or copy this email. Please notify the sender immediately by email if you have received this email by mistake and delete this email from your system. If you are not the intended recipient, you are notified that disclosing, copying, distributing or taking any action in reliance on the contents of this information is strictly prohibited.<br><br>

      Please consider the environment before printing this email.</p>

  </body>
</html>
'''
lst = []
selc = ()
conn = sqlite3.connect('clients.sqlite')
cur = conn.cursor()
cur.execute('SELECT id, first_name, last_name, title, e_mail, company FROM Clients')
for row in cur :
    lst.append(row)
    print(row)
cur.close()

selc = input('Who to send to? (select by id, separated by comma or type all)')
if selc == 'all' :
    for i in range(len(lst)) :
        seld = int(i)
        print(text.format(title = lst[seld][3], last_name = lst[seld][2]))
else :
    selc = selc.split(',')
    for i in selc :
        seld = int(i)-1
        print(text.format(title = lst[seld][3], last_name = lst[seld][2]))

cur.close()

prompt = input('Above ok to send? (Cannot send to all due to security) (y/n)')
prompt = prompt.lower()
if prompt == 'y' :
    password = getpass.getpass(prompt='Please enter your password: ')
else :
    quit()

smtp_server = "smtp-mail.outlook.com"
port = 587
sender_email = 'SENDER E-MAIL'

for i in selc :
    seld = int(i)-1
    receiver_email = lst[seld][4]
    message = MIMEMultipart('alternative')
    message['From'] = sender_email
    message['To'] = receiver_email
    txt = text.format(title = lst[seld][3], last_name = lst[seld][2])
    htm = html.format(title = lst[seld][3], last_name = lst[seld][2])
    message['Subject'] = 'Weekly Mark-to-Market Report ' + str(datetime.now())[:-7]
    p1 = MIMEText(txt, 'plain')
    p2 = MIMEText(htm, 'html')
    message.attach(p1)
    message.attach(p2)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server,port) as server :
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
password = 0
quit()
