# https://leetcode.com/submissions/detail/230406265/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = sorted(nums)
        left = 0
        right = len(nums) - 1
        while True:
            if n[left] + n[right] == target:
                left = n[left]
                right = n[right]
                if left == right:
                    return [index for index, value in enumerate(nums) if value == left]
                else:
                    return [nums.index(left), nums.index(right)]
            elif n[left] + n[right] > target:
                right -= 1
            elif n[left] + n[right] < target:
                left += 1
            else:
                return []

