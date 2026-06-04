import math

history = []

def add(a, b):
    return f"{a} + {b} = {a + b}"

def subtract(a, b):
    return f"{a} - {b} = {a - b}"

def multiply(a, b):
    return f"{a} x {b} = {a * b}"

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return f"{a} / {b} = {a / b}"

def percentage(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return f"({a}/{b}) x 100 = {(a / b) * 100}%"

def power(a, b):
    return f"{a}^{b} = {a ** b}"

def square_root(num):
    if num < 0:
        return "Square root of a negative number is not allowed."
    return f"√{num} = {math.sqrt(num)}"

def show_history():
    print("\n HISTORY ")

    if not history:
        print("No calculations yet.")
    else:
        for item in history:
            print(item)

while True:
    print("\n CALCULATOR ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Power (x^y)")
    print("7. Square Root")
    print("8. View History")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 0:
        print("Thank you!")
        break
    elif choice == 8:
        show_history()
        continue
    elif choice == 7:
        num = float(input("Enter a number: "))
        result = square_root(num)
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = percentage(num1, num2)
        elif choice == 6:
            result = power(num1, num2)
        else:
            print("Invalid choice.")
            continue
    print(result)
    if "Cannot" not in result and "not allowed" not in result:
        history.append(result)