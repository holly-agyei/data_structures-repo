class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # Maps key -> node
        self.capacity = capacity

        # Dummy head and tail nodes to avoid edge checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: Add node right after head (most recent position)
    def _insert(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # Helper: Remove any node from the list
    def _remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)  # Move to front as most recently used
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # Remove old node

        new_node = Node(key, value)
        self._insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove from both DLL and hashmap
            lru = self.tail.prev  # Least recently used
            self._remove(lru)
            del self.cache[lru.key]
