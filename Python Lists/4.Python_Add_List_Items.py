#Append Items

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
# print(thislist)


#Insert Items

thisList = ["apple", "banana", "cherry"]
thisList.insert(1,"watermelon") #The insert() method inserts an item at the specified index, so the new item will be inserted before the specified index.
#print(thisList)

#Extend List

#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

#print(thislist)

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thisList = ["apple","banana","charry"]
thisTuple = ("kiwi","orange")
thisSet = {"mango","pineapple","papaya"}
thisDict = {"name":"John","age":36}
thisList.extend(thisDict)
print(thisList)
