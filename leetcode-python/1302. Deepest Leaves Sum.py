# 제출 코드 - Runtime 57.91 Memory 25.20
from collections import deque, defaultdict


class Solution:
    def deepestLeavesSum(self, root):

        level_map = defaultdict(list)

        level = 1
        level_map[level].append(root.val)
        queue = deque([root])
        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                level_map[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum(level_map[level])


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
