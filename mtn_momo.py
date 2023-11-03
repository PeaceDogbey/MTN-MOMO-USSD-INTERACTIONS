import time
from datetime import datetime
start_time = datetime.now()


#Functions

send_with_care_screen_input = " "
def home_page():
    print('1. Transfer Money')
    print('2. MoMo Pay & Pay Bill')
    print('3. Airtime & Bundles')
    print('4. Allow Cash Out')
    print('5. Financial Services')
    print('6. My Wallet')
    print('7. MoMo Promo')     

def transfer_money_screen():
    print('1. MoMo User')
    print('2. Non MoMo user')
    print('3. Send With Care')
    print('4. Favorite')
    print('5. Other Networks')
    print('6. Bank Account')
    print('0. Back')

def send_with_care_screen():
    print('Send With Care')
    print('1. Mobile User')
    print('2. Mycaretaker')
    print('3. AYO Send With Care Balance or Claim')
    print('0. Back')

def go_back_screen():
    print('1. Exit')
    print('0. Back')

def  send_with_care_screen_3 ():
    print('1. Balances')
    print('2. Mycaretaker')
    print('3. what is send with care?')
    print('4. Claim')
    print('0. Exit')

transfer_money_screen_input =''
def send_with_care_screen_0 (transfer_money_screen_input):
    if transfer_money_screen_input == '1':
        enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
        repeat_number_to_transfer_money =int(input('Confirm Number: '))

        if enter_number_to_transfer_money == repeat_number_to_transfer_money:
            amount_to_transfer_input = float(input('Enter Amount: '))
            print('Payment of {} Ghana Cedis has been successfully sent to +233 {}'.format(amount_to_transfer_input,enter_number_to_transfer_money))

        else: 
            print('Number Mismatched, Try Again')
            
            enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
            repeat_number_to_transfer_money =int(input('Confirm Number: '))

            if enter_number_to_transfer_money == repeat_number_to_transfer_money:
                amount_to_transfer_input = float(input('Enter Amount: '))
                print('Payment of {} Ghana Cedis has been successfully sent to +233 {}' .format(amount_to_transfer_input,enter_number_to_transfer_money))

                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")

    elif transfer_money_screen_input == '2':
        receiver_name_input = input('Enter Receiver Name: ')
        amount_sent_input = float(input('Enter Amount: '))
        reference_number_input = input('Enter Reference: ')
        secret_code_input = int(input('Enter secret code: '))
        confirm_secret_code_input = int(input('Confirm secret code: '))

        if secret_code_input == confirm_secret_code_input:
            print(receiver_name_input)
            print(amount_sent_input)
            print(reference_number_input)
            print('Payment of {} Ghana Cedis has been sent to {} with reference of {}' .format(amount_sent_input,receiver_name_input,reference_number_input))
        else:
            print('Secret code mismatch')
            print('Please Try Again')
            secret_code_input = int(input('Enter secret code: '))
            confirm_secret_code_input = int(input('Confirm secret code: '))
            if secret_code_input == confirm_secret_code_input:
                print(receiver_name_input)
                print(amount_sent_input)
                print(reference_number_input)
                print('Payment of {} Ghana Cedis has been sent to {} with reference of {}' .format(amount_sent_input,receiver_name_input,reference_number_input))
            else:
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")


    elif transfer_money_screen_input == '3':
        send_with_care_screen()
        global send_with_care_screen_input 
        send_with_care_screen_input = input('User Choice: ')
        if send_with_care_screen_input == '1':
            enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                    enter_amount_input = float(input('Please enter Amount: '))
                    send_with_care_reference = input('Enter rererence: ')
                    print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
            else:
                    print("Mobile Number Mismatched")
                    print("Please Try Again")
                    enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                        enter_amount_input = float(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")


        elif send_with_care_screen_input =='2':           
            print('This feature is temporaily unavailable')
            go_back_screen()
            go_back = input('User Input: ')

            if go_back == '1':
                print('Thank you very much of Choosing MTN.')

            elif go_back =='0':
                send_with_care_screen()
                send_with_care_screen_input = input('User Choice: ')

                if send_with_care_screen_input =='1':
                    enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                        enter_amount_input = float(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        print("Mobile Number Mismatched")
                        print("Please Try Again")
                        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                        repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                        if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                            enter_amount_input = float(input('Please enter Amount: '))
                            send_with_care_reference = input('Enter rererence: ')
                            print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                        else:
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

                            

                elif send_with_care_screen_input =='2':           
                    print('This feature is temporaily unavailable')
                    go_back_screen()
                    go_back = input('User Input: ')

                    if go_back == '1':
                        print('Thank you very much of Choosing MTN.')
                    else:
                        current_time = datetime.now()
                        time_diff = current_time - start_time
                        minutes_diff = time_diff * 60
                        if minutes_diff >= 3:
                            print("Network Timeout")

                        

                elif send_with_care_screen_input == '3':
                    send_with_care_screen_3 ()
                    send_with_care_input_3_screen()

                    
                    



        

def  send_with_care_input_3_screen():
        if send_with_care_screen_input == '3':
                send_with_care_screen_3_input = input('user choice ') 
                if send_with_care_screen_3_input == '1':
                    print(' 0.00 balance')
                    print('Thank you')
                    
                elif send_with_care_screen_3_input == '2':
                    print('not subscribed')

                elif send_with_care_screen_3_input == '3':
                    print('This information is currently not available, please try again later')

                elif send_with_care_screen_3_input == '4':
                    print('Sorry, you currently have no claim to this offer contact our customer service to suscribe')

                elif send_with_care_screen_3_input == '0':
                    print('Thank you for using Send With Care') 

        else:
            print('Incorrect input, Cancelled.')

def other_network_screen():
        print('1. Airtel tigo')
        print('2. vodaphone')
        print('3. E-zwish')
        print('4. G-Money')
        print('5. Zeepay')
        print('6. Ghana Pay')
        print('0. Back')
repeat_mobile_number_to_send_with_care=' '
enter_mobile_number_to_send_with_care=' '

def other_network_input_result():
        global enter_mobile_number_to_send_with_care,repeat_mobile_number_to_send_with_care
        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
        repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
        if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
            enter_amount_input = float(input('Please enter Amount: '))
            send_with_care_reference = input('Enter rererence: ')
            print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}'.format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
        else:
            print("Mobile Number Mismatched")
            print("Please Try Again")
            enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                enter_amount_input = float(input('Please enter Amount: '))
                send_with_care_reference = input('Enter rererence: ')
                print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}'.format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
            else:
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")




def bank_account_screen():
    print('BANKS')
    print('1. Assess Bank')
    print('2. Zennith Bank')
    print('3. CAL Bank')




