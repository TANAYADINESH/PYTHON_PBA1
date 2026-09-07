principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

interest = principal * rate * time / 100
total = principal + interest

print("Interest:", interest)
print("Total Repayment:", total)

id = input("Enter customer ID: ")
name = input("Enter customer name: ")
loan = float(input("Enter loan amount: "))

customer = (id, name, loan)

print("ID:", customer[0])
print("Name:", customer[1])
print("Loan:", customer[2])