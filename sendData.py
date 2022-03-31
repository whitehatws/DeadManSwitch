import smtplib
from config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send():
    if Config.switchTesting:
        print('sent')
    else:    
        msg = MIMEMultipart()
        msg['Subject'] = Config.subject
        msg['From'] = Config.sender
        msg['To'] = Config.recievers
        msg['Body'] = Config.body
        msg['Files'] = Config.Files
        
        try:
            smtpObject = smtplib.SMTP(Config.server, Config.port)
            smtpObject.sendmail(Config.sender, Config.recievers, msg)
            print('Dead man switch successfully activated. Email sent.')

        except smtplib.SMTPException:
            print('Error: Unabale to active dead man switch. Email NOT sent.')