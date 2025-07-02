class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        so this is recursive backtracking problem
        we are making paths and trying to make sure each path is unique, no duplicates
        -iteratively:
            -use set to keep track of each duplicates
        """
        k = len(nums)
        stack = [([], set())]
        permutations = []

        while stack: # the stack will always pop and try, until we are not done trying
            path, visits = stack.pop()
            #check the len
            if len(path) == k: #we have a valid permuation
                permutations.append(path)
            
            else: #now, for this particular path, check through the nums to build a new path
                for i,num in enumerate(nums):
                    if i not in visits:
                        stack.append((path+[num], visits | {i})) #create a new path and new vis
        
        return permutations





