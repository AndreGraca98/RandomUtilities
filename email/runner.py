from datetime import datetime
import time
import traceback as tb

from email_class import Email


def email_notification(func):
    def wrapper(*args, **kwargs): 
        try:
            func(*args, **kwargs)
            
        except:
            e = tb.format_exc()
            Email()(subject='Error occured !', body=f'Time: {datetime.today().strftime("%Y-%m-%d %Hh%Mm%Ss")}\n\nERROR:\n\n{e}\n-----')
            print('ERROR:\n\n',e)
        finally:
            print('DONE!')
            
    return wrapper 
    
    

@email_notification
def example_func(a, b=99):
    for _ in range(10):
        time.sleep(.1)
        
    print(a, b)

if __name__ == '__main__':
    example_func(123, b=54)
