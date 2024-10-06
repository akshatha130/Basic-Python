#to find the length of a string
a = input("Enter a charcter: ")
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count=0
for b in a:
    if b in alphabets:
        count = count+1
print(count)
