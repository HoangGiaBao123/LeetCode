class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        else:
            while val in nums:
                nums.remove(val)
            return len(nums)
