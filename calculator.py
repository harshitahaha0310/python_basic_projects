# Simple Calculator - Level 1 (Basic)

# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division with Zero Handling
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

# Main Program
print("----- Simple Calculator -----")
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user choice
choice = input("Enter choice (1/2/3/4): ")

# Take input numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

except ValueError:
    print("Invalid input! Please enter numeric values.")

