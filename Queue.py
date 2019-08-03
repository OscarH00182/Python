""" 
Queue:
Is like a roller coaster line, first person in line gets out first,
all in single file
"""
class Queue:

    def __init__(self):
        self.queue = list()

    def addToQ(self,dataValue):
        self.queue.insert(0,dataValue)#we insert at position 0

    def size(self):
        return len(self.queue)

    def removeFromQ(self):
        return self.queue.pop()


QueueOne = Queue()
QueueOne.addToQ(5)
QueueOne.addToQ(10)
QueueOne.addToQ(15)
QueueOne.addToQ(20)

print("\nQueue")
print("The size of the Queue is: ",QueueOne.size())
print("\nThe values of the Queue are: ")
for i in range(QueueOne.size()):
    print(QueueOne.removeFromQ())
