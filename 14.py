# https://leetcode.com/submissions/detail/231733318/


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        s_len = len(strs)
        if s_len <= 1:
            if s_len == 0:
                return ""
            return strs[0]
        if ''.join(strs) == "":
            return ""
        count = s_len
        idx = 0
        least = min(strs, key=len)
        if len(least) < 1:
            return least
        while count == s_len and idx < len(least):
            count = 0
            letter = least[idx]
            for i in range(s_len):
                if strs[i][idx] == letter:
                    count += 1
                else:
                    return least[:idx]
            idx += 1
        return least[:idx]

