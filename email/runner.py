from datetime import datetime
import time
import traceback as tb

from email_pkg import send_email

try:
    ts = time.time()
    
    ###### START ######
    for _ in range(10):
        time.sleep(.1)
    ####### END #######
        
    send_email(subject='Done!', body=f'Took {time.time()-ts:3.2f} seconds', attachments=['some_file.txt'])
    
except:
    e = tb.format_exc()
    send_email(subject='Error occured', body=f'Time: {datetime.today().strftime("%Y-%m-%d %Hh%Mm%Ss")}\n\nERROR:\n\n{e}\n-----')
    print('ERROR:\n\n',e)
finally:
    print('DONE!')

