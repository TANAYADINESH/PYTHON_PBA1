distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time

print("Average Speed:", speed)

bus = input("Enter bus number: ")
route = input("Enter route: ")
driver = input("Enter driver name: ")

details = (bus, route, driver)

print("Bus:", details[0])
print("Route:", details[1])
print("Driver:", details[2])