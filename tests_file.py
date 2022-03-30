from pathlib import Path
from tools.email_class import Email
from tools.encryption import create_credentials_csv, generate_key, get_all_credentials, get_credentials


if __name__ == '__main__':
    # generate_key()
    # create_credentials_csv(["email@domain"], ["password"], force=False)
    
    # print( get_credentials('domain') )
    # print( get_all_credentials() )
    
    Email(sender_email=input('sender email: '), sender_pwd=input('sender pwd: ')).send(attachments='tools/some_file.txt')
    
    pass