#to add/extend the list
def ext(list1,list2):
    return list1.extend(list2)
list1 = list(input("Enter a List: "))
list2= list(input("Enter a number: "))
print("First list:",list1)
print("Elements to be added:", list2)
ext(list1,list2)
print("Merged list:",list1)
