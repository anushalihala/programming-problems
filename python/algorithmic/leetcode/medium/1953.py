# 1953. Maximum Number of Weeks for Which You Can Work
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maximum = max(milestones)
        s = sum(milestones)
        remaining = s - maximum
        return s if maximum <= remaining+1 else s - (maximum - remaining - 1)