# 제출 코드 - Runtime 5.00 Memory 9.34
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = defaultdict(set)
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)

        for course in range(numCourses):
            if not self.dfs(numCourses, graph, course):
                return False

        return True

    def dfs(self, n, graph, start):

        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)
            for prerequisite in graph[node]:
                if prerequisite in visited:
                    if prerequisite == start:
                        return False
                    continue
                stack.append(prerequisite)

        return True


n1, p1 = 2, [[1, 0]]
n2, p2 = 2, [[1, 0], [0, 1]]
n3, p3 = 5, [[1, 4], [2, 4], [3, 1], [3, 2]]
n4, p4 = 4, [[0, 1], [3, 1], [1, 3], [3, 2]]

sol = Solution()
print(sol.canFinish(n1, p1))
print(sol.canFinish(n2, p2))
print(sol.canFinish(n3, p3))
print(sol.canFinish(n4, p4))
