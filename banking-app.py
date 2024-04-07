print("Welcome to my banking app... \n")

while True:
    balance = input("Enter your current balance: ")

    if balance.isnumeric():
        balance = int(balance)
        if balance > 0:
            print("Your balance is " + str(balance))
            break

    print("HINT: Please enter a positive number...\n")

while True:
    print("""
    Please select an option:
        1: Deposit Amount
        2: Withdraw Amount
        3: Check Current Balance
    
    Enter "exit" to Exit App
    """)

    choice = input("Option: ")

    if choice == "1":
        while True:
            deposit = input("\nEnter Amount: ")
            if deposit.isnumeric():
                deposit = int(deposit)
                if deposit > 0:
                    balance += deposit
                    print("Your balance is " + str(balance))
                    break

    elif choice == "2":
        while True:
            withdraw = input("\nEnter Amount: ")
            if withdraw.isnumeric():
                withdraw = int(withdraw)
                if withdraw > 0:
                    if balance - withdraw > 0:
                        balance -= withdraw
                        print("Your balance is " + str(balance))
                        break
                    else:
                        print("Insufficient funds to withdraw.\n")

    elif choice == "3":
        print("\nYour balance is " + str(balance))

    elif choice == "exit":
        exit()

    else:
        print("\nPlease select a valid option!!!\n")
