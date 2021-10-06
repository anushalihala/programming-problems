# 2023. Number of Pairs of Strings With Concatenation Equal to Target
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

# Runtime: 28 ms, faster than 99.78% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.
# Memory Usage: 14.5 MB, less than 7.30% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.

from collections import  Counter
class Solution:
    def numOfPairs(self, nums, target: str):
        def countPairsViaTarget():
            pairs = 0
            numsDict = Counter(nums)
            for i in range(1, len(target)):
                firstPart = target[0:i]
                secondPart = target[i:]
                if firstPart != secondPart:
                    pairs += numsDict[firstPart] * numsDict[secondPart]
                else:
                    pairs += numsDict[firstPart] * (numsDict[firstPart]-1)
            return pairs

        def countPairsViaNums():
            numsDict = Counter(nums)
            pairs = 0
            for firstPart in nums:
                if target.startswith(firstPart):
                    secondPart = target[len(firstPart):]
                    pairs += numsDict[secondPart]
                    if firstPart==secondPart:
                        pairs -= 1
            return pairs

        if len(target) > len(nums):
            return countPairsViaNums()
        else:
            return countPairsViaTarget()

if __name__=='__main__':
    print(Solution().numOfPairs(["1","1","1"],"11"))