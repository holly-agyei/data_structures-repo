class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = None #when we make a linkedlist..the head points to None
        self.size = 0
    def addFront(self, val):
        #make a node with the val
        newNode = Node(val) 
        #point newNode to self.head 
        newNode.next = self.head
        #make the new head as newNode
        self.head = newNode
        self.size +=1 
    def removeFront(self):
        #this is making the pop
        if not not self.head:
            return None
        val = self.head.val
        self.head = self.head.next #tell me why im wrong
        self.size -=1
        return val 

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self,val):
        #dont return anything
        self.list.addFront(val)

    def pop(self, val):
        return self.list.addFront(val) 


    def peek(self):
        return self.list.head.val #what if it's none, catch it


    def size(self):
        return self.list.size


    def empty(self):
        return self.list.head is None
    