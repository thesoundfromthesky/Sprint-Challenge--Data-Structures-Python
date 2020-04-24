import time

start_time = time.time()

# f = open('names_1.txt', 'r')
f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


### Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime complexity of starter code
"""
time: O(n^2) 
space: O(n)
"""

#import bst
from bst import BinarySearchTree
#variable bst will be the root
bst = None
#transform names_1 to bst by iterating 
for i in names_1:
    #if bst is None assign bst
    if not bst:
        #create bst with first element of names_1
        bst = BinarySearchTree(i)
    #keep inserting an element from names_1 to bst    
    else:
        bst.insert(i)

#iterate names_2
for i in names_2:
    #if bst contains element from names_2
    if bst.contains(i):
        #store it to duplicates array
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# start_time2 = time.time()
# # f = open('names_1.txt', 'r')
# f = open('./names/names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# # f = open('names_2.txt', 'r')
# f = open('./names/names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()
# dup=[]
# for name_1 in names_1:
#     if name_1 in names_2:
#         dup.append(name_1)
# end_time2 = time.time()

# print (f"{len(dup)} duplicates:\n\n{', '.join(dup)}\n\n")
# print (f"runtime: {end_time2 - start_time2} seconds")