# 583. Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/

#   . e   a   t
# . 0 1   2   3
# s 1 1+1 1+2 1+3
# e 2 1   1+1 1+2
# a 3 1+1 1  1+1

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for j in range(0, len(word2) + 1)] for i in range(0, len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            ch1 = word1[i - 1]
            for j in range(1, len(word2) + 1):
                ch2 = word2[j - 1]
                if ch1 == ch2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]