#check positive or negative
n = -3

if n >= 0:
    print("Positive")
else:
    print("Negative")

#check greatest of two numbers
a = 10
b = 20

print(a if a>b else b)

#check  voter eligibility


age = 16
if age>=18:
    print("Eligible")

else:
    print("Not eligible")


#Grading system

marks = 50

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 33:
    print("D")

else:
    print("Fail")


#Leap year check
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")

else:
    print("Not Leapyear")


#Check divisible by 3 or 5

n = 15 

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

#password length check

password = "abc123"

if len(password) >= 6:
    print("Strong")

else:
    print("Week")

#compare three numbers

a, b, c = 20, 5, 10

print(max(a,b,c))


#check if number lies in range

n = 7

if 1 <= n <= 10:
    print("In range")
else:
    print("out of range")


