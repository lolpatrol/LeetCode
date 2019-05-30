# https://leetcode.com/submissions/detail/231701547/

class Solution:
    def maxArea(self, height: list) -> int:
        mv = 0
        left, right = 0, len(height)-1
        while left < right:
            l,  r = height[left], height[right]
            d = (right-left) * min(l, r)
            if mv < d:
                mv = d
            if l < r:
                left += 1
            else:
                right -= 1
        return mv

