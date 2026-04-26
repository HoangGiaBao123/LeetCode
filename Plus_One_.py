class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[:] = [str(n) for n in digits]
        string = "".join(digits)
        number = int(string)
        number = str(number + 1)
        digits[:] = [int(c) for c in number]
        return digits
