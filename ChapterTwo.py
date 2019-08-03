name = "Oscar Hernandez"
print(name.title())
print("Upper Function: ",name.upper())
print("Lower Function: ",name.lower())
firstName = "Oscar"
lastName = "Hernandez"
fullName = firstName + " " +lastName
print("Combinding Strings: ",fullName)

#rstrip Function
languagee = "Python "
language = "Python "#Notice: "Python " has a space vs "Python"
#rstrip function drops the extra space
print("\nReducing Space",language.rstrip()+"|")
print("No Reducing Space",language+"|")

print("\nExcerises 2-3 to 2-7")
"""
Store a person’s name in a variable, and print a message to that person.
Your message should be simple, such as, “Hello Eric, would you like to 
learn some Python today?”
"""
name = "Eric"
print("2-3")
print("Hello " + name +",would you like to learn some Python today?")

"""
Store a person’s name in a variable, and then print that person’s name 
in lowercase, uppercase, and titlecase
"""
print("\n2-4")
name = "Jack"
print(name.lower())
print(name.upper())
print(name.title())

"""
Find a quote from a famous person you admire. Print the quote and the 
name of its author. Your output should look something like the following, 
including the quotation marks:
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
"""

print("\n2-5")
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")

#Skipped 2-6: Too easy

""""
Store a person’s name, and include some whitespace characters at the beginning
and end of the name. Make sure you use each character combination, "\t" and "\n",
at least once. Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()
"""
print("\n2-7")
name = " Oscar "
print(name)
print("\n",name)#new space
print("\t",name)#tab
print(name.lstrip())#left whitespace
print(name.rstrip())#right whitespace
print(name.strip())#both whitespace


#str():converts int/float/etc to string so accept into another string
age = 21
message = "Happy " + str(age) + "st birthday!"
print(message)
