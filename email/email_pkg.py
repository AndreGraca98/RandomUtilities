import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Tuple


def send_email(subject: int="Subject", body: int='Body', attachments: Tuple[str]=None):
    smtp_server = "localhost:25"
    receiver_email = 'your-email@domain' # 
   
    message = MIMEMultipart()
    message["From"] = Path.home().stem
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # send these files
    if attachments is not None:
        for f in attachments:
            if os.path.isfile(f):
                with open(f, "rb") as attachment:  # text file
                    part = MIMEBase("application", "octet-stream", )
                    part.set_payload(attachment.read())
                    part.add_header("Content-Disposition", f"attachment; filename= {f}")
                    encoders.encode_base64(part)
                    message.attach(part)

    text = message.as_string()

    with smtplib.SMTP(smtp_server) as server:
        server.sendmail(message["From"], message["To"], text)


if __name__ == '__main__':
    send_email(attachments=['file.txt'])
