# 제출 코드 - Runtime 5.25 Memory 91.03
class Solution:
    def threeSum(self, nums):
        result = set()

        nums = sorted(nums)
        for i, num1 in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                num2, num3 = nums[l], nums[r]
                sum = num1 + num2 + num3
                if sum == 0:
                    result.add((num1, num2, num3))
                if sum >= 0:
                    r -= 1
                else:
                    l += 1

        return result


sol = Solution()

n1 = [-1, 0, 1, 2, -1, -4]
n2 = [3, 0, -2, -1, 1, 2]
n3 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(sol.threeSum(n1))
print(sol.threeSum(n2))
print(sol.threeSum(n3))
