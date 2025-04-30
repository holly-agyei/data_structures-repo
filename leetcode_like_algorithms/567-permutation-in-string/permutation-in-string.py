from collections import deque, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        ref = Counter(s1)
        arr = deque()

        for i in range(len(s1)):
            arr.append(s2[i])

        if Counter(arr) == ref:
            return True

        right = len(s1)
        while right < len(s2):
            arr.popleft()
            arr.append(s2[right])
            if Counter(arr) == ref:
                return True
            right += 1

        return False

        

        
        
        
        
        








        