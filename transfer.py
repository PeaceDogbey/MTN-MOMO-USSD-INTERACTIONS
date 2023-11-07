
#Favourites
    
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

