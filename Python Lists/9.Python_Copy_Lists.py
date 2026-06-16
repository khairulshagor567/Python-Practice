#Copy a List

#Use the copy() method

thislist = ["apple", "banana", "cherry","Kiwi"]

mylist = thislist.copy()

# print(mylist)

# Use the list() method
thislist = ["apple", "banana", "cherry","Kiwi"]
mylist = list(thislist)
# print(mylist)

#Use the slice Operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)