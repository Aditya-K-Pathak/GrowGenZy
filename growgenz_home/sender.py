import os

SENDER = os.environ.get('SENDER')
PASSWORD = os.environ.get('PASSWORD')

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Response Submitted!</title>
</head>
<body>
    <h1 style="font-family: 'Playfair Display'">WE HEAR YOU!</h1>
    <img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8146/confirm.png" alt="" style="height: 250px;">
    <p style="font-family: Georgia, 'Times New Roman', Times, serif; line-height: 120%; letter-spacing: 1px; word-spacing: 3px;">
        Hey <span>username</span>, We have received your response and we assure you that one of our collegue will be contacting you soon.
    </p>
    <p style="font-family: Georgia, 'Times New Roman', Times, serif; line-height: 120%; letter-spacing: 1px; word-spacing: 3px;">
        You may also receive an automated email with a meeting link to connect with our associate, make sure to check your spams too.
    </p>
    <p style="font-family: Georgia, 'Times New Roman', Times, serif; line-height: 120%; letter-spacing: 1px; word-spacing: 3px;">
        Thank You for having trust in us.

        GrowGenZy
    </p>
</body>
</html>
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail:
    def __init__(self):
        self.sender = "weatherupdate.adityapathak@gmail.com"
        self.password = 'laxt lrmv jpxs fsng'

    def sendMail(self, receiverAddress: str, mail: str):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        message = MIMEMultipart()
        message['From'] = 'GROWGENZY @noreply'
        message['To'] = receiverAddress
        message['Subject'] = 'We have received your response!'
        message.attach(MIMEText(mail, 'html'))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.sender, self.password)
            server.send_message(message)
