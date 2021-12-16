# 제출 코드 - Runtime 96.19 Memory 24.85
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(i + 1):
                if j == 0:
                    row.append(triangle[i - 1][j])
                elif j == i:
                    row.append(triangle[i - 1][j - 1])
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)

        return triangle


n1 = 5

sol = Solution()
print(sol.generate(n1))
