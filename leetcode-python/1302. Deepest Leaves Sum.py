# 제출 코드 - Runtime 52.43 Memory 64.86
from collections import deque, defaultdict


class Solution:
    def deepestLeavesSum(self, root):

        level_map = defaultdict(list)
        level_map[1].append(root.val)

        queue = deque([root])
        level = 1
        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_map[level].append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_map[level].append(node.right.val)

        return sum(level_map[max(level_map)])


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
