def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        result = add(num1, num2)

    elif op == "-":
        result = subtract(num1, num2)

    elif op == "*":
        result = multiply(num1, num2)

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            result = None
        else:
            result = divide(num1, num2)

    else:
        print("Invalid operation")
        result = None

    if result is not None:
        print("Result:", result)

    choice = input("Do you want to continue? (y/n): ").lower()


    if choice == "n":
        break
