class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        """
        stack = [([], 0)]
        subsets = []

        while stack:
            path, idx = stack.pop()

            #goal: when idx explores to the end of arr
            if idx >= len(nums):
                subsets.append(path)
                continue
            stack.append((path+[nums[idx]], idx+1))
            stack.append((path, idx+1))
        return subsets