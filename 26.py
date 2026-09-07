investment = float(input("Enter investment: "))
rate = float(input("Enter return percentage: "))

return_amount = investment * rate / 100
final_amount = investment + return_amount

print("Return:", return_amount)
print("Final Amount:", final_amount)

accounts = {}

n = int(input("Enter number of accounts: "))

for i in range(n):
    account_number = input("Enter account number: ")
    balance = float(input("Enter account balance: "))

    accounts[account_number] = balance

print("Account Details:", accounts)