class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #making the best optimal choice locally
        #greedy and monotonic....
        #we are keeping the smallest to the very front possible and relative order should be kept. 
        #we are using all our k chances to keep the front small, dont worry about the later

        stack = [] 

        for n in num:
            while stack and k>0 and n<stack[-1]:
                stack.pop()
                k-=1
            stack.append(n)
        
        if k> 0:
            stack = stack[:-k] #cut from 0 to -k to handle that particular test case of 9, k=1 where the while loop doesnt run
        results = "".join(stack).lstrip("0")
        return results if results else "0"
