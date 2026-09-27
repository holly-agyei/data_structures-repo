class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        whenever u see ), process it(reverse) and add it to the last thing on the stack
        i want o keep stack of arrays
        """
        # FIX 1: Start with a base array [[]] instead of [] so letters 
        # outside of parentheses have a place to go without crashing.
        stack = [[]] 
        
        def reverse(input):
            final = "".join(reversed(input))
            return final 
        
        i = 0
        while i < len(s):
            
            if s[i] == "(":
                stack.append([])
                i += 1
                # Your inner loop logic works fine here!
                while i < len(s) and s[i].isalnum():
                    stack[-1].append(s[i])
                    i += 1 
                # We remove the extra i += 1 that was here because the inner 
                # loop already moved `i` to the next character.
            
            elif s[i] == ")":
                processed = reverse(stack[-1])
                stack.pop()
                
                # We know 'stack' will never be empty because of our [[]] base
                for c in processed:
                    stack[-1].append(c)
                
                # FIX 2: You MUST increment i after processing a ')'
                # Otherwise, it stays on ')' and causes an infinite loop.
                i += 1
                
            else:
                # FIX 3: We need an 'else' block for letters that happen 
                # BEFORE any '(' or directly AFTER a ')'.
                stack[-1].append(s[i])
                i += 1
                
        # The base array now contains the final string
        return "".join(stack[0])