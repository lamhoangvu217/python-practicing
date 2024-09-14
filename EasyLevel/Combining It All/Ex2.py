# Create a program that simulates a simple ATM. 
# The user should be able to check their balance, deposit money, and withdraw money using a menu-driven interface. 
# Implement control flow to handle various choices.

def atm_simulation():
    balance = 500  # Initial balance
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Your current balance is: {balance}")
        elif choice == 2:
            depositQuantity = int(input("How much money you want to deposit?: "))
            balance += depositQuantity
            print(input(f"Deposit successfully. Your current balance is {balance}"))
        elif choice == 3:
            moneyWithdraw = int(input("How much money you want to withdraw?: "))
            if (moneyWithdraw > balance):
                print(f"Withdraw money must be smaller than your balance. Your current balance is: {balance}")
            else:
                balance -= moneyWithdraw
                print(input(f"Withdraw successfully. Your current balance is {balance}"))
        elif choice == 4:
            print("Exited")
            break
        else:
            print("Don't have any choice suitable for you, please try again")
atm_simulation()