# 제출 코드 - Runtime 77.73 Memory 16.90
from collections import defaultdict, deque


class Solution:
    def destCity(self, paths):
        graph = defaultdict(set)

        for departure, arrival in paths:
            graph[departure].add(arrival)
        print(graph)

        queue = deque()
        queue.append(paths[0][0])

        visited = set()
        while len(queue) != 0:
            city = queue.popleft()
            visited.add(city)
            queue.extend(graph[city] - visited)

        return city


p1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
p2 = [["B", "C"], ["D", "B"], ["C", "A"]]
p3 = [["A", "Z"]]

sol = Solution()
print(sol.destCity(p1))
print(sol.destCity(p2))
print(sol.destCity(p3))
