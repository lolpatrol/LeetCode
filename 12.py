# https://leetcode.com/submissions/detail/231718781/


class Solution:
    key = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    def intToRoman(self, num: int) -> str:
        roman = ""
        s = 0
        for i in range(4):
            p = 10**(3 - i)
            n = p * (num // p) - s
            s += n
            val = n // p
            if n in self.key:
                roman += self.key[n]
            elif val == 4 or val == 9:
                roman += self.key[p] + self.key[n+p]
            else:
                if val-5 > 0:
                    roman += self.key[5*p]
                    val -= 5
                roman += self.key[p]*val
        return roman

