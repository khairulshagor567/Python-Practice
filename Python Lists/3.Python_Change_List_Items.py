#Python - Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #change or update the second item of the thislist.
# print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #range between index 1 and 3 (not included) will be replaced with the new items.
# print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:1] = ["blackcurrant", "watermelon"]
# print(thislist)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "orange") #The insert() method inserts an item at the specified index, so the new item will be inserted before the specified index.
print(thislist)