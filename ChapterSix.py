#Simple dictionary
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned ",str(new_points)," points!")

#Adding new key-value pairs
alien_0['x_position']=0
alien_0['y_position']=25
print("\n",alien_0)

#Modifying values
print("\nThe alien is, ",alien_0['color'])
alien_0['color'] = 'yellow'
print("The alien is, ",alien_0['color'])

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("\nOrignal X-position: ",alien_0['x_position'])
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position']= alien_0['x_position']+x_increment
print("New X-position: ", str(alien_0['x_position']))

#Removing Key-Value Pairs
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#dictionary of similar objects
favorite_languages = { 'jen':'python','sarah':'c','edward':'java','phil':'python','ali':'C'}
print("\nSarah's favorite language is ", favorite_languages['sarah'].title())

"""
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary
"""
print("\n6-1")
person = {'FirstName':'Danny','LastName':'Hernandez','age':14,'city':'corona'}
print(person)

"""
Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program
"""
print("\n6-2")
friends ={'Oscar':5,'Dan':10,'Ali':12,'Bob':13,'Mark':31}
print(friends)

#Looping through a dictionary
user_0 = {'username':'eferni','first':'enrico','last':'fermi'}
for key, value in user_0.items():
    print("\nKey: ",key)
    print("Value: ",value)

for k,v in favorite_languages.items():
    print("\nKey: ",k, "'s favorite Lanuage: ",v)
#looping through just keys
print("\n")
for key in favorite_languages.keys():
    print(key)

#looping through keys in order
print("\n")
for key in sorted(favorite_languages.keys()):
    print(key)

#List in dictionaries
print("\n")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
del aliens

aliens = []

#make 30 aliens
print("\n")
for alienNum in range(1,31):
    aliens.append(alienNum)
#showing first 5 aliens
for alienNum in aliens[:5]:
    print(alien)
print("Total umber of aliens: ",str(len(aliens)))

#List in a dictionary
print("\n")
pizza = {'crust':'thicc','toppings':['[pizza','sausage','cheese']}
print(pizza['toppings'])

languages ={'Dan':['C++','Python'],'Oscar':['C','java'],'Steve':['html']}
for names,lan in languages.items():
    print("\n",names,"'s favorite lagnuage(s) are")
    for l in lan:
        print(l.title())
