class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #if ( < n, add (
        #number of cp shouldnt < number of >
        #hence only if )<(, add close 

        #stack state is path so far, open count, close count

        stack = [("", 0, 0)]
        res = []

        while stack:
            path, o, c = stack.pop()

            if o==c==n:
                res.append(path)
                continue
            if o<n:
                stack.append((path+"(", o+1, c))
            if c<o:
                stack.append((path+")", o, c+1))
        return res