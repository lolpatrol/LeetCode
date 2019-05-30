# https://leetcode.com/submissions/detail/230873659/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        if len(s) <= 1:
            return s
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            t1 = self.expand(i, s, longest)
            t2 = self.expand2(i, s, longest)
            longest = max(t1, t2, longest, key=len)
            if len(longest) > len(s)/2 and i >= len(s)/2:
                return longest
        return longest

    def expand(self, i: int, s: str, longest: str) -> str:
        count = 0
        index = i
        a, b = 0, 0
        while index - count >= 0 and index + count < len(s) and s[index - count] == s[index + count]:
            a = index - count
            b = index + count + 1
            count += 1
        s_long = s[a:b]
        if len(s_long) > len(longest):
            return s_long
        return longest

    def expand2(self, i: int, s: str, longest: str) -> str:
        count = 0
        index = i
        a, b = 0, 0
        while index-count >= 0 and index+count+1 < len(s) and s[index-count] == s[index+count+1]:
            a = index - count
            b = index+count+2
            count += 1
        s_long = s[a:b]
        if len(s_long) > len(longest):
            return s_long
        return longest

