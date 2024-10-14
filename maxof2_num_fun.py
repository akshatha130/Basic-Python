def max_of_two(x,y):
    if (x.isdigit() and y.isdigit()):
            if x > y:
                return x
            return y
    else:
         print("not a proper input")
#print(max_of_two(-2,0)) #error with 'isdigit'
print(max_of_two('A',4)) #error 'A is not defined'
