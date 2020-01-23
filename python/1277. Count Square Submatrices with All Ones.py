# 제출 코드 - Runtime 5.04 Memory 100
class Solution:
    def countSquares(self, matrix):

        rowSize = len(matrix)
        colSize = len(matrix[0])
        count = 0

        for i in range(rowSize):
            for j in range(colSize):
                if matrix[i][j] == 0:
                    continue
                else:
                    size = 0
                    while True:
                        size += 1
                        try:
                            if self.checker(matrix, i, j, size) == True:
                                count += 1
                            else:
                                break
                        except:
                            break

        return count

    def checker(self, matrix, r, c, n):
        flag = 1
        for i in range(n):
            for j in range(n):
                if matrix[r+i][c+j] == 0:
                    flag = 0
                    return False

        return True



tc1 = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

tc2 = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]


sol = Solution()

print(sol.countSquares(tc1))
print(sol.countSquares(tc2))