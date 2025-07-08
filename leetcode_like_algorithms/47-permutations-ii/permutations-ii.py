class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        stack =[([],set())]
        res = []
        k = len(nums)

        while stack:
            path, visit = stack.pop()

            if len(path)==k:
                res.append(path)
            #im coming to loop but how to check for dup
            #when im appendin, i should check if nums[i] != 
            for i in range(len(nums)):
                #Now permuation is level by level
                #at the same level, we dont want to have duplicates 
                #so if i>0 and nums[i]==nums[i-1] and (i-1) not in visited...means this is starting a new thing.
                if i>0 and nums[i]==nums[i-1] and i-1 not in visit:
                    continue
                if i not in visit:
                    stack.append((path+[nums[i]], visit|{i}))
        return res
