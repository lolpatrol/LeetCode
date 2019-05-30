# https://leetcode.com/submissions/detail/231071541/
# Slow


import re


class Solution:
    def isNumber(self, s: str) -> bool:
        p = r"[-+]?([.]{1}[0-9]+|[0-9]+[.]{1}[0-9]+|[0-9]+[.]{1}|[0-9]+)([e]{1}[-+]?[0-9]+)?"
        asd = re.search(p, s)
        if asd is not None:
            return len(str(asd.group())) == len(s.strip())
        return False

