# 제출 코드 - Runtime 62.75 Memory 10.38
class Solution:
    def search(self, nums, target):

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return -1
