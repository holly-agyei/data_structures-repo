class Solution:
    def myPow(self, x: float, n: int) -> float:
        new_n = n
        ans = 1

        if n < 0: 
            new_n = -(new_n)
        while(new_n>0):
            if new_n %2 ==0:
                x*=x
                new_n = new_n/2
            else:
                ans = ans*x
                new_n = new_n-1
        if n < 0:
            ans = float(1/ans)
        return ans
        
        






        