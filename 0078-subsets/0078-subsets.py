class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        """
        stack = [([], 0)]
        subsets = []

        while stack:
            path, idx = stack.pop()

            #goal: when idx explores to the end of arr
            subsets.append(path)

            for i in range(idx, len(nums)):
                stack.append((path+[nums[i]], i+1))
                
        return subsets