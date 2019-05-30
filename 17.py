# https://leetcode.com/submissions/detail/232240656/


class Solution:
    key = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> list:
        if len(digits) > 1:
            return self.combinations(digits)
        else:
            if len(digits) == 1:
                return list(self.key[digits])
        return []

    def combinations(self, digits: str) -> list:
        asd = []
        a = self.key[digits[0]]
        d = digits[1:]
        if len(d) > 1:
            b = self.combinations(d)
        else:
            b = self.key[d]
        for m in a:
            for n in b:
                 asd.append(m+n)
        return asd

