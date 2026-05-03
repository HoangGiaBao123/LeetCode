class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            indexes = []
            for i, num in enumerate(nums):
                if num == target:
                    indexes.append(i)
                    break
            for i, num in reversed(list(enumerate(nums))):
                if num == target:
                    indexes.append(i)
                    break
            return indexes
