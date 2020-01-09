# 제출 코드 - Runtime 94.27 Memory 45.40
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val + root.right.val == root.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
