#input
message = input("What's your name?")
print("Hello, ",message," how are you?")

prompt = "\nIf you can tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, ",name)

age = input("\nHow old are you?")
age = int(age)
print("You are",age," years old!")

height = input("\nHow tall are you?")
height = int(height)
print("you are ",height," feet tall")
if height >= 6:
    print("Youre pretty tall!")
else:
    print("Youre not to tall...")
#modulos
number = input("\nEnter a number and Ill tell you if its even or odd")
number = int(number)

if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
