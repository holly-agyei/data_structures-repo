import heapq
def solve(self, A, B, C):
        A.sort(reverse = True)
        B.sort(reverse = True)
        max_heap = []
        results = []
        visit = {}
        #push to the max_heap
        heapq.heappush(max_heap, (-(A[0]+B[0]),0,0))
        visit = {0,0}
        for _ in range(C):
            current_sum, i, j = heapq.heappop(max_heap)
            results.append(-current_sum)
            
            
            if i+1 <len(A) and (i+1,j) not in visit:
                heapq.heappush(max_heap, (-(A[i+1]+B[j]), i+1, j))
                visit.add((i+1,j))
                
            if j+1 < len(B) and (i, j+1) not in visit:
                heapq.heappush(max_heap, (-(A[i]+B[j+1]), i, j+1))
                visit.add((i,j+1))
        return results
                
            