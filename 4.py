name = input("Enter passenger name: ")
bus = input("Enter bus number: ")
source = input("Enter source: ")
destination = input("Enter destination: ")
fare = float(input("Enter fare: "))

print("\nBUS TICKET")
print("Passenger:", name)
print("Bus:", bus)
print("Source:", source)
print("Destination:", destination)
print("Fare:", fare)

dest = input("Enter destination name: ")
city = input("Enter city to search: ")

if city in dest:
    print("City is present")
else:
    print("City is not present")