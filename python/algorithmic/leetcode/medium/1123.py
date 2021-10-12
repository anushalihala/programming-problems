# 1123. Lowest Common Ancestor of Deepest Leaves
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfsTree(curr, depth):
            if curr is None:
                return None

            left = dfsTree(curr.left, depth + 1)
            right = dfsTree(curr.right, depth + 1)

            if (left is None) and (right is None):
                return {"type": "leaf", "node": curr, "depth": depth}
            elif (left is None) or (right is None):
                node = left if right is None else right
                # if node["type"]=="leaf":
                node["type"] = "anc"
                return node
            elif (left["type"] == "leaf") and (right["type"] == "leaf"):
                return {"type": "anc", "node": curr, "depth": depth + 1}
            elif (left["type"] == "leaf") or (right["type"] == "leaf"):
                node = left if left["type"] == "anc" else right
                return node
            elif (left["type"] == "anc") and (right["type"] == "anc"):
                if left["depth"] == right["depth"]:
                    return {"type": "anc", "node": curr, "depth": left["depth"]}
                node = left if left["depth"] > right["depth"] else right
                return node
            else:
                raise Exception("Unforeseen circumstance " + left + ", " + right)

        node = dfsTree(root, 0)
        return node["node"]

# 2: [leaf node7, 3] [leaf node4, 3]
#    [anc, node2, 3]

# 5: [leaf, node6, 2] [anc, node2, 3]
#    [anc, node2, 3]

# 1: [leaf node0 2] [leaf node8 2]
#    [anc, node1, 2]

# 3: [anc node2 3] [anc node1 2]
#    [anc node2 3]

