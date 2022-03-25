# 제출 코드 - Runtime 86.25 Memory 21.60
class Solution:
    def createTargetArray(self, nums, index):
        target = [nums[0]]

        for i in range(1, len(nums)):
            target = target[:index[i]] + [nums[i]] + target[index[i]:]

        return target


n1 = [0, 1, 2, 3, 4]
i1 = [0, 1, 2, 2, 1]
n2 = [1, 2, 3, 4, 0]
i2 = [0, 1, 2, 3, 0]
n3 = [1]
i3 = [0]

sol = Solution()
print(sol.createTargetArray(n1, i1))
print(sol.createTargetArray(n2, i2))
print(sol.createTargetArray(n3, i3))
