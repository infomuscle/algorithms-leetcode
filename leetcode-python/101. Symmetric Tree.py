# 제출 코드 - Runtime 70.38 Memory 61.05
from collections import deque


class Solution:
    def isSymmetric(self, root) -> bool:
        queue = deque([root])
        while len(queue):
            line = []
            for i in range(len(queue)):
                node = queue.popleft()
                line.extend([node.left, node.right])
            half = len(line) // 2
            if [n.val if n else None for n in line[:half]] != [n.val if n else None for n in reversed(line[half:])]:
                return False
            queue.extend(filter(lambda x: x is not None, line))

        return True


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
