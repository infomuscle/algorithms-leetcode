# 제출 코드 - Runtime 91.49 Memory 69.06
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
