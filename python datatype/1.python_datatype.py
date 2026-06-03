"""
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
"""

"""
Getting the Data Type
You can get the data type of any object by using the type() function:
"""

#1. Datatype of a string
x = "Hello World"
#print(type(x)) #this will print <class 'str'>, because x is a string.

#2. Datatype of a int or float
x = 20
#print (type(x)) #this will print <class 'int'>, because x is an integer.

x = 20.5
#print (type(x)) #this will print <class 'float'>, because x is a float.

#3. Datatype of a list,tupe,range
x = ["apple", "banana", "cherry"]
#print (type(x)) #this will print <class 'list'>, because x is a list.

x = ("apple", "banana", "cherry")
#print (type(x)) #this will print <class 'tuple'>, because x is a tuple.

x = range(6)
print (list(x)) #this will print <class 'range'>, because x is a range.