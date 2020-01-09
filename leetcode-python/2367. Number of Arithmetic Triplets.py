# 제출 코드 - Runtime 46.66 Memory 97.69
class Solution:
    def arithmeticTriplets(self, nums, diff):
        triplets = 0
        for i in range(len(nums)):
            if nums[i] + diff in nums:
                j = nums.index(nums[i] + diff)
                if nums[j] + diff in nums:
                    triplets += 1

        return triplets
