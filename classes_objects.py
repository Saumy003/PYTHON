# Creating a cute atm operating program using the concept of classes & objects.

class Atm :
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input=input("""
Hii, How can I help you?
1. Press 1 to create a pin 
2. Press 2 to change the pin 
3. Press 3 to check balance
4. Press 4 to withdraw the amount
""")
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter the PIN:")
        self.pin = user_pin 

        user_balance = int(input("Enter your current balance:"))
        self.balance = user_balance

        print("Your pin is created sucessfully")
        self.menu()

    def change_pin(self):
        current_pin = input("Enter the current pin:")

        if self.pin == current_pin:
            new_pin = input("Enter the New PIN:")
            self.pin = new_pin
            print("Your PIN has been changed successfully!")
            self.menu()

        else:
            print("nai karne de sakta re baba")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN:")

        if self.pin == user_pin:
            print("Your bank balance is:" , self.balance)
            self.menu()

        else:
            print("chal nikal yahan se")
            self.menu()

    def withdraw(self):
        user_pin = input("Enter the PIN:")

        if user_pin == self.pin:
            amount = int(input("Enter the withdwawl amount:"))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdwawal successful.. visit again, your current balance is: " , self.balance)

            else:
                print("abe garib")

        else:
            print("sale chor")
        self.menu()
     
obj = Atm()                          # object
        


    
    
