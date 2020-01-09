# 제출 코드 - Runtime 81.79 Memory 12.58
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = []

        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current.val % 2 == 0:
                result.extend(self.find_grandsons(current.left))
                result.extend(self.find_grandsons(current.right))
            queue.extend(list(filter(lambda x: x, [current.left, current.right])))

        return sum([r.val for r in result])

    def find_grandsons(self, son: TreeNode):
        if not son:
            return []
        return list(filter(lambda x: x, [son.left, son.right]))
