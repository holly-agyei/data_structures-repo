class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            # The Horizontal Hashmap
        # Horizontal Hashmap (lowercase)
        digit_map = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ' '}

        if not digits:
            return []
        stack = [("", 0)]
        output = []
        
        while stack: #while weve not explored all
            path, idx = stack.pop()

            #goal:
            if idx == len(digits):
                output.append(path)
                continue
            
            cur_letters = digit_map[str(digits[(idx)])]
            for l in cur_letters:
                stack.append((path+l, idx+1))

        return output

            


        