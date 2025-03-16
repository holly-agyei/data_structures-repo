class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # 32-bit integer range
        
        # Convert x to string and reverse it while handling the sign
        if x < 0:
            rev_x = int("-" + str(abs(x))[::-1])
        else:
            rev_x = int(str(x)[::-1])
        
        # Check if reversed number is within 32-bit range
        if rev_x < INT_MIN or rev_x > INT_MAX:
            return 0
        
        return rev_x
