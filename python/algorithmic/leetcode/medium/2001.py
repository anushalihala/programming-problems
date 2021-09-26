# 2001. Number of Pairs of Interchangeable
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

# Runtime: 1512 ms, faster than 87.30% of Python online submissions for Number of Pairs of Interchangeable Rectangles.
# Memory Usage: 70.8 MB, less than 69.84% of Python online submissions for Number of Pairs of Interchangeable Rectangles.

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        def distinctPairCount(num):
            return num * (num - 1) / 2

        ratios = {}
        for width, height in rectangles:
            ratio = width / float(height)
            ratios[ratio] = ratios.get(ratio, 0) + 1

        pair_counts = 0
        for k, v in ratios.items():
            pair_counts += distinctPairCount(v)

        return pair_counts