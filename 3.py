sender = input("Enter sender name: ")
receiver = input("Enter receiver name: ")
parcel = input("Enter parcel type: ")
location = input("Enter location: ")

print("\nCOURIER RECEIPT")
print("Sender:", sender)
print("Receiver:", receiver)
print("Parcel:", parcel)
print("Location:", location)

code = input("Enter tracking code: ")

letters = 0
digits = 0

for ch in code:
    if ch.isalpha():
        letters = letters + 1
    elif ch.isdigit():
        digits = digits + 1

print("Letters:", letters)
print("Digits:", digits)