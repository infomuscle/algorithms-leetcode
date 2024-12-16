# 제출 코드 - Runtime 96.78 Memory 17.41
from collections import deque


class Solution:
    def cloneGraph(self, node):
        if node is None or node.neighbors is None:
            return node

        copies = {}
        queue = deque([node])
        visited = set()
        while queue:
            next = queue.popleft()
            if next is None or next.val in visited:
                continue
            visited.add(next.val)
            if next.val not in copies:
                copies[next.val] = Node(next.val, next.neighbors)
            for neighbor in next.neighbors:
                queue.append(neighbor)

        for key in copies:
            copy = copies[key]
            if copy.neighbors is None:
                continue

            copied_neighbors = []
            for neighbor in copy.neighbors:
                copied_neighbors.append(copies[neighbor.val])
            copy.neighbors = copied_neighbors

        return copies[node.val]


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
