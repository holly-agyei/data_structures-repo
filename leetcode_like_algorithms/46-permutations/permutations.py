class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        so this is recursive backtracking problem
        we are making paths and trying to make sure each path is unique, no duplicates
        -iteratively:
            -use set to keep track of each duplicates
        """
        k = len(nums)
        stack = [([], set(), 0)]
        permutations = []

        while stack: #until we are done poping and exploing all possibilities, chale continue
            path, visit, size= stack.pop()

            if size == k: #check progress
                permutations.append(path)
            else: #update state
                #loop through the whole array to add every other possibilty to it
                for i , num in enumerate(nums):
                    if i not in visit: #use the index to keep track of visits, and dont use num, cox there might be duplicate
                        stack.append((path+[num], visit|{i}, size+1))
        return permutations









