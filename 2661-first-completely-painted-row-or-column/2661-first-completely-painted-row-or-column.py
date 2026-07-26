from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # value -> (row, col)
        pos = {}
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)

        rowCount = [0] * m
        colCount = [0] * n

        for i, val in enumerate(arr):
            r, c = pos[val]

            rowCount[r] += 1
            colCount[c] += 1

            if rowCount[r] == n or colCount[c] == m:
                return i

        return -1