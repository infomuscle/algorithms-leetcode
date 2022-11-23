# 제출 코드 - Runtime 25.79 Memory 40.73
class Solution:
    def maxSum(self, grid):
        n, m = len(grid[0]), len(grid)

        max_sum = 0
        for i in range(m - 2):
            for j in range(n - 2):
                max_sum = max(max_sum, self.sum_of_hourglass(i, j, grid))

        return max_sum

    def sum_of_hourglass(self, x, y, grid):
        result = grid[x + 1][y + 1]
        for i in range(3):
            result += grid[x][y + i]
            result += grid[x + 2][y + i]

        return result


sol = Solution()

g1 = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
g2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
g3 = [[520626, 685427, 788912, 800638, 717251, 683428], [23602, 608915, 697585, 957500, 154778, 209236], [287585, 588801, 818234, 73530, 939116, 252369]]

print(sol.maxSum(g1))
print(sol.maxSum(g2))
print(sol.maxSum(g3))
