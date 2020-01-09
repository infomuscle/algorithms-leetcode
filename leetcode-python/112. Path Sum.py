# 제출 코드 - Runtime 88.12 Memory 15.71
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        stack = [root]
        path_sums = {root: root.val}
        while len(stack) != 0:
            node = stack.pop()
            if node.left != None:
                stack.append(node.left)
                path_sums[node.left] = path_sums[node] + node.left.val
            if node.right != None:
                stack.append(node.right)
                path_sums[node.right] = path_sums[node] + node.right.val

            if node.left == None and node.right == None and path_sums[node] == targetSum:
                return True

        return False


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
