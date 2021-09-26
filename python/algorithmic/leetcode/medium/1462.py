# 1462. Course Schedule IV
# https://leetcode.com/problems/course-schedule-iv/

# Runtime: 1004 ms, faster than 65.58% of Python3 online submissions for Course Schedule IV.
# Memory Usage: 17.9 MB, less than 23.22% of Python3 online submissions for Course Schedule IV.

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = [set() for i in range(numCourses)]
        for a, b in prerequisites:
            graph[a].add(b)

        def dfs(curr_node, visited, parents):
            if visited[curr_node]:
                return

            visited[curr_node] = 1
            for parent in parents:
                graph[parent].add(curr_node)

            parents.append(curr_node)
            for prereq in list(graph[curr_node]):
                dfs(prereq, visited, parents)
            parents.pop()

        for i in range(numCourses):
            visited = [False for i in range(numCourses)]
            dfs(i, visited, [])
        # print(graph)

        result = []
        for a,b in queries:
            result.append(b in graph[a])
        return result

