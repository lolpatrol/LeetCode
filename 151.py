# https://leetcode.com/submissions/detail/230931922/


class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.strip().split(" ")
        a = [i for i in a if i != ""]
        a.reverse()
        return ' '.join(a)

