# def cal():

#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     operation = input("+, -, *, /: ")


#     if operation == "+":
#         print("result", a+b)

#     elif operation == '-':
#         print("result", a-b)

#     elif operation == '*':
#         print("Result", a*b)
    
#     elif operation == '/':
#         if b == 0:

#             return "cannot divided by zero"
#         return a/b
    
#     else:
#         print("Invaild operation")


# cal()

# def greet(name="Guest"):
    
#     return f"Hello, {name}! Welcome to python."
# print(greet("Aman"))
# print(greet())
            
# def string_len(text):

#     return len(text)

# print(string_len("my name is aamar"))


# nums = [1,2,3]

# print(list(map(lambda x: x*2, nums)))
# print(list(filter(lambda x: x%2==0, nums)))

# data = [{"name":"aman","age":23}, {"name":"raj", "age":20}]

# print(sorted(data, key=lambda x: x["age"]))


#default arguments, *args, **kwargs

# def power(base, exp=2):
#     return base**exp

# print(power(3))
# print(power(2, 3))

# #*args example

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,3,4,5))

# #**kwargs example

# def describe(**kwars):
#     for k, v in kwars.items():
#         print(k,v)

# describe(name="Amar", role = "learner")


# #lambda, map, filter, reduce

# #lambda

# square = lambda x: x * x
# print(square(5))

# #map

# nums = [1,2,3]
# sq = list(map(lambda x: x*x, nums))
# print(sq)

# #filter

# evens = list(filter(lambda x: x%2 == 0, range(1, 11)))
# print(evens)



# # modules & packages

# def welcome(name):
#     return f"welcome, {name}"

# if __name__ == "__main__":
#     print(welcome("local run"))

# #create another file to import it.
# #practice/import_test.py

# # from modules_demo import welcome
# # print(welcome("japa"))

##Error Handling(try/except/finally)

# basic try/except

# try:
#     x = int(input("Enter a number: "))
#     print(10/x)

# except ValueError:
#     print("please enter a vaild integer")

# except ZeroDivisionError:
#     print("cannot divide by zero")

# except Exception as e:
#     print("unexpected error:")

# finally:
#     print("this is run always")

#Custom Exception  example

# class Nagitvenumbererror(Exception):
#     pass

# def sqrt(n):
#     if n < 0 :
#         raise Nagitvenumbererror("n must be >= 0")
#     return n ** 0.5

# try:
#     print(sqrt(-4))
# except Nagitvenumbererror as ne:
#     print("error", ne)

  