a = int(input("enter a start range number:"))
b = int(input("enter a end range number:"))
n = int(input("enter a multiplication number:"))
def multiplication(n):
    for i in range(a,b):
        print(f"{n} x {i} = {n*i}")
multiplication(n) 
