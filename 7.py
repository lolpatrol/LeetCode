# https://leetcode.com/submissions/detail/230919189/

class Solution:
    def reverse(self, x: int) -> int:
        min_lim = -2147483648
        max_lim = 2147483647
        t = str(x)[::-1]
        if t[-1] == "-":
            t = int("-"+t[:-1])
        else:
            t = int(t)

        if min_lim <= t <= max_lim:
            return t
        return 0

