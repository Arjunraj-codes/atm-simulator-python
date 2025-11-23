# ATM Simulator Project

accounts = {
    1: [50000, 1234],
    2: [3000, 4321],
    3: [5000, 5678],
    4: [12000, 8765],
    5: [43000, 7890]
}

while True:
    card = int(input("Enter your card number: "))

    if card in accounts:
        pin = int(input("Enter your PIN: "))

        if pin == accounts[card][1]:

            print("\n----- ATM MENU -----")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Exit")
            print("---------------------\n")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = int(input("Enter withdrawal amount: "))
                accounts[card][0] -= amount
                print("Withdrawal Successful!")
                print("Remaining Balance:", accounts[card][0])

            elif choice == 2:
                amount = int(input("Enter deposit amount: "))
                accounts[card][0] += amount
                print("Deposit Successful!")
                print("Updated Balance:", accounts[card][0])

            elif choice == 3:
                print("Your Total Balance:", accounts[card][0])

            elif choice == 4:
                old_pin = int(input("Enter current PIN: "))

                if old_pin == accounts[card][1]:
                    new_pin = int(input("Enter new PIN: "))
                    accounts[card][1] = new_pin
                    print("PIN changed successfully!")
                else:
                    print("Incorrect current PIN!")

            elif choice == 5:
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Try again.")

        else:
            print("Incorrect PIN!")

    else:
        print("Invalid card number!")
