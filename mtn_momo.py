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
            amount_to_transfer_input = int(input('Enter Amount: '))
            print('Payment of {} Ghana Cedis has been successfully sent to +233 {}'.format(amount_to_transfer_input,enter_number_to_transfer_money))

        else: 
            print('Number Mismatched, Try Again')
            
            enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
            repeat_number_to_transfer_money =int(input('Confirm Number: '))

            if enter_number_to_transfer_money == repeat_number_to_transfer_money:
                amount_to_transfer_input = float(input('Enter Amount: '))
                print('Payment of {} Ghana Cedis has been successfully sent to +233 {}' .format(amount_to_transfer_input,enter_number_to_transfer_money))
            else:
                print("Network Timeout")

    elif transfer_money_screen_input == '2':
        receiver_name_input = input('Enter Receiver Name: ')
        amount_sent_input = int(input('Enter Amount: '))
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
                print("Network Timeout")
 
    elif transfer_money_screen_input == '3':
        send_with_care_screen()
        global send_with_care_screen_input 
        send_with_care_screen_input = input('User Choice: ')
        if send_with_care_screen_input == '1':
            enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                    enter_amount_input = int(input('Please enter Amount: '))
                    send_with_care_reference = input('Enter rererence: ')
                    print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
            else:
                    print("Mobile Number Mismatched")
                    print("Please Try Again")
                    enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                        enter_amount_input = int(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        print('Network Timeout')
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
                        enter_amount_input = int(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        print("Mobile Number Mismatched")
                        print("Please Try Again")
                        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                        repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                        if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                            enter_amount_input = int(input('Please enter Amount: '))
                            send_with_care_reference = input('Enter rererence: ')
                            print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                        else:
                            print('Network Timeout')
                elif send_with_care_screen_input =='2':           
                    print('This feature is temporaily unavailable')
                    go_back_screen()
                    go_back = input('User Input: ')

                    if go_back == '1':
                        print('Thank you very much of Choosing MTN.')
                    else:
                        print('Network Timeout')
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
            enter_amount_input = int(input('Please enter Amount: '))
            send_with_care_reference = input('Enter rererence: ')
            print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}'.format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
        else:
            print("Mobile Number Mismatched")
            print("Please Try Again")
            enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                enter_amount_input = int(input('Please enter Amount: '))
                send_with_care_reference = input('Enter rererence: ')
                print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}'.format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
            else:
                print('Network Timeout')



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
        
        bank_amount_input=int(input('Amount: '))
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








#variable list
tv_station =['1. DStv/GOtv','2. Startimes','3. GCNET Payment',
            '0. Back']
pay_bills =['1. ECG','2. Ghana Water','0. Back']

airtime_or_bundle =['1. Airtime','2. Internet bundle','3. Fixed Broadband','4. Schedule Airtime','0. Back']
        
financial_services=['1. Bank services', '2. Savings','3. Loans','4. Pension and Investment','5. Insurance','6. Trade shares','0. Back']
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
            print('Network Timeout')
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
                    print('Network Timeout')
    elif report_fraud_input =='3':
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
                    print('Network Timeout')
    elif report_fraud_input =='4':
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
                    print('Network Timeout')
    elif report_fraud_input =='5':
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
                    print('Network Timeout')
    else:
        print('Network Timeout')

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
                print('Network Timeout')
                


        elif self_reset_input =='0':
                print('1. Change Pin')
                print('2. Reset Pin')
                reset_pin_input = input('User Choice: ')
                if reset_pin_input == '1':
                   enter_old_mm_pin_code_input =input('Enter old MM Pin Code: ')
                   enter_new_mm_pin_code_input = input('Enter New MM Pin Code: ')
                   print('Pin Code has Successfully been changed, Thank You.')
        else: 
            print('Network Timeout')

            
    
    
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
                    print("Network Timeout")
            else:
                print('Network Timeout')
    else:
        print('Network Timeout')            


    







       
              
       
            
      
                       


            
           


    
    
















        

















            
    #Main codes  
         
home_page()
home_page_input = input("select choice: ")

if home_page_input == "1":
    transfer_money_screen()
    transfer_money_screen_input = input('Select choice: ')

