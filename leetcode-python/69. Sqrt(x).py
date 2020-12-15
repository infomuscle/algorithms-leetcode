# 제출 코드 - Runtime 90.20 Memory 100
import math

class Solution:
    def mySqrt(self, x: int):
        return int(math.sqrt(x))

tc1 = 5
tc2 = 8
sol = Solution()

print(sol.mySqrt(tc1))
print(sol.mySqrt(tc2))