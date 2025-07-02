class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [([], 0)] #we are starting from index 0 for this path
        results, k = [], len(nums)

        while stack:
            path, idx = stack.pop()

            if idx == k:
                #we have explored all paths, let's this is complete..i dont really know why we should finish exploring all path cox i thought every path is a subset
                results.append(path)
            else: #make your decisions and update your stack
                stack.append((path+[nums[idx]], idx+1))
                stack.append((path, idx+1))
        return results