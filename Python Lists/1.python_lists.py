#Python List

#1.Lists are used to store multiple items in a single variable.
#2.List items are ordered, changeable, and allow duplicate values.

#Allow Duplicates:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#List Length:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(len(thislist))

#List items can be of any data type:

mixeddatatype_list = ["apple",True,3,5.6,False,"banana"]
# print(mixeddatatype_list)

#type() function can be used to determine the data type of the list:
# print(type(mixeddatatype_list)) #<class 'list'>

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
thislist2 = list({"apple", "banana", "cherry"}) # note the double round-brackets
thislist3 = list({"apple":1, "banana":2, "cherry":3}) # note the double round-brackets
print(type(thislist)) #<class 'list'>
print(type(thislist2)) #<class 'list'>
print(thislist3) #<class 'list'>
