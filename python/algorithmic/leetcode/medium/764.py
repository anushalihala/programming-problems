# 764. Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/

class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        mines = set(map(tuple, mines))

        def grid_value(i, j):
            if (i, j) in mines:
                return 0
            else:
                return 1

        dp = [[ [0,0,0,0] for j in range(n)] for i in range(n)]
        # left arm counts
        for j in range(0, n):
            count = 0
            for i in range(0, n):
                dp[i][j][0] = count
                if grid_value(i, j) == 1:
                    count += 1
                else:
                    count = 0
        # right arm
        for j in range(0, n):
            count = 0
            for i in range(n-1,-1,-1):
                dp[i][j][1] = count
                if grid_value(i, j) == 1:
                    count += 1
                else:
                    count = 0
        # top arm
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                dp[i][j][2] = count
                if grid_value(i, j) == 1:
                    count += 1
                else:
                    count = 0
        # bottom arm
        for i in range(0, n):
            count = 0
            for j in range(n - 1, -1, -1):
                dp[i][j][3] = count
                if grid_value(i, j) == 1:
                    count += 1
                else:
                    count = 0

        plus_length = 0
        for i in range(n):
            for j in range(n):
                if grid_value(i,j)==1:
                    plus_length = max(plus_length, min(dp[i][j])+1)
        return plus_length

    def orderOfLargestPlusSign2(self, n, mines):
        mines = set(map(tuple, mines))

        def grid_value(i,j):
            if (i,j) in mines:
                return 0
            else:
                return 1

        def findPlusAt(i, j, max_possible, found):
            if max_possible<=found:
                return found

            if 0 <= i < n and 0 <= j < n:
                if grid_value(i,j) == 1:
                    curr = max_possible
                    # right arm
                    for d in range(1, max_possible):
                        if grid_value(i+d,j)!=1:
                            curr = min(curr, d)
                    # left arm
                    for d in range(1, max_possible):
                        if grid_value(i-d,j)!=1:
                            curr = min(curr, d)
                    # top
                    for d in range(1, max_possible):
                        if grid_value(i,j-d)!=1:
                            curr = min(curr, d-1)
                    # bottom
                    for d in range(1, max_possible):
                        if grid_value(i,j+d)!=1:
                            curr = min(curr, d-1)

                    if curr >= max_possible-1:
                        return curr
                else:
                    curr = found

                maximum = curr
                maximum = max(maximum, findPlusAt(i - 1, j - 1, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i - 1, j + 1, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i + 1, j - 1, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i + 1, j + 1, max_possible - 1, maximum))

                maximum = max(maximum, findPlusAt(i - 1, j, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i + 1, j, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i, j - 1, max_possible - 1, maximum))
                maximum = max(maximum, findPlusAt(i, j + 1, max_possible - 1, maximum))
                return maximum
            else:
                return found

        if n % 2 == 1:
            return findPlusAt(n//2, n//2, 1+n//2, 0)
        else:
            maximum = 0
            maximum = max(maximum, findPlusAt(n // 2, n // 2, n // 2, maximum))
            maximum = max(maximum, findPlusAt((n // 2) - 1, n // 2, n // 2, maximum))
            maximum = max(maximum, findPlusAt(n // 2, (n // 2) - 1, n // 2, maximum))
            maximum = max(maximum, findPlusAt((n // 2) - 1, (n // 2) - 1, n // 2, maximum))
            return maximum

if __name__ == '__main__':
    print(Solution().orderOfLargestPlusSign(5, [[4,2]])) #2
    print(Solution().orderOfLargestPlusSign(1, [[0, 0]])) #0
    print(Solution().orderOfLargestPlusSign(2, [[0,1],[1,0],[1,1]])) #1



