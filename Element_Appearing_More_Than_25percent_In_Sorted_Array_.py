class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        frequency = len(arr) / 4
        for n in arr:
            if arr.count(n) > frequency:
                return n
