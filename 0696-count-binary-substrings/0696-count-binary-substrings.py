class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #i got the math lol, for any valid window with length n(even), number of subs = n/2
        #so the hustle is finding the valid window

        l, r, count= 0,0, 0
        map_ = {"1":0, "0":0}

        one_side = True
        ref = s[0]
        change_point = None

        while r<len(s):
            if s[r] != ref:
                change_point = r
                ref = s[r]
                one_side = not one_side

            map_[s[r]]+=1 #update the map_
            if (r<len(s)-1 and not one_side and s[r]!=s[r+1])or (r == len(s)-1 and not one_side):
                count+=((min(map_["1"], map_["0"]))*2)//2
                l=change_point
                one_side = True 
                x = map_[ref]
                map_["1"] =0
                map_["0"] = 0
                map_[ref] = x 
                
            
            

            r+=1

        return count
        

            
            
            
