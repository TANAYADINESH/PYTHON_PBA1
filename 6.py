name = input("Enter participant name: ")
event = input("Enter event name: ")
id = input("Enter registration ID: ")
venue = input("Enter venue: ")

print("\nEVENT PASS")
print("Name:", name)
print("Event:", event)
print("ID:", id)
print("Venue:", venue)

message = input("Enter message: ")

words = len(message.split())
vowels = 0
spaces = 0

for ch in message:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1

    if ch == " ":
        spaces = spaces + 1

print("Words:", words)
print("Vowels:", vowels)
print("Spaces:", spaces)