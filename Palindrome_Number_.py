class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = list(str(x))
        if "".join(reversed(digits)) == str(x):
            return True
        return False
