class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        whenever you find a valid word in dict, add it to path with space
        whenver an index fail, prune by adding it to seen
        when a path is done exploring, i=len(s), take record
        """
        arr = [1]*len(wordDict)
        valid_words = dict(zip(wordDict, arr))
       
        stack = [("", 0)] #path, index to explore from
        res = [] 
        seen = set()
        
        while stack:
            path, idx = stack.pop()

            #goal
            if idx == len(s):
                res.append(path.rstrip()) #a path explored it and failed

            if idx in seen:
                continue
            valid = False
            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring in valid_words:
                    stack.append((path+substring+" ", i+1))
                    valid = True
            if not valid: #this path  never got a valid path
                seen.add(idx)
        return res




        