class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_num = set(nums)
        not_appear = []
        for n in range(1, len(nums) + 1):
            if n not in set_num:
                not_appear.append(n)
        return not_appear
