# 1424. Diagonal Traverse II
# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        maxcols = max([len(row) for row in nums])
        output = [[] for i in range(rows + maxcols)]
        for i, row in enumerate(nums):
            for j in range(len(row)):
                val = row[j]
                idx = i + j
                output[idx].append(val)

        output2 = []
        for row in output:
            row.reverse()
            output2.extend(row)
        return output2

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        maxcols = max([len(row) for row in nums])
        output = []
        for r in range(0, rows):
            i = r
            j = 0
            while i >= 0:
                if len(nums[i]) > j:
                    output.append(nums[i][j])
                i = i - 1
                j = j + 1
        for c in range(1, maxcols):
            i = len(nums) - 1
            j = c
            while i >= 0:
                if len(nums[i]) > j:
                    output.append(nums[i][j])
                i = i - 1
                j = j + 1
        return output
