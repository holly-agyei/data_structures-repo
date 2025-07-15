class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #we are making a path
        """
        say a pth contains idx, from idx to the end of string, cut one by one and check with is palindrome,
        add it to path and keep xploring from that end 
        """
        stack = [([], 0)]
        res = []

        while stack:
            path, idx =stack.pop()

            if idx == len(s): #len of s cox u want to 
                res.append(path)
                continue
            
            for i in range(idx, len(s)):
                sub = s[idx:i+1]
                if sub[::-1] == sub:
                    stack.append((path+[sub], i+1)) #idx+1 cox u want the nex
        return res
