import time
from tools.email_class import Email
from tools.encryption import create_credentials_csv, generate_key, get_all_credentials, get_credentials
from tools.runner_wrapper import email_notification


if __name__ == '__main__':
    generate_key()
    email=input('Enter sender email ["user@isr.uc.pt"]: '); pwd=input('Enter sender pwd ["password"]: ')
    create_credentials_csv([email], [pwd], force=True)
    
    print( get_all_credentials() )
    # print( get_credentials('domain') )
    
    Email(sender_email=email, sender_pwd=pwd).send(attachments='tools/some_file.txt')
    
    @email_notification
    def function():
        print(f'Press Ctrl+C to send an error message to the email added above {email}')
        for _ in range(10):
            time.sleep(1)
            
        raise RuntimeError(f'Ctrl+C not pressed. Sending Runtime Error message to {email}')
            
    function()
    
    
    pass