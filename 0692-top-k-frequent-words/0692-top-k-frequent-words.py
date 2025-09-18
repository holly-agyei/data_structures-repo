import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        you do be sorting in any, so the time complexity will be around o(nlogn)
        i just want to use max heap and pop k times.
        just build a max heap of -count, word, and then pop k times.

        """
        counter = {}
        heap = []

        for word in words:
            counter[word]=counter.get(word, 0)+1 #O(n)
        
        #push to the heap.
        for word, freq in counter.items():       #O(N)
            
            heap.append((-counter[word], word))
            heapq.heapify(heap) 
        
        return [w for _ in range(k) for freq, w in [heapq.heappop(heap)]] #o(klogN)









