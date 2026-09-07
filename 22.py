price = float (input("Enter price: "))
tax_percent = float (input("Enter tax percentage: "))
tax_amount = price * tax_percent / 100
total_price = price + tax_amount
print ("Tax Amount:", tax_amount)
print ("Total Price:", total_price)         

categories = set()
n = int(input("Enter number of categories: "))
for i in range(n):
    category = input("Enter category name: ")
    categories.add(category)
print ("Categories:", categories)    