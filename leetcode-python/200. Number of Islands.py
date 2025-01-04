# 제출 코드 - Runtime 33.61 Memory 20.32
class Solution:
    def numIslands(self, grid):

        ways = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])

        islands = 0
        visited = set()
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if (row, column) in visited or grid[row][column] == "0":
                    continue
                stack = [(row, column)]
                while stack:
                    land = stack.pop()
                    if land in visited:
                        continue
                    visited.add(land)
                    for x, y in ways:
                        next_land = (x + land[0], y + land[1])
                        if 0 <= next_land[0] < m and 0 <= next_land[1] < n and next_land not in visited and grid[next_land[0]][next_land[1]] == "1":
                            stack.append(next_land)
                islands += 1

        return islands


sol = Solution()

g1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
g2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(sol.numIslands(g1))
print(sol.numIslands(g2))
