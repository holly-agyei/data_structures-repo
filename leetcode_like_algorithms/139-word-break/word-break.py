class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True #so that s[0] is always a starting point.
        valid_starts = [0]
        wordDict = set(wordDict)

        for cur in range(1, len(s)+1):
            #now loop through to see if theres a word
            for start in valid_starts:
                if s[start:cur] in wordDict:
                    dp[cur] = True
                    valid_starts.append(cur)
                    break #found a valid start
        return dp[-1]
            

