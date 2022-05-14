# 제출 코드 - Runtime 90.19 Memory 13.42
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        inorder = []
        if root == None:
            return inorder

        visited = set()
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()

            if ((node.left == None) or (node.left in visited)) and node not in visited:
                inorder.append(node.val)
                visited.add(node)

            if node.right != None and node.right not in visited:
                stack.append(node.right)
            if node not in visited:
                stack.append(node)
            if node.left != None and node.left not in visited:
                stack.append(node.left)

        return inorder


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
