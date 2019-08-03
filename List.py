"""
LISTS: An ordered sequence of heterogeneous elements(different type elements)
stuff = [1,'apple',foo]
The key diffence between an Array and A List is the different functions
that each one can access and be used by, for example: if you create an 
array with value[3,6,9], and divide that array by 3, and select print
the program will display the new values of that array as 1,2,3, while if
you try divide a list by 3, you will get an error!

"""

print("\nCreating and printing Lists")
listOne = ['Physics','Chemistry',1997,2000]
listTwo = [1,2,3,4,5]
listThree = [["a","b","c"],["d","e","f"]]
print("ListOne[0]: ", listOne[0])
print("ListTwo[1:5]: ",listTwo[1:5])

print("\nUpdating Lists")
print(listOne[3])
listOne[3]=1998
print(listOne[3])

print("\nDeleting value off a List")
print(listOne[0:4])
del listOne[3]
print(listOne[0:4])
"""
Python Expression:               Results: 	         Description:
len([1, 2, 3])	                    3	               Length
[1, 2, 3] + [4, 5, 6]	    [1, 2, 3, 4, 5, 6]	    Concatenation
['Hi!'] * 3	                ['Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	                    True	        Membership
for x in [1, 2, 3]:print x         1 2 3	        Iteration
"""
print("\nRandom useful List Operations:")
print("The Length of ListOne is: ",len(listOne))
print("\nThe concatention of ListOne & ListTwo is: ",listOne + listTwo)
print("\nRepetition of ListOne: ", listOne *2)
print("\nIs Chemistry in ListOne?: ", 'Chemistry' in listOne)
print("\nIteration:")
for x in listOne:print(x)

print("\nPrinting Subsets in List: ")
for i in range(0,2):
    print("Subset:",i)
    for j in range(0,3):
        print("Value: ",listThree[i][j])
