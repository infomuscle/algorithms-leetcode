# 제출 코드 - Runtime 99.59 Memory 42.56
class Solution:
    def twoSum(self, nums, target):
        vals = {}
        for i in range(len(nums)):
            if nums[i] in vals:
                return [vals[nums[i]], i]
            vals[target - nums[i]] = i


sample1 = [[2, 7, 11, 15], 9]
sample2 = [[3, 2, 4], 6]
sample3 = [[3, 3], 6]

sol = Solution()
print(sol.twoSum(sample1[0], sample1[1]))
print(sol.twoSum(sample2[0], sample2[1]))
print(sol.twoSum(sample3[0], sample3[1]))

# Code 1 - Runtime 5.01 Memory 78.37
# def twoSum(self, nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             temp = nums[i] + nums[j]
#             if temp == target:
#                 return [i, j]


# Code 2 - Runtime 31.95 Memory 80.46
# def twoSum(self, nums, target):
#     vals = []
#     for i in range(len(nums)):
#         if nums[i] in vals:
#             return [vals.index(nums[i]), i]
#         vals.append(target - nums[i])
