class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #I KNOW u can use dp but lemme try iterative backtracking 

        stack = [(0,0)] #idx, number of words matched
        dictionary = Counter(wordDict)
        visited = set()

        while stack:
            idx, matches =stack.pop()

            if idx == len(s):
                return True
            if idx in visited:
                continue
            visited.add(idx)
            
            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if substring in dictionary:
                    stack.append((i+1, matches+1))
        return False

