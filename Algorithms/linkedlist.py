class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
        self.prev = None

Node1 = Node(2)
Node2 = Node(3)
Node3 = Node(6)
Node4 = Node(-4)

Node2.next = Node3
Node2.prev = Node1
Node1.next = Node2

Node3.next = Node4
Node3.prev = Node3
Node4.prev = Node3

currentNode = Node1

while currentNode: #whole currentNode.next isnot null
    print(currentNode, end="->")
    currentNode = currentNode.next
    if currentNode is None:
        print("None")



