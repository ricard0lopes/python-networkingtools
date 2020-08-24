# SMTP client to send emails to a SMTP server

import smtplib

message = """From: From Hackerman <hackerman@mail.com>
To: To Someone <someone@victimail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is an email message sent as HTML

<b>THis is a test HTML message.</b>
<h1>Big Head</h1>
"""

try:
    smtp = smtplib.SMTP("ip")
    smtp.sendmail("hackerman@mail.com", "someone@victimail.com", message)
    print("Email sent successfully!")
except Exception as err:
    print(str(err))