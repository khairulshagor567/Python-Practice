#The Ternary Operator
#Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.

num = 10

x = "Even" if num%2 == 0 else "Odd"

# print(x)

week_name = "Sun"

x = "Weekend" if week_name == "Fri" or week_name == "Sat" else "Weekday"

#print(x)

# if(week_name == "Fri" or week_name == "Sat"):
#     print("Weekend")
# else:
#     print("Weekday")    

num = 5

weekName = "Friday" if num == 5 else "Saturday" if num == 6 else "Sunday" if num == 7 else "weekday"
print(weekName)