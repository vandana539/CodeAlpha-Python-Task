import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

print("Welcome to Password Generator!")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    password = generate_password(length)
    print("Your generated password is:", password)

    save = input("Save password to a file? (yes/no): ").lower()

    if save == "yes":
        with open("password.txt", "w") as file:
            file.write(password)
        print("Password saved successfully!")

print("Thank you for using Password Generator!")