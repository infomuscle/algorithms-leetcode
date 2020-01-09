# 제출 코드 - Runtime 88.94 Memory 11.80
import itertools


class Solution:
    def countNegatives(self, grid):
        return len(list(filter(lambda x: x < 0, itertools.chain(*grid))))


g1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
g2 = [[3, 2], [1, 0]]

sol = Solution()
print(sol.countNegatives(g1))
print(sol.countNegatives(g2))
