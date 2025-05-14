class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        i = 0

        for interval in intervals[:]:
            #first condition is if it ends before(smaller than) the new interval:
            if interval[1]<newInterval[0]:
                res.append(interval)
            
            #if interval explicitly starts after new ends, put new there
            elif newInterval[1]<interval[0]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(interval)
                    
                
                
                #append the interval too cox of the loop structure
            
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])

                
                newInterval = [start, end]
             

        if not inserted:
            res.append(newInterval)
       


        return res
            
        

        