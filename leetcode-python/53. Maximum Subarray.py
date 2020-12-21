class Solution:
    def maxSubArray(self, nums):
        left, right = 0, 1

        max = nums[0]
        while right < len(nums) or left < right:
            s = sum(nums[left:right + 1])
            if (s > max):
                max = s
                right += 1
            else:
                if right > left:
                    left += 1
                else:
                    right += 1

        return max


tc1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
tc2 = [1]
tc3 = [-2, 1]
tc4 = [-1]

sol = Solution()
print(sol.maxSubArray(tc1))
print(sol.maxSubArray(tc2))
print(sol.maxSubArray(tc3))
print(sol.maxSubArray(tc4))
