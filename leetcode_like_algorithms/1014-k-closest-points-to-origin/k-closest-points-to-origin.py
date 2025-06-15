import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maintain a heap of size k
        #find push(-distance, point) to heap and heapyfy

        heap = []
        
        for x,y in points:
            d = math.sqrt((y**2)+(x**2))
            
            if len(heap)<k:
                heapq.heappush(heap,(-d,x,y))
            elif len(heap)>=k:
                  heapq.heappushpop(heap,(-d,x,y))
        result = [[x, y] for _ in range(k) for _, x, y in [heapq.heappop(heap)]]

        return result
