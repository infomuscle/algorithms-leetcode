# 제출 코드 - Runtime 90.36 Memory 39.83
class Solution:
    def findCenter(self, edges):
        return set(edges[0]).intersection(set(edges[1])).pop()


sol = Solution()

e1 = [[1, 2], [2, 3], [4, 2]]
e2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

print(sol.findCenter(e1))
print(sol.findCenter(e2))
