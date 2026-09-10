name = input("Enter guest name: ")
room = input("Enter room number: ")
date = input("Enter check-in date: ")

print("\nHOTEL REGISTRATION")
print("Name:", name)
print("Room:", room)
print("Date:", date)

id = input("Enter guest ID: ")

if id.isdigit():
    print("ID contains only numbers")
else:
    print("ID contains letters or symbols")