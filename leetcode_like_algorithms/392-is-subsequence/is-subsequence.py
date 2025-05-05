class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        problem: return bool if it's a is subs of B.
        relative order matters.

        Approach:
        two pointers: one on str a and one on str B

        """
        pointerA, pointerB = 0, 0

        while pointerA < len(s) and pointerB <len(t):
            if s[pointerA] == t[pointerB]:
                pointerA+=1
            pointerB+=1
        
        return pointerA == len(s)
            
            


        