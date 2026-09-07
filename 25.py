bill = float(input("Enter bill: "))
discount_percent = float(input("Enter discount percentage: "))

discount = bill * discount_percent / 100
final_bill = bill - discount

print("Discount:", discount)
print("Final Bill:", final_bill)

customer1 = []
customer2 = []

n = int(input("Enter items for Customer 1: "))

for i in range(n):
    item = input("Enter item: ")
    customer1.append(item)

n = int(input("Enter items for Customer 2: "))

for i in range(n):
    item = input("Enter item: ")
    customer2.append(item)

print("Common Items:")

for item in customer1:
    if item in customer2:
        print(item)