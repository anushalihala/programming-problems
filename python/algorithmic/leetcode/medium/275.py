# 275. H-Index II
# https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)

        while low <= high:
            mid = int((low + high) / 2)
            h = len(citations) - mid
            # print(mid,h)
            if (mid == len(citations) or citations[mid] >= h) and (mid == 0 or citations[mid - 1] <= h):
                return h
            elif citations[mid] < h:
                low = mid + 1
            else:
                high = mid - 1
        return "NA"

