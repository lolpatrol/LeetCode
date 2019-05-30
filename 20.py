# https://leetcode.com/submissions/detail/232287783/


class Solution:
    key = {
        ")": "(",
        "]": "[",
        "}": "{",
        "(": ")",
        "[": "]",
        "{": "}"
    }
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        k = ["()", "[]", "{}"]
        left = list(s)
        right = []
        while len(left) > 0:
            right.append(left.pop())
            while len(left) > 0 and len(right) > 0 and self.key[right[-1]] == left[-1]:
                left.pop()
                right.pop()
        return len(left) == len(right) == 0

