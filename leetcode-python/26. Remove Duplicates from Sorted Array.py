# 제출 코드 - Runtime 42.82 Memory 98.36
class Solution:
    def removeDuplicates(self, nums):
        idx = 0
        for i in range(len(nums)-1):
            if nums[idx] != nums[idx+1]:
                idx += 1
            else:
                del nums[idx]

        return len(nums)

sample1 = [1,1,2]
sample2 = [0,0,1,1,1,2,2,3,3,4]
sample3 = [1]
sample4 = [1,1]

sol = Solution()
print(sol.removeDuplicates(sample1))
print(sol.removeDuplicates(sample2))
print(sol.removeDuplicates(sample3))
print(sol.removeDuplicates(sample4))

### Code 1: 성공 - Runtime 9.64 Memory 98.36
# class Solution:
#     def removeDuplicates(self, nums):
#         for i in range(len(nums)):
#             if len(nums) == 1:
#                 return len(nums)
#
#             last = nums.pop()
#             if nums[0] != last:
#                 nums.append(last)
#                 nums.append(nums[0])
#                 del nums[0]
#             else:
#                 nums.append(last)
#                 del nums[0]
#         return len(nums)