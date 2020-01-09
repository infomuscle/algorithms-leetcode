# 제출 코드 - Runtime 96.76 Memory 75.46
from collections import deque


class Solution:
    def isSameTree(self, p, q) -> bool:
        visited_p = set()
        visited_q = set()

        queue_p = deque([p])
        queue_q = deque([q])
        while len(queue_p) != 0:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            if node_p is None and node_q is None:
                continue

            if node_p is None or node_q is None or node_p.val != node_q.val:
                return False

            visited_p.add(node_p)
            visited_q.add(node_q)

            queue_p.extend([node_p.left, node_p.right])
            queue_q.extend([node_q.left, node_q.right])

        return True


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
