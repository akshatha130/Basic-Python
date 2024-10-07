#to find squeres of n number using Arbitrary Arguments concept
def square(*n):
    i = 0
    for i in n:
        c = i*i
        print(c)
square(2,3,4)
