class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        we want to jump to the last: the minimum:

        we can use the greedy approach to see the maximum jum we could have.

        
        

        
        """
        cur_end = 0
        max_jump = 0
        jumps =0

        if len(nums)==1:
            return 0
        
        for i in range(len(nums)):
            #we are guaranteed to reach the end

            max_jump = max(max_jump, i + nums[i])
            


            if i == cur_end:
                cur_end = max_jump
                jumps+=1
            
            if cur_end >= len(nums)-1:
                return jumps

        
        


        
        
        