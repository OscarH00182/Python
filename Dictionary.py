"""
Dictionary: each key is serparated from its value by a colon(:),
the itmes are seperated by commas,everything is enclosed in curly 
braces. Keys are unique within a dictionary, while values may not be
values can be any type, but keys must be an immutable data type such
as strings, numbers, or turples
"""

print("\nDictionary")
dict = {'Name':'Zoey','Age': 21}
print("Name: ",dict['Name'], " Age: ", dict['Age'])
#If you use the wrong KEY: you will get a error,
#In this case 'Name' is KEY, Zoey is the Value

print("\nUpdating Dictionary")
print("Before UPDATE: ",dict)
dict['Age'] = 22
dict['School'] = "CSUSB"
#print(dict["Age"], " ",dict["School"])
print("After  UPDATE: ",dict)

print("\nDeleting Dictionary Element")
print("Before Deletion ",dict)
del dict['Name']
print("After  Deletion ",dict)
