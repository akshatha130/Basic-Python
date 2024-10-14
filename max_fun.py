def max_of_two(x,y):
    if x>y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

def max_of_four(x,y,z,w):
    return max_of_three(x,y,max_of_three(y,z,w))
print(max_of_two(2,6))
print(max_of_three(3,6,9))
print(max_of_four(2,3,4,5))
