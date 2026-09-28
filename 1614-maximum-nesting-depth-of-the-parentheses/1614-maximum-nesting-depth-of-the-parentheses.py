class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_stack_length = 0

        for char in s:
            if char == "(":
                current_stack_length += 1
                max_depth = max(max_depth, current_stack_length)
            elif char == ")":
                current_stack_length -= 1

        return max_depth