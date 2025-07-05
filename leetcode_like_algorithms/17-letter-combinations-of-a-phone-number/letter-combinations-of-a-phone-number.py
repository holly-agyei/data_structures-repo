class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        # if not digits:
        #     return []
        # stack = [("", 0)] #we are taking the first digit
        # k, results = len(digits), []
        # while stack:#while we have not explored all the possibilities
        #     path, idx = stack.pop()

        #     if idx == k: #meaning this particular path has the lenght of digits
        #         results.append(path)
        #     else:
        #         cur_digit = digits[idx]
        #         for letter in digit_map[cur_digit]:
        #             #we want to add that letter to the cur path, stack up with for loop
        #             stack.append((path+letter, idx+1)) #idx +1 cox the next time we pop we want to check the letters of the digit of the next index. say we were at 2 in "123", idx +1 takes to 3 in 123 and the next time we explore.
        
        # return results

        if not digits:
            return [] #nothing to explore
        stack,results, k = [("", 0)], [], len(digits)
        while stack:
            path, idx = stack.pop()
            #this could pop "a", 1
            if idx != k: #the goal hasnt been met
                curr_digit = digits[idx]
                for letter in digit_map[curr_digit]:
                    stack.append((path+letter, idx+1))
                continue
            results.append(path)



        return results
