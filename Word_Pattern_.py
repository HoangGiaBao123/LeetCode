class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split(" ")
        if len(pattern) != len(string):
            return False
        else:
            return len(set(pattern)) == len(set(string)) == len(set(zip(string, pattern)))
