patient = input("Enter patient name: ")
id = input("Enter appointment ID: ")
doctor = input("Enter doctor name: ")
time = input("Enter time: ")

print("\nAPPOINTMENT")
print("Patient:", patient)
print("ID:", id)
print("Doctor:", doctor)
print("Time:", time)

text = input("Enter a sentence: ")

upper = 0
lower = 0
digits = 0
special = 0

for ch in text:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digits = digits + 1
    else:
        special = special + 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Special:", special)