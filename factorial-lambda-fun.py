factorial = lambda n: 1 if n == 0 else eval('*'.join(str(i) for i in range(1, n + 1)))

# Example usage
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
