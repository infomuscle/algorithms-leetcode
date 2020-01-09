# 제출 코드 - Runtime 82.84 Memory 100
class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[0] != val:
                nums.append(nums[0])
                del nums[0]
            else:
                del nums[0]
        return len(nums)

sample1 = [3,2,2,3]
sample2 = [0,1,2,2,3,0,4,2]

sol = Solution()
print(sol.removeElement(sample1,3))
print(sol.removeElement(sample2,2))