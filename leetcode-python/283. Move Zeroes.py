# 제출 코드 - Runtime 59.87 Memory 64.50
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if 0 in nums:
            start = nums.index(0)
            for i in range(len(nums)):
                if nums[i] != 0 and i > start:
                    nums[start], nums[i] = nums[i], nums[start]
                    start += 1


sol = Solution()

n1 = [0, 1, 0, 3, 12]
n2 = [0]
n3 = [1, 0]

print(sol.moveZeroes(n1))
print(sol.moveZeroes(n2))
print(sol.moveZeroes(n3))
