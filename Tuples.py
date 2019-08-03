'''
Tuples: they are just like list except that tuples cannot be changed,
as well as they use parentheses, and not brackets
'''

tup1 = ('math','history',1995,2001)
tup2 = (1,2,3,4,5)
#tup1 = (): This is an empty tup1
#tup1 = (10,): Even if you have one item you need a comma
print("tup1[2]", tup1[2])
print("tup2[1 through 5]", tup2[1:4])

print("\nAlthough you can't edit Tuples, you CAN combine them on another")
tup3 = tup1 + tup2
print(tup3)

print("\nDeleting Tuples")
print(tup3)
del tup3
#print(tup3): If we try to print tup3 we get an error
