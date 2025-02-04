class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        arr = s.split()
        