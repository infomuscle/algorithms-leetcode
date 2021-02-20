# 제출 코드 - Runtime 99.05 Memory 83.02
class Solution:
    def flipAndInvertImage(self, A):

        reverse = []
        for row in A:
            row.reverse()
            reverse.append(row)

        inverse = []
        for row in reverse:
            tmp = []
            for r in row:
                if r == 0:
                    tmp.append(r + 1)
                else:
                    tmp.append(r - 1)
            inverse.append(tmp)

        return inverse


sol = Solution()

a1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
a2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

print(sol.flipAndInvertImage(a1))
print(sol.flipAndInvertImage(a2))
