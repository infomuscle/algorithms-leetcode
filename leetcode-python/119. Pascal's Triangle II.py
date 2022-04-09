# 제출 코드 - Runtime 95.81 Memory 19.20
class Solution:
    def getRow(self, rowIndex):
        pascal = [[1], [1, 1]]

        if rowIndex < 2:
            return pascal[rowIndex]

        for r in range(2, rowIndex + 1):
            row = [1]
            for c in range(r - 1):
                row.append(pascal[r - 1][c] + pascal[r - 1][c + 1])
            row.append(1)
            pascal.append(row)

        return pascal[rowIndex]


sol = Solution()

r1 = 3
r2 = 0
r3 = 1

print(sol.getRow(r1))
print(sol.getRow(r2))
print(sol.getRow(r3))
