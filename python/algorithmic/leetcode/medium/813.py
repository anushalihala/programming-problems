# 813. Largest Sum of Averages
# https://leetcode.com/problems/largest-sum-of-averages/

from collections import defaultdict

class Solution:
    def largestSumOfAverages(self, nums, k: int) -> float:
        memo = defaultdict(dict)
        def helper(start_index, k):
            if k==1:
                return sum(nums[start_index:])/(len(nums)-start_index)
            if start_index in memo[k]:
                return memo[k][start_index]

            maximum = 0
            # print(start_index, k)
            for next_start_index in range(start_index+1, len(nums)):
                curr_avg = sum(nums[start_index:next_start_index])/(next_start_index-start_index)
                remaining_parts_avg_sum = helper(next_start_index, k-1)
                if maximum < (curr_avg + remaining_parts_avg_sum):
                    maximum = curr_avg + remaining_parts_avg_sum
                    max_segment = nums[start_index:next_start_index]
                # print("  [",start_index,"] ",next_start_index,maximum)
            memo[k][start_index] = maximum
            return memo[k][start_index]

        return helper(0,k)


# 9 9 9 1 1 1
# k = 4

# 9,9,9, 1 1 1 => 28
# 9 9 9, 1, 1, 1 => 12

if __name__=='__main__':
    print(Solution().largestSumOfAverages([9,1,2,3,9],3))
    print(Solution().largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4))