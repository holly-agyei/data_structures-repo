class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        this is a combination problem
        WHAT TO DO:
            find k-len combination from 1-9 with sum n and no repeatition of num in same path
            -Combination recap
            -constraint
                goal-> when path len=3 and sum = n
        """
        arr = [1,2,3,4,5,6,7,8,9]
        stack = [([], 0, 0, 0)] #path idx size sum
        res = []

        while stack:
            path, idx,size, total = stack.pop()

            if size == k and total ==n:
                res.append(path)
                

            for i in range(idx, 9):
                stack.append((path+[i+1],i+1, size+1, total+i+1))
        return res

        