# 제출 코드 - Runtime 79.52 Memory 73.97
class Solution:
    def kClosest(self, points, k):
        distances = [(self.distance(x, y), [x, y]) for x, y in points]
        distances = sorted(distances, key=lambda item: item[0])
        return list(map(lambda item: item[1], distances[:k]))

    def distance(self, x, y):
        return x ** 2 + y ** 2
