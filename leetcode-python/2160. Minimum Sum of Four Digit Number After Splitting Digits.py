# 제출 코드 - Runtime 94.57 Memory 62.98
class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted([n for n in str(num)])

        return int(nums[0] + nums[2]) + int(nums[1] + nums[3])


sol = Solution()

n1 = 2932
n2 = 4009

print(sol.minimumSum(n1))
print(sol.minimumSum(n2))
