class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        stack = [([], set())]
        perms = []
        nums.sort()
        
        while stack:
            path, visited = stack.pop()

            if len(path) == len(nums):
                perms.append(path)
                continue
            
            for i in range(len(nums)):
                if i>0 and nums[i-1]==nums[i] and i-1 not in visited: #dont start a new path for this
                    continue
                if i not in visited:
                    stack.append((path+[nums[i]], visited|{i}))
        return perms
