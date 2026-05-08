class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2:
            return max(nums)
        else:
            first_max = max(nums)
            second_max = max([x for x in nums if x != first_max])
            return max([n for n in nums if n != first_max and n != second_max])
