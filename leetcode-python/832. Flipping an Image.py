# 제출 코드 - Runtime 99.05 Memory 83.02
class Solution:
    def flipAndInvertImage(self, A):
        answer = []
        for row in A:
            row.reverse()
            answer.append([r + 1 if r == 0 else r - 1 for r in row])

        return answer


sol = Solution()

a1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
a2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

print(sol.flipAndInvertImage(a1))
print(sol.flipAndInvertImage(a2))
