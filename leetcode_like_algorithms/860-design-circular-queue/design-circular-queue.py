class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        #we need to define the node
        self.head = None
        self.tail = None 
        self.k = k 
        self.size = 0

    def enQueue(self, value: int) -> bool:
        #here we are adding a node to the que
        """
        say node is 1. we want the head to be 1 and the tail to be one and the tail points back to head
        1-2
        """
        if self.size == self.k:
            return False # we are full
        if self.size ==0:
            self.head = self.tail = Node(value)
            self.tail.next = self.head
            
            self.size+=1
            return True
        else:
        
            node = Node(value)
            self.tail.next = node 
            self.tail = node
            self.tail.next = self.head  #node.next = self.next equal right
            self.size+=1
            return True
    def deQueue(self) -> bool:
        """
        This removes the head, they dont require us to return it, but we basically disconet and the size too
        if the node is none?
        if the node is one?
        if the nodes are >2?>
        """
        if self.size ==0:
            return False
        if self.size ==1:
            self.head = None
            self.size-=1
            
        else:
             #so do u mean head and tail are the same? so i can replace head with tail here?
            self.head = self.head.next
            self.tail.next = self.head
            self.size-=1
            
        return True
    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size ==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()