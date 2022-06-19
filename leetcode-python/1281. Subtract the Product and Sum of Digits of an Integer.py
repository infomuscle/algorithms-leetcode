# 제출 코드 - Runtime 63.81 Memory 52.43
import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = [int(c) for c in str(n)]

        return math.prod(s) - sum(s)


sol = Solution()

n1 = 234
n2 = 4421

print(sol.subtractProductAndSum(n1))
print(sol.subtractProductAndSum(n2))
