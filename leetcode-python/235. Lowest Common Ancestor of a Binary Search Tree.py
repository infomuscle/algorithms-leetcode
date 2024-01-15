# 제출 코드 - Runtime 78.88 Memory 20.11
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parents = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        way_p = self.get_way(parents, p)
        way_q = self.get_way(parents, q)

        lca = None
        for i in range(min(len(way_p), len(way_q))):
            if way_p[i] == way_q[i]:
                lca = way_p[i]

        return lca

    def get_way(self, parents, node):
        current = node
        way_upward = [current]
        while current in parents:
            current = parents[current]
            way_upward.append(current)

        return way_upward[::-1]
