class Solution:
    def tmaxSubArray(self, nums):

        i = 0
        j = 0

        max = nums[i]
        tmax = nums[i]

        while True:
            if i == len(nums) or j == len(nums):
                break

            if tmax + nums[j+1] > tmax:
                tmax += nums[j+1]
                j += 1
            elif tmax - nums[i] > tmax:
                tmax -= nums[i]
                i += 1
            elif tmax + nums[j+1] > tmax - nums[i]:
                tmax += nums[j+1]
                tmax -= nums[i]
                i += 1
                j += 1

            if tmax > max:
                max = tmax

        return max

tc1 = [-2,1,-3,4,-1,2,1,-5,4]
tc2 = [1]
tc3 = [-2,1]

sol = Solution()
print(sol.tmaxSubArray(tc1))
print(sol.tmaxSubArray(tc2))
print(sol.tmaxSubArray(tc3))