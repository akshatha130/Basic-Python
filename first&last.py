a = input("Enter a Character:")
if a:
    b = a[0:1].upper()+a[1:len(a)-1]+a[len(a)-1:len(a)].upper()
else:
    b = ""
print("new_string:",b)
