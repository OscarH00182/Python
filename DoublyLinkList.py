class Node:
    def __init__(self,dataVal = None): #Constuctor
        self.dataVal = dataVal #Node dataVal will be set to dataVal based
        self.next = None #Next is set to None
        self.prev = None #Prec is set to None

class doubly_linked_list:
    def __init__(self):
        self.head = None #We set to None

    def printList(self):
        printVal = self.head #We set printVal to
        while printVal is not None: #While we dont reach end of list
                print(printVal.dataVal) #print out data of current node
                last = printVal #We set last to printVal
                printVal = printVal.next #We shift printVal down by one

    def printHead(self):  #head shifts for this doubly link
        currentHead = self.head  #we set currentHead to head of list
        print(currentHead.dataVal)

    def pushToList(self,newData): #MOVE HEAD
        NewNode = Node(newData) #We create a new node
        NewNode.next = self.head #we set the newNode's next to head
        if self.head is not None: #If list already exists
            self.head.prev = NewNode #Set head's prev to NewNode
        self.head = NewNode #head is set to NewNode
        #                          <-|head|-> None
        #                  |head|<-->|node|-> None
        #        |head|<-->|node|<-->|node|-> None

    def append(self, newData):
        NewNode = Node(newData) #NewNode's data is set to data passed

        #When we first begin the list
        if self.head is None: #If head is None(list doesnt exist)
            self.head = NewNode #head is now that new node
            return

        #OTHERWISE:
        currentNode = self.head #currentNode is set to head
        while (currentNode.next is not None): #while currentNode doesnt reach end of list
            currentNode = currentNode.next #we shift currentNode over
        #Once we each end of the list
        currentNode.next = NewNode #currentNode's nxt is set to newNode
        NewNode.prev = currentNode #NewNode's prev is set to currentNode
        return
        #|head|<-->|node|<-->|node|     Add: |NewNode|
        #|head|<-->|node|<-->|node|<-->|NewNode|
        #HEAD IS SHIFTED BECAUSE WE USE THE PUSH FUNCTION!!

    def insert(self,prev_node,newData):#inserts nodes in specific location of list
        if prev_node is None:
            return
        NewNode = Node(newData)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def remove(self,deleteVal):#deletes value from list
        currVal = self.head #we set currVal to head of the list

        if currVal is not None:
            if currVal.dataVal == deleteVal:
                self.head = currVal.next
                currVal = None
                return

        while currVal is not None:
            if currVal.dataVal == deleteVal:
                break
            else:
                prevNode = currVal
                currVal = currVal.next


        if currVal is None:
            print("Item is not in the list")

        prevNode.next = currVal.next
        if currVal.next is not None:
            currVal.next.prev = prevNode
        currVal = None



DoubleLinkList = doubly_linked_list()
DoubleLinkListTwo = doubly_linked_list()
DoubleLinkListThree = doubly_linked_list()

DoubleLinkList.pushToList(5)
DoubleLinkList.pushToList(10)
DoubleLinkList.pushToList(15)
print("\nPrint out head of the list: ")
DoubleLinkList.printHead()
print("\nPrinting out current list: ")
DoubleLinkList.printList()#Head is shifted to the left everytime a
#node is added, head is moved

DoubleLinkListTwo.append(2)
DoubleLinkListTwo.append(4)
DoubleLinkListTwo.append(6)
print("\nPrint out head of the list: ")
DoubleLinkListTwo.printHead()
print("\nAppending into the Doubly Linked List: ")
DoubleLinkListTwo.printList()#Nodes are added to the right everytime a
#node is added, head is NOT MOVED, head is stationary!

print("\nInserting value 66 into the Doubly Linked List: ")
DoubleLinkList.insert(DoubleLinkList.head,66)
DoubleLinkList.printList()

print("\nUsing Double Link List in a For Loop: ")
for i in range(1,6):
    DoubleLinkListThree.append(i)
DoubleLinkListThree.printList()
print("\nHead of this List is: ")
DoubleLinkListThree.printHead()

print("\nDelete Head of list: 1 ")
DoubleLinkListThree.remove(1)
DoubleLinkListThree.printList()

print("\nDelete Head of list: 3 ")
DoubleLinkListThree.remove(3)
DoubleLinkListThree.printList()

print("\nDelete Head of list: 5 ")
DoubleLinkListThree.remove(5)
DoubleLinkListThree.printList()
