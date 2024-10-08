def calculator(a, b):
    def add():
        return a + b
    
    def subtract():
        return a - b
    
    def multiply():
        return a * b
    
    def divide():
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    
    return add, subtract, multiply, divide

# to get user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Get the calculator functions
add, subtract, multiply, divide = calculator(a, b)

# Display results
print(f"Addition: {add()}")
print(f"Subtraction: {subtract()}")
print(f"Multiplication: {multiply()}")
print(f"Division: {divide()}")
