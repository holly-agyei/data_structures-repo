class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = [([],0)]
        res = []

        while stack:
            path, idx = stack.pop()

            res.append(path)

            for i in range(idx, len(nums)):
                if i>idx and nums[i] == nums[i-1]: #skip
                    continue
                stack.append((path+[nums[i]], i+1))
        return res