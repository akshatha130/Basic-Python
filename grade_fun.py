#to calculate the result using the return concept
def result():
    def marks(b):
        return b
    sub1 = float(input("Enter marks for Subject 1: "))
    sub2 = float(input("Enter marks for Subject 2: "))
    sub3 = float(input("Enter marks for Subject 3: "))
    sub4 = float(input("Enter marks for Subject 4: "))
    sub5 = float(input("Enter marks for Subject 5: "))
    
    a = marks(sub1+sub2+sub3+sub4+sub5)
    percentage = (a/500)*100

    if percentage >= 70:
        print("grade= A") 
    elif percentage >= 60:
        print("grade= B") 
    elif percentage >= 35:
        print("grade= c") 
    else:
        print("grade= D") 
    print("Total Score:",a)
    print("Percentage:" ,percentage)
    
result()
