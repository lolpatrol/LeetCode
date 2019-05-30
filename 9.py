# https://leetcode.com/submissions/detail/231078289/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

