class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            while len(str(num)) > 1:
                num = sum(int(d) for d in str(num))
            return num
