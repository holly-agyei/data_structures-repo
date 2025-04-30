from collections import deque, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        What is permutation and what is substring.
        Question is: if S1 permutation is a substring(continous line of chars) of s2.
        any re-arrangements of s1 is a substring of.

        at every point check if the window = the s1
        """
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

        """
        Try with fixed window and dictionaries next instead of making a counter everytime!
        in this case u only update and compare dictionaries.

        """
       
         

        

        
        
        
        
        








        