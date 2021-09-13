# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # generate graph
        g = {}
        for i in range(numCourses):
            g[i] = []
        for i, j in prerequisites:
            g[i].append(j)

        status = [0 for i in range(numCourses)]
        order=[]
        for i in range(numCourses):
            if not self.dfs(i, g, status, order):
                return []
        return order

    def dfs(self, curr, graph, status, order):
        if status[curr] == 1:
            return False
        elif status[curr] == 2:
            return True

        status[curr] = 1

        for nextCourse in graph[curr]:
            if not self.dfs(nextCourse, graph, status, order):
                return False
        status[curr] = 2
        order.append(curr)
        return True

if __name__=='__main__':
    print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
