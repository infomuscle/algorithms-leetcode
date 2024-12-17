# 제출 코드 - Runtime 94.06 Memory 6.17

class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root):
        self.traverse(root)

        return self.max_diameter

    def traverse(self, node):
        if not node.left and not node.right:
            return (0, 0)

        left_diameter = max(self.traverse(node.left)) + 1 if node.left else 0
        right_diameter = max(self.traverse(node.right)) + 1 if node.right else 0

        self.max_diameter = max(self.max_diameter, left_diameter + right_diameter)

        return (left_diameter, right_diameter)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
