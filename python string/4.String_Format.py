age = 35
# txt = "My name is Khairul islam and i am is" + age
# we cannot combine strings and numbers like this:
# print(txt)


txt = f"my name is khairul islam and i am {age} years old"

# print(txt)

price = 55
# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
txt = f"The product costs is {price:.2f} dollars"
# print(txt)

txt = f"Total product price is {price*20} dollars."
# print(txt)