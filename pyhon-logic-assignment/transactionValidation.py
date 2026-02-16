balance=int(input("Enter your acc balance: "))
amount=int(input("Enter withdraw amount: "))
status= bool(input("Verification status (Yes/No): "))

if amount<=balance and status==True:
    print("Withdrawal successful")
else:
    print("Withdrawal denied")