#momo_user
    if transfer_money_screen_input == '1':
        enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
        repeat_number_to_transfer_money =int(input('Confirm Number: '))

        if enter_number_to_transfer_money == repeat_number_to_transfer_money:
            amount_to_transfer_input = int(input('Enter Amount: '))
            print('Payment of {} Ghana Cedis has been successfully sent to +233 {}'.format(amount_to_transfer_input,enter_number_to_transfer_money))

        else: 
            print('Number Mismatched, Try Again')
            
            enter_number_to_transfer_money = int(input('Enter MoMo Number: '))
            repeat_number_to_transfer_money =int(input('Confirm Number: '))

            if enter_number_to_transfer_money == repeat_number_to_transfer_money:
                amount_to_transfer_input = int(input('Enter Amount: '))
                print('Payment of {} Ghana Cedis has been successfully sent to +233 {}' .format(amount_to_transfer_input,enter_number_to_transfer_money))
            else:
                print("Network Timeout")





#non_momo_user
    elif transfer_money_screen_input == '2':
        receiver_name_input = input('Enter Receiver Name: ')
        amount_sent_input = int(input('Enter Amount: '))
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
                print("Network Timeout")



 #send_with_care
    elif transfer_money_screen_input == '3':
        send_with_care_screen()
        send_with_care_screen_input = input('User Choice: ')

        if send_with_care_screen_input == '1':
            enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number: "))
            repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number: '))
            if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                    enter_amount_input = int(input('Please enter Amount: '))
                    send_with_care_reference = input('Enter rererence: ')
                    print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
            else:
                    print("Mobile Number Mismatched")
                    print("Please Try Again")
                    enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                        enter_amount_input = int(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        print('Network Timeout')



        elif send_with_care_screen_input =='2':           
            print('This feature is temporaily unavailable')
            go_back_screen()
            go_back = input('User Input: ')

            if go_back == '1':
                print('Thank you very much of Choosing MTN.')

            elif go_back =='0':
                send_with_care_screen()
                send_with_care_screen_input = input('User Choice: ')

                if send_with_care_screen_input == '1':
                    enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number: "))
                    repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number: '))
                    if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                        enter_amount_input = int(input('Please enter Amount: '))
                        send_with_care_reference = input('Enter rererence: ')
                        print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                    else:
                        print("Mobile Number Mismatched")
                        print("Please Try Again")
                        enter_mobile_number_to_send_with_care  = int(input("Please enter recipient mobile number "))
                        repeat_mobile_number_to_send_with_care =int(input('please repeat recipient number '))
                        if enter_mobile_number_to_send_with_care==repeat_mobile_number_to_send_with_care:
                            enter_amount_input = int(input('Please enter Amount: '))
                            send_with_care_reference = input('Enter rererence: ')
                            print('Payment of {} Ghana Cedis has been sucessfully sent to +233 {} with reference of {}' .format(enter_amount_input,enter_mobile_number_to_send_with_care,send_with_care_reference))
                        else:
                            print('Network Timeout')
                elif send_with_care_screen_input =='2':
                    print('This feature is temporaily unavailable')

                    go_back_screen()
                    go_back = input('User Input: ')

                    if go_back == '1':
                        print('Thank you very much of Choosing MTN.')
                    elif go_back == '0':
                        print('Network Timeout')
                elif send_with_care_screen_input == '3':
                    send_with_care_screen_3()
                    send_with_care_screen_3_input = input('user choice: ') 
            
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


        elif send_with_care_screen_input == '3':
            send_with_care_screen_3()
            send_with_care_screen_3_input = input('user choice: ') 
    
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


        elif send_with_care_screen_input == '0':
            send_with_care_screen_0(transfer_money_screen_input) 
       
                        
#Favourites
    elif transfer_money_screen_input == '4':
        print('Favourites') 
        print('1. Name')
        print('2. Find')
        print('0. Back')
        favourite_screen_input = input('user choice: ')
        if favourite_screen_input == '1':
            enter_name =input('Enter Name: ')
            enter_pin =input('Enter Pin: ')
            print('No contact found.')
        elif favourite_screen_input == '2':
            enter_name =input('Enter Name: ')
            enter_pin =input('Enter Pin: ')
            print('No contact found.')
        elif favourite_screen_input =='0':
            transfer_money_screen()
        else:
            print('Invalid input, please try again')
            favourite_screen_input = input('user choice: ')
            if favourite_screen_input == '1':
                enter_name =input('Enter Name: ')
                enter_pin =input('Enter Pin: ')
                print('No contact found.')
            elif favourite_screen_input == '2':
                enter_name =input('Enter Name: ')
                enter_pin =input('Enter Pin: ')
                print('No contact found.')
            elif favourite_screen_input =='0':
                transfer_money_screen()
            else:
                print('Network Timeout')
    



#other networks
    elif transfer_money_screen_input == '5':
        other_network_screen()
        other_networks_screen_input =input('user choice: ')
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
            if other_networks_screen_input =='1':
                other_network_input_result()
            elif other_networks_screen_input =='2':
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
                print('Network Timeout')
            else:
                print('Network Timeout')
        else:
            print('Incorrect Input')
            print('Please Try Again')
            other_networks_screen_input =input('user choice: ')
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
                print('Network timeout')
            else:
                print('Network Timeout')


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
 




#momo pay

elif home_page_input == '2':
    momopay_paybill()
    momo_pay_input =input("input choice: ")
    

    if momo_pay_input == '1':
        merchant_id_input =int(input('Enter Merchant id / Payment Reference: '))

    elif momo_pay_input == '2':
        paybills()
        pay_bills_input = input('user choice: ')



        if pay_bills_input == '1':
            for paybill in pay_bills:
                print(paybill)

            paybills_result_input= input('user choice: ')

        elif pay_bills_input == '2':
            for tv_station in tv_station:
                print(tv_station)
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
        for airtime_and_bundle in airtime_or_bundle:
            print(airtime_or_bundle)
        airtime_bundle_input = input('input choice ')


        if airtime_bundle_input =='0':
          home_page()

        elif airtime_bundle_input == '1':
           print('1. Self')
           print('2. Others')
           print("3. Welcome Back")
           print('4. Other networks')
           print('0. Back')
           self =' '
           airtime_input = input('User choice: ')

           if airtime_input == '0':
                for airtime_and_bundle in airtime_or_bundle:
                    print(airtime_or_bundle)
                    airtime_bundle_input = input('input choice ')

           elif airtime_input == '1':
                amount_sent_to_self = float(input('Amount: '))
                print('Payment made for airtime of',amount_sent_to_self,'Ghana Cedis has been sent to',self,'. Should the Transaction be continued')
                yes = input('1. Yes: ')
                no = input('2. No')
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
            print('0. Back ')
            


#allow cashout
elif home_page_input == '4':
    allow_cashout_screen()

   
#financial services
elif home_page_input == '5':
    for financial_sevice in financial_services:
        print(financial_sevice)
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
                enter_frauster_number = ("enter frauster's number: ")
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
                        enter_frauster_number = ("enter frauster's number: ")
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
                            print('Network Timeout')
                    elif report_fraud_input =='2':
                        enter_frauster_number = ("enter frauster's number: ")
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
                                    report_fraud_back()
                                else:
                                    print('incorrect input')
                                    print('Network Timeout')
                    elif report_fraud_input =='3':
                        enter_frauster_number = ("enter frauster's number: ")
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
                                enter_frauster_number = ("enter frauster's number: ")
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
                                    print('Network Timeout')
                    elif report_fraud_input =='4':
                        enter_frauster_number = ("enter frauster's number: ")
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
                                enter_frauster_number = ("enter frauster's number: ")
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
                                    print('Network Timeout')
                    elif report_fraud_input =='5':
                        enter_frauster_number = ("enter frauster's number: ")
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
                                enter_frauster_number = ("enter frauster's number: ")
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
                                    print('Network Timeout')
                    else:
                        print('Network Timeout')
                    
                    

            elif report_fraud_input =='2':
                enter_frauster_number = ("enter frauster's number: ")
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
                        enter_frauster_number = ("enter frauster's number: ")
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
                            print('Network Timeout')

            elif report_fraud_input =='3':
                enter_frauster_number = ("enter frauster's number: ")
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
                        enter_frauster_number = ("enter frauster's number: ")
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
                            print('Network Timeout')

            elif report_fraud_input =='4':
                enter_frauster_number = ("enter frauster's number: ")
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
                        enter_frauster_number = ("enter frauster's number: ")
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
                            print('Network Timeout')

            elif report_fraud_input =='5':
                enter_frauster_number = ("enter frauster's number: ")
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
                        enter_frauster_number = ("enter frauster's number: ")
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
                            print('Network Timeout')

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
                   print('Network Timeout')


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
                        print('Network Timeout') 
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
                            print("Network Timeout")
                    else:
                        print('Network Timeout')

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






    













 