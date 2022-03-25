from tools import Email, get_credentials, email_notification

if __name__ == '__main__':
    Email().send(attachments='tools/some_file.txt')