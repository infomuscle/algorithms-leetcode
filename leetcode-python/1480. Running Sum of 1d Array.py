# 제출 코드 - Runtime 68.34 Memory 45.75
class Solution:
    def runningSum(self, nums):
        return [sum(nums[:i + 1]) for i in range(len(nums))]


n1 = [1, 2, 3, 4]
n2 = [1, 1, 1, 1, 1]
n3 = [3, 1, 2, 10, 1]

sol = Solution()
print(sol.runningSum(n1))
print(sol.runningSum(n2))
print(sol.runningSum(n3))
