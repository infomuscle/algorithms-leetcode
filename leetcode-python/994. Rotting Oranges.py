# 제출 코드 - Runtime 7.28 Memory 7.29
from collections import deque


class Solution:
    def orangesRotting(self, grid):
        ways = (0, 1), (0, -1), (1, 0), (-1, 0)
        m = len(grid)
        n = len(grid[0])

        def is_oragnge(tile):
            return (0 <= tile[0] < m and 0 <= tile[1] < n) and grid[tile[0]][tile[1]] != 0

        rotten_oranges = []
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    rotten_oranges.append((row, column))

        time = 0
        visited = set()
        queue = deque(rotten_oranges)
        while queue:
            current_oranges = []
            while queue:
                current_oranges.append(queue.popleft())
            rotting = False
            for current_orange in current_oranges:
                visited.add(current_orange)
                if grid[current_orange[0]][current_orange[1]] == 1:
                    grid[current_orange[0]][current_orange[1]] = 2
                    rotting = True
                for x, y in ways:
                    next_tile = (current_orange[0] + x, current_orange[1] + y)
                    if is_oragnge(next_tile) and next_tile not in visited:
                        queue.append(next_tile)
            if rotting:
                time += 1

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    return -1

        return time


sol = Solution()

g1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
g2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
g3 = [
    [0, 2]
]
g4 = [
    [2, 1, 1],
    [1, 1, 1],
    [0, 1, 2]
]

print(sol.orangesRotting(g1))
print(sol.orangesRotting(g2))
print(sol.orangesRotting(g3))
print(sol.orangesRotting(g4))
