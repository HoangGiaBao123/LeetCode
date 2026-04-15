class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        words = string.split()
        return len(words[-1])
