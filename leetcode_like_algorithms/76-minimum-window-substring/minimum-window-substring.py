from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t) #turn t into dict {x:2, y:1 z:1}
        t_len = len(t_count) #counter for t = 3
        window = {} #we are building a window
        needed_count =0 #our count should be equal to count of t for window to be valid
        min_count = float("inf") #higher number first
        res = [-1,-1] # we will find the indexes of the min window

        r,l = 0,0

        while r < len(s):
            #add the element to out dict
            window[s[r]] = window.get(s[r],0)+1 
            
            if window[s[r]] == t_count[s[r]]:
                needed_count+=1
            while needed_count == t_len: #while we have a valid window
                #update count
                if r-l+1 < min_count:
                    min_count = r-l+1 
                    res = [l,r]
                if s[l] in t_count:
                    window[s[l]]-=1
                    if window[s[l]]<t_count[s[l]]:
                        needed_count-=1
                l+=1
            r+=1
        
        if min_count !=float("inf"):
            return s[res[0]: res[-1]+1]
        else:
            return ""