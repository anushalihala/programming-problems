# 934. Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/

from collections import  deque
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j, old_value, new_value):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] != old_value:
                return

            grid[i][j] = new_value
            dfs(i - 1, j, old_value, new_value)
            dfs(i + 1, j, old_value, new_value)
            dfs(i, j - 1, old_value, new_value)
            dfs(i, j + 1, old_value, new_value)

        def bfs(isle1, isle2):
            visited_state = isle2+1
            q = deque([])
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == isle1:
                        q.append([row,col,0])
            while len(q)>0:
                i, j, bridge_length = q.popleft()
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    continue
                if grid[i][j]==visited_state:
                    continue
                if grid[i][j] == isle2:
                    return bridge_length - 1
                else:
                    grid[i][j] = visited_state
                    bridge_length += 1
                    q.append([i - 1, j, bridge_length])
                    q.append([i + 1, j, bridge_length])
                    q.append([i, j - 1, bridge_length])
                    q.append([i, j + 1, bridge_length])

        island_number = 2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col, 1, island_number)
                    island_number += 1
        return bfs(2, 3)

if __name__ == "__main__":
    print(Solution().shortestBridge([[0,1],[1,0]]))