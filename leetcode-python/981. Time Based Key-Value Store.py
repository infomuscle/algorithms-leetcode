# 제출 코드 - Runtime 80.39 Memory 9.42
import heapq
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map_heap = defaultdict(list)
        self.map_set = defaultdict(set)

        return

    def set(self, key, value, timestamp) -> None:
        if ((timestamp, value) in self.map_set):
            return
        heapq.heappush(self.map_heap[key], (timestamp, value))
        self.map_set[key].add((timestamp, value))
        return

    def get(self, key, timestamp) -> str:
        if key not in self.map_heap or len(self.map_heap[key]) <= 0 or timestamp < self.map_heap[key][0][0]:
            return ""

        l, r = 0, len(self.map_heap[key]) - 1
        while l < r:
            mid = (l + r) // 2
            if timestamp > self.map_heap[key][mid][0]:
                l = mid + 1
                continue
            if timestamp < self.map_heap[key][mid][0]:
                r = mid - 1
                continue
            if timestamp == self.map_heap[key][mid][0]:
                return self.map_heap[key][mid][1]

        if timestamp < self.map_heap[key][l][0]:
            return self.map_heap[key][l - 1][1]
        else:
            return self.map_heap[key][l][1]
