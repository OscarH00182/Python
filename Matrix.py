
"""
Matrix:
A matrix is a special case of 2D Arrays where each data element is of 
the same size. So every matrix is also a 2D Array but not every 2D Array 
is a matrix.We need to use the numpy package for matrix manipulation
"""
from numpy import *
print("\nMatrix")
matrix = array([['Mon',18,20,22,17],['Tue',11,18,21,18],['Wed',15,21,20,19],
                ['Thu',11,43,22,21],['Fri',18,17,23,22],['Sat',12,22,20,18],
                ['Sun',13,15,19,16]])
m = reshape(matrix,(7,5))

"""
We have a matrix with 7 elements, and each subset has 5 values, if we make 
on of the subsets have less or more than 5 values the program will crash
"""

print(matrix)

print("\nAcessing Values in a Matrix")
print(" ",matrix[0])
print(" ",matrix[0][1])

print("\nAdding a row in a Matrix")
matrix = append(matrix,[['APP',66,66,66,66]],0)#The 0 gives the box display
print(matrix)

print("\nAdding a column in a Matrix")
matrix = insert(matrix,[5],[[0],[0],[0],[0],[0],[0],[0],[0]],1)
print(matrix)
#Column Syntax:
# insert(matrixName,[#addingNewColumn],[[valueToAdd],[MustHaveSame#ofRows]],1)
# 1:Is to adjust it as a column,if 0 is used 5 rows are generated with 7 columns of 0
# [['Mon' '18' '20' '22' '17']
#  ['Tue' '11' '18' '21' '18']
#  ['Wed' '15' '21' '20' '19']
#  ['Thu' '11' '43' '22' '21']
#  ['Fri' '18' '17' '23' '22']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['0' '0' '0' '0' '0']
#  ['Sat' '12' '22' '20' '18']
#  ['Sun' '13' '15' '19' '16']
#  ['APP' '66' '66' '66' '66']]

print("\nDeleting a row from a Matrix")
matrix = delete(matrix,[0],0)
print(matrix)

print("\nDeleting a column from a Matrix")
matrix = delete(matrix,[2],1)
#delete(nameOfMatrix,[#OfColumnToDelete],1)
#1: Deletes row, 0 does do anything
print(matrix)

print("\nUpdating a row in a Matrix")
matrix[0] = ['Mon','xx','xx','xx','x']
print(matrix)
