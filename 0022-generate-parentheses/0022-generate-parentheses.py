class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = [("", 0,0)]
        res = []

        while stack:
            path, o,c = stack.pop()
            if c==o==n:
                res.append(path)
                continue
            if o<n:
                stack.append((path+"(", o+1, c))
            if c<o:
                stack.append((path+")", o, c+1))
        return res
            