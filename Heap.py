
class maxHeap:

    def __init__(self,items=[]):#constuctor recieves list
        self.heap = [0]#insert 0 in index 0
        for i in items:#use for loop to insert items passed in
            self.heap.append(i)#append values to heap
            self.__floatUp(len(self.heap)-1)#call float up function,uses index NOT VALUE,float up
            #function makes sure parent is bigger than child


    def push(self,data):#ADDS VALUE TO INDEX

        self.heap.append(data)#adds value to heap
        self.__floatUp(len(self.heap)-1)#adjusts up to position correctly


    def peek(self):#returns root

        if len(self.heap) > 1:
            return self.heap[1]
        else:
            print("Heap is empty")


    def popNode(self):#WE POP OFF THE ROOT OF THE HEAP EVERYTIME, THEN ADJUST

        if len(self.heap) > 2:#if heap has a size bigger than one
            self.__swap(1,len(self.heap)-1)#we swap value in index 1 with last indez
            self.heap.pop()#we pop off value that is now in last index(WHICH WAS ROOT)
            self.__bubbleDown(1)#we bubble down value in root

        elif len(self.heap)==2:#if theres only 1 value in heap:TWO BECAUSE 0 IN IN INDEX 1
            self.heap.pop()#pop off only value

        else:
            print("The heap is empty")


    def __swap(self,i,j):#SWAPPING TWO VALUES USING INDEX

        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]#IT JUST WORKS


    def __floatUp(self,index):#ADJUST SO THAT PARENT IS BIGGER THAN CHILD

        parent = index//2#we just find where the parent is!

        if index <=1:#if list empty we return
            return

        elif self.heap[index] > self.heap[parent]:#IF INDEX IS GREATER THAN ITS PARENT
            self.__swap(index,parent)#we swap their positions, so child is now parent
            self.__floatUp(parent)#child WHICH IS NOW PARENT gets passed into this function,until
            #it finds its proper position


    def __bubbleDown(self,index):#WE ONLY USE BUBBLE DOWN WHEN WE USE POPNODE FUNCTION

        left = index *2  #Index passed left child's index
        right = index *2+1 #Index passed right child's index
        largest = index #set largest to index passed

        #if length of heap greater than index of child and value of largest is less than of left
        if len(self.heap)>left and self.heap[largest] < self.heap[left]:
            largest = left #we set largest to left REMEMBER THIS IS INDEX NOT VALUE

        # if length of heap greater than index of child and value of largest is less than of right
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right #we set largest to right REMEMBER THIS IS INDEX NOT VALUE

        if largest != index: #if largest isnt index passed
            self.__swap(index,largest)#we swap their position
            self.__bubbleDown(largest)#pass now new largest to continue checking

max = maxHeap([35,32,30,4,3])
print(str(max.heap[0:len(max.heap)]))
print(str(max.peek()))
max.popNode()
print(str(max.heap[0:len(max.heap)]))
max.push(452)
print(str(max.heap[0:len(max.heap)]))









class minHeap:

    def __init__(self,items=[]):#CONSTRUCTOR: WE ALLOW ITEMS TO BE PASSED
        self.Heap=[0]#Heap has Index 0 filled in with 0
        for i in items:#for every value in items[]
            self.Heap.append(i)#add i to Heap
            self.floatUp(len(self.Heap)-1)#call floatUp function to adjust bit by bit

    def Peek(self):
        if len(self.Heap)>2:
            print(self.Heap[1])
        else:
            print("Min Heap is empty")
    def push(self,value):
        self.Heap.append(value)
        self.floatUp(len(self.Heap)-1)

    def popNode(self):#THIS POPS THE ROOT AND ADJUSTS TREE

        if len(self.Heap) >2:#length of Heap is greater than 2
            self.swap(1,len(self.Heap)-1)#swap root with last value of minHeap
            self.Heap.pop()#pop off from Heap
            self.bubbleDown(1)#Use bubbleDown Function to adjust

        elif len(self.Heap)==2:#If there's only 1 item in heap
            self.Heap.pop()

        else:#OTHERWISE
            print("The Heap is empty")

    def swap(self,i,j): #TWO INDEX TO SWAP

        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]  # IT JUST WORKS

    def floatUp(self,index):#WE MOVE THE VALUE UP
        parent = index//2#Parent of value passed is got by dividing by 2

        if index <=1:#if theres no heap
            return

        elif self.Heap[index] < self.Heap[parent]:#Check if value passed is smaller than its parent, IF IT IS
            self.swap(index,parent)#swap index and parent
            self.floatUp(parent)#pass new parent into function

    def bubbleDown(self,index):

        smallest = index #we ASSUME smallest is the index
        print("Smallest: ", smallest)
        left = index *2#To find the left, get the index and multiple by 2
        right = index *2+1#To find the left, get the index and multiple by 2 + 1

        if len(self.Heap) > left and self.Heap[left] < self.Heap[smallest]:
            smallest = left

        if len(self.Heap) > right and self.Heap[right] < self.Heap[smallest]:
            smallest = right

        if smallest != index:#While smallest isnt orginal number passed
            self.swap(index,smallest)#swap the number passed and new small number
            self.bubbleDown(smallest)#now pass new smallest number

print("\nMin Heap")
min = minHeap([95,40,35,30])
min.Peek()

print("\n",str(min.Heap[0:len(min.Heap)]))
min.popNode()
print("\n",str(min.Heap[0:len(min.Heap)]))
min.push(3)
print("\n",str(min.Heap[0:len(min.Heap)]))

