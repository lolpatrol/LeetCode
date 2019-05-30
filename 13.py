# https://leetcode.com/submissions/detail/231722340/


class Solution:
    key = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        num = 0
        s = list(s)
        while len(s) > 0:
            n = self.key[s.pop(0)]
            if len(s) > 0:
                n1 = self.key[s[0]]
                if n1//n == 10 or n1//n == 5:
                    num -= n
                    n = n1
                    s.pop(0)
            num += n
        return num

