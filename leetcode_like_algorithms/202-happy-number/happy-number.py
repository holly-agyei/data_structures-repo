class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            # sum of squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True
