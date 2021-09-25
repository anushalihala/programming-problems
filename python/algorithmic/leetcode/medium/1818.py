# 1818. Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/
# Runtime: 704 ms, faster than 100.00% of Python online submissions for Minimum Absolute Sum Difference.
# Memory Usage: 34.9 MB, less than 29.41% of Python online submissions for Minimum Absolute Sum Difference.

# import heapq
from bisect import  bisect_right
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        diffs = [0 for num in nums1]
        total = 0
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            diff = abs(a - b)
            # heapq.heappush(diffs, [diff, i])
            diffs[i] = diff
            total += diff

        nums1.sort()
        delta = 0
        for i in range(len(nums1)):
            # diff, i = heapq.heappop(diffs)
            diff = diffs[i]
            if diff < delta:
                continue
            index = bisect_right(nums1, nums2[i])
            if 0 < index <= len(nums1):
                reduction = diff - abs(nums1[index - 1]-nums2[i])
                if reduction > delta:
                    delta = reduction

            if 0 <= index < len(nums1):
                reduction = diff - abs(nums1[index] - nums2[i])
                if reduction > delta:
                    delta = reduction

        return (total-delta) % (10**9 + 7)