# https://leetcode.com/submissions/detail/230434907/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all = sorted(nums1 + nums2)
        if len(all) % 2 == 0:
            num = int(len(all) / 2)
            return (all[num - 1] + all[num]) / 2
        else:
            return all[int((len(all) - 1) / 2)] / 1.0

