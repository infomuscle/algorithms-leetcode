# 제출 코드 - Runtime 84.57 Memory 19.62
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1

        for key in nums_map:
            if nums_map[key] == 1:
                return key


n1 = [2, 2, 1]

sol = Solution()
print(sol.singleNumber(n1))
