from Customer import *
class ATM:
    def __init__(self, filename):
        self.filename = filename

    def login(self):
        uuid = str(input("Enter your user id: "))
        pin = str(input("Enter your PIN: "))

        try:
            customer = self.verify_customer(uuid, pin)
        
            choice = self.menu()
            while choice != 4:
                
                if choice == 1:
                    acct = str(input("Please enter the account you would like to withdraw from (s)Savings or (c)Checking: ")).lower()
                    if acct != 's' or acct != 'c':
                        amt = float(input("Please enter the amount you would like to withdraw: "))
                    
                    if acct == 's':
                        if customer.get_savings_bal() > amt:  
                            customer.withdraw(amt, acct)
                            self.replace_line(self.find_line(customer.id, customer.pin), str(customer.id )+ " " +
                                      str(customer.pin) + " " + str(customer.checking_balance) + " " + str(customer.savings_balance))
                            print("Successfully withdrew " + str(amt) + " dollars!")
                        else:
                            print("Insufficient Funds")
                    elif acct == 'c':
                        if customer.get_checking_bal() > amt:  
                            customer.withdraw(amt, acct)
                            self.replace_line(self.find_line(customer.id, customer.pin), str(customer.id )+ " " +
                                      str(customer.pin) + " " + str(customer.checking_balance) + " " + str(customer.savings_balance))
                            print("Successfully withdrew " + str(amt) + " dollars!")
                        else:
                            print("Insufficient Funds")
                    
                    choice = self.menu()
                    
                elif choice == 2:
                    acct = str(input("Please enter the account you would like to deposit into (s)Savings or (c)Checking: ")).lower()
                    if acct != 's' or acct != 'c':
                        amt = float(input("Please enter the amount you would like to deposit: "))
                    
                        
                    customer.deposit(amt, acct)
                    self.replace_line(self.find_line(customer.id, customer.pin), str(customer.id )+ " " +
                                      str(customer.pin) + " " + str(customer.checking_balance) + " " + str(customer.savings_balance))
                    print("Successfully deposited " + str(amt) + " dollars!")
                    choice = self.menu()
                    
                elif choice == 3:
                    acct1 = str(input("Please enter the account you would like to transfer from (s)Savings or (c)Checking: ")).lower()
                    acct2 = str(input("Please enter the account you would like to transfer to (s)Savings or (c)Checking: ")).lower()
                    if acct != 's' or acct != 'c' or acct1 != 's' or acct2 != 'c' or (acct1 == 's' and acct2 == 's') or (acct1 =='c' and acct2 =='s'):
                        amt = float(input("Please enter the amount you would like to transfer: "))

                    customer.transfer(acct1, acct2, amt)
                    self.replace_line(self.find_line(customer.id, customer.pin), str(customer.id )+ " " +
                                      str(customer.pin) + " " + str(customer.checking_balance) + " " + str(customer.savings_balance))
                    print("Successfully transfered " + str(amt) + " dollars!")
                    choice = self.menu()
                    
                elif choice == 4:
                    print("Thank you for using the ATM System")
                    quit()

                else:
                    print("Please enter a valid number (1,2,3,4)")
                    choice = self.menu()        
        except:
            print("Error! Please Try Again")
            self.login()
        
    def menu(self):
        print("\nWelcome to the ATM Main Menu")
        print("'1' -- Withdraw")
        print("'2' -- Deposit")
        print("'3' -- Transfer")
        print("'4' -- Exit")
        choice = int(input("\nPlease enter a choice: "))
        return choice

    def verify_customer(self, cust_id, cust_pin):
        file = open(self.filename, 'r')
        for customer in file:
            uuid, pin, check_bal, sav_bal = customer.split(" ")
            check_bal = int(check_bal)
            sav_bal = int(sav_bal)
            if uuid == str(cust_id) and pin == str(cust_pin):
                return Customer(uuid, pin, check_bal, sav_bal)
        file.close()

    def find_line(self, cust_id, cust_pin):
        file = open(self.filename, 'r')
        for linenum, customer in enumerate(file, 1):
            uuid, pin, check_bal, sav_bal = customer.split(" ")
            check_bal = int(check_bal)
            sav_bal = int(sav_bal)
            if uuid == str(cust_id) and pin == str(cust_pin):
                return linenum
        file.close()
                  
    def replace_line(self, line_num, text):
        lines = open(self.filename, 'r').readlines()
        lines[line_num] = text
        out = open(self.filename, 'w')
        out.writelines(lines)
        out.close()

            
        
def main():
    atm = ATM("accounts.txt")
    atm.login()
main()
