# 제출 코드 - Runtime 45.87 Memory 67.30
from collections import deque


class Solution:
    def minDepth(self, root) -> int:
        if root is None:
            return 0

        depth_map = {root: 0}
        parent_map = {root: root}

        queue = deque([root])
        visited = set()
        while len(queue) != 0:
            node = queue.popleft()
            if node is None:
                continue
            visited.add(node)

            parent_map[node.left], parent_map[node.right] = node, node
            depth_map[node] = depth_map[parent_map[node]] + 1
            if node.left is None and node.right is None:
                return depth_map[node]

            queue.extend({node.left, node.right} - visited)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
