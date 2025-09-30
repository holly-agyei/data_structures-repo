from collections import deque 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #make a window, size = size of p
        #sort p once and for all
        #results array

        l,r, res = 0, len(p)-1, []
        if r>= len(s):
            return []
        p_sorted = "".join(sorted(p))
        
        
        
        
        while r < len(s):
            word = s[l:r+1] 
            sorted_word = sorted(word) #["sdfk","sdf"]
            joined = "".join(sorted_word) #final sorted word
            if joined == p_sorted:
                res.append(l)
            
            l+=1
            r+=1
        return res