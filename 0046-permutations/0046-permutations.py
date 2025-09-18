class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = [([], set())]
        perms = []

        while stack:
            path, visited = stack.pop()

            if len(path) == len(nums):
                perms.append(path)
                continue
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                stack.append((path+[nums[i]], visited|{i}))
        return perms