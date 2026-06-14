#Access Items

#You can access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
# print(thislist[1]) #banana
 
#Negative Indexing
#Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
# print(thislist[-1]) #cherry 

#Range of Indexes
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5]) #last item is not included

#By leaving out the start value, the range will start at the first item:
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[:4]) #last item is not included

#By leaving out the end value, the range will go to the end of the list:
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[:5]) #last item is not included

#Range of Negative Indexes
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[-4:-1]) #last item is not included

