class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def sub(index, sol):
            if index == len(nums):
                res.append(sol[:])
                return 
            
            sol.append(nums[index])
            sub(index+1, sol)
            sol.pop()
            sub(index+1, sol)
            
        sub(0,[])
        return res
        


                





            
            





        