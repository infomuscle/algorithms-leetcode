# 제출 코드 - Runtime 83.1 Memory 78.33
class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        parents = [i for i in range(n)]

        for parent, son in edges:
            parents[son] = self.find_parent(parents, parent)

        return set([self.find_parent(parents, parents[i]) for i in range(len(parents))])

    def find_parent(self, parents, x):
        if parents[x] != x:
            parents[x] = self.find_parent(parents, parents[x])
        return parents[x]


sol = Solution()

n1, e1 = 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
n2, e2 = 5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
n3, e3 = 5, [[1, 2], [3, 2], [4, 1], [3, 4], [0, 2]]

print(sol.findSmallestSetOfVertices(n1, e1))
print(sol.findSmallestSetOfVertices(n2, e2))
print(sol.findSmallestSetOfVertices(n3, e3))