bank_account_number_input =' '
bank_account_result_input=' '
bank_amount_input =' '
def bank_account_input_result():
    print('1. mobile wallet to bank account')
    print('2. Bank account to mobile wallet')
    global bank_account_result_input
    global bank_amount_input
    global bank_account_number_input
    bank_account_result_input=input('user choice: ')
    
    
    if bank_account_result_input == '1':
        bank_account_number_input= int(input('Account Number: '))
        bank_amount_input=float(input('Amount: '))
        print("Payment of",bank_amount_input,'Ghana Cedis has sucessfully been tranfered to',bank_account_number_input, 'Thank you')
    elif bank_account_result_input=='2':
        bank_account_number_input= int(input('Account Number: '))
        
        bank_amount_input=float(input('Amount: '))
        print("Payment of",bank_amount_input,'Ghana Cedis has sucessfully been tranfered to your mobile wallet form ',bank_account_number_input, 'Thank you')

    else:
        print('Cancelled')

def my_wallet():
    print('1. Check Balance')
    print('2. Allow Cash Out')
    print('3. My Approval')
    print('4. Report Fraud')
    print('5. Statement')
    print('6. Change Pin & Reset Pin')
    print('7. Airtime')
    print('8. Check Wallet Limit')
    print('9. Favorite')
    print('10. Name & Next of Kin')
    print('0. Back') 

def allow_cashout_screen ():
    print('Allow Cash Out')
    print('1. Yes')
    print('2. No')
    print('0. Back')
    allow_cashout_input = input("input choice: ")
    if allow_cashout_input == '1':
        print('Cash out allowed')
    elif allow_cashout_input=='2':
        print('cashout not allowed')
    else:
        print('Rejected')


def momopay_paybill(): 
    print('1. MoMo pay')
    print('2. Pay Bills')
    print('3. Gh Pay')
    print('0. Back')

def paybills():
    print('1. Utilities:')
    print('2. TV & Entertainment:')
    print('3. School Fees')
    print('4. MTN Bills') 
    print('5. General Payment')
    print('6. EVD')
    print('0. Back')

def report_fraud_screen():
    print('1. Wrong Transfer')
    print('2. New Reversal')
    print('3. Fake SMS')
    print('4. Fake Blocking')
    print('5. Fake Promotion')
    print('0. Back')








        

enter_frauster_number =' '

