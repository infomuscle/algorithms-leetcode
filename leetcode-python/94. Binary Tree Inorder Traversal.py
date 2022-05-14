# 제출 코드 - Runtime 90.19 Memory 13.42
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        visited = set()
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            if node == None:
                visited.add(node)
                continue

            if node.left in visited and node not in visited:
                inorder.append(node.val)
                visited.add(node)

            stack.extend(filter(lambda x: x not in visited, [node.right, node, node.left]))

        return inorder


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
