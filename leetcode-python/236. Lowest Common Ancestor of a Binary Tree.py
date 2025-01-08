# 제출 코드 - Runtime 81.15 Memory 70.20
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parents = {}

        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                if node.left not in visited:
                    queue.append(node.left)
            if node.right:
                parents[node.right] = node
                if node.right not in visited:
                    queue.append(node.right)

        path_p = set()
        current = p
        while True:
            path_p.add(current)
            if current not in parents:
                break
            current = parents[current]

        current = q
        result = None
        while True:
            if current in path_p:
                result = current
                break
            current = parents[current]

        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
