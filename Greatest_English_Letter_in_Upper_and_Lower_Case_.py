class Solution:
    def greatestLetter(self, s: str) -> str:
        lowercase_letters = set([c for c in s if c.islower()])
        uppercase_letters = set([c for c in s if c.isupper()])
        appear_in_both = []
        for char in uppercase_letters:
            if char.lower() in lowercase_letters:
                appear_in_both.append(char)
        if not appear_in_both:
            return ""
        return max(appear_in_both)
