class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack= [([], 0, 0)]
        output = []
        candidates.sort()
        
        while stack:
            path, idx, total = stack.pop()

            if total == target:
                output.append(path)
                continue
            elif total > target or idx>=len(candidates):#can never work
                continue

            for i in range(idx, len(candidates)):
                if i>idx and candidates[i-1]==candidates[i]: #skip this else it will be a repeatition
                    continue
                stack.append((path+[candidates[i]], i+1, total+candidates[i])) #i+1, we dont wanna use the same num over and over
                

        return output


                