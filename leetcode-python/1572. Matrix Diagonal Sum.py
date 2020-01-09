# 제출 코드 - Runtime 84.63 Memory 77.51
class Solution:
    def diagonalSum(self, mat):
        l, r = 0, len(mat) - 1

        sum = 0
        for row in mat:
            if l != r:
                sum += row[l] + row[r]
            else:
                sum += row[l]
            l += 1
            r -= 1

        return sum


m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
m2 = [[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]
m3 = [[5]]
sol = Solution()
print(sol.diagonalSum(m1))
print(sol.diagonalSum(m2))
print(sol.diagonalSum(m3))
