# 제출 코드 - Runtime 5.41 Memory 7.85
class Solution:

    def isValidBST(self, root):
        parents = {}
        edges = set()

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
            if not node.left and not node.right:
                edges.add(node)

        for edge in edges:
            valid = self.validate(edge, parents)
            if not valid:
                return valid

        return True

    def validate(self, node, parents):
        parent = parents[node] if node in parents else None
        current = node
        while parent is not None:
            if parent.right is current and (parent.val >= current.val or parent.val >= node.val):
                return False
            if parent.left is current and (parent.val <= current.val or parent.val <= node.val):
                return False
            current = parent
            parent = parents[current] if current in parents else None

        return True


#    5
# 4     6
#     3   7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


sol = Solution()

# n3 = TreeNode(val=3)
# n7 = TreeNode(val=7)
# n6 = TreeNode(val=6, left=n3, right=n7)
# n4 = TreeNode(val=4)
# n5 = TreeNode(val=5, left=n4, right=n6)
# print(sol.isValidBST(n5))

# n3 = TreeNode(val=3)
# n6 = TreeNode(val=6)
# n4 = TreeNode(val=4, left=n3, right=n6)
# n1 = TreeNode(val=1)
# n5 = TreeNode(val=5, left=n1, right=n4)
# print(sol.isValidBST(n5))

# n1 = TreeNode(val=1)
# n3 = TreeNode(val=3)
# n2 = TreeNode(val=2, left=n1, right=n3)
# print(sol.isValidBST(n2))

n0 = TreeNode(val=0)
print(sol.isValidBST(n0))