def report_fraud_back():
    report_fraud_screen()
    report_fraud_input= input('user choice: ')
    global enter_frauster_number
    if report_fraud_input=="1":
        enter_frauster_number = ("enter frauster's number: ")
        print('Did you send the money')
        print("1. Yes")
        print('No')
        print('0.Back')
        did_you_send = input('user chioce: ')
        if did_you_send =='1':
            print('Your Money would be transfered in 30 minuted')
        elif did_you_send == '2':
            print('Thank you for reporting a fraudster')
        elif did_you_send =='0':
            report_fraud_screen()
        else:
            print('incorrect input')
            current_time = datetime.now()
            time_diff = (current_time - start_time).seconds/60
    
            if time_diff >= 1:
                print("Network Timeout")

    elif report_fraud_input =='2':
        enter_frauster_number = ("enter frauster's number: ")
        print('Did you send the money')
        print("1. Yes")
        print('No')
        print('0.Back')
        did_you_send = input('user chioce: ')
        if did_you_send =='1':
            print('Your Money would be transfered in 30 minuted')
        elif did_you_send == '2':
            print('Thank you for reporting a fraudster')
        elif did_you_send =='0':
            report_fraud_screen()
        else:
            print('incorrect input, please try again')
            report_fraud_screen()
            report_fraud_input= input('user choice: ')
            if report_fraud_input=="1":
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_screen()
                else:
                    print('incorrect input')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")

    elif report_fraud_input =='3':
        enter_frauster_number = int(input("enter frauster's number: "))
        print('Did you send the money')
        print("1. Yes")
        print('No')
        print('0.Back')
        did_you_send = input('user chioce: ')
        if did_you_send =='1':
            print('Your Money would be transfered in 30 minuted')
        elif did_you_send == '2':
            print('Thank you for reporting a fraudster')
        elif did_you_send =='0':
            report_fraud_screen()
        else:
            print('incorrect input, please try again')
            report_fraud_screen()
            report_fraud_input= input('user choice: ')
            if report_fraud_input=="1":
                enter_frauster_number = int(input("enter frauster's number: "))

            
                print('Did you send the money')
                print("1. Yes")
                print('No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_screen()
                else:
                    print('incorrect input')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")

    elif report_fraud_input =='4':
        enter_frauster_number = int(input("enter frauster's number: "))
        print('Did you send the money')
        print("1. Yes")
        print('No')
        print('0.Back')
        did_you_send = input('user chioce: ')
        if did_you_send =='1':
            print('Your Money would be transfered in 30 minuted')
        elif did_you_send == '2':
            print('Thank you for reporting a fraudster')
        elif did_you_send =='0':
            report_fraud_screen()
        else:
            print('incorrect input, please try again')
            report_fraud_screen()
            report_fraud_input= input('user choice: ')
            if report_fraud_input=="1":
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_screen()
                else:
                    print('incorrect input')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")

    elif report_fraud_input =='5':
        enter_frauster_number = int(input("enter frauster's number: "))
        print('Did you send the money')
        print("1. Yes")
        print('No')
        print('0.Back')
        did_you_send = input('user chioce: ')
        if did_you_send =='1':
            print('Your Money would be transfered in 30 minuted')
        elif did_you_send == '2':
            print('Thank you for reporting a fraudster')
        elif did_you_send =='0':
            report_fraud_screen()
        else:
            print('incorrect input, please try again')
            report_fraud_screen()
            report_fraud_input= input('user choice: ')
            if report_fraud_input=="1":
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_screen()
                else:
                    print('incorrect input')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")

    else:
        current_time = datetime.now()
        time_diff = (current_time - start_time).seconds/60
    
        if time_diff >= 1:
            print("Network Timeout")


def self_reset_input_screen():
    global self_pin_reset_input 
    self_pin_reset_input = input('user choice: ')
    global add_recovery_number
    global enter_new_mm_pin_code_input
    global  enter_old_mm_pin_code_input
    if self_pin_reset_input == '1':
        add_recovery_number = input('Add Recovery Number: ')
        print('Your recovery number is +233 ', add_recovery_number)

    elif self_pin_reset_input == '2':
        print(add_recovery_number)

    elif self_pin_reset_input=='3':
        print('You do not have recovery number')
    
    elif self_pin_reset_input== '4':
        print('You do not have recovery number')

    elif self_pin_reset_input =='0':
        print('1. Self pin Reset')
        print('0. Back')
        self_reset_input = input('user choice: ')
        if self_reset_input=='1':
            print('1. Add Recovery Contact')
            print('2. Remove Recovery Contact')
            print('3. View Recovery Contact')
            print('4. Pin Reset')
            print('0. Back')


        
            self_pin_reset_input ==''
            self_pin_reset_input = input('user choice: ')
            add_recovery_number ==''
            global enter_new_mm_pin_code_input
            global  enter_old_mm_pin_code_input
            if self_pin_reset_input == '1':
                add_recovery_number = input('Add Recovery Number: ')
                print('Your recovery number is +233 ', add_recovery_number)

            elif self_pin_reset_input == '2':
                print(add_recovery_number)

            elif self_pin_reset_input=='3':
                print('You do not have recovery number')
            
            elif self_pin_reset_input== '4':
                print('You do not have recovery number')
            else: 
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")

                


        elif self_reset_input =='0':
                print('1. Change Pin')
                print('2. Reset Pin')
                reset_pin_input = input('User Choice: ')
                if reset_pin_input == '1':
                   enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                   enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                   print('Pin Code has Successfully been changed, Thank You.')
        else: 
            current_time = datetime.now()
            time_diff = (current_time - start_time).seconds/60
    
            if time_diff >= 1:
                print("Network Timeout")


            
    
    
def change_next_of_kin():
    change_next_of_kin = input('User choice: ')
    if change_next_of_kin =='1':
        new_next_of_kin_number = int(input('Enter Phone number of your new next of kin: '))
        new_next_of_kin_first_name = input('Enter First name of your new next of kin: ')
        new_next_of_kin_last_name = input('Enter Last name of your new next of kin: ')
        print('You have entered {} {} as new next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
        print('1. Confirm')
        print('2. Cancel')
        confirm_new_next_of_kin = input('user choice: ')
        if confirm_new_next_of_kin =='1':
            enter_pin_to_confirm = input('Enter pin: ')
            print('{} {} has successfully been make the next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
        elif confirm_new_next_of_kin =='2':
            print('cancelled')
        else:
            print("incorrect input, please try again")
            change_next_of_kin = input('User choice: ')
            if change_next_of_kin =='1':
                new_next_of_kin_number = int(input('Enter Phone number of your new next of kin: '))
                new_next_of_kin_first_name = input('Enter First name of your new next of kin: ')
                new_next_of_kin_last_name = input('Enter Last name of your new next of kin: ')
                print('You have entered {} {} as new next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                print('1. Confirm')
                print('2. Cancel')
                confirm_new_next_of_kin = input('user choice: ')
                if confirm_new_next_of_kin =='1':
                    enter_pin_to_confirm = input('Enter pin: ')
                    print('{} {} has successfully been make the next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                elif confirm_new_next_of_kin =='2':
                    print('cancelled')
                else:
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                       print("Network Timeout")
                    
                    

            else:
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                   print("Network Timeout")

    else:
        current_time = datetime.now()
        time_diff = (current_time - start_time).seconds/60
    
        if time_diff >= 1:
            print("Network Timeout")
            





            
#Main codes 


home_page()
home_page_input = input("select choice: ")
current_time = datetime.now()
time_diff = (current_time - start_time).seconds/60
    
if time_diff >= 1:
    print("Network Timeout")

else:
    if home_page_input == "1":
        transfer_money_screen()
        transfer_money_screen_input = input('Select choice: ')

        current_time = datetime.now()
        time_diff = (current_time - start_time).seconds/60
    
        if time_diff >= 1:
            print("Network Timeout")






        else:
            if transfer_money_screen_input == '1':
                enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
                
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
                if time_diff >= 1:
                    print("Network Timeout")
                else:     
                    repeat_number_to_transfer_money =int(input('Confirm Number: '))




                if enter_number_to_transfer_money == repeat_number_to_transfer_money:
                    amount_to_transfer_input = float(input('Enter Amount: '))
                    
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60

                    if time_diff >= 1:
                        print("Network Timeout")
                    else:
                        print('Payment of {} Ghana Cedis has been successfully sent to +233 {}'.format(amount_to_transfer_input,enter_number_to_transfer_money))

                else: 
                    print('Number Mismatched, Try Again')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")

        
                    else:
                        enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                                print("Network Timeout")
                        else:
                            repeat_number_to_transfer_money =int(input('Confirm Number: '))

                            if enter_number_to_transfer_money == repeat_number_to_transfer_money:
                                amount_to_transfer_input = float(input('Enter Amount: '))
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")
                                else:  
                                    print('Payment of {} Ghana Cedis has been successfully sent to +233 {}' .format(amount_to_transfer_input,enter_number_to_transfer_money))
                                

            
            elif transfer_money_screen_input == '2':
                receiver_name_input = input('Enter Receiver Name: ')
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")
                else:
                    amount_sent_input = float(input('Enter Amount: '))

                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")
                        
                    else:
                        reference_number_input = input('Enter Reference: ')
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")
                        else:
                            secret_code_input = int(input('Enter secret code: '))
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")
                            else:
                                confirm_secret_code_input = int(input('Confirm secret code: '))

                                if secret_code_input == confirm_secret_code_input:
                                    print(receiver_name_input)
                                    print(amount_sent_input)
                                    print(reference_number_input)
                                    print('Payment of {} Ghana Cedis has been sent to {} with reference of {}' .format(amount_sent_input,receiver_name_input,reference_number_input))
                                else:
                                    print('Secret code mismatch')
                                    print('Please Try Again')
                                    secret_code_input = int(input('Enter secret code: '))
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")
                                    else:
                                        confirm_secret_code_input = int(input('Confirm secret code: '))

                                        if secret_code_input == confirm_secret_code_input:
                                            print(receiver_name_input)
                                            print(amount_sent_input)
                                            print(reference_number_input)
                                            print('Payment of {} Ghana Cedis has been sent to {} with reference of {}' .format(amount_sent_input,receiver_name_input,reference_number_input))
                                        else:
                                            print("Network Timeout")
                                        




 #send_with_care
            elif transfer_money_screen_input == '3':
                send_with_care_screen()
                send_with_care_screen_input = input('User Choice: ')
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")

                else:
                    if send_with_care_screen_input == '1':
                        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number: "))
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")
                        else:
                            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number: '))
                            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                                enter_amount_input = float(input('Please enter Amount: '))
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")
                                else:
                                    send_with_care_reference = input('Enter rererence: ')
                                    print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                            else:
                                print("Mobile Number Mismatched")
                                print("Please Try Again")
                                enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")
                                else:
                                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                                        enter_amount_input = float(input('Please enter Amount: '))
                                        send_with_care_reference = input('Enter rererence: ')
                                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                                    else:
                                        current_time = datetime.now()
                                        time_diff = (current_time - start_time).seconds/60
    
                                        if time_diff >= 0.005:
                                            print("Network Timeout")




                    elif send_with_care_screen_input =='2':           
                        print('This feature is temporaily unavailable')
                        go_back_screen()
                        go_back = input('User Input: ')
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")
                        else:   

                            if go_back == '1':
                                print('Thank you very much of Choosing MTN.')

                            elif go_back =='0':
                                send_with_care_screen()
                                send_with_care_screen_input = input('User Choice: ')
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")


                                else:
                                    if send_with_care_screen_input == '1':
                                        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number: "))
                                        current_time = datetime.now()
                                        time_diff = (current_time - start_time).seconds/60
    
                                        if time_diff >= 1:
                                            print("Network Timeout")

                                        else:
                                            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number: '))
                                            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                                                enter_amount_input = float(input('Please enter Amount: '))
                                                current_time = datetime.now()
                                                time_diff = (current_time - start_time).seconds/60
    
                                                if time_diff >= 1:
                                                    print("Network Timeout")

                                                else:
                                                    send_with_care_reference = input('Enter rererence: ')
                                                    current_time = datetime.now()
                                                    time_diff = (current_time - start_time).seconds/60
    
                                                    if time_diff >= 1:
                                                        print("Network Timeout")
                                                    else:
                                                        enter_pin= input('Enter Pin: ')
                                                        current_time = datetime.now()
                                                        time_diff = (current_time - start_time).seconds/60
    
                                                        if time_diff >= 1:
                                                            print("Network Timeout")


                                                        else:
                                                            print("Payment of"{}'Ghana Cedis has been sucessfully sent to +233'{}'with reference of'{}.format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                                            else:
                                                print("Mobile Number Mismatched. Please Try Again")
                            
                                                enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                                                current_time = datetime.now()
                                                time_diff = (current_time - start_time).seconds/60
    
                                                if time_diff >= 1:
                                                     print("Network Timeout")
                                                else:
                                                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                                                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                                                        enter_amount_input = float(input('Please enter Amount: '))
                                                        current_time = datetime.now()
                                                        time_diff = (current_time - start_time).seconds/60
    
                                                        if time_diff >= 1:
                                                            print("Network Timeout")
                                                        else:
                                                            send_with_care_reference = input('Enter rererence: ')
                                                            current_time = datetime.now()
                                                            time_diff = (current_time - start_time).seconds/60
    
                                                            if time_diff >= 1:
                                                                print("Network Timeout")
                                                            else:
                                                                enter_pin = input('Enter pin: ')
                                                                current_time = datetime.now()
                                                                time_diff = (current_time - start_time).seconds/60
    
                                                                if time_diff >= 1:
                                                                    print("Network Timeout")
                                                                else:
                                                                    print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                        


                                    elif send_with_care_screen_input =='2':
                                        print('This feature is temporaily unavailable')

                                        go_back_screen()
                                        go_back = input('User Input: ')
                                        current_time = datetime.now()
                                        time_diff = (current_time - start_time).seconds/60
    
                                        if time_diff >= 1:
                                            print("Network Timeout")

                                        else:
                                            if go_back == '1':
                                                print('Thank you very much of Choosing MTN.')
                                            elif go_back == '0':
                                                current_time = datetime.now()
                                                time_diff = (current_time - start_time).seconds/60
    
                                                if time_diff >= 1:
                                                    print("Network Timeout")


                                    elif send_with_care_screen_input == '3':
                                        send_with_care_screen_3()
                                        send_with_care_screen_3_input = input('user choice: ')
                                        current_time = datetime.now()
                                        time_diff = (current_time - start_time).seconds/60
    
                                        if time_diff >= 1:
                                            print("Network Timeout")


            
                                        else:
                                            if send_with_care_screen_3_input == '1':
                                                    print(' 0.00 balance')
                                                    print('Thank you')
                    
                                            elif send_with_care_screen_3_input == '2':
                                                print('Not subscribed')

                                            elif send_with_care_screen_3_input == '3':
                                                    print('This information is currently not available, please try again later')

                                            elif send_with_care_screen_3_input == '4':
                                                    print('Sorry, you currently have no claim to this offer contact our customer service to suscribe')

                                            elif send_with_care_screen_3_input == '0':
                                                    print('Thank you for using Send With Care') 

                                            elif send_with_care_screen_input == '0':
                                                send_with_care_screen_0()      
                        
#Favourites
            elif transfer_money_screen_input == '4':
                print('Favourites') 
                print('1. Name')
                print('2. Find')
                print('0. Back')
                favourite_screen_input = input('user choice: ')
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")

                else:
        
                    if favourite_screen_input == '1':
                        enter_name =input('Enter Name: ')
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")

                        else:
                            enter_pin =input('Enter Pin: ')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

                            else:
                                print('No contact found.')

                    elif favourite_screen_input == '2':
                        enter_name =input('Enter Name: ')
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")

                        else:
                            enter_pin =input('Enter Pin: ')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

                            else:
                                print('No contact found.')

                    elif favourite_screen_input =='0':
                        transfer_money_screen()
                    else:
                        print('Invalid input, please try again')
                        favourite_screen_input = input('user choice: ')
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")

                        else:
                            if favourite_screen_input == '1':
                                enter_name =input('Enter Name: ')
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")

                                else:
                                    enter_pin =input('Enter Pin: ')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")

                                    else:
                                        print('No contact found.')

                            elif favourite_screen_input == '2':
                                enter_name =input('Enter Name: ')
                                current_time = datetime.now()
                                time_diff = (current_time - start_time).seconds/60
    
                                if time_diff >= 1:
                                    print("Network Timeout")

                                else:
                                    enter_pin =input('Enter Pin: ')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")
                                    else:    
                                        print('No contact found.')

                            elif favourite_screen_input =='0':
                                transfer_money_screen()
                            else:
                                print('incorrect input, please try again later')
                    
#other networks
            elif transfer_money_screen_input == '5':
                    other_network_screen()
                    other_networks_screen_input =input('user choice: ')
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")
                    else:    
                        if other_networks_screen_input =='1':
                            other_network_input_result()
                        elif other_networks_screen_input == '2':
                            other_network_input_result()
                        elif other_networks_screen_input =='3':
                            other_network_input_result()
                        elif other_networks_screen_input =='4':
                            other_network_input_result()
                        elif other_networks_screen_input=='5':
                            other_network_input_result()
                        elif other_networks_screen_input =='6':
                            other_network_input_result()
                        elif other_networks_screen_input == '0':
                            other_network_screen()
                
                        else:
                            print('Incorrect Input')
                            print('Please Try Again')
                            other_networks_screen_input =input('user choice: ')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")
                            else:    
                                if other_networks_screen_input =='1':
                                    other_network_input_result()
                                elif other_networks_screen_input == '2':
                                    other_network_input_result()
                                elif other_networks_screen_input =='3':
                                    other_network_input_result()
                                elif other_networks_screen_input =='4':
                                    other_network_input_result()
                                elif other_networks_screen_input=='5':
                                    other_network_input_result()
                                elif other_networks_screen_input =='6':
                                    other_network_input_result()
                                elif other_networks_screen_input == '0':
                                    print("Please try again later")

#Bank Account
            elif transfer_money_screen_input== '6':
                bank_account_screen()
                bank_accout_screen_input = input('User choice: ')
                if bank_accout_screen_input == '1':
                    print('Assess Bank')
                    bank_account_input_result()
                elif bank_accout_screen_input == '2':
                    print('Zennith Bank')
                    bank_account_input_result()
                elif bank_accout_screen_input == '3':
                    print('CAl Bank')
                    bank_account_input_result()    

            

            
#Back
            elif transfer_money_screen_input == '0':
                home_page()
                home_page_input=input('user choice: ')
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")
                
 




#momo pay
    elif home_page_input == '2':
        momopay_paybill()
        momo_pay_input =input("input choice: ")
        current_time = datetime.now()
        time_diff = (current_time - start_time).seconds/60
    
        if time_diff >= 1:
            print("Network Timeout")
        else:
            if momo_pay_input == '1':
                merchant_id_input =int(input('Enter Merchant id / Payment Reference: '))
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")
                else:
                    print('You would receive a message shortly')

            elif momo_pay_input == '2':
                paybills()
                pay_bills_input = input('user choice: ')
                current_time = datetime.now()
                time_diff = (current_time - start_time).seconds/60
    
                if time_diff >= 1:
                    print("Network Timeout")
                else:
                    if pay_bills_input == '1':
                        print('1. ECG') 
                        print('2. Ghana Water') 
                        print('0. Back')
                        paybills_result_input= input('user choice: ')


                    elif pay_bills_input == '2':
                        print('1. DStv/GOtv') 
                        print('2. Startimes') 
                        print('3. GCNET Payment')
                        print('0. Back')
                        tv_entertainament_input=input('user choice: ')            
                        if tv_entertainament_input=='1':
                            print("Currently not available")
                        elif tv_entertainament_input == '2':
                            print("Currently not available")
                        elif tv_entertainament_input == '3':
                            print("Currently not available")
                        elif tv_entertainament_input=='0':
                            home_page()
                
                    elif pay_bills_input== '3':
                        name_of_school = input('Enter name of school: ')
                        amount_to_be_paid = float(input('Enter amount: '))

                    elif pay_bills_input == '4':
                        print('To be worked on')

                    elif pay_bills_input =='5':
                        print('To be worked on')

                    elif pay_bills_input=='6':
                        print('To be worked on')

                    elif pay_bills_input=='0':
                     home_page()


    elif home_page_input =='3':
        print('1. Airtime') 
        print('2. Internet bundle') 
        print('3. Fixed Broadband') 
        print('4. Schedule Airtime')
        print('0. Back')
        airtime_bundle_input = input('input choice ')
        current_time = datetime.now()
        time_diff = (current_time - start_time).seconds/60
    
        if time_diff >= 1:
            print("Network Timeout")
        else:
            if airtime_bundle_input =='0':
                home_page()

            elif airtime_bundle_input == '1':
                print('1. Self')
                print('2. Others')
                print("3. Welcome Back")
                print('4. Other networks')
                print('0. Back')
           
                airtime_input = input('User choice: ')

        
           if airtime_input == '1':
                amount_sent_to_self = float(input('Amount: '))
                print('Payment made for airtime of',amount_sent_to_self,'Ghana Cedis has been sent to' self,'. Should the Transaction be continued')
                print('1. Yes')
                print('2. No')
                yes_no_input = input('User choice: ')
                if yes_no_input == '1':
                    print('Payment for airtime of',amount_sent_to_self,'has been made to',self,'Thank you.')
                else:
                    print('Cancelled')

           elif airtime_input == '2':
                other_amount = float(input('Amount: '))
                other_number = int(input('Enter Number: '))
                repeat_other_number=int(input('Repeat Number: '))

                if other_number == repeat_other_number:
                    print('Payment for Airtime has been made for',other_number,'Ghana Cedis to',other_amount)
                else:
                    print('Number mismatched')

           elif airtime_input == '3':
                print('Currently not available')

           elif airtime_input == '4':
                B1 = int(input('Enter Recipient Number: '))
                B2 = int(input('Re_enter Recipient Number: '))
                if B1==B2:
                    B3 = float(input('Enter Amount minimum of 0.20, maximum of 500: '))
                    print('Payment of {0} for airtime has been sucessfully sent to +233{1}'.format(B1,B2))
                else:
                    print('Number mismatched')
                    print('Cancelled')

        elif airtime_bundle_input == '2':
            print('Welcome to Bundle Portal. Please select your bundle.')
            print('1. Buy Data Bundle')
            print('2. Midnight Bundles')
            print('3. Kokrokoo Bundle')
            print('4. Social Media Bundle')
            print('5. Video Bundles')
            print('6. IDD Bundles')
            print('7. More')
            print('0. Back')
            bundle_portal_input = input('User Choice: ')

            if bundle_portal_input == '1':
                print('Please enter your choice')
                print('1. Buy for self')
                print('2. Buy for others')
                buy_data_bundle_input =('User choice: ')

                if buy_data_bundle_input == '1':
                    print('1. Flexi bundle(GHC 0.03 - 399)')
                    print('2. GHC 0.5 (24.05 MB)')
                    print('3. GHC1 (48.10 MB)')
                    print('4. GHC 3 (471.70 MB)')
                    print('5. GHC 10 (971.82 MB)')
                    print('6. GHC 399 (214.09 GB)')
                    print('0. Back')
                    bundle_for_self_input = input('User choice: ')

                    if bundle_for_self_input == '1':
                        enter_amount_to_bundle_for_self_input = float(input('Enter amount to buy preferred bundle: '))
                        if enter_amount_to_bundle_for_self_input == "0.5":
                            print("Y'ello the GHC 0.5 Data bundle will give you 24.05 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            

                        elif enter_amount_to_bundle_for_self_input == "0.6":
                            print("Y'ello the GHC 0.6 Data bundle will give you 24.55 MB") 
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    

                        elif enter_amount_to_bundle_for_self_input == '1':
                            print("Y'ello the GHC 1.0 Data bundle will give you 48.1 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    

                        elif enter_amount_to_bundle_for_self_input == '1.5':
                            print("Y'ello the GHC 1.5 Data bundle will give you 50 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            
                    
                        elif enter_amount_to_bundle_for_self_input == '2':
                            print("Y'ello the GHC 2.0 Data bundle will give you 50.55 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            

                        elif enter_amount_to_bundle_for_self_input == '3':
                            print("Y'ello the GHC 3.0 Data bundle will give you 471.70 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            

                        elif enter_amount_to_bundle_for_self_input == '10':
                            print("Y'ello the GHC 10.0 Data bundle will give you 971.82 MB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            

                        elif enter_amount_to_bundle_for_self_input == '339':
                            print("Y'ello the GHC 399.0 Data bundle will give you 214.09 GB")
                            print('This bundle does not expire')
                            choose_one_to_buy = input('1. Buy: ')
                            if choose_one_to_buy == '1':
                                print('Choose Payment Mode')
                                print('1. Airtime')
                                print('2. Mobile Money')
                                choose_payment_mode_input = input('User Choice: ')

                                if choose_payment_mode_input == '1':
                                    print('Your Balance is insufficient to buy this bundle, choose')
                                    print('1. Mobile Money')
                                    print('0. Cancel')
                                    momo_for_bundle_payment = input('User Choice: ')
                                    if momo_for_bundle_payment == "1":
                                        print('You would soon receive a prompt')
                                    else:
                                        print('cancelled')
                                elif choose_payment_mode_input == "2":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')    
                            else:
                                print('Incorrect Input, Cancelled')    
                            
                    elif bundle_for_self_input == '2':
                        print("Y'ello The GHS 0.5 Data Bundle will give 24.05 MB.") 
                        print("This bundle does not expire")
                        choose_one_to_buy = input('1. Buy: ')
                        if choose_one_to_buy == '1':
                            print('Choose Payment Mode')
                            print('1. Airtime')
                            print('2. Mobile Money')
                            choose_payment_mode_input = input('User Choice: ')

                            if choose_payment_mode_input == '1':
                                print('Your Balance is insufficient to buy this bundle, choose')
                                print('1. Mobile Money')
                                print('0. Cancel')
                                momo_for_bundle_payment = input('User Choice: ')
                                if momo_for_bundle_payment == "1":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')
                            elif choose_payment_mode_input == "2":
                                print('You would soon receive a prompt')
                            else:
                                print('cancelled')    
                        else:
                            print('Incorrect Input, Cancelled') 


                    elif bundle_for_self_input == "3":
                        print("Y'ello The GHS 1.0 Data Bundle will give 48.10 MB.") 
                        print("This bundle does not expire")
                        choose_one_to_buy = input('1. Buy: ')
                        if choose_one_to_buy == '1':
                            print('Choose Payment Mode')
                            print('1. Airtime')
                            print('2. Mobile Money')
                            choose_payment_mode_input = input('User Choice: ')

                            if choose_payment_mode_input == '1':
                                print('Your Balance is insufficient to buy this bundle, choose')
                                print('1. Mobile Money')
                                print('0. Cancel')
                                momo_for_bundle_payment = input('User Choice: ')
                                if momo_for_bundle_payment == "1":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')
                            elif choose_payment_mode_input == "2":
                                print('You would soon receive a prompt')
                            else:
                                print('cancelled')    
                        else:
                            print('Incorrect Input, Cancelled')

                    elif bundle_for_self_input =='4':
                        print("Y'ello The GHS 3.0 Data Bundle will give 471.70 MB.") 
                        print("This bundle does not expire")
                        choose_one_to_buy = input('1. Buy: ')
                        if choose_one_to_buy == '1':
                            print('Choose Payment Mode')
                            print('1. Airtime')
                            print('2. Mobile Money')
                            choose_payment_mode_input = input('User Choice: ')

                            if choose_payment_mode_input == '1':
                                print('Your Balance is insufficient to buy this bundle, choose')
                                print('1. Mobile Money')
                                print('0. Cancel')
                                momo_for_bundle_payment = input('User Choice: ')
                                if momo_for_bundle_payment == "1":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')
                            elif choose_payment_mode_input == "2":
                                print('You would soon receive a prompt')
                            else:
                                print('cancelled')    
                        else:
                            print('Incorrect Input, Cancelled') 

                    elif bundle_for_self_input == '5':
                        print("Y'ello The GHS 10.0 Data Bundle will give 971.82 MB.") 
                        print("This bundle does not expire")
                        choose_one_to_buy = input('1. Buy: ')
                        if choose_one_to_buy == '1':
                            print('Choose Payment Mode')
                            print('1. Airtime')
                            print('2. Mobile Money')
                            choose_payment_mode_input = input('User Choice: ')

                            if choose_payment_mode_input == '1':
                                print('Your Balance is insufficient to buy this bundle, choose')
                                print('1. Mobile Money')
                                print('0. Cancel')
                                momo_for_bundle_payment = input('User Choice: ')
                                if momo_for_bundle_payment == "1":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')
                            elif choose_payment_mode_input == "2":
                                print('You would soon receive a prompt')
                            else:
                                print('cancelled')    
                        else:
                            print('Incorrect Input, Cancelled')

                    elif bundle_for_self_input =='6':
                        print("Y'ello The GHS 399.00 Data Bundle will give 214.09 MB.") 
                        print("This bundle does not expire")
                        choose_one_to_buy = input('1. Buy: ')
                        if choose_one_to_buy == '1':
                            print('Choose Payment Mode')
                            print('1. Airtime')
                            print('2. Mobile Money')
                            choose_payment_mode_input = input('User Choice: ')

                            if choose_payment_mode_input == '1':
                                print('Your Balance is insufficient to buy this bundle, choose')
                                print('1. Mobile Money')
                                print('0. Cancel')
                                momo_for_bundle_payment = input('User Choice: ')
                                if momo_for_bundle_payment == "1":
                                    print('You would soon receive a prompt')
                                else:
                                    print('cancelled')
                            elif choose_payment_mode_input == "2":
                                print('You would soon receive a prompt')
                            else:
                                print('cancelled')    
                        else:
                            print('Incorrect Input, Cancelled')        

#allow cashout
    elif home_page_input == '4':
        allow_cashout_screen()

#financial services
    elif home_page_input == '5':
        print('1. Bank services') 
        print('2. Savings') 
        print('3. Loans') 
        print('4. Pension and Investment') 
        print('5. Insurance') 
        print('6. Trade shares') 
        print('0. Back')
        financial_services_input = input('input choice: ')

        if financial_services_input== '1':
            print('1. Transfer to Bank')
            print('2. Transfer from Bank')
            print('3. ATM Cashout')
            print('4. Card Services')
            print('0. Back')
            bank_services_input = input('User choice: ')


        else:
            print("Cancelled")


#my wallet
    elif home_page_input =='6':
            my_wallet()
            my_wallet_input = input('input choice: ')

            if my_wallet_input == '1':
                enter_user_pin= int(input('Enter Pin: '))
                print('Your account balance is 1000.00 Ghana Cedis')


            elif my_wallet_input == '2':
                allow_cashout_screen()

            elif my_wallet_input== '3':
                print('No pending approvals')

#report fraud
            elif my_wallet_input== '4':
                report_fraud_screen()
                report_fraud_input= input('user choice: ')
            
                if report_fraud_input=="1":
                    enter_frauster_number = int(input("enter frauster's number: "))
                    print('Did you send the money')
                    print("1. Yes")
                    print('2. No')
                    print('0.Back')
                    did_you_send = input('user chioce: ')
                    if did_you_send =='1':
                        print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_back()
                else:
                    print('incorrect input, please try again')
                    report_fraud_screen()
                    report_fraud_input= input('user choice: ')
                    if report_fraud_input=="1":
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

                    elif report_fraud_input =='2':
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input, please try again')
                            report_fraud_screen()
                            report_fraud_input= input('user choice: ')
                            if report_fraud_input=="1":
                                enter_frauster_number = int(input("enter frauster's number: "))
                                print('Did you send the money')
                                print("1. Yes")
                                print('No')
                                print('0.Back')
                                did_you_send = input('user chioce: ')
                                if did_you_send =='1':
                                    print('Your Money would be transfered in 30 minuted')
                                elif did_you_send == '2':
                                    print('Thank you for reporting a fraudster')
                                elif did_you_send =='0':
                                    report_fraud_back()
                                else:
                                    print('incorrect input')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")

                    elif report_fraud_input =='3':
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input, please try again')
                            report_fraud_screen()
                            report_fraud_input= input('user choice: ')
                            if report_fraud_input=="1":
                                enter_frauster_number = int(input("enter frauster's number: "))
                                print('Did you send the money')
                                print("1. Yes")
                                print('2. No')
                                print('0.Back')
                                did_you_send = input('user chioce: ')
                                if did_you_send =='1':
                                    print('Your Money would be transfered in 30 minuted')
                                elif did_you_send == '2':
                                    print('Thank you for reporting a fraudster')
                                elif did_you_send =='0':
                                    report_fraud_back()
                                else:
                                    print('incorrect input')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")

                    elif report_fraud_input =='4':
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user choice: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input, please try again')
                            report_fraud_screen()
                            report_fraud_input= input('user choice: ')
                            if report_fraud_input=="1":
                                enter_frauster_number = int(input("enter frauster's number: "))
                                print('Did you send the money')
                                print("1. Yes")
                                print('2. No')
                                print('0.Back')
                                did_you_send = input('user chioce: ')
                                if did_you_send =='1':
                                    print('Your Money would be transfered in 30 minuted')
                                elif did_you_send == '2':
                                    print('Thank you for reporting a fraudster')
                                elif did_you_send =='0':
                                    report_fraud_back()
                                else:
                                    print('incorrect input')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")

                    elif report_fraud_input =='5':
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minute, sorry for any inconvinience.')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input, please try again')
                            report_fraud_screen()
                            report_fraud_input= input('user choice: ')
                            if report_fraud_input=="1":
                                enter_frauster_number = int(input("enter frauster's number: "))
                                print('Did you send the money')
                                print("1. Yes")
                                print('2. No')
                                print('0.Back')
                                did_you_send = input('user chioce: ')
                                if did_you_send =='1':
                                    print('Your Money would be transfered in 30 minute,sorry for any inconvinience.')
                                elif did_you_send == '2':
                                    print('Thank you for reporting a fraudster')
                                elif did_you_send =='0':
                                    report_fraud_back()
                                else:
                                    print('incorrect input')
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")

                    else:
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")

                    
                    

            elif report_fraud_input =='2':
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('2. No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minute, sorry for any inconvinience.')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_back()
                else:
                    print('incorrect input, please try again')
                    report_fraud_screen()
                    report_fraud_input= input('user choice: ')
                    if report_fraud_input=="1":
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

            elif report_fraud_input =='3':
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('2. No')
                print('0.Back')
                did_you_send = input('user choice: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minute,sorry for any inconvinience.')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_back()
                else:
                    print('incorrect input, please try again')
                    report_fraud_screen()
                    report_fraud_input= input('user choice: ')
                    if report_fraud_input=="1":
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minute, sorry for any inconvinience.')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input')
                            current_time = datetime.now()
                            time_diff = current_time - start_time
                            minutes_diff = time_diff * 60
                            if minutes_diff >= 3:
                                print("Network Timeout")


            elif report_fraud_input =='4':
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('2. No')
                print('0.Back')
                did_you_send = input('user choice: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minuted')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_back()
                else:
                    print('incorrect input, please try again')
                    report_fraud_screen()
                    report_fraud_input= input('user choice: ')
                    if report_fraud_input=="1":
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minute, sorry for any inconvinience.')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")


            elif report_fraud_input =='5':
                enter_frauster_number = int(input("enter frauster's number: "))
                print('Did you send the money')
                print("1. Yes")
                print('2. No')
                print('0.Back')
                did_you_send = input('user chioce: ')
                if did_you_send =='1':
                    print('Your Money would be transfered in 30 minute, sorry for any inconvinience.')
                elif did_you_send == '2':
                    print('Thank you for reporting a fraudster')
                elif did_you_send =='0':
                    report_fraud_back()
                else:
                    print('incorrect input, please try again')
                    report_fraud_screen()
                    report_fraud_input= input('user choice: ')
                    if report_fraud_input=="1":
                        enter_frauster_number = int(input("enter frauster's number: "))
                        print('Did you send the money')
                        print("1. Yes")
                        print('2. No')
                        print('0.Back')
                        did_you_send = input('user chioce: ')
                        if did_you_send =='1':
                            print('Your Money would be transfered in 30 minuted')
                        elif did_you_send == '2':
                            print('Thank you for reporting a fraudster')
                        elif did_you_send =='0':
                            report_fraud_back()
                        else:
                            print('incorrect input')
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")
                            
                            


            elif report_fraud_input =='0':
                my_wallet()

        elif my_wallet_input =='5':
            print('Your stament would be sent to you via SMS. Thank you.')


            #reset pin
        elif my_wallet_input == '6':
            print('1. Change Pin')
            print('2. Reset Pin')
            reset_pin_input = input('User Choice: ')
            if reset_pin_input == '1':
                enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                print('Pin Code has Successfully been changed, Thank You.')

            elif reset_pin_input == '2':
                print('1. Self pin Reset')
                print('0. Back')
                self_reset_input = input('user choice: ')
                if self_reset_input=='1':
                    print('1. Add Recovery Contact')
                    print('2. Remove Recovery Contact')
                    print('3. View Recovery Contact')
                    print('4. Pin Reset')
                    print('0. Back')
                    self_reset_input_screen()


                elif self_reset_input =='0':
                    print('1. Change Pin')
                    print('2. Reset Pin')
                    reset_pin_input = input('User Choice: ')
                    if reset_pin_input == '1':
                        enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                        enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                        print('Pin Code has Successfully been changed, Thank You.')

                    elif reset_pin_input == '2':
                        print('1. Self pin Reset')
                        print('0. Back')
                        self_reset_input = input('user choice: ')
                        if self_reset_input=='1':
                            print('1. Add Recovery Contact')
                            print('2. Remove Recovery Contact')
                            print('3. View Recovery Contact')
                            print('4. Pin Reset')
                            print('0. Back')
                            self_reset_input_screen()
                        else:
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")


                else:
                    print('Incorrect Input, please choose correct')
                    print('1. Change Pin')
                    print('2. Reset Pin')
                    reset_pin_input = input('User Choice: ')
                    if reset_pin_input == '1':
                        enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                        enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                        print('Pin Code has Successfully been changed, Thank You.')

                    elif reset_pin_input == '2':
                        print('1. Self pin Reset')
                        print('0. Back')
                        self_reset_input = input('user choice: ')
                        if self_reset_input=='1':
                            print('1. Add Recovery Contact')
                            print('2. Remove Recovery Contact')
                            print('3. View Recovery Contact')
                            print('4. Pin Reset')
                            print('0. Back')
                            self_reset_input_screen()

                        elif self_reset_input =='0':
                            print('1. Change Pin')
                            print('2. Reset Pin')
                            reset_pin_input = input('User Choice: ')
                            if reset_pin_input == '1':
                                enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                                enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                                print('Pin Code has Successfully been changed, Thank You.')

                            elif reset_pin_input == '2':
                                print('1. Self pin Reset')
                                print('0. Back')
                                self_reset_input = input('user choice: ')
                                if self_reset_input=='1':
                                    print('1. Add Recovery Contact')
                                    print('2. Remove Recovery Contact')
                                    print('3. View Recovery Contact')
                                    print('4. Pin Reset')
                                    print('0. Back')
                                    self_reset_input_screen()
                                else:
                                    current_time = datetime.now()
                                    time_diff = (current_time - start_time).seconds/60
    
                                    if time_diff >= 1:
                                        print("Network Timeout")




        elif my_wallet_input == '7':
            print('Select Transaction')
            print('1. 0555728522 - GhC 15')
            print('Kindly confirm the reversal of GHC 15 airtime to 0555728522 on 4-NOV-2022 10:07 PM to your wallet at a fee of GHC 0.00 T&C Apply.')
            reversal_of_airtime_input = input('User Choice: ')
            if reversal_of_airtime_input =='1':
                print("Y'ello, kindly not that 0555728522 does not have enough airtime to fulfill your reversal request of GHC 15.00.")
            else:
                print('Incorrect input please try again')
                print('Select Transaction')
                print('1. 0555728522 - GhC 15')
                print('Kindly confirm the reversal of GHC 15 airtime to 0555728522 on 4-NOV-2022 10:07 PM to your wallet at a fee of GHC 0.00 T&C Apply.')
                reversal_of_airtime_input = input('User Choice: ')
                if reversal_of_airtime_input =='1':
                    print("Y'ello, kindly not that 0555728522 does not have enough airtime to fulfill your reversal request of GHC 15.00.")
                else:
                    current_time = datetime.now()
                    time_diff = (current_time - start_time).seconds/60
    
                    if time_diff >= 1:
                        print("Network Timeout")



        elif my_wallet_input == '8':
            check_wallet_code_input = input('Enter MM Code: ')
            print(' Your Daily limit is GHS 5000.00. You have used GHS 0.00. Your balance left is GHS 5000.00. No monthly limit is available.')


        elif my_wallet_input == '9':
            print('Favorite')
            print('1. Add Favourite')
            print('2. Delect Favourite')
            print('0. Back') 
            my_wallet_favourite_input = ('User Choice: ')
            if my_wallet_favourite_input =='1':
                my_wallet_enter_favourite_name= input('Enter Name: ')
                my_wallet_enter_favourite_number= input('Enter Number: ')
                my_wallet_repeat_favourite_number = input('Repeat Number: ')
                if my_wallet_enter_favourite_number == my_wallet_repeat_favourite_number:
                    my_wallet_favourite_enter_pin = input('Enter MM Pin Code: ')
                    print('New name was added successfully' )
                else:
                    print('Number mismatched, please try again')
                    my_wallet_enter_favourite_number= input('Enter Number: ')
                    my_wallet_repeat_favourite_number = input('Repeat Number: ')
                    if my_wallet_enter_favourite_number == my_wallet_repeat_favourite_number:
                        my_wallet_favourite_enter_pin = input('Enter MM Pin Code: ')
                        print('New name was added successfully' )
                    else:
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")

            elif my_wallet_favourite_input =='2':
                print('currently not available')

            elif my_wallet_favourite_input =='0':
                print('yet to work on')

        elif my_wallet_input =='10':
            print('Check wallet name & Next of kin, walllet name: Peace Dogbey, Next of kin: Peace Dogbey.')
            print('1. Change Next of kin')
            change_next_of_kin = input('User choice: ')
            if change_next_of_kin =='1':
                new_next_of_kin_number = int(input('Enter Phone number of your new next of kin: '))
                new_next_of_kin_first_name = input('Enter First name of your new next of kin: ')
                new_next_of_kin_last_name = input('Enter Last name of your new next of kin: ')
                print('You have entered {} {} as new next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                print('1. Confirm')
                print('2. Cancel')
                confirm_new_next_of_kin = input('user choice: ')
                if confirm_new_next_of_kin =='1':
                    enter_pin_to_confirm = input('Enter pin: ')
                    print('{} {} has successfully been make the next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                elif confirm_new_next_of_kin =='2':
                    print('cancelled')
                else:
                    print("incorrect input, please try again")
                    change_next_of_kin = input('User choice: ')
                    if change_next_of_kin =='1':
                        new_next_of_kin_number = int(input('Enter Phone number of your new next of kin: '))
                        new_next_of_kin_first_name = input('Enter First name of your new next of kin: ')
                        new_next_of_kin_last_name = input('Enter Last name of your new next of kin: ')
                        print('You have entered {} {} as new next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                        print('1. Confirm')
                        print('2. Cancel')
                        confirm_new_next_of_kin = input('user choice: ')
                        if confirm_new_next_of_kin =='1':
                            enter_pin_to_confirm = input('Enter pin: ')
                            print('{} {} has successfully been make the next of kin' .format(new_next_of_kin_first_name,new_next_of_kin_last_name))
                        elif confirm_new_next_of_kin =='2':
                            print('cancelled')
                        else:
                            current_time = datetime.now()
                            time_diff = (current_time - start_time).seconds/60
    
                            if time_diff >= 1:
                                print("Network Timeout")

                    else:
                        current_time = datetime.now()
                        time_diff = (current_time - start_time).seconds/60
    
                        if time_diff >= 1:
                            print("Network Timeout")


            else:
                print('Incorrect input, please try again')
                change_next_of_kin()


        

        elif my_wallet_input == '0':
            home_page()
            home_page_input= input("select choice: ")

    elif home_page_input == '7':
        print('1. MoMo Promo Checker')
        print('2. weekly Promo Checker')
        print('0. Back')
        user_stage_7 = input('User choice: ')
        if user_stage_7 =='1':
            print("Y'ello, you have earned 14 points in the MoMo promo. Pay more and send more to stand a chance of winning exciting e-cash prices.")
        elif user_stage_7 =='2':
            print('Error occured. Please try after some time')

        elif user_stage_7 == '0':
            home_page()
            home_page_input = input("select choice: ") 

