import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*."


password_lenght = int(input("Enter password lenght(minimum 8): "))


if password_lenght < 8:
    print("password lenght must be at least 8 characters!")
    exit()

use_lower = input("include lowercase letter?(y/n): ").lower()
use_upper = input("include uppercase letter?(y/n): ").lower()
use_number = input("include number?(y/n): ").lower()
use_special = input("include special character?(y/n): ").lower()



charcter_pool = " "

if use_lower == "y":
    charcter_pool += lowercase

if use_upper == 'y':
    charcter_pool += uppercase

if use_number == 'y':
    charcter_pool += numbers

if use_special == 'y':
    charcter_pool += special_chars


if charcter_pool == '':
    print("you must select at least one character type.")
    exit()


password = ''
for i in range(password_lenght):
    password += random.choice(charcter_pool)


strength = ''

if password_lenght >= 12 and use_lower == 'y' and use_upper ==  'y' and use_number == 'y' and use_special == 'y':
    strength = "strong"

elif password_lenght >= 10:
    strength = "medium"

else:
    strength = 'Week'


print("\nGenerated password:", password)
print("Password Strength:", strength)