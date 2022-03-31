from email.mime.application import MIMEApplication
from http import server
from pathlib import Path
from tokenize import Name

from importlib_metadata import files


class Config:

    switchTesting = True

    url = "http://127.0.0.1:5000"

    secretKey = "yourSecretKey1234!@#$"


    server = 'mail.your-domain.com'
    port = 25
    sender = 'you@youremail.com'
    recievers = ['to@toemail.com', 'to@toemail.com']
    subject =  'DEAD MAN SWITCH'
    body = 'Email body here'

    with open('/path/to/zipfile', 'r') as file:
       Files = (MIMEApplication(file.read(), Name='filename.zip'))
    