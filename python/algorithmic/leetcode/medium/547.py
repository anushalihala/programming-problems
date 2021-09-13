# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = [False for item in isConnected]
        count = 0
        for i in range(len(isConnected)):
            if self.findCircleNumHelper(i, isConnected, visited):
                count += 1
        return count

    def findCircleNumHelper(self, curr, isConnected, visited):
        if visited[curr]:
            return False

        visited[curr] = True
        for i, connected in enumerate(isConnected[curr]):
            if i != curr and connected == 1:
                self.findCircleNumHelper(i, isConnected, visited)

        return True

if __name__=='__main__':
    print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
