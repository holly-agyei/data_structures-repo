def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        tuple_list= []
        min_heap = []
        results = []
        heaplen = 0