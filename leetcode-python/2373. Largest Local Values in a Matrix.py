# 제출 코드 - Runtime 32.70 Memory 42.2
class Solution:
    def largestLocal(self, grid):
        n = len(grid)

        result = [[] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                max_value = 0
                for x in range(3):
                    for y in range(3):
                        max_value = max(max_value, grid[i + x][j + y])
                result[i].append(max_value)

        return result


sol = Solution()

g1 = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
g2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

print(sol.largestLocal(g1))
print(sol.largestLocal(g2))
