# 제출 코드 - Runtime 79.33 Memory 5.15
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        depth_map = {root: 0}
        parent_map = {root: root}

        stack = [root]
        visited = set()
        while len(stack) != 0:
            node = stack.pop()
            if node is None:
                continue
            visited.add(node)

            parent_map[node.left], parent_map[node.right] = node, node
            depth_map[node] = depth_map[parent_map[node]] + 1

            stack.extend({node.left, node.right} - visited)

        return max(depth_map.values())


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
