class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers = [0]*len(temperatures)
        stack = []

        for index,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                
                answers[stack[-1]]= index-stack[-1]
                stack.pop()
            stack.append(index)
        
        return answers