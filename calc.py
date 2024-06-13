# A simple calculator program

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero is impossible."
    else:
        return x / y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter operation choice: ")

    if choice in ('addition', 'subtraction', 'multiplication', 'division'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'addition':
            print("Result:", add(num1, num2))
        elif choice == 'subtraction':
            print("Result:", subtract(num1, num2))
        elif choice == 'multiplication':
            print("Result:", multiply(num1, num2))
        elif choice == 'division':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

#
# add = lambda x, y: x + y
# result = add(3, 4)
# print(result)  # Output: 7