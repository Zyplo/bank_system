HOME = '''
-----------------------------------------------------------------------------
                                    Welcome to our Bank!! --------------------        
                                        ---------------------------------------------
  @     @     @  ======= ==    =        [A]- Deposit.----------------
  @@   @@@   @@  ===   =  ==  =         [B]- Extract.--------------
  @@@@@@@@@@@@@  =======    ==          [C]- Serve.-------------
  @@@@@@@@@@@@@  ===        =           (S)- Stop system.-----------
----------------------------------------------------------------------------------
        ---------------------------------------------------------------
            ---------------------- The Python Bank!!-------------------------
                   -------------------------------------------------
Type here:
'''

account = 0
MAX = 500
extract = ""
MAX_WITH = 3
num_with = int(0)



while True:

    option = input(HOME)

    if option == "A":
        value = float(input("How much you want to deposit? \n"))
        if value > 0:
            account += value  
            extract += f"Deposit:      US$ {value:2f}"
            print(extract)
        else:
            print("TYPE ERROR!!")


    elif option =="a":
        value = float(input("How much you want to deposit? \n"))
        if value > 0:
            account += value  
            extract += f"Deposit:      US${value:2}\n" 
            print(extract) 
        else:
            print("TYPE ERROR!!")
    
    elif option == "B":
        value = float(input("The Extract value:   "))
        more_account  = value > account
        more_bank = value > MAX
        more_with  = num_with >= MAX_WITH
        if more_account:
            print("Error: Exceeded the maximum withdrawal amount.")
        elif more_bank:
            print("Error: The withdrawal amount exceeds the limit ")
        elif more_with:
            print("Error: Maximum number of withdrawals exceeded ")
        elif value > 0:
            account -= value
            extract += f"Withdrawal: US${value:.2f}"
            num_with += 1
            print(extract) 

    elif option =="b":
        value = float(input("The Extract value:\n"))
        more_account  = value > account
        more_bank = value > MAX
        more_with  = num_with >= MAX_WITH
        if more_account:
            print("Error: Exceeded the maximum withdrawal amount.")
        elif more_bank:
            print("Error: The withdrawal amount exceeds the limit ")
        elif more_with:
            print("Error: Maximum number of withdrawals exceeded ")
        elif value > 0:
            account -= value
            extract += f"Withdrawal: US${value:.2f}"
            num_with += 1
            print(extract) 
              
    elif option == "C":
        print("================\=======^==============Extract===============^=========/================")
        print("No translations yet" if not extract else extract)
        print(f"Account:  US${value:2}\n")    
        print("================\=======^==============Extract===============^=========/================")

    elif option =="c":
        print("================\=======^==============Extract===============^=========/================")
        print("No translations yet" if not extract else extract)
        print(f"Account:  US${value:2}\n")    
        print("================\=======^==============Extract===============^=========/================")

    
    elif option == "S":
        print("THANKS FOR USE THE PYTHON BANK!!!")
        input(
        '''
        @@@@@@@@@/The Python Bank\@@@@@@@@@@@
        =====================================
        @@@@@@Tell us your feedback:***@@@@@@
        @@@@@@(1) Really bad **********@@@@@@
        @@@@@@(2) Bad *****************@@@@@@
        @@@@@@(3) Average *************@@@@@@
        @@@@@@(4) Good ****************@@@@@@
        @@@@@@(5) Perfect *************@@@@@@
        =====================================
        ''')
    elif option =="s":
         print("THANKS FOR USE THE PYTHON BANK!!!")
         feedback = input(
        '''
        @@@@@@@@@/The Python Bank\@@@@@@@@@@@
        =====================================
        @@@@@@Tell us your feedback:***@@@@@@
        @@@@@@(1) Bad *****************@@@@@@
        @@@@@@(2) Average *************@@@@@@
        @@@@@@(3) Good ****************@@@@@@
        =====================================
        ''' ) 
         if feedback == "1": 
             print('''
Contact me and I hope I can solve your problem:
email:                   
mateushleonardi@gmail.com                   
                   ''')
             break
         elif feedback == "2":
            print(''' 
Fell free for give us a suggestion of what to do: 
contact my email: 
mateushleonardi@gmail.com
                  ''')
            break
         elif feedback == "3":
             print('''
Thanks and enjoy it!                   

''')   
             break
         else:
             print("TYPE ERROR!!")
             break
            
    else:
        print("TYPE_ERROR: this type characather is not acepteded! Try Again!")

            
            
