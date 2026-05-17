import bisect
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        numbers = sorted(nums)
        start = bisect.bisect_left(numbers, target)
        end = bisect.bisect_right(numbers, target)
        return list(range(start, end))
