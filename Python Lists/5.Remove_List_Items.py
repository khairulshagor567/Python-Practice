#Python - Remove List Items

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #The remove() method removes the specified item.  
# print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #The pop() method removes the specified index, (or the last item if index is not specified).
thisList = ["apple", "banana", "cherry"]
thisList.pop() #The pop() method removes the specified index, (or the last item if index is not specified).
#print(thisList)
#print(thislist)

#Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear() #The clear() method empties the list.  
print(thislist)

#del Keyword
thislist = ["apple", "banana", "cherry"] 
del thislist
print(thislist) #This will raise an error because the list no longer exists.