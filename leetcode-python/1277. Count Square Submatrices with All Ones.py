# 제출 코드 - Runtime 31.60 Memory 100
class Solution:
    def countSquares(self, matrix):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r = i
                c = j
                n = 1
                while True:
                    try:
                        if matrix[r][c] == 0:
                            break
                        if self.checker(matrix, r, c, n) == True:
                            count += 1
                            r += 1
                            c += 1
                            n += 1
                        else:
                            break
                    except:
                        break
        return count

    def checker(self, matrix, r, c, n):
        for i in range(n-1):
            if matrix[r-1-i][c] == 0:
                return False
        for j in range(n-1):
            if matrix[r][c-1-j] == 0:
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

tc3 = [
    [0,0,0],
    [0,1,0],
    [0,1,0],
    [1,1,1],
    [1,1,0]
]


sol = Solution()

print(sol.countSquares(tc1))
print(sol.countSquares(tc2))
print(sol.countSquares(tc3))



# Code 1: 성공 - Runtime 18.21 Memory 100
# class Solution:
#     def countSquares(self, matrix):
#
#         rowSize = len(matrix)
#         colSize = len(matrix[0])
#         count = 0
#
#         for i in range(rowSize):
#             for j in range(colSize):
#                 if matrix[i][j] == 0:
#                     continue
#                 else:
#                     size = 0
#                     while True:
#                         size += 1
#                         try:
#                             if self.checker(matrix, i, j, size) == True:
#                                 count += 1
#                             else:
#                                 break
#                         except:
#                             break
#
#         return count
#
#     def checker(self, matrix, r, c, n):
#         flag = 1
#         for i in range(n):
#             for j in range(n):
#                 if matrix[r+i][c+j] == 0:
#                     flag = 0
#                     return False
#
#         return True

# Code 2: 성공 - Runtime 31.60 Memory 100
# class Solution:
#     def countSquares(self, matrix):
#         count = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 r = i
#                 c = j
#                 n = 1
#                 while True:
#                     try:
#                         if matrix[r][c] == 0:
#                             break
#                         if self.checker(matrix, r, c, n) == True:
#                             count += 1
#                             r += 1
#                             c += 1
#                             n += 1
#                         else:
#                             break
#                     except:
#                         break
#         return count
#
#     def checker(self, matrix, r, c, n):
#         for i in range(n-1):
#             if matrix[r-1-i][c] == 0:
#                 return False
#         for j in range(n-1):
#             if matrix[r][c-1-j] == 0:
#                 return False
#
#         return True