class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack= [([], 0, 0)]
        output = []

        while stack:
            path, idx, total = stack.pop()

            if total == target:
                output.append(path)
                continue
            elif total > target or idx>=len(candidates):#can never work
                continue
            for i in range(idx, len(candidates)):
                stack.append((path+[candidates[i]], i, total+candidates[i])) #instead of i+1
                

        return output


                