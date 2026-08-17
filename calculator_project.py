#CALCULATOR
num1=int(input("enter your first num:"))
num2=int(input("enter your second num:"))
print(f"sum:{num1+num2}, \ndif:{num1-num2},\nmultiply:{num1*num2},\ndivision:{num1/num2}, \nroot:{num1**num2},remainder:{num1%num2},floor division:{num1//num2}")


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error!."
    return x / y

print("--- Simple Calculator ---")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("enter your num (1/2/3/4): ")

if choice in ("1", "2", "3", "4"):
    try:
        num1 = float(input("first num: "))
        num2 = float(input("second num: "))
    except ValueError:
        print("enter correct num!")
    else:
        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")

        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

        elif choice == "4":
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("wrong number! only 1, 2, 3, or 4 works.")