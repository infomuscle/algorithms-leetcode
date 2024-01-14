# 제출 코드 - Runtime 45.45 Memory 14.65
from collections import deque


class Solution:
    def invertTree(self, root):

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

