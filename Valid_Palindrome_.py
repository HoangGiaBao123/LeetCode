class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_str = "".join(c for c in s if c.isalnum()).lower()
        return alnum_str[::-1] == alnum_str
