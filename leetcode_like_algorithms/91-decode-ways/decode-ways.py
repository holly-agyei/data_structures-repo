class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] =='0':
            return 0
        
        #if there is s, the number of ways to start prefix is 1-->dp[0]
        prev2, prev1 =1,1
        current = 0

        for i in range(1, len(s)):
            current = 0  
            if s[i]!= "0":
                current += prev1

            if 10<= int(s[i-1:i+1]) <=26: #take it
                current+=prev2
            
            prev2, prev1 = prev1, current

        
        return prev1
