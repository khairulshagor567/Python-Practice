#Join Sets:

#Union 1:

# set1 = {"apple","banana","guava"}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)

#Union 2:

# set1 = {"apple","banana","guava"}
# set2 = {1,2,3}
# set3 = set1 | set2
# print(set3)

#Join Multiple Sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# set5 = set1.union(set2,set3,set4)
#set5 = set1 |set2 | set3 | set4
# print(set5)

#Update

set1 = {"a", "b" , "c",4}
set2 = {1, 2, 3,4}

set1.update(set2) #this method changes original set
# print(set1)

#Intersection (Keep ONLY the duplicates)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#it gives only duplicate value both set.
# set3 = set1.intersection(set2) 
set3 = set1 & set2 #this is another way for intersection

# print(set3)

#intersection update (Keep ONLY the duplicates)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2) #intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# print(set1)

#The values True and 1 are considered the same value. The same goes for False and 0.

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
# print(set3)

#Difference

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#it gives only the items from the first set that are no present in the other set.

#set3 = set1.difference(set2) 

set3 = set1 - set2 
print(set3)

