class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maximum = 0
        for i in range(len(number)):
            if number[i] == digit:
                current_num = int(number[:i] + number[i+1:])
                if current_num > maximum:
                    maximum = current_num
        return str(maximum)
