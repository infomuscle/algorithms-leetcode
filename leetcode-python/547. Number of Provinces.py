# 제출 코드 - Runtime 17.40 Memory 96.08
from collections import deque


class Solution:
    def findCircleNum(self, isConnected):
        size = len(isConnected)

        cnt = 0
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1:
                    connections_of_i = deque([j])
                    while connections_of_i:
                        current_i = connections_of_i.popleft()
                        for j_in_i in range(size):
                            if isConnected[current_i][j_in_i] == 1:
                                connections_of_i.append(j_in_i)
                                isConnected[current_i][j_in_i] = 0
                    cnt += 1

        return cnt


sol = Solution()

c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
c2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
c3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

print(sol.findCircleNum(c1))
print(sol.findCircleNum(c2))
print(sol.findCircleNum(c3))
