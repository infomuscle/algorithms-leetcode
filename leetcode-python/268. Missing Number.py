# 제출 코드 - Runtime 69.52 Memory 77.23
class Solution:
    def missingNumber(self, nums) -> int:
        space = [False] * (10 ** 4)
        for num in nums:
            space[num] = True
        return space.index(False)
