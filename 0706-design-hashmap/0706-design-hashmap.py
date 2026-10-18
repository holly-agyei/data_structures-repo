class MyHashMap:

    def __init__(self):
        
        self.capacity = 50
        self.size =0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key):
        if isinstance(key, int):
            return key
        h = 0
        for char in key:
            h = h*31 + ord(char) #polynomial hash rolling 
        return h

    def _index(self, key):
        index = self._hash(key)%self.capacity
        return index


    def put(self, key: int, value: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
                
        self.buckets[index].append([key, value])
        self.size +=1

    def get(self, key: int) -> int:
        index = self._index(key)
        bucket = self.buckets[index]
        for k, value in bucket:
            if k == key:
                return value
        return -1


    def remove(self, key: int) -> None:
        index = self._index(key)
        bucket = self.buckets[index]
        for idx, buck in enumerate(bucket):
            if buck[0] == key:
                del self.buckets[index][idx]
                self.size-=1 
    
    

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)