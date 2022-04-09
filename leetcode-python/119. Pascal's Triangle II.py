# 제출 코드 - Runtime 95.81 Memory 19.20
class Solution:
    def getRow(self, rowIndex):
        pascal = [[1]]

        for r in range(1, rowIndex + 1):
            pascal.append([1] + [pascal[r - 1][c] + pascal[r - 1][c + 1] for c in range(0, r - 1)] + [1])

        return pascal[rowIndex]


sol = Solution()

r1 = 3
r2 = 0
r3 = 1

print(sol.getRow(r1))
print(sol.getRow(r2))
print(sol.getRow(r3))
