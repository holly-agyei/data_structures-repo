class TimeMap:

    def __init__(self):
        #this is like a dictionary but comes with key value and time 
        #must be able to retrieve the keys value at the time given
        #so i think we just do a binary search on the tuples and find the the time<= timestamp 
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value]) #[time, value]
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            arr = self.store[key]
            n = len(arr)
            l,r = 0, n-1
            ans = ""
            while l<=r:
                mid = (l+r)//2
                if arr[mid][0]<=timestamp:
                    ans = arr[mid][1]
                    l = mid+1
                else:
                    r = mid-1 
            return ans
        return ""
                



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)