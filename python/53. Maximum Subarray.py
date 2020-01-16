class Solution:
    def tmaxSubArray(self, nums):

        i = 0
        j = 1

        max = nums[i]
        
        tmax = nums[i]
        idx = []


        if len(nums) == 1:
            return nums[0]

        while True:
            # print("i : %d, j : %d" % (i,j))
            # print(tmax)
            if i == len(nums) or j == len(nums):
                break


            if j == 1:
                if tmax + nums[j] > tmax:
                    tmax += nums[j]
                    j += 1
                else:
                    tmax -= nums[i]
                    i += 1
            elif j == len(nums) -1:
                if tmax -nums[i] > tmax:
                    tmax -= nums[i]
                    i += 1
                else:
                    j += 1
            else:
                if tmax + nums[j] > tmax - nums[i]:
                    tmax += nums[j]
                    j += 1
                else:
                    tmax -= nums[i]
                    i += 1
            if tmax > max:
                max = tmax
                idx = [i,j]

        # print(idx)
        return max

tc1 = [-2,1,-3,4,-1,2,1,-5,4]
tc2 = [1]
tc3 = [-2,1]

sol = Solution()
print(sol.tmaxSubArray(tc1))
print(sol.tmaxSubArray(tc2))
print(sol.tmaxSubArray(tc3))