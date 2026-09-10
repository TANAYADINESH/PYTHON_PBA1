name = input("Enter customer name: ")
table = input("Enter table number: ")
food = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = quantity * price

print("\nRESTAURANT BILL")
print("Customer:", name)
print("Table:", table)
print("Food:", food)
print("Quantity:", quantity)
print("Price:", price)
print("Total:", total)

orders = input("Enter food orders: ")
search = input("Enter food to search: ")

if search in orders:
    print("Food is available")
else:
    print("Food is not available")