class Solution:
    def isNumber(self, s: str) -> bool:
        if s.lower() in ["+infinity","-infinity","inf","-inf","+inf","infinity","nan","-nan","+nan"]:
            return False
        try:
            num = float(s)
        except ValueError:
            return False
        return True
