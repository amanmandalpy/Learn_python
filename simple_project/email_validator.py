import re

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

print("Email Validator")

print("========================\n")

while True:
    email = input("enter an email address (or 'quit' to exit): ")

    if email.lower() == "quit":
        print("\nThank you for using Email validator!")

        break

    if re.match(pattern, email):
        print(f"Valid email: {email}\n")

    else:
        print(f"Invaild email: {email}\n")

        