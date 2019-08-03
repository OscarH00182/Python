from array import *
"""Array: ordered sequence of homogeneous elements(same type elements)
#array('i',[1,2,3,4])
i : Represents signed integer of size 2 bytes
f : Represents signed float of size 4 bytes

Type code:	Python Type:	Minimum size in bytes:
'c'		    character	        1
'b'		    int	              1
'B'		    int	              1
'u'		    Unicode           2 (see note)
          character	        
'h'		    int 	            2
'H'		    int	              2
'i'		    int	              2
'I'		    long	            2
'l'		    int	              4
'L'		    long	            4
'f'		    float	            4
'd'		    float	            8   

"""
arrayOne = array('i',[10,20,30,40])#Cant hold float
arrayTwo = array('f',[10.32323,2.0,.303,4.02])
print("\nArray with Integers")
for x in arrayOne:
    print(x)

print("\nArray with Floats")
for y in arrayTwo:
    print(y)

print("\nDisplay certain index of array")
print(arrayOne[0])

print("\nInserting inside of an Array")
arrayOne.insert(3,35)
for x in arrayOne:
    print(x)

print("\nAppending inside of an Array")
arrayOne.append(50)
for x in arrayOne:
    print(x)

print("\nDeleting inside of an array")
arrayOne.remove(20)#Insrt the value NOT the index!
for x in arrayOne:
    print(x)

print("\nSearching inside of an Array")
print(arrayOne.index(40))#Returns the index

print("\nUpdating inside of an Array")
print("---Before updating number---")
for x in arrayOne:
    print(x)
print("---After updating number---")
arrayOne[2] = 10000
for x in arrayOne:
    print(x)
