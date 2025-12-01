#For Loop

for i in range(5):
    print(i)

#while loop

i = 1
while i<=5:
    print(i)
    i += 1

#print 1 to 10

for i in range(1, 11):
    print(i)

#sum of first 10 numbers

s = 0

for i in range(1,11):
    s += i

print(s)

#print even numbers
 
for i in range(2, 21, 2):
    print(i)

#Reverse loop

for i in range(10, 0, -1):
    print(i)

#table of number

n = 5

for i in range(1, 11):
    print(n*i)

####################


#While loop countdown

i = 5
while i > 0:
    print(i)
    i -= 1

#Sum of digits

n = 1234
s = 0
while n> 0:
    s += n %10
    n //= 10
print(s)


# factorial

n = 4
f = 1
for i in range(1, n+1):
    f *= i
print(f)

#count digits

n = 98762
c = 0
while n>0:
    c +=1
    n //= 10
print(c)


#break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)



#nested loops with patterns

#star pattern
for i in range(1,6):
    print("*" * i)

#square pattern

for i in range(5):
    print("* " * 5)


#triangle number
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()