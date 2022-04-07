# 제출 코드 - Runtime 95.66 Memory 81.06
class Solution:
    def decompressRLElist(self, nums):
        return [n for i in range(1, len(nums) + 1, 2) for n in [nums[i]] * nums[i - 1]]


sol = Solution()

n1 = [1, 2, 3, 4]
n2 = [1, 1, 2, 3]

print(sol.decompressRLElist(n1))
print(sol.decompressRLElist(n2))
