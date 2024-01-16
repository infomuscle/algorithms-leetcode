# 제출 코드 - Runtime 64.90 Memory 99.37
from collections import deque


class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        queue = deque([root])
        while queue:
            node = queue.popleft()

            depth_left = self.calculate_depth(node.left)
            depth_right = self.calculate_depth(node.right)
            difference = abs(depth_left - depth_right)
            if difference > 1:
                return False

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True

    def calculate_depth(self, node):
        depth = 0
        if not node:
            return depth
        queue = deque([node])
        while queue:
            sub_nodes = set()
            while queue:
                sub_node = queue.popleft()
                if sub_node:
                    sub_nodes.add(sub_node)
            if len(sub_nodes) > 0:
                depth += 1

            for sub_node in sub_nodes:
                if sub_node.left:
                    queue.append(sub_node.left)
                if sub_node.right:
                    queue.append(sub_node.right)

        return depth
