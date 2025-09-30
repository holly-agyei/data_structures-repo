class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = [([], 0, 0)]
        res = []
        candidates.sort()

        while stack:
            path, idx, total = stack.pop()

            if total == target:
                res.append(path)
                continue
            elif total> target:
                continue

            #combination with repition
            for j in range(idx, len(candidates)):
                if j>idx and candidates[j]==candidates[j-1]:
                    continue

                stack.append((path+[candidates[j]],j+1, total+ candidates[j])) #include idx
        return res
    