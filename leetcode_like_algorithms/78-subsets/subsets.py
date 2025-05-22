class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def sub(index, x, sol):
            if index == len(x):
                res.append(sol[:])
                return 
            
            sol.append(x[index])
            sub(index+1, x, sol)
            sol.pop()
            sub(index+1,x, sol)
            
        sub(0,nums,sol=[])
        return res
        


                





            
            





        