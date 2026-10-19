class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.lrudict = {}
        self.head = None
        self.tail = None
        self.size = 0

   
    def _prepend(self, node):
        if node is self.head:
            return

        # Detach an existing node from its current position.
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev

    # Your prepend logic.
        node.prev = None

        if self.head is None:
            self.head = node
            self.tail = node
            node.next = None
        else:
            old_head = self.head
            old_head.prev = node
            node.next = old_head
            self.head = node
            
    def _remove(self, node):
        old_tail = self.tail
        if old_tail.prev is not None:
            before = old_tail.prev 
            old_tail.prev = None 
            before.next = None
            self.tail = before
            del self.lrudict[old_tail.key]
        else:
            self.tail = None
            self.head = None
            del self.lrudict[old_tail.key]     
     
    def get(self, key: int) -> int:
        #return the value if exist else -1
        if key not in self.lrudict:
            return -1
        node = self.lrudict[key]
        self._prepend(node)
        return node.value
        
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key not in self.lrudict:
            self.lrudict[key] = node 
            self.size+=1 
            self._prepend(node) 

            if self.size>self.capacity:
                self._remove(self.tail)
                self.size-=1
            return

        #this means the key exist, so just update the node and in dict as well
        node = self.lrudict[key]
        node.value = value
        self._prepend(node)


        #update if it exisits, else add
        #if number of keys > than capacity, evict the least recently used


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)