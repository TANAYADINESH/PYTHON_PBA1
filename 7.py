name = input("Enter account holder name: ")
transaction = input("Enter transaction type: ")
amount = float(input("Enter amount: "))
balance = float(input("Enter balance: "))

print("\nATM RECEIPT")
print("Name:", name)
print("Transaction:", transaction)
print("Amount:", amount)
print("Balance:", balance)

account = input("Enter account number: ")

if len(account) > 4:
    account = "*" * (len(account) - 4) + account[-4:]

print("Account Number:", account)