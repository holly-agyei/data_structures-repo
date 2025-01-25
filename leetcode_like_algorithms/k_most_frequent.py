import heapq
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        tuple_list= []
        min_heap = []
        results = []
        heaplen = 0
        for key in nums:
            if not key in mapp:
                #initialise
                mapp[key] = 1
        else:
                mapp[key] +=1 
        for key, frequency in mapp.items():
            tuple_list.append((frequency, key))
        for element in range(k):
            heapq.heappush(min_heap, tuple_list.pop()) # i just want to pop k tuples first