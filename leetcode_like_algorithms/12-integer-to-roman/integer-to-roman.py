class Solution:
    def intToRoman(self, num: int) -> str:
        # List of (value, symbol) pairs in descending order
        val_to_symbol = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = ""

        # Greedily use the largest possible values
        for value, symbol in val_to_symbol:
            # While current value fits into num, use it
            while num >= value:
                result += symbol  # Add symbol to the result string
                num -= value       # Reduce the number

                # \U0001f4a1 Example: 58
                # First match: 50 -> 'L', now num = 8
                # Then: 5 -> 'V', now num = 3
                # Then: 1 -> 'I', three times → 'III'

        return result
