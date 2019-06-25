class Node:
    """
    Every Node has 2 parts: data and a pointer to the next node
    _init_ : is the constructor for python, allows to initalize attributes of a class
    self: self binds the attributes with the given agruments
    This class makes the node that will contain the data value and essentially point to the next value
    |data|next| -->"""
    def __init__(self,dataVal = None):#dataValue is first set to None
        self.dataVal = dataVal #To assign dataVal
        self.next = None #For the next value

class SLinkedList:
    """
    Below we have functions to traverse through the list in different ways,
    but first we have to create the constructor that will handle the data that
    will be passed and how to handle a pointer.
    """
    def __init__(self):#For the constructor we just set it to None
        self.head = None #The head of the list
        self.size = 0

    def listprint(self):#This is the print function
        printVal = self.head#printVal is set to the head of the list
        while printVal is not None:#while it doesnt reach the end of the lsit
            print(printVal.dataVal)#print the value
            printVal = printVal.next#value is set to the next node
            self.size+=1
        print("The size of the list is: ", self.size)
        self.size = 0

    def insertAtBegin(self,newdata):
        NewNode = Node(newdata)#We create a new node
        NewNode.next = self.head#This nodes next will point at head, which links to the rest of the list
        self.head = NewNode#head is now reset to the node that was just created and attached

    def insertAtEnd(self,newdata):#inserts value at end of the list
            NewNode = Node(newdata)#first we create a new node thatll contain the new data
            if self.head is None:#if head is none
                self.head = NewNode#then the new node is head
                return
            last = self.head#last is assigned at head
            while(last.next):#while last doesnt reach end of the list
                last = last.next#last is assigned to the node next to it
            last.next = NewNode#once you reach the end of the list, the new node is attached here

    def InBetween(self,middle,newdata):
        #if middle is None:
         #   print("Middle node isnt being used")
         #   return
        NewNode = Node(newdata)
        NewNode.next = middle.next
        middle.next= NewNode

    def RemoveNode(self,Remove):
        CurrVal = self.head# Curr val is set to head

        if(CurrVal is not None):#IF CurrVal isnt None then list exists
            if(CurrVal.dataVal == Remove):#if first value of list is item to be deleted
                self.head = CurrVal.next#head is now shifted over
                CurrVal = None#headval is deleted
                return

        while(CurrVal is not None):#WHILE CurrVal isnt NONE so we dont reach end of list

            if CurrVal.dataVal == Remove:#If CurrVal is value to be deleted IS FOUND
                break#WE BREAK

            else:
                prev = CurrVal#we set previous to CurrVal
                CurrVal = CurrVal.next#and shift CurVal one over

        if(CurrVal == None):#If CurrVal is NONE
            print("Value doesnt exist")
            return

        prev.next = CurrVal.next#prev's next now points to currval's next
        CurrVal = None#delete CurrVal


listOne = SLinkedList()

for i in range(1,7):
    listOne.insertAtEnd(i)

listOne.listprint()
print("Now we insert 0 at the begining of the list using the insertatbegin function")
listOne.insertAtBegin("0")
listOne.listprint()
print("Now we insert 4 at the end of the list using the insertatend function")
listOne.insertAtEnd(7)
listOne.listprint()
print("Now we insert it in between")
listOne.InBetween(listOne.head.next,"1.5")
listOne.listprint()
print("Now we remove 3 ")
listOne.RemoveNode(7)
listOne.listprint()
