# 제출 코드 - Runtime 23.64 Memory 89.60
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root) -> int:

        sum_left = 0
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                if node.left:
                    if not node.left.left and not node.left.right:
                        sum_left += node.left.val
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum_left


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
