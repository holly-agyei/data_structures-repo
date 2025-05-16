class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = [1]*(1+i) #fill each sace with ones

            for j in range(1, i):
                row[j] = res[i-1][j-1]+res[i-1][j]
            res.append(row)
        return res