"""
Binary Seach Tree(BST): left node is less than or equal to its parent, right node is greater than its parent,to search
for a value we use the binary seach algrothim, we cut in half every time
"""

class Node:

    def __init__(self,data):#CONSTRUCTOR HOLDS CREATES NEW NODE, ASSIGNS VALUE TO IT

        self.left = None#We set left pointer to none
        self.right = None#We set right pointer to none
        self.data = data#set data to whatever data is passed


    def insertValue(self,data):

        parent = self.data #we set root to parent, and if goes down, greater node to parent

        if data <= parent:#if data is less  or equal to than parent

            if self.left is None:#if there isnt a left node
                self.left = Node(data)#create new left node and add data into it
            else:#if there is a another left node
                self.left.insertValue(data)#pass value to see if its bigger/smaller to next node

        elif data > parent:#if data is greater than parent

            if self.right is None:#if there isnt a right node
                self.right = Node(data)#create new right node and add data into it

            else:
                self.right.insertValue(data)#pass value to see if its bigger/smaller to next node


    def findValue(self,dataToFind):

        parent = self.data#parent is set to whatever value it holds

        if dataToFind < parent:#if data passed is less than in node

            if self.left is None:#if left node is empty, then we've reached bottom of the list
                print(str(dataToFind), " Is NOT in this tree")

            else:#else pass it to the next left node to check
                self.left.findValue(dataToFind)

        elif dataToFind > parent:#if data passed is greater than in node

            if self.right is None:#if right node is none, we've reached end of list
                print(str(dataToFind)," is NOT in this tree")

            else:#else pass it to the next right node to check
                self.right.findValue(dataToFind)

        else:
            print(str(self.data)," is FOUND")
            return parent


    def printTree(self):

        if self.left:
            self.left.printTree()

        print(self.data)

        if self.right:
            self.right.printTree()

    def inOrderTraversal(self,root):

        res=[]

        if root:
            res = self.inOrderTraversal(root.left)#first add leftest left of tree
            res.append(root.data)#then root of the leftest left
            res = res + self.inOrderTraversal(root.right)#then right

        return res

    def postOrderTraversal(self,root):

        res = []

        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)

        return res

    def preOrderTraversal(self,root):

        res = []

        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)

        return res


    def removeValue(self,data):

        if self is None:
            print("Tree is empty")
            return None

        if data < self.data:
            self.left = self.left.removeValue(data)

        elif data > self.data:
            self.right = self.right.removeValue(data)

        else:

            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.removeValue(temp.data)

        return self

    def minValueNode(self,node):

        current = self.data
        while current.left is not None:
            current = current.left
        return current

tree = Node(10)
tree.insertValue(5)
tree.insertValue(20)
tree.insertValue(5)
tree.insertValue(8)
tree.insertValue(15)
tree.insertValue(25)
tree.insertValue(7)

print("\nPrint the tree")
tree.printTree()

print("\nCheck if 5 is in the tree")
tree.findValue(5)

print("\nCheck if 100 is in the tree")
tree.findValue(100)

#tree.removeValue(5)

print("\nInOrder  [LNR]: ",tree.inOrderTraversal(tree))
print("\nPostOrder  [LRN]: ",tree.postOrderTraversal(tree))
print("\nPreOrder  [NLR]: ",tree.preOrderTraversal(tree))
