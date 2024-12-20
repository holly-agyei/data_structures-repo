class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self):
        return f"{self.data}"

def TraverseLinkedList(head):
    currentNode =   head
    while currentNode:
        print(currentNode, end="->")
        currentNode = currentNode.next
    print("Null")
def deletespecific(head, todel):
    if head == todel:
        return head.next
    currentNode = head
    while currentNode.next and currentNode.next != todel:
        currentNode = currentNode.next
    
    currentNode.next = currentNode.next.next
    if currentNode.next is None:
        return head
    
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

TraverseLinkedList(node1)
deletespecific(node1, node3)
TraverseLinkedList(node1)