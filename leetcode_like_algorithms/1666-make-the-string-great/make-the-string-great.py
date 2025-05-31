class Solution:
    def makeGood(self, s: str) -> str:
        """
        a bad string:
            two adjacent chars where i = small and i+1= upper like oO or Oo
            applys up to last but one element and the last element: all the s
        """

        stack = [] #stack to keep store the chars so far

        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower():

                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

            

        