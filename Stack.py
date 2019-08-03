"""
Stack:
This is how we create a stack, we create a simple class for it
and create its functions to handle values being pass to it
"""
class Stack:
    def __init__(self):#constructor
        self.stack = [] #we create an array named stack to handle the stack
        self.size = -1

    def Push(self,datavalue):#This is what adds values to the stack
        self.stack.append(datavalue)#we add the value to the stack
        self.size +=1

    def Pop(self):
        print("Value that was popped: ",self.stack.pop())
        self.size -=1

        if(self.size == -1 ):
            print("The stack is empty")

    def Peek(self):#We create peek to look at the first value of the stack
        return self.stack[0]

    def Size(self):
        return self.size

stackOne = Stack()
stackOne.Push(66)
stackOne.Push(77)
stackOne.Push(88)
stackOne.Push(99)

print("First Value of stack: ",stackOne.Peek())
stackOne.Pop()

stackOne.Push(11)
print("Size of Stack: ",stackOne.Size())
print("\nPopping Entire Stack")
for i in range(stackOne.Size()+1):
   stackOne.Pop()

