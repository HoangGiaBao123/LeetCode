class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        nums = [num]
        for n in range(0, len(digits)):
            copy_digits = digits.copy()
            changed = ""
            if digits[n] == "9":
                changed = "6"
            else:
                changed = "9"
            copy_digits[n] = changed
            nums.append("".join(copy_digits))
        nums[:] = list(map(int, nums))
        return max(nums)
