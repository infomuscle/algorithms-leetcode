# 제출 코드 - Runtime 84.19 Memory 56.83
class Solution:
    def maxSubArray(self, nums):
        memo = [0] * len(nums)
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i] = max(memo[i - 1] + nums[i], nums[i])

        return max(memo)
