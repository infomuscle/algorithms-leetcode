# 제출 코드 - Runtime 96.78 Memory 51.72
class Solution:
    def explore(self, province, isConnected, visited):
        size = len(isConnected)
        for other in range(size):
            if other not in visited and isConnected[province][other] == 1:
                visited.add(other)
                self.explore(other, isConnected, visited)

    def findCircleNum(self, isConnected):
        size = len(isConnected)
        provinces = 0
        visited = set()
        for province in range(size):
            if province not in visited:
                visited.add(province)
                provinces += 1
                self.explore(province, isConnected, visited)

        return provinces


sol = Solution()

c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
c2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
c3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

print(sol.findCircleNum(c1))
print(sol.findCircleNum(c2))
print(sol.findCircleNum(c3))
