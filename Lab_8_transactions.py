from Lab_8_library import BankAccount

def main():
    # Creating 2 bank accounts and performing some transactions

    
    account1 = BankAccount(100, 1) # Keeping Initial bank balance 100
    account2 = BankAccount(100, 2) # Keeping Initial bank balance 100
 

    accounts_objects_list = [account1, account1] # A list of 2 bank accounts


    #Withdraw 40 respectively.
    account1.withdraw(40)
    account2.withdraw(40)


    #Display balance for all accounts
    account1.get_balance()
    account2.get_balance()


    #Deposit 20 respectively.
    account1.deposit(20)
    account2.deposit(20)


    #Display balance for all accounts
    account1.get_balance()
    account2.get_balance()


    #Transfer 20 from second account to the first one
    account2.transfer(20, 1)


    #Display balance for all accounts
    account1.get_balance()
    account2.get_balance()

if __name__ == "__main__":
    main()