#Function to generate a list of prime numbers up to a given number
def generate_primes(n):
    primes = []
    for num in range(2, n+1): 
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)  
    return primes
n = int(input("Generate prime numbers up to: "))
print("Prime numbers:", generate_primes(n))   
    
