class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = tail = Node(5)
tail.next = head

second = Node(6)
tail.next = second
tail = second
tail.next = head 

cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next
    break
        