# https://leetcode.com/submissions/detail/231812392/
# Messy and slow


class Solution:
    def threeSum(self, nums: list):
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            p = self.find(i, v, nums)
            if p:
                for m in p:
                    res.append([v, m[0], m[1]])
        return res

    def find(self, i: int, v: int, nums: list) -> [int, int]:
        lefts, rights = [], []
        left, right = i+1, len(nums)-1
        while left < right:
            v1, v2 = nums[left], nums[right]
            if v1+v2+v == 0 and left != i and right != i:
                lefts.append(left)
                rights.append(right)
                left += 1
                right -= 1
            elif v1+v2+v < 0:
                left += 1
            else:
                right -= 1
        res = [(nums[l], nums[r]) for l, r in zip(lefts, rights)]
        return set(res)

