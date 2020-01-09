# 제출 코드 - Runtime 93.99 Memory 86.09
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for num in nums[1:]:
            n = n ^ num

        return n


n1 = [2, 2, 1]
n2 = [4, 1, 2, 1, 2]
n3 = [1]

sol = Solution()
print(sol.singleNumber(n1))
print(sol.singleNumber(n2))
print(sol.singleNumber(n3))
