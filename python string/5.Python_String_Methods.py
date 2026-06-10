#String Methods of python

#capitalize()
txt="python practice."
# print(txt.capitalize())

#casefold()/lower() both are same but casefold is stronger than lower.
txt = "Python Is A Dynamic Programming Language."
# print(txt.casefold())
# print(txt.lower())

#count()
txt="I love apples, apple are my favorite fruit."
#The count() method returns the number of times a specified value appears in the string.
# print(txt.count("apple"))
#you can find find a specific value from a sentence with indexing range.
# print(txt.count("apple",5,25))

#find()

txt = "Hello, welcome to my world."

x = txt.find("welcome")

# print(x)

#join()
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

# print(x)