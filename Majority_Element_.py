class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        num = None
        for n in nums:
            if count == 0:
                num = n
            if num == n:
                count += 1
            else:
                count -= 1
        return num
