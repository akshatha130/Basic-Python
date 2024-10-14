def max_of_three(x,y,z):
    if x>y:
        if x>z:
            return x
        if y>z:
            return y
        else:
            return z
#print("not a proper input")
print(max_of_three(3,5,9))
