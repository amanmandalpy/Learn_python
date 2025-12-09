try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))


    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1-num2

    elif op == "*":
        result = num1*num2

    elif op == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not vaild")
        result = num1/num2

    else:
        raise ValueError("Invaild operator")
    
    print("Result =", result)
except ValueError as ve:
    print("Input error:", ve)

except ZeroDivisionError as zde:
    print("Math error:", zde)

except Exception as e:
    print("Unexpected error:", e)

    
    
