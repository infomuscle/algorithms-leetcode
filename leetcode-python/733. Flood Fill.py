# 제출 코드 - Runtime 80.20 Memory 64.64
from collections import deque


class Solution:
    def floodFill(self, image, sr, sc, color):
        target = image[sr][sc]
        ways = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        visited = set()
        queue = deque([(sr, sc)])

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            cr, cc = current[0], current[1]
            if image[cr][cc] != target:
                continue

            image[cr][cc] = color
            for h, v in ways:
                if 0 <= cr + h < len(image) and 0 <= cc + v < len(image[0]):
                    queue.append((cr + h, cc + v))

        return image
