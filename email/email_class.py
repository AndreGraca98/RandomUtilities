import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Tuple



class Email:
    """ Email class
    
        Sends an email with attachments from localhost to a receiver email. """
        
    def __init__(self, smtp_server: str="localhost:25", receiver_email: str='your-email@gmail.com', sender_email: str=Path.home().stem) -> None:
        """ Initialize email class
        
            Args:
                smtp_server (str, optional): Email server. Defaults to "localhost:25".
                receiver_email (str, optional): Your receiver email. Defaults to 'your-email@gmail.com'.
                sender_email (str, optional): Local sender user name. Defaults to Path.home().stem. """
        self.smtp_server = smtp_server 
        self.receiver_email = receiver_email 
        self.sender_email = sender_email 
    
    def __call__(self, **kwds) -> None:
        """ Sends an email with specified subject, body and attachments """
        self.send(**kwds)
        
    def create_message(self, subject: str, body: str, attachments: Tuple[str]):
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = subject

        # send these files
        if attachments is not None:
            if isinstance(attachments, tuple) or isinstance(attachments, list):
                for file in attachments:
                    assert isinstance(file, str), f'Filename: {file} , must be of type str'
                    if os.path.isfile(file): # File exosts
                        self.append_attachment_to_message(file)
                    else:
                        body += f'\n\nFile: {file} , does not exist'
                        
            elif isinstance(attachments, str):
                if os.path.isfile(attachments): # File exosts
                    self.append_attachment_to_message(file)
                else:
                    body += f'\n\nFile: {attachments} , does not exist'
                    
            else:
                raise TypeError(f'Filenames: {attachments} , must be of type str, list of str or tuple of str')
                
        self.message.attach(MIMEText(body, "plain"))

    def append_attachment_to_message(self, filename: str):
        """ Appends attachment to the message

            Args:
                filename (str): path to the filename -> /path-to-the-file/filename.suffix        """
        with open(filename, "rb") as attachment:  # text file
            part = MIMEBase("application", "octet-stream", )
            part.set_payload(attachment.read())
            part.add_header("Content-Disposition", f"attachment; filename= {filename}")
            encoders.encode_base64(part)
            
            self.message.attach(part)
            
    def connect_server_and_send_email(self):
        if self.message["To"] == 'your-email@gmail.com':
            raise ValueError('Must change the receiver email to a different email: your-email@gmail.com')
        with smtplib.SMTP(self.smtp_server) as server:
            server.sendmail(self.message["From"], self.message["To"], self.message.as_string())
            
    def send(self, subject: str="Subject", body: str='Body', attachments: Tuple[str]=None):
        self.create_message(subject=subject, body=body, attachments=attachments)
        self.connect_server_and_send_email()
        self.cleannup()
        
    def cleannup(self):
        """ TODO:  """
        pass


if __name__ == '__main__':
    ### EMAIL USAGE
    Email().send(subject='this is the subject', body='this is the body', attachments=['some_file.txt', 'not_a_file.txt']) 
    # OR
    Email(receiver_email='a-different-email@gmail.com', sender_email='the name that will appear before the computer name')(subject='this is the subject', body='this is the body', attachments=['some_file.txt', 'not_a_file.txt'])

