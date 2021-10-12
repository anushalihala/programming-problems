# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

# Runtime: 176 ms, faster than 69.45% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 15 MB, less than 11.96% of Python3 online submissions for Is Graph Bipartite?.

class Solution:
    def isBipartite(self, graph) -> bool:
        node_group_dict = {}

        def dfs(curr_node, curr_group, alt_group):
            if curr_node in node_group_dict:
                if node_group_dict[curr_node] == curr_group:
                    return True
                else:
                    return False

            node_group_dict[curr_node] = curr_group
            for neighbour in graph[curr_node]:
                if not dfs(neighbour, alt_group, curr_group):
                    return False
            return True

        for node in range(0, len(graph)):
            if node in node_group_dict:
                continue
            if not dfs(node, 0, 1):
                return False
        return True

if __name__=='__main__':
    print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))