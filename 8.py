# https://leetcode.com/submissions/detail/231077740/

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        min_lim = -2147483648
        max_lim = 2147483647
        p = r"[-+]?[\d]+"
        asd = re.search(p, str)
        if asd is None:
            return 0
        dist = asd.span()
        if dist[0] != 0:
            sub = str[:dist[0]]
            ws_count = sum([1 for k in sub if k == " "])
            if ws_count != len(sub):
                return 0
        num = int(asd.group())
        if num < min_lim:
            num = min_lim
        elif num > max_lim:
            num = max_lim
        return num

