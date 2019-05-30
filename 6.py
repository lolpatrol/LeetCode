# https://leetcode.com/submissions/detail/230916402/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= 1:
            return s
        res = ""
        dist = numRows + numRows - 2
        for i in range(numRows):
            index = i
            c = 1
            while index < len(s):
                res += s[index]
                if 0 < i < len(s)-1:
                    mid_index = index + dist - 2*i
                    if (index != mid_index) and mid_index < len(s):
                        res += s[mid_index]
                        c += 1
                index += dist
        return res

