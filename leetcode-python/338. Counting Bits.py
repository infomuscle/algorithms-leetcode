# 제출 코드 - Runtime 53.51 Memory 34.83
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [str(bin(i)).count("1") for i in range(n + 1)]


n1 = 2
n2 = 5

sol = Solution()
print(sol.countBits(n1))
print(sol.countBits(n2))
