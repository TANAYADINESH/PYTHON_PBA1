customer = input("Enter customer name: ")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = quantity * price

print("\nPURCHASE INVOICE")
print("Customer:", customer)
print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Total:", total)

code = input("Enter product code: ")

if code.startswith("PROD"):
    print("Code starts with PROD")
else:
    print("Code does not start with PROD")