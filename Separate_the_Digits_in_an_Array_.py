class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            digits = list(map(int, str(n)))
            result = result + digits
        return result
