#12 Function to calculate the sum of digits in a number
def sum_of_digits():
    n = int(input("Enter a number: ")) 
    total = 0
    while n > 0:
        d = n%10
        total= total+d
        n = n//10
    return total
print(f"The sum of digits is: {sum_of_digits()}")
