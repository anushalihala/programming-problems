# 447. Number of Boomerangs
# https://leetcode.com/problems/number-of-boomerangs/

import math

class Solution:
    def numberOfBoomerangs(self, points) -> int:
        def distance(a, b):
            return math.sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))

        boomerangs = 0
        for i in range(len(points)):
            distances = {}
            for j in range(len(points)):
                if i == j:
                    continue
                distance_ij = distance(points[i], points[j])
                distances[distance_ij] = distances.get(distance_ij, 0) + 1
            for dist, count in distances.items():
                # print(i,dist, count)
                boomerangs += count*(count-1)
        return int(boomerangs)

if __name__ == '__main__':
    ans = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print(ans)

