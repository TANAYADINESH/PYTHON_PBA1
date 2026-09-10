name = input("Enter applicant name: ")
id = input("Enter application ID: ")
qualification = input("Enter qualification: ")
position = input("Enter position: ")

print("\nAPPLICATION")
print("Name:", name)
print("ID:", id)
print("Qualification:", qualification)
print("Position:", position)

email = input("Enter email: ")

username = email.split("@")[0]

print("Username:", username)