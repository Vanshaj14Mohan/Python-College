def create_account():
  account_number = input("Enter account number: ")
  name = input("Enter account holder name: ")
  initial_balance = float(input("Enter initial balance: "))
  accounts[account_number] = {"name": name, "balance": initial_balance}
  print("Account created successfully!")

def deposit_money():
  account_number = input("Enter account number: ")
  if account_number not in accounts:
    print("Account not found.")
    return
  amount = float(input("Enter amount to deposit: "))
  accounts[account_number]["balance"] += amount
  print("Deposit successful!")

def withdraw_money():
  account_number = input("Enter account number: ")
  if account_number not in accounts:
    print("Account not found.")
    return
  amount = float(input("Enter amount to withdraw: "))
  if amount > accounts[account_number]["balance"]:
    print("Insufficient balance.")
    return
  accounts[account_number]["balance"] -= amount
  print("Withdrawal successful!")

def check_balance():
  account_number = input("Enter account number: ")
  if account_number not in accounts:
    print("Account not found.")
    return
  print("Account balance:", accounts[account_number]["balance"])

accounts = {}

while True:
  print("\nBanking System Menu:")
  print("1. Create Account")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Check Balance")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    create_account()
  elif choice == '2':
    deposit_money()
  elif choice == '3':
    withdraw_money()
  elif choice == '4':
    check_balance()
  elif choice == '5':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")