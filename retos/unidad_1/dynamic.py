# Dynamic
#
# Representation Scenario: Simulating a bank account.
#
# Task: Create a program that uses a dynamic data structure (like a list) to represent a bank account's transaction history. The program should allow users to:
#
# Deposit money: Add a transaction record with the amount and type "deposit". Withdraw money: Add a transaction record with the amount and type "withdrawal". View transaction history: Display all transactions in chronological order. Check balance: Calculate the current balance based on all transactions. Example:


""" """
transactions = []

def deposit(amount):
  transactions.append({'type': 'deposit', 'amount': amount})

def withdraw(amount):
  transactions.append({'type': 'withdrawal', 'amount': amount})

def view_history():
  for transaction in transactions:
    print(f"{transaction['type'].capitalize()}: {transaction['amount']}")

def check_balance():
  balance = 0
  for transaction in transactions:
    if transaction['type'] == 'deposit':
      balance += transaction['amount']
    else:
      balance -= transaction['amount']
  return balance

# Example usage
deposit(1000)
withdraw(200)
deposit(500)

view_history()
print(f"Current balance: {check_balance()}")
