import time
from datetime import datetime
start_time = datetime.now()


#Functions

def time():
    current_time = datetime.now()
    time_diff = (current_time - start_time).seconds/60
    
    if time_diff >= 1:
        print("Network Timeout")


#main code
receiver_name_input = input('Enter Receiver Name: ')
iftime()    
amount_sent_input = float(input('Enter Amount: '))
reference_number_input = input('Enter Reference: ')
secret_code_input = int(input('Enter secret code: '))
confirm_secret_code_input = int(input('Confirm secret code: '))
