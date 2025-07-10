class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = [([], 0, 0)]
        res = []

        while stack:
            path, idx, total = stack.pop()

            if total == target:
                res.append(path)
                continue
            elif total> target:
                continue

            #combination with repition
            for j in range(idx, len(candidates)):
                stack.append((path+[candidates[j]], j, total+ candidates[j])) #include idx
        return res