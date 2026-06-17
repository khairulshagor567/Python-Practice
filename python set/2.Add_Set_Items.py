#Add Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add Sets

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "mango", "papaya"}

set1.update(set2)

print(set1)

#Add Any Iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